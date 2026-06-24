# HD Monsters Reworked 5.0 NextGen 3580

Date: 2026-06-23

## Source

- https://www.nexusmods.com/witcher3/mods/3580

## Installed Downloads

- `C:\Users\marti\Downloads\HD Monsters Reworked 5.0 Next Gen - Part 1-3580-5-0-1679834194.7z`
- `C:\Users\marti\Downloads\1- HD Monsters Reworked 5.0 Next Gen - Part 2-3580-5-0-1679836281.7z`
- `C:\Users\marti\Downloads\HDMR 5 LOD Optimization Next Gen-3580-5-0-1678619941.7z`

## Installed Game Folders

- `mods\modHDMonstersReworked5`
- `mods\modHDMonstersReworked5_Exp`
- `mods\modHDMR5_LOD`

## Load Order

Added to both active `mods.settings` copies:

- `modHDMonstersReworked5`: priority `195`
- `modHDMonstersReworked5_Exp`: priority `196`
- `modHDMR5_LOD`: priority `197`

The LOD optimization is intentionally loaded after the two HDMR content folders so it can override matching distance/LOD records.

## Script Merger

No Script Merger pass needed. The archive contents are bundled texture/cache/metadata content only and include no `.ws` scripts.

## Verification

- Confirmed the three HDMR folders exist under `mods`.
- Installed size summary:
  - `modHDMonstersReworked5`: about `4.187 GB`, `3` files.
  - `modHDMonstersReworked5_Exp`: about `2.872 GB`, `3` files.
  - `modHDMR5_LOD`: about `0.096 GB`, `3` files.
- DX12 smoke test passed when launching `bin\x64_dx12\witcher3.exe` with its own working directory; process stayed alive for 45 seconds and was killed manually.

## Notes

- This is a content-only monster texture/mesh pass, so the main residual risk is visual overlap with other creature/NPC appearance mods rather than script instability.
- Inspect common monsters and DLC monsters in a loaded save later if doing a visual QA pass.
