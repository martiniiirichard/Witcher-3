# Preinstall Check - 2026-06-21

## Game Install

- Root: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY`
- Detected executables:
  - `bin\x64\witcher3.exe`
  - `bin\x64_dx12\witcher3.exe`
- Detected executable version: `4.0.0.103190`
- No existing `mods` folder detected.
- No `Documents\The Witcher 3` folder detected yet.

## Downloaded Archives Found

- `C:\Users\marti\Downloads\modSharedImports-v0.6 - NEXT-GEN.zip-2110-v0-6-1720539533.zip`
  - Status: compatible dependency candidate.
  - Contains `mods/modSharedImports/...`.
- `C:\Users\marti\Downloads\Redux for W3EE (OldGen).zip`
  - Status: blocked for this install.
  - Reason: current game install is Next-Gen 4.x; this archive is explicitly OldGen.
  - Contains `mods/modReduxW3EE`, `dlc/dlcW3EE`, menu XML files, and `input.settings`, but should not be deployed to this game branch.

## Decision

Do not install yet. Download `Redux for W3EE (NextGen)` from W3EE Redux before modifying the game directory.
