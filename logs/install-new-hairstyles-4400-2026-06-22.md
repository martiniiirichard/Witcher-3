# New Hairstyles And Beards Install Checkpoint

Date: 2026-06-22

## Mod

- Nexus: `https://www.nexusmods.com/witcher3/mods/4400`
- Mod name: `New Hairstyles and Beards For Geralt (DLC2 Improved)`
- Version: `3.0.2`
- Archive: `New Hairstyles and - BiA-4400-3-0-2-1771845621.zip`
- AMM bridge archive: `DLC2 Improved for AMM-7598-1-0-1673202652.zip`

## Runtime Changes

Installed:

- `mods/modNewHairstylesAndBeards`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modNewHairstylesAndBeards]
Enabled=1
Priority=19
```

## AMM Integration

The AMM bridge archive contains full replacements for:

- `mods/modAMM/content/scripts/local/AMM.ws`
- `bin/config/r4game/user_config_matrix/pc/AMM.xml`

Those files were not overwritten wholesale because the current AMM stack already includes Shades of Iron, Swords on Roach, and AMM async-loading changes.

Instead:

- `HairArrayInit()` was grafted from the bridge into the installed `AMM.ws`.
- `AltHairArrayInit()` was grafted from the bridge into the installed `AMM.ws`.
- Only the `AMMHead` group was replaced in `AMM.xml`.

## Backup

Runtime backup created before install:

- `backups/new-hairstyles-4400-20260622-101133`

## Verification

- Confirmed `modNewHairstylesAndBeards` exists in the game root.
- Confirmed `mods.settings` contains the enabled priority entry.
- Confirmed AMM now includes DLC2 Improved hair entries such as `Ard Rivian Tail Hairstyle`.
- Confirmed no new script conflicts appeared beyond the existing baseline conflicts.
- Launched with the direct DX12 launcher.
- User confirmed launch passes.

Next step: commit this working checkpoint before installing additional mods.
