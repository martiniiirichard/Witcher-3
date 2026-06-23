# Install - Realistic Rain V3 10942

Date: 2026-06-23

## Source

Downloaded archive:

`C:\Users\marti\Downloads\Realistic Rain V3-10942-1-2-1750125428.rar`

Staging folder:

`staging\realistic-rain-v3-10942-20260623`

## Installed Payload

Installed:

`mods\modRealisticRainV3`

Payload contents:

- `content\blob0.bundle`
- `content\metadata.store`
- `content\texture.cache`
- `ReadMe.txt`

No scripts were present.

## Load Order

Added to:

`C:\Games\The Witcher 3\mods.settings`

```ini
[modRealisticRainV3]
Enabled=1
Priority=134
```

Created a timestamped backup of `mods.settings` before editing.

## Verification

Static checks:

- `modRealisticRainV3`: 4 files, 0 scripts.
- No Script Merger work expected.
- Game `dlc` root stayed clean; only the known pre-existing `DLCScabbards` package lacks metadata.

Runtime smoke:

- First 45-second launch check did not find `witcher3.exe` alive.
- No obvious script error log surfaced.
- Retried launch for 75 seconds.
- On retry, `witcher3.exe` was alive and responding.
- Closed the game after the successful retry.

## Residual Risk

This validates launch/load after retry only. Visual confirmation still needs rainy weather in-game. This mod may overlap visually with `modDenseRainfall` and any later weather/atmosphere mods.
