# Assessment - Skellige Winter Weather System - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/4138`

## Downloads

Downloaded:

- `C:\Users\marti\Downloads\Skellige Winter Weather System - Next Gen and GOTY-4138-2-0-1672175067.rar`
- `C:\Users\marti\Downloads\Skellige Ice Breath Compatibility - Next Gen-4138-2-0-1672174955.rar`

## Current State

Already installed:

- `modSkelligeWinterWeather`

`mods.settings`:

- `modSkelligeWinterWeather`: priority `137`

The main archive also includes `dlcSkelligeWinterWeather`. That DLC component should be verified separately if needed, but the active mod folder and priority are already present in the weather stack.

## Optional Patch

The `Skellige Ice Breath Compatibility` archive contains:

- `modIceBreath`
- `local\ModICEBreath.ws`

It has one script file.

No installed Ice Breath base mod was found during local search, so the compatibility patch is not currently needed.

## Decision

Main mod: already installed.

Optional Ice Breath compatibility patch: not installed.

## Notes

If the Ice Breath base mod is installed later, revisit `modIceBreath` and run a script compile test.
