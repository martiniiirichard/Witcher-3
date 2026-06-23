# Install - Live Bestiary 2937

Date: 2026-06-23

## Source

Downloaded archive:

`C:\Users\marti\Downloads\LiveBestiary-2937-2.zip`

Staging folder:

`staging\live-bestiary-2937-20260623`

## Installed Payload

Installed:

- `mods\modLiveBestiary`
- `dlc\DLCLiveBestiary`

Copied `lbTable.csv` to both:

- `dlc\globals\lbTable.csv`
- `dlc\dlclb\data\gameplay\globals\lbTable.csv`

The first path is the active path used by `mod0_E3HUD_W3EER_NG`; the second path mirrors the original Live Bestiary script path for rollback/compatibility.

## Script Strategy

Did not allow the original old Live Bestiary script to participate in script loading.

Renamed:

`mods\modLiveBestiary\content\scripts`

to:

`mods\modLiveBestiary\content\scripts.disabled-by-codex`

Reason: the current stack already has Live Bestiary support inside:

`mods\mod0_E3HUD_W3EER_NG\content\scripts\game\gui\menus\glossaryBestiaryMenu.ws`

That E3/W3EE-aware script reads:

`LoadCSV( "dlc\globals\lbTable.csv" )`

This avoids introducing a new conflict against W3EE, E3 HUD, and Better Icons bestiary menu scripts.

## Settings

Added to:

`C:\Games\The Witcher 3\mods.settings`

```ini
[modLiveBestiary]
Enabled=1
Priority=128
```

Added to:

`C:\Games\The Witcher 3\dx12user.settings`

```ini
[E3HudMenu]
version=1
video=true
map=true
minimap=true
loading=0
livebestiray=true
```

Note: `livebestiray` is the typo used by the E3 HUD config and script.

## Backups

Created timestamped backups of:

- `C:\Games\The Witcher 3\mods.settings`
- `C:\Games\The Witcher 3\dx12user.settings`

## Verification

Static checks:

- Confirmed `mods\modLiveBestiary\content\scripts` does not exist.
- Confirmed `scripts.disabled-by-codex` exists for reference/rollback.
- Confirmed `dlc\globals\lbTable.csv` exists.
- Confirmed `mod0_E3HUD_W3EER_NG` still points at `dlc\globals\lbTable.csv`.

Runtime smoke:

- Launched `Witcher3DirectDX12.exe`.
- `witcher3.exe` was alive and responding after 45 seconds.
- Closed the game after the smoke test.

## Residual Risk

This proves the game compiles and launches, but not that every Bestiary entry renders correctly. Known upstream risk from this old mod on Next Gen 4.04: some monster models can appear bald, missing parts, or angled oddly.
