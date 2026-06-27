#!/usr/bin/env python3
"""
Analyze Witcher 3 script compilation errors against the active mod stack.

Typical use:

  python tools/analyze-witcher-compile-errors.py --errors compile-errors.txt

Or paste errors through stdin:

  Get-Clipboard | python tools/analyze-witcher-compile-errors.py

The tool is intentionally read-only. It parses common WitcherScript compiler
messages, searches active mod scripts for the failing symbols, and reports
likely owners, duplicate definitions, disabled candidates, and next actions.
"""

from __future__ import annotations

import argparse
import configparser
import dataclasses
import os
import re
import sys
from pathlib import Path
from typing import Iterable


DEFAULT_GAME_ROOT = Path(r"C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY")
DEFAULT_MODS_SETTINGS = Path(r"C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings")


ERROR_RE = re.compile(
    r"^(?P<level>Error|Warning)\s+\[(?P<source>[^\]]+)\](?P<path>.+?)\((?P<line>\d+)\):\s*(?P<message>.+)$",
    re.IGNORECASE,
)


SYMBOL_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("missing_function", re.compile(r"Could not find function '([^']+)'", re.I)),
    ("unknown_identifier", re.compile(r"I dont know any '([^']+)'", re.I)),
    ("unknown_type", re.compile(r"Unknown type '([^']+)'", re.I)),
    ("unknown_base_class", re.compile(r"Unknown base class '([^']+)'", re.I)),
    ("class_already_defined", re.compile(r"Class '([^']+)' already defined", re.I)),
    ("global_function_already_defined", re.compile(r"Global function '([^']+)'(?: is)? already defined", re.I)),
    ("property_already_exists", re.compile(r"Property '([^']+)' already exists", re.I)),
    ("not_member", re.compile(r"'([^']+)' is not a member", re.I)),
    ("private_function", re.compile(r"Cannot call private function '([^']+)'", re.I)),
    ("wrap_missing", re.compile(r"Wrap function '([^']+)' must wrap an existing function", re.I)),
    ("overwrite_missing", re.compile(r"(?:Overwrite|Replace) function '([^']+)' must .*existing function", re.I)),
    ("native_already_exported", re.compile(r"Native function '([^']+)' was already exported", re.I)),
    ("signature_mismatch", re.compile(r"Function '([^']+)' takes \d+ parameter", re.I)),
    ("bad_param_count", re.compile(r"Function '([^']+)' does not take \d+ param", re.I)),
    ("parse_near", re.compile(r"near '([^']+)'", re.I)),
]


DISABLED_MARKERS = (
    ".disabled",
    "disabled-by-codex",
    ".codex-backup",
    ".bak",
    ".orig",
    ".old",
)


@dataclasses.dataclass(frozen=True)
class CompileIssue:
    level: str
    source: str
    script_path: str
    line: int
    message: str
    kind: str
    symbol: str | None


@dataclasses.dataclass(frozen=True)
class ScriptHit:
    file: Path
    line: int
    text: str
    active: bool
    owner: str
    hit_kind: str


def normalize_path(path: Path) -> str:
    try:
        return str(path.resolve())
    except OSError:
        return str(path)


def read_errors(path: Path | None) -> str:
    if path:
        return path.read_text(encoding="utf-8-sig", errors="replace")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


def parse_issues(text: str) -> list[CompileIssue]:
    issues: list[CompileIssue] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        m = ERROR_RE.match(line)
        if not m:
            continue
        message = m.group("message").strip()
        kind = "unclassified"
        symbol: str | None = None
        for candidate_kind, pattern in SYMBOL_PATTERNS:
            sm = pattern.search(message)
            if sm:
                kind = candidate_kind
                symbol = sm.group(1)
                break
        issues.append(
            CompileIssue(
                level=m.group("level"),
                source=m.group("source"),
                script_path=m.group("path").strip(),
                line=int(m.group("line")),
                message=message,
                kind=kind,
                symbol=symbol,
            )
        )
    return issues


