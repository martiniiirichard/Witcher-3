# Install - Weather and Lighting Stack

Date: 2026-06-23

## Installed In Order

Installed these visual/weather mods after Dense Rainfall, NextgenBetterFX, and Realistic Rain V3:

1. `mod_FilterlessToussaint`
2. `modRealisticWeather4`
3. `modSkelligeWinterWeather` + `dlcSkelligeWinterWeather`
4. `modPromotionalAtmosphereLighting` + `modprobetest` + `dlcPromotionalAtmosphereLighting`
5. New Lightning FX alternative `weathers_list.ws`

## Sources

- `C:\Users\marti\Downloads\Filterless Toussaint.rar`
- `C:\Users\marti\Downloads\Realistic Weather 4.0-2084-4-0-1673889087.zip`
- `C:\Users\marti\Downloads\Skellige Winter Weather System - Next Gen and GOTY-4138-2-0-1672175067.rar`
- `C:\Users\marti\Downloads\Promotional Atmosphere Lighting Mod V2-10322-2-0-1767199114.7z`
- `C:\Users\marti\Downloads\New Lightning FX - Alternative Script For Weathers-2985-3-0-1780921783.7z`

## Load Order

Added to:

`C:\Games\The Witcher 3\mods.settings`

```ini
[mod_FilterlessToussaint]
Enabled=1
Priority=135

[modRealisticWeather4]
Enabled=1
Priority=136

[modSkelligeWinterWeather]
Enabled=1
Priority=137

[modPromotionalAtmosphereLighting]
Enabled=1
Priority=138

[modprobetest]
Enabled=1
Priority=139
```

Created timestamped backups of `mods.settings` before each load-order edit.

## Script Change

Replaced:

`mods\modnewlightningfx\content\scripts\local\weathers_list.ws`

with the alternative weather-compatible script from:

`New Lightning FX - Alternative Script For Weathers`

Created a timestamped backup of the previous static weather list:

`weathers_list.ws.codex-backup-static-weather-list-<timestamp>`

Reason: the previous script only activated New Lightning FX for a small static storm list. The alternative script reads the current region weather CSV and enables lightning for weather rows where `backgroundThunder` is `TRUE`, which is better for weather overhauls.

## Verification

Static checks:

- `mod_FilterlessToussaint`: 0 scripts.
- `modRealisticWeather4`: 0 scripts.
- `modSkelligeWinterWeather`: 0 scripts.
- `dlcSkelligeWinterWeather`: valid `content\metadata.store`.
- `modPromotionalAtmosphereLighting`: 0 scripts.
- `modprobetest`: 0 scripts.
- `dlcPromotionalAtmosphereLighting`: valid `content\metadata.store`.
- Game `dlc` root stayed clean; only the known pre-existing `DLCScabbards` package lacks metadata.

Runtime smoke checks:

- After Filterless Toussaint: `witcher3.exe` alive after 45 seconds.
- After Realistic Weather: `witcher3.exe` alive after 45 seconds.
- After Skellige Winter Weather: `witcher3.exe` alive after 45 seconds.
- After Promotional Atmosphere Lighting: `witcher3.exe` alive after 60 seconds.
- After New Lightning FX alternative weather script: `witcher3.exe` alive after 60 seconds.

## Deferred

Skipped `Skellige Ice Breath Compatibility - Next Gen` because the actual Ice Breath base mod is not currently installed.

## Residual Risk

This validates launch/load and script compilation. The remaining risk is visual priority/quality interaction across:

- Dense Rainfall
- Realistic Rain V3
- NextgenBetterFX
- Realistic Weather
- Skellige Winter Weather
- Promotional Atmosphere Lighting
- Filterless Toussaint
- New Lightning FX

Visual QA should check Novigrad/Velen, Skellige, Toussaint, rain, storm, dusk/night, and interiors.
