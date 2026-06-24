# No Enemy Dots And No Herbs - NGE 1369

Date: 2026-06-23

## Source

- https://www.nexusmods.com/witcher3/mods/1369

## Installed Download

- `C:\Users\marti\Downloads\No Enemy Dots And No Herbs - NGE-1369-1-40-1686918606.zip`

## Installed Game Folder

- `mods\modNoEnemyDotsAndNoHerbs`

## Load Order

Added to both active `mods.settings` copies:

- `modNoEnemyDotsAndNoHerbs`: priority `202`

## Script Merger

No Script Merger pass needed. The archive contains bundled content only and no `.ws` scripts.

## Verification

- Confirmed the mod folder exists under `mods`.
- DX12 smoke test passed when launching `bin\x64_dx12\witcher3.exe` with its own working directory; process stayed alive for 45 seconds and was killed manually.

## Notes

- Expected behavior: enemy dots and herb markers are hidden from the minimap/HUD layer this mod edits.
- Main residual risk is UI/marker overlap with other HUD and map mods, especially Colored Map Markers or E3 HUD-related assets.