def parse_mods_settings(path: Path) -> dict[str, dict[str, int]]:
    parser = configparser.ConfigParser()
    parser.optionxform = str
    if not path.exists():
        return {}
    parser.read(path, encoding="utf-8-sig")
    mods: dict[str, dict[str, int]] = {}
    for section in parser.sections():
        enabled = parser.getint(section, "Enabled", fallback=0)
        priority = parser.getint(section, "Priority", fallback=999999)
        mods[section] = {"Enabled": enabled, "Priority": priority}
    return mods


def is_disabled_path(path: Path) -> bool:
    lowered = str(path).lower()
    return any(marker in lowered for marker in DISABLED_MARKERS)


def owner_for_script(path: Path, game_root: Path) -> str:
    parts = path.parts
    lowered = [p.lower() for p in parts]
    for folder in ("mods", "dlc", "content"):
        if folder in lowered:
            idx = lowered.index(folder)
            if idx + 1 < len(parts):
                return parts[idx + 1]
    try:
        rel = path.relative_to(game_root)
        return rel.parts[0] if rel.parts else "game"
    except ValueError:
        return "unknown"


def active_script_roots(game_root: Path, mod_settings: dict[str, dict[str, int]]) -> list[tuple[Path, bool]]:
    roots: list[tuple[Path, bool]] = []

    # Vanilla/base scripts are useful as search targets for wrap/replace failures.
    content0_scripts = game_root / "content" / "content0" / "scripts"
    if content0_scripts.exists():
        roots.append((content0_scripts, True))

    mods_dir = game_root / "Mods"
    if mods_dir.exists():
        for mod_dir in sorted(p for p in mods_dir.iterdir() if p.is_dir()):
            name = mod_dir.name
            settings = mod_settings.get(name)
            active = bool(settings and settings.get("Enabled") == 1)
            scripts = mod_dir / "content" / "scripts"
            if scripts.exists():
                roots.append((scripts, active))

    dlc_dir = game_root / "DLC"
    if dlc_dir.exists():
        for dlc_mod_dir in sorted(p for p in dlc_dir.iterdir() if p.is_dir()):
            scripts = dlc_mod_dir / "content" / "scripts"
            if scripts.exists():
                # DLC folders are not directly controlled by mods.settings.
                roots.append((scripts, True))

    return roots


def iter_script_files(roots: Iterable[tuple[Path, bool]], include_disabled: bool) -> Iterable[tuple[Path, bool]]:
    for root, active_root in roots:
        for path in root.rglob("*.ws*"):
            if not path.is_file():
                continue
            disabled = is_disabled_path(path) or path.suffix.lower() != ".ws"
            if disabled and not include_disabled:
                continue
            yield path, active_root and not disabled


def classify_hit(symbol: str, line: str) -> str:
    escaped = re.escape(symbol)
    checks: list[tuple[str, re.Pattern[str]]] = [
        ("class_definition", re.compile(rf"\bclass\s+{escaped}\b", re.I)),
        ("enum_definition", re.compile(rf"\benum\s+{escaped}\b", re.I)),
        ("function_definition", re.compile(rf"\bfunction\s+{escaped}\b", re.I)),
        ("global_function_definition", re.compile(rf"\b(?:public|private|protected|final|exec|latent|static|\s)*function\s+{escaped}\b", re.I)),
        ("field_or_property", re.compile(rf"^\s*(?:saved\s+)?(?:editable\s+)?(?:private\s+|public\s+|protected\s+)?(?:var\s+)?\b{escaped}\b\s*[:=;]", re.I)),
        ("field_or_property", re.compile(rf"^\s*(?:saved\s+)?(?:editable\s+)?(?:private\s+|public\s+|protected\s+)?var\s+[^;\n]*\b{escaped}\b", re.I)),
        ("annotation", re.compile(rf"@(addField|addMethod|wrapMethod|replaceMethod|wrapField|replaceField)\b.*\b{escaped}\b", re.I)),
        ("direct_reference", re.compile(rf"\b{escaped}\b", re.I)),
    ]
    for hit_kind, pattern in checks:
        if pattern.search(line):
            return hit_kind
    return "direct_reference"


