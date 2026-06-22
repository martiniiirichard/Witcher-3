# New Signs FX - Yrden Install - 2026-06-22

## Goal
Install mod 8565 as a separate visual pass after confirming the 2853 Yrden/Igni lightsource mod.

## Installed Download
- `New Signs Fx - Yrden-8565-1-0-1696986600.rar`

## Installed Game Folder
- `mods\modNewSignsFXYrden`

## Priority Decision
Lower numeric priority wins in `mods.settings`.

- `modNewSignsFXYrden` was placed after `modYrdenAndIgni2013LightSourceDimmerFlare`.
- W3EE Redux, W3EE, E3 Quen, and the 2853 lightsource mod remain above it.
- This lets the New Signs FX Yrden visual bundle win only where it is loaded later in the visual cluster, while keeping core gameplay/script mods untouched.

## Validation
- Archive contents inspected before install.
- No `.ws` scripts were introduced.
- No Script Merger pass required.
- DX12 direct launcher started the game.
- `witcher3` process remained alive and responding after the initial launch window.

## Backup
- Pre/post `mods.settings` backup and any replaced `modNewSignsFXYrden` folder were stored under repo `backups\new-signs-fx-yrden-8565-20260622-141203`.

## Risk
This mod overlaps visually with Yrden. If the in-game effect looks too busy or visually wrong, remove `modNewSignsFXYrden` and its `mods.settings` entry rather than changing scripts or merged files.
