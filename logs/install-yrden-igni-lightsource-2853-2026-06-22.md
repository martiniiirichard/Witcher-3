# Yrden and Alt Igni Lightsource Install - 2026-06-22

## Goal
Install the selected mod 2853 variant for sign lighting without mixing it with New Signs FX yet.

## Installed Download
- `Yrden and Alt Igni 2013 icon Lightsource (Dimmer Flare)-2853-1-1-1593183518.7z`

## Installed Game Folders
- `mods\modYrdenAndIgni2013LightSourceDimmerFlare`
- `DLC\DLCYrdenAndIgni2013LightSourceDimmerFlare`

## Priority Decision
Lower numeric priority wins in `mods.settings`.

- The mod was placed after the E3 Quen visual entries.
- W3EE Redux and W3EE remain higher priority.
- New Signs FX Yrden was not installed in this pass because it overlaps with Yrden visuals.

## Validation
- Archive contents inspected before install.
- No `.ws` scripts were introduced.
- No Script Merger pass required.
- DX12 direct launcher started the game.
- `witcher3` process remained alive and responding after the initial launch window.

## Backup
- Pre/post `mods.settings` backup and any replaced 2853 folders were stored under repo `backups\yrden-igni-lightsource-2853-20260622-140800`.

## Deferred
- `New Signs Fx - Yrden-8565-1-0-1696986600.rar`
- Other mod 2853 variants, which are mutually exclusive with the selected dimmer-flare combined version.
