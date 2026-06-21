# AMM - Swords on Roach Next-Gen Patch Review - 2026-06-21

## Nexus Pages

- Patch: `https://www.nexusmods.com/witcher3/mods/10830`
- Base requirement: `https://www.nexusmods.com/witcher3/mods/3952`

## Decision

Do not install `10830` by itself. It is only an AMM compatibility patch for Swords on Roach.

## Requirements

Patch `10830` requires:

- AMM - The Appearances Menu Mod
- Swords on Roach

AMM is already installed and confirmed working. Swords on Roach is not currently installed and was not found in Downloads.

## Download Found

- `Next-Gen Compatibility Patch-10830-1-0-1747366393.zip`

Extracted contents:

- `readme.txt`
- `swordsonroach.ws`

Patch readme:

```text
Drop the swordsonroach.ws file into [Game Directory]/Mods/modSwordsonroach/content/scripts/local
```

## Required Install Order

1. Download/install base Swords on Roach first.
2. Add `modASwordsonroach.xml;` to both Next-Gen filelists:
   - `bin\config\r4game\user_config_matrix\pc\dx11filelist.txt`
   - `bin\config\r4game\user_config_matrix\pc\dx12filelist.txt`
3. Overlay patch `10830` by replacing/adding:
   - `mods\modSwordsonroach\content\scripts\local\swordsonroach.ws`
4. Review script conflicts against AMM/W3EE Redux before launch.
5. Launch-test before committing the install log.

## Notes

The base Swords on Roach page says the mod is merge-free and installed by extracting `bin`, `dlc`, and `mods` into the game root, then adding `modASwordsonroach.xml;` to the Next-Gen filelists.

The base page also warns:

- Take swords back from Roach before some quests, especially `Open Sesame`.
- Some clipping is unavoidable.
- It is not compatible with Magical (un)sheathing of weapons.
- It is not compatible with W3EE - Lazarus Project.

No install was performed because the base Swords on Roach archive is missing.
