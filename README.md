# Witcher 3 Mod Deployment

Lightweight deployment repo for The Witcher 3 modding on the local GOG install.

## Current Target

- Game root: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY`
- Platform: GOG GOTY / Next-Gen capable install
- Primary executable: `bin\x64_dx12\witcher3.exe`
- Current detected game executable version: `4.0.0.103190`
- Mod target: W3EE Redux `1.46`
- Required dependency for Next-Gen: Community Patch - Shared Imports `v0.6`

## Source Links

- W3EE Redux: https://www.nexusmods.com/witcher3/mods/5802
- Community Patch - Shared Imports: https://www.nexusmods.com/witcher3/mods/2110

## Repo Policy

Do not commit:

- The base game files.
- Nexus archive downloads.
- Extracted mod payloads.
- Generated backups.
- External tools.

Commit:

- Install notes.
- Mod/version manifests.
- Script Merger notes.
- Load order decisions.
- Local scripts that make the install repeatable.
- Known errors and fixes.

## Recommended Install Line

1. Launch the game once to create `Documents\The Witcher 3`.
2. Download these Nexus files manually into local `downloads/`:
   - `Community Patch - Shared Imports`
   - `Redux for W3EE (NextGen)` unless choosing the lighter build deliberately.
3. Back up game config and `Documents\The Witcher 3`.
4. Install Shared Imports first.
5. Install W3EE Redux second.
6. Copy Redux `input.settings` into `Documents\The Witcher 3`.
7. Add Redux menu XML entries to `dx12filelist.txt` and, if using DX11, `dx11filelist.txt`.
8. Run the game and resolve script compilation conflicts before adding any other mods.

## Decision

Do not copy the base game into this repo. The stronger versioning model is manifest-driven: keep the GOG install as the deploy target, keep archives local-only, and version the exact steps, deltas, and troubleshooting notes here.
