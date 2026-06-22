# Auto Loot Redux For W3EE 11743 Install

Date: 2026-06-22

## Source

- Nexus: https://www.nexusmods.com/witcher3/mods/11743
- Main file: `AutoLoot Redux for W3EE-11743-2-3-1770600253.zip`
- Required optional file: `Oneliners - REQUIRED FILE-11743-1-1770654764.zip`

## Page Notes

- Built specifically for W3EE Redux.
- Nexus description calls the mod merge-free.
- Files tab lists main file version `2.3`.
- Oneliners is required unless another installed mod already includes it.
- Built for TW3 `4.04+` with W3EE Redux.

## Runtime Changes

Installed:

- `mods/mod_sharedutils_oneliners`
- `mods/modAutoLootRedux`
- `bin/config/r4game/user_config_matrix/pc/mod_autoloot.xml`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[mod_sharedutils_oneliners]
Enabled=1
Priority=22

[modAutoLootRedux]
Enabled=1
Priority=23
```

## Backup

- `backups/auto-loot-redux-11743-20260622-110518`

## Inspection Notes

- No existing `mod_sharedutils_oneliners` install was found.
- Existing `modSharedImports` is unrelated and was left untouched.
- Staged `.ws` paths were checked against the installed mod stack.
- No script-path overlaps were found, matching the author's merge-free claim.
- No Script Merger work is expected.

## Verification

- Confirmed both runtime mod folders exist.
- Confirmed `mod_autoloot.xml` exists in the game config folder.
- Confirmed both mods are enabled in `mods.settings`.
- Confirmed no script-path conflicts with existing installed mods.
- Game launch: passed after direct DX12 launch.
