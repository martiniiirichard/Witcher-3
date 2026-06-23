# Install - Dense Rainfall 3272

Date: 2026-06-23

## Source

Downloaded archive:

`C:\Users\marti\Downloads\DenseRainfall-3272-1-0.zip`

Staging folder:

`staging\dense-rainfall-3272-20260623`

## Installed Payload

Installed:

`mods\modDenseRainfall`

Payload contents:

- `content\blob0.bundle`
- `content\metadata.store`

No scripts were present.

## Load Order

Added to:

`C:\Games\The Witcher 3\mods.settings`

```ini
[modDenseRainfall]
Enabled=1
Priority=132
```

Created a timestamped backup of `mods.settings` before editing.

## Verification

Static checks:

- `modDenseRainfall`: 2 files, 0 scripts.
- No Script Merger work expected.
- Game `dlc` root stayed clean; only the known pre-existing `DLCScabbards` package lacks metadata.

Runtime smoke:

- Launched `Witcher3DirectDX12.exe`.
- `witcher3.exe` was alive and responding after 45 seconds.
- Closed the game after the smoke test.

## Residual Risk

This validates launch/load only. Visual confirmation still needs rainy weather in-game. Later weather/rain mods may overwrite or conflict visually with this.
