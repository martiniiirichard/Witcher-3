# Correct Burning Name 11862

Source: https://www.nexusmods.com/witcher3/mods/11862

Date: 2026-06-24

## Page Notes

- Mod name: Correct burning name (Classic and Next Gen)
- Version checked: 1.0
- Purpose: changes the burning effect label from `Fire damage` to `Burning`.
- Nexus install instruction says to place `modCorrectBurningName` into `Mods` and use Script Merger if needed.

## Local Decision

Did not install `modCorrectBurningName` as a standalone mod.

Reason: the archive contains a full `baseEffect.ws`, and this file is already owned by active W3EE/Better Icons scripts. Installing the whole mod would add another owner for a broad core effect script just to apply one localization guard.

## Implemented Manual Graft

Added the one functional line from the mod after `effectNameLocalisationKey = tmpName;` in both active owners:

```witcherscript
if(effectNameLocalisationKey == "attribute_name_firedamage") effectNameLocalisationKey = "BurningEffect";
```

Patched files:

- `mods\modBetterIcons2025_NextGen_W3EE\content\scripts\game\gameplay\effects\effects\baseEffect.ws`
- `mods\modW3EE\content\scripts\game\gameplay\effects\effects\baseEffect.ws`

`modBetterIcons2025_NextGen_W3EE` has priority `13` and is the likely active winner over `modW3EE` priority `23`. W3EE was patched too so the fix remains if Better Icons is later removed or reprioritized.

## Backups

Created timestamped backups next to both patched files:

- `baseEffect.ws.codex-backup-correct-burning-name-11862-<timestamp>`

## Verification

- Confirmed `modCorrectBurningName` was not added to `mods`.
- Confirmed no `[modCorrectBurningName]` entry exists in either active `mods.settings`.
- DX12 smoke test passed: game process stayed alive for 45 seconds and was killed manually.
