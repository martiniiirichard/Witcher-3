#!/usr/bin/env python3
"""Patch a Witcher 3 .w3strings entry in place.

This implements the small subset of WolvenKit's W3Strings reader/writer needed
to shorten one menu title while preserving the rest of the string table.
"""

from __future__ import annotations

import argparse
import shutil
import struct
from dataclasses import dataclass
from pathlib import Path


LANG = {
    "en": {"key1": 0x4397, "key2": 0x5139, "magic": 0x79321793},
}


@dataclass
class Block1:
    str_id: int
    str_id_hashed: int
    offset: int
    strlen: int
    text: str = ""


@dataclass
class Block2:
    str_key_hex: int
    str_id: int


def read_u16(data: bytes, pos: int) -> tuple[int, int]:
    return struct.unpack_from("<H", data, pos)[0], pos + 2


def read_u32(data: bytes, pos: int) -> tuple[int, int]:
    return struct.unpack_from("<I", data, pos)[0], pos + 4


def read_bit6(data: bytes, pos: int) -> tuple[int, int]:
    result = 0
    shift = 0
    i = 1
    while True:
        b = data[pos]
        pos += 1
        s = 6
        mask = 255
        if b > 127:
            mask = 127
            s = 7
        elif b > 63 and i == 1:
            mask = 63
        result |= (b & mask) << shift
        shift += s
        i += 1
        if b < 64 or (i >= 3 and b < 128):
            return result, pos


def write_bit6(value: int) -> bytes:
    if value == 0:
        return bytes([128])
    chunks: list[int] = []
    left = value
    i = 0
    while left > 0:
        if i == 0:
            chunks.append(left & 63)
            left >>= 6
        else:
            chunks.append(left & 255)
            left >>= 7
        i += 1
    out = bytearray()
    for i, chunk in enumerate(chunks):
        last = i == len(chunks) - 1
        remaining = len(chunks) - 1 - i
        if not last:
            if remaining >= 1 and i >= 1:
                chunk |= 128
            elif chunk < 64:
                chunk |= 64
            else:
                chunk |= 128
        if chunk == 128:
            raise ValueError("Unsupported bit6 encoding edge case")
        out.append(chunk)
    return bytes(out)


def decrypt_text(raw: bytes, strlen: int, magic: int) -> str:
    chars: list[str] = []
    string_key = (magic >> 8) & 0xFFFF
    for i in range(strlen):
        b1 = raw[i * 2]
        b2 = raw[i * 2 + 1]
        char_key = ((strlen + 1) * string_key) & 0xFFFF
        b1 ^= (char_key >> 0) & 0xFF
        b2 ^= (char_key >> 8) & 0xFF
        string_key = ((string_key << 1) | (string_key >> 15)) & 0xFFFF
        chars.append(chr(b1 + (b2 << 8)))
    return "".join(chars)


def encrypt_text(text: str, magic: int) -> bytes:
    out = bytearray()
    strlen = len(text)
    string_key = (magic >> 8) & 0xFFFF
    for ch in text:
        code = ord(ch)
        b1 = code & 0xFF
        b2 = code >> 8
        char_key = ((strlen + 1) * string_key) & 0xFFFF
        b1 ^= (char_key >> 0) & 0xFF
        b2 ^= (char_key >> 8) & 0xFF
        string_key = ((string_key << 1) | (string_key >> 15)) & 0xFFFF
        out.extend((b1, b2))
    out.extend((0, 0))
    return bytes(out)


def read_w3strings(path: Path, lang: str) -> tuple[int, list[Block1], list[Block2]]:
    spec = LANG[lang]
    data = path.read_bytes()
    if data[:4] != b"RTSW":
        raise ValueError(f"{path} is not a W3Strings file")
    version = struct.unpack_from("<I", data, 4)[0]
    key1 = struct.unpack_from("<H", data, 8)[0]
    key2 = struct.unpack_from("<H", data, len(data) - 2)[0]
    if key1 != spec["key1"] or key2 != spec["key2"]:
        raise ValueError(f"Unexpected language keys: {key1:04x}/{key2:04x}")

    pos = 10
    count1, pos = read_bit6(data, pos)
    block1: list[Block1] = []
    for _ in range(count1):
        str_id_hashed, pos = read_u32(data, pos)
        offset, pos = read_u32(data, pos)
        strlen, pos = read_u32(data, pos)
        block1.append(Block1(str_id_hashed ^ spec["magic"], str_id_hashed, offset, strlen))

    count2, pos = read_bit6(data, pos)
    block2: list[Block2] = []
    for _ in range(count2):
        str_key_hex, pos = read_u32(data, pos)
        str_id_hashed, pos = read_u32(data, pos)
        block2.append(Block2(str_key_hex, str_id_hashed ^ spec["magic"]))

    block3_count, pos = read_bit6(data, pos)
    string_start = pos
    for block in block1:
        start = string_start + block.offset * 2
        end = start + block.strlen * 2
        block.text = decrypt_text(data[start:end], block.strlen, spec["magic"])

    expected_end = string_start + block3_count * 2
    if expected_end > len(data) - 2:
        raise ValueError("String block length points past end of file")
    return version, block1, block2


def write_w3strings(path: Path, lang: str, version: int, block1: list[Block1], block2: list[Block2]) -> None:
    spec = LANG[lang]
    string_buffer = bytearray()
    for block in block1:
        block.offset = len(string_buffer) // 2
        block.strlen = len(block.text)
        string_buffer.extend(encrypt_text(block.text, spec["magic"]))

    out = bytearray()
    out.extend(b"RTSW")
    out.extend(struct.pack("<I", version))
    out.extend(struct.pack("<H", spec["key1"]))
    out.extend(write_bit6(len(block1)))
    for block in block1:
        out.extend(struct.pack("<III", block.str_id ^ spec["magic"], block.offset, block.strlen))
    out.extend(write_bit6(len(block2)))
    for block in block2:
        out.extend(struct.pack("<II", block.str_key_hex, block.str_id ^ spec["magic"]))
    out.extend(write_bit6(len(string_buffer) // 2))
    out.extend(string_buffer)
    out.extend(struct.pack("<H", spec["key2"]))
    path.write_bytes(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--lang", default="en", choices=sorted(LANG))
    parser.add_argument("--id", type=int, required=True)
    parser.add_argument("--text", required=True)
    parser.add_argument("--backup", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    version, block1, block2 = read_w3strings(args.path, args.lang)
    matches = [block for block in block1 if block.str_id == args.id]
    if len(matches) != 1:
        raise SystemExit(f"Expected one string id {args.id}, found {len(matches)}")
    old = matches[0].text
    print(f"{args.id}: {old!r} -> {args.text!r}")
    if args.dry_run:
        return 0
    matches[0].text = args.text
    if args.backup:
        shutil.copy2(args.path, args.path.with_suffix(args.path.suffix + ".codex-backup"))
    write_w3strings(args.path, args.lang, version, block1, block2)
    _, verify_block1, _ = read_w3strings(args.path, args.lang)
    verify = [block.text for block in verify_block1 if block.str_id == args.id][0]
    if verify != args.text:
        raise SystemExit(f"Verification failed: got {verify!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
