# E3 Quen + W3EE Redux Compatibility Install - 2026-06-22

## Goal
Install the E3 Quen visual stack while keeping W3EE Redux compatibility in control of conflicts.

## Installed Downloads
- `E3Quen 4.0-2366-4-0-1671749722.rar`
- `1. E3Quen-8710-1-1-1739540326.zip`
- `E3 Quen - W3EE Redux-9957-v1-1731794425.zip`

## Installed Game Folders
- `mods\modE3Quen`
- `mods\mod0E3Quen_NextGen`
- `mods\modE3QuenEER`
- `DLC\dlc_quen`

## Priority Decision
Lower numeric priority wins in `mods.settings`.

- `modE3QuenEER` was placed above `modReduxW3EE` and `modW3EE` because it is the W3EE Redux compatibility patch.
- `mod0E3Quen_NextGen` was placed above `modE3Quen` so the Next Gen adjustments win over the base E3 Quen files.
- Both E3 Quen visual folders were placed below W3EE/W3EE localizations.

## Validation
- Archive contents inspected before install.
- No `.ws` scripts were introduced by this stack.
- No Script Merger pass required.
- DX12 direct launcher started the game.
- `witcher3` process remained alive and responding after the initial launch window.

## Backup
- Pre/post `mods.settings` backup and any replaced Quen folders were stored under repo `backups\e3-quen-20260622-124218`.

## Deferred
The Yrden/Igni lighting variants from mod 2853 and New Signs FX Yrden from mod 8565 were not installed yet. They overlap in sign visual space and should be evaluated separately after Quen is confirmed in game.
