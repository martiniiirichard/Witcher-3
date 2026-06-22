# Unofficial AMM Additions - The Tailory 2448 Install

Date: 2026-06-22

## Source

- Nexus: https://www.nexusmods.com/witcher3/mods/2448
- Main file: `The Griffon Update 2.2-2448-2-2.rar`
- Optional file: `Stag Helmet Replacer-2448-1.rar`

## Page Notes

- Requires AMM to be installed and working.
- Author reports multiple Next-Gen compatibility confirmations.
- Install instructions say to drop folders into the game directory and overwrite when prompted.
- Because this stack has a patched AMM, the AMM files were grafted instead of overwritten.

## Runtime Changes

Installed main Tailory content folders:

- `dlc/ac_dlc`
- `dlc/armor_of_george`

Installed optional Stag Helmet Replacer:

- `mods/modBaratheon`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modBaratheon]
Enabled=1
Priority=21
```

## AMM Compatibility Graft

The archive includes older AMM replacements:

- `mods/modAMM/content/scripts/local/AMM.ws`
- `bin/config/r4game/user_config_matrix/pc/AMM.xml`

These were not copied over directly because the active AMM already contains compatibility work for:

- AMM async loading
- AMM + W3EE Redux
- Shades of Iron
- New Hairstyles and Beards

Instead, Tailory-only additions were grafted into the active AMM files.

Script additions were appended into these AMM arrays:

- `HeadGearArrayInit`
- `ArmsArrayInit`
- `AccessoriesArrayInit`
- `CChestGearArrayInit`
- `CGlovesGearArrayInit`
- `ClegsGearArrayInit`
- `CBootsGearArrayInit`

Menu additions were appended into:

- `HeadGearSelection`
- `ArmsSelection`
- `Accessories1GearSelection` through `Accessories10GearSelection`
- `CChestSelection`
- `CGlovesSelection`
- `CLegsSelection`
- `CBootsSelection`

The graft appends new option IDs after the current active IDs to avoid renumbering existing AMM, Shades of Iron, and hairstyle options.

## Backup

- `backups/tailory-2448-20260622-103836`

## Verification

- Main archive size matched Nexus files tab: about 125.7 MB.
- Confirmed `dlc/ac_dlc` and `dlc/armor_of_george` exist in the game root.
- Confirmed optional `modBaratheon` exists and is enabled at priority `21`.
- Confirmed Tailory AMM script paths such as `armor_of_george`, `ac_dlc`, and `s_02_mg__george` exist in active `AMM.ws`.
- Confirmed Tailory menu options such as `0780_Griffon1`, `0780_Crest1`, and `0780_Armor_of_George` exist in active `AMM.xml`.
- Script Merger: no new standalone script-conflict mod was added; changes were grafted into existing `modAMM`.
- Game launch: passed after active AMM script/config graft.
