# Geralt In Brothel 5384

Date: 2026-06-23

## Source

- https://www.nexusmods.com/witcher3/mods/5384

The Nexus description was behind the adult-content gate in the browser, so the local archive contents were used as the install source of truth.

## Installed Download

- `C:\Users\marti\Downloads\Geralt In Brothel 3.1-5384-3-1-1611256856.7z`

## Installed Game Folder

- `mods\modGeraltInBrothel`

## Load Order

Added to both active `mods.settings` copies:

- `modGeraltInBrothel`: priority `212`

## Script Merger

No Script Merger pass needed. The archive contains bundled content only:

- `content\blob0.bundle`
- `content\metadata.store`

## Verification

- Confirmed the mod folder exists under `mods`.
- DX12 smoke test passed when launching `bin\x64_dx12\witcher3.exe` with its own working directory; process stayed alive for 45 seconds and was killed manually.

## Residual Risk

- Main risk is visual overlap with the Naked Geralt/body scene stack installed immediately before this.
- Visual QA target: brothel scenes and any Geralt nude/body state used there.
