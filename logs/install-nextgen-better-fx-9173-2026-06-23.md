# Install - NextgenBetterFX 9173

Date: 2026-06-23

## Source

Downloaded archive:

`C:\Users\marti\Downloads\NextgenBetterFX-9173-12-5-1-1771698366.zip`

Staging folder:

`staging\nextgen-better-fx-9173-20260623`

## Installed Payload

Installed:

- `mods\modnextgenbetterfx`
- `dlc\dlcshore`

Payload summary:

- `modnextgenbetterfx`: 8 files, 0 scripts.
- `dlcshore`: 4 files, 0 scripts.
- `dlcshore` includes `content\metadata.store`.

No Script Merger work expected.

## Load Order

Added to:

`C:\Games\The Witcher 3\mods.settings`

```ini
[modnextgenbetterfx]
Enabled=1
Priority=133
```

Created a timestamped backup of `mods.settings` before editing.

## Verification

Static checks:

- Confirmed no `.ws` scripts in either installed payload.
- Confirmed `dlcshore\content\metadata.store` exists.
- Game `dlc` root stayed clean; only the known pre-existing `DLCScabbards` package lacks metadata.

Runtime smoke:

- Launched `Witcher3DirectDX12.exe`.
- `witcher3.exe` was alive and responding after 60 seconds.
- Closed the game after the smoke test.

## Residual Risk

This validates launch/load only. NextgenBetterFX is a large visual/shader/texture mod, so visual QA is still needed in multiple regions and lighting/weather conditions. It may visually overlap with later atmosphere, weather, RT, and lighting mods.
