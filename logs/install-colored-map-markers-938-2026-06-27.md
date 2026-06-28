# Install: Colored Map Markers - Next Gen (938)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/938
Archive: `C:\Users\marti\Downloads\Colored Map Markers - Next Gen-938-1-50-1779902790.zip`

## Decision

Installed the main Colored Map Markers package.

Skipped the downloaded SGUI compatibility patch from Nexus 8206 because the target stack is not installed.

## Why

The main archive is a bundle-only marker asset package:

- `modColoredMapMarkers/content/blob0.bundle`
- `modColoredMapMarkers/content/metadata.store`

It contains no `.ws` scripts and no menu XML.

The downloaded SGUI patch archive is:

- `mod00RestoredBuffedMonsters_CMM_SGUI`

That patch is not needed for the current stack. We do not have Smooth GUI or the target restored/buffed-monsters compatibility package active.

## Install

Installed:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modColoredMapMarkers`

Added to `mods.settings`:

```ini
[modColoredMapMarkers]
Enabled=1
Priority=14
```

Priority 14 places it below the active E3 HUD and Better Icons UI owners while still keeping it near the UI stack.

Backup path:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\colored-map-markers-938-20260627-224521`

## Validation

- Enabled mod count after install: 196.
- Enabled duplicate priority count stayed at the known baseline of 6.
- `modColoredMapMarkers` contains 0 `.ws` scripts.
- `modColoredMapMarkers` contains 0 menu XML files.
- SGUI patch folder was not installed.
- DX12 game launched and remained responding for 35 seconds.

## Residual Risk

Visual confirmation is still needed on the world map/minimap. If marker colors do not appear because E3 HUD wins overlapping bundled assets, the next test would be moving CMM above E3 HUD temporarily and comparing screenshots.