def search_symbol(symbol: str, files: Iterable[tuple[Path, bool]], game_root: Path, limit: int) -> list[ScriptHit]:
    if not symbol:
        return []

    hits: list[ScriptHit] = []
    needle = symbol.lower()
    for file_path, active in files:
        try:
            for idx, line in enumerate(file_path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
                if needle not in line.lower():
                    continue
                hit_kind = classify_hit(symbol, line)
                hits.append(
                    ScriptHit(
                        file=file_path,
                        line=idx,
                        text=line.strip(),
                        active=active,
                        owner=owner_for_script(file_path, game_root),
                        hit_kind=hit_kind,
                    )
                )
                if len(hits) >= limit:
                    return hits
        except OSError:
            continue
    return hits


def likely_cause(issue: CompileIssue, hits: list[ScriptHit]) -> str:
    provider_kinds = {"class_definition", "enum_definition", "function_definition", "global_function_definition", "field_or_property", "annotation"}
    active_defs = [h for h in hits if h.active and h.hit_kind in provider_kinds]
    inactive_defs = [h for h in hits if not h.active and h.hit_kind in provider_kinds]

    if issue.kind in {"class_already_defined", "global_function_already_defined", "property_already_exists", "native_already_exported"}:
        if len(active_defs) > 1:
            return "Duplicate active definitions. Disable one provider or convert one side to a compatibility patch."
        return "Compiler reports a duplicate, but the scan found limited definitions. Check merged files and generated Script Merger output."

    if issue.kind in {"missing_function", "unknown_identifier", "not_member", "wrap_missing", "overwrite_missing"}:
        if inactive_defs:
            return "Likely disabled or losing dependency/annotation provider. Inspect inactive hits first."
        if active_defs:
            return "Symbol exists somewhere active, so this is likely a load-order, class-scope, generation mismatch, or private/access issue."
        return "No provider found in active scripts. The mod may target another game version, require a missing dependency, or need a custom compatibility shim."

    if issue.kind in {"unknown_type", "unknown_base_class"}:
        if inactive_defs:
            return "Type exists only in disabled files; restore the dependency or remove references to it."
        if active_defs:
            return "Type exists active but may compile later than this reference or be hidden by class/file ordering."
        return "Missing class/type provider. Search staging/downloaded dependency mods before patching references."

    if issue.kind in {"signature_mismatch", "bad_param_count"}:
        return "Function exists but signature differs. Compare base/W3EE/current signature and update call or override parameters."

    if issue.kind == "private_function":
        return "Access violation. Prefer wrapping the owner class method or adding a public helper inside the owning class."

    if issue.kind == "parse_near":
        return "Syntax-level issue. Inspect surrounding lines, especially manual merge markers, missing commas, or WitcherScript generics syntax."

    return "Unclassified. Inspect source file and search nearby symbols manually."


def render_report(
    issues: list[CompileIssue],
    symbol_hits: dict[str, list[ScriptHit]],
    game_root: Path,
    mods_settings: Path,
    mod_settings: dict[str, dict[str, int]],
) -> str:
    lines: list[str] = []
    lines.append("# Witcher 3 Compile Error Analysis")
    lines.append("")
    lines.append(f"- Game root: `{game_root}`")
    lines.append(f"- mods.settings: `{mods_settings}`")
    lines.append(f"- Enabled mods in settings: `{sum(1 for v in mod_settings.values() if v.get('Enabled') == 1)}`")
    lines.append(f"- Parsed issues: `{len(issues)}`")
    lines.append("")

    if not issues:
        lines.append("No compiler issues were parsed. Provide raw lines like:")
        lines.append("")
        lines.append("```text")
        lines.append("Error [modname]path\\file.ws(123): Could not find function 'Example'")
        lines.append("```")
        return "\n".join(lines)

    grouped: dict[str, list[CompileIssue]] = {}
    for issue in issues:
        grouped.setdefault(issue.symbol or issue.message, []).append(issue)

    lines.append("## Summary")
    lines.append("")
    for key, group in grouped.items():
        first = group[0]
        hits = symbol_hits.get(first.symbol or "", [])
        active_hits = sum(1 for h in hits if h.active)
        inactive_hits = len(hits) - active_hits
        lines.append(
            f"- `{key}`: {len(group)} issue(s), kind `{first.kind}`, active hits `{active_hits}`, inactive/disabled hits `{inactive_hits}`"
        )
    lines.append("")

    for key, group in grouped.items():
        first = group[0]
        symbol = first.symbol
        hits = symbol_hits.get(symbol or "", [])
        lines.append(f"## `{key}`")
        lines.append("")
        lines.append(f"- Kind: `{first.kind}`")
        lines.append(f"- Likely cause: {likely_cause(first, hits)}")
        lines.append("")
        lines.append("Occurrences:")
        lines.append("")
        for issue in group:
            lines.append(
                f"- `{issue.level} [{issue.source}]{issue.script_path}({issue.line})`: {issue.message}"
            )
        lines.append("")

        if symbol:
            if hits:
                lines.append("Symbol hits:")
                lines.append("")
                for hit in hits[:30]:
                    state = "active" if hit.active else "inactive/disabled"
                    try:
                        display_path = hit.file.relative_to(game_root)
                    except ValueError:
                        display_path = hit.file
                    lines.append(
                        f"- `{state}` `{hit.owner}` `{hit.hit_kind}` `{display_path}:{hit.line}`: {hit.text[:220]}"
                    )
                if len(hits) > 30:
                    lines.append(f"- ... {len(hits) - 30} more hit(s) omitted")
            else:
                lines.append("No symbol hits found in scanned scripts.")
        else:
            lines.append("No symbol extracted from this message.")
        lines.append("")
        lines.append("Suggested next action:")
        lines.append("")
        lines.append(f"- {next_action(first, hits)}")
        lines.append("")
    return "\n".join(lines)


def next_action(issue: CompileIssue, hits: list[ScriptHit]) -> str:
    if issue.kind in {"class_already_defined", "global_function_already_defined", "property_already_exists", "native_already_exported"}:
        return "Compare active definition providers. Usually disable the redundant compatibility mod or remove the duplicate annotation/full-file override."
    if issue.kind in {"missing_function", "unknown_identifier", "not_member"}:
        return "Find which dependency should add the symbol; if no active provider exists, either install/enable dependency or remove/replace the referring code."
    if issue.kind in {"wrap_missing", "overwrite_missing"}:
        return "Verify target game/W3EE method exists. If W3EE removed or renamed it, disable that patch or rewrite it against the current method."
    if issue.kind in {"unknown_type", "unknown_base_class"}:
        return "Search staging/downloaded mods for the missing type. Avoid stubbing gameplay classes unless the type is truly unused."
    if issue.kind in {"signature_mismatch", "bad_param_count"}:
        return "Open the current winning base function and update parameter list/calls to match it."
    if issue.kind == "private_function":
        return "Move the call into a wrapper on the owning class or expose a safe helper in a compatibility patch."
    if issue.kind == "parse_near":
        return "Open the reported file around the line and inspect manual merge syntax."
    return "Open the reported file and search related symbols."


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze Witcher 3 compile errors against active scripts.")
    parser.add_argument("--errors", type=Path, help="Text file containing compiler errors. If omitted, reads stdin.")
    parser.add_argument("--game-root", type=Path, default=DEFAULT_GAME_ROOT)
    parser.add_argument("--mods-settings", type=Path, default=DEFAULT_MODS_SETTINGS)
    parser.add_argument("--out", type=Path, help="Write report to this file.")
    parser.add_argument("--include-disabled", action="store_true", help="Also search disabled/backup .ws files.")
    parser.add_argument("--hit-limit", type=int, default=80, help="Maximum symbol hits per symbol.")
    args = parser.parse_args()

    text = read_errors(args.errors)
    issues = parse_issues(text)
    mod_settings = parse_mods_settings(args.mods_settings)
    roots = active_script_roots(args.game_root, mod_settings)
    script_files = list(iter_script_files(roots, include_disabled=args.include_disabled))

    symbol_hits: dict[str, list[ScriptHit]] = {}
    for issue in issues:
        if issue.symbol and issue.symbol not in symbol_hits:
            symbol_hits[issue.symbol] = search_symbol(issue.symbol, script_files, args.game_root, args.hit_limit)

    report = render_report(issues, symbol_hits, args.game_root, args.mods_settings, mod_settings)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
