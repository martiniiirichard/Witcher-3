# Knight Hips For AMM 2348 Review

Date: 2026-06-22

## Source

- Nexus: https://www.nexusmods.com/witcher3/mods/2348
- Mod name: `Knight Hips for AMM`
- Downloaded archive: `Hip Armor Retexture-2348-1.rar`

## Page Notes

- Requires Blood and Wine.
- Requires AMM.
- Author describes this as a simple drop-into-`mods` install.
- The page warns that texture-related issues after install may indicate hitting the Witcher 3 texture mod limit.

## Local State

Already installed:

- `mods/modKnightHips`

Enabled in `C:\Games\The Witcher 3\mods.settings`:

```ini
[modKnightHips]
Enabled=1
Priority=17
```

Installed files:

- `content/blob0.bundle`
- `content/metadata.store`
- `content/texture.cache`

## Decision

No new runtime install needed. This mod is already present as `modKnightHips` from the earlier knight accessories install checkpoint.

## Verification

- Confirmed `modKnightHips` exists in the game `mods` folder.
- Confirmed `modKnightHips` is enabled in `mods.settings`.
- Confirmed the installed folder contains no `.ws` scripts.
- No Script Merger work is needed.
- No additional launch test is needed because no new runtime change was made.
