# Brothel Addicted Core 3201

Date: 2026-06-23

## Source

- https://www.nexusmods.com/witcher3/mods/3201

The Nexus description was behind the adult-content gate in the browser, so local archive contents were used as the install source of truth.

## Installed Download

- `C:\Users\marti\Downloads\Brothel Addicted Main File 1.2.2-3201-1-2-2-1608562378.zip`

## Installed Game Folder

- `mods\modBrothel2`

## Load Order

Added to both active `mods.settings` copies:

- `modBrothel2`: priority `214`

## Script Merger

No Script Merger pass needed. The main archive contains bundled content only:

- `content\blob0.bundle`
- `content\metadata.store`

## Optional Appearance Packs Downloaded

Multiple optional appearance variants were downloaded but not installed automatically because several are mutually exclusive for the same NPC.

Downloaded option groups include:

- Amrynn: `Amrynn 1`, `Amrynn 2`, `Amrynn 3`
- Viola: `Viola 1`, `Viola 2`, `Viola 3`
- Susy/Suzy: `Susy`, `Suzy 2`
- Mercia/Marcia: `Mercia`, `Mercia 2`
- Narcissa: `Narcissa 1`, `Narcissa 3`
- Bertha: `Bertha 1`, `Bertha 2`
- Belles of Beauclair courtisans: `Courtisan 1`, `Courtisan 2`, `Courtisan 2b`, `Courtisan 3`, `Courtisan 3b`

Each inspected optional archive was content-only, but variants for the same NPC should be installed one-at-a-time by preference.

## Verification

- Confirmed the core mod folder exists under `mods`.
- DX12 smoke test passed when launching `bin\x64_dx12\witcher3.exe` with its own working directory; process stayed alive for 45 seconds and was killed manually.

## Residual Risk

- This is core-only; optional NPC appearances remain uninstalled.
- Main risk is visual/content overlap with other brothel/NPC/body mods, especially `modGeraltInBrothel` and the Naked Geralt stack.
- Visual QA target: brothel locations and NPCs affected by the mod.
