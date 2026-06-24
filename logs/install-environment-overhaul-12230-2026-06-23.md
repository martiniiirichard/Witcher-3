# Environment Overhaul 12230

Date: 2026-06-23

## Source

- https://www.nexusmods.com/witcher3/mods/12230

## Installed Download

- `C:\Users\marti\Downloads\Environment Overhaul-12230-1-2-1780820299.zip`

Earlier this file was incomplete/zero-byte; it was later redownloaded successfully at about `3.5 GB`.

## Installed Game Folder

- `mods\modenvironmentoverhaul`

## Load Order

Added to both active `mods.settings` copies:

- `modenvironmentoverhaul`: priority `204`

This is intentionally higher than HDRP and HDMR. The mod page notes that when used with HDRP, Environment Overhaul should have the highest priority so its terrain/rock texture changes win.

## Script Merger

No Script Merger pass needed. The archive contains bundled content only and no `.ws` scripts.

## Extraction Note

7-Zip reported:

- `Headers Error`

But it also reported:

- `Everything is Ok`
- `Files: 6`

Installed folder verification also found six files and the expected `content\texture.cache`.

## Verification

- Installed folder exists under `mods`.
- Installed size is about `3.267 GB`.
- DX12 smoke test passed when launching `bin\x64_dx12\witcher3.exe` with its own working directory; process stayed alive for 45 seconds and was killed manually.

## Residual Risk

- This mod overlaps visually with HDRP and other terrain/rock/vegetation texture work.
- Visual QA target: Velen/White Orchard/Skellige terrain, rocks, cliffs, roads, cave walls, and shoreline transitions. Toussaint is expected to be less affected or excluded.
