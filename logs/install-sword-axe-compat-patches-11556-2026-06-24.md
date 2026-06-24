# Sword and Axe Compatibility Patches 11556

Date: 2026-06-24

## Mod Page

Nexus: `https://www.nexusmods.com/witcher3/mods/11556`

This page provides compatibility patches for `Content Expansion - Time of the Sword and Axe`.

## Applied

Applied because these match the current stack:

- `Sword and Axe and Extra Skill Slots-11556-1-0-1765230402.rar`
- `Sword and Axe and Extra-REDUX gweent patch-11556-1-0-1767318094.rar`

The Gwent patch overwrote:

- `modexpansionzero\content\blob0.bundle`
- `modexpansionzero\content\metadata.store`
- `modexpansionzero\content\scripts\game\gui\menus\gwintManager.ws`

The Extra Skill Slots patch overwrote:

- `modexpansionzero\content\scripts\game\gameplay\ability\PlayerAbilityManager.ws`

## Skipped

Skipped for now:

- `Basic Cooking Recipes patch-11556-1-0-1768698173.rar`
  - No active Basic Cooking Recipes mod was found.
- `inventoryComponent-11556-1-0-1765403323.rar`
  - This touches a high-risk core file already owned by W3EE/BiA/merged files. Do not apply unless a specific error proves it is needed.

## Fixes Required After Applying

The patch exposed a few integration issues with the W3EE Redux stack.

Disabled duplicate or incompatible `modexpansionzero` local scripts:

- `local\effects\potions\tiara.ws`
- `local\gameplay\projectiles\ThrowingKnives.ws`
- `local\decoctions\mutagen60.ws`
- `local\decoctions\mutagen61.ws`
- `local\decoctions\mutagen70.ws`
- `local\decoctions\mutagen71.ws`
- `local\decoctions\mutagen72.ws`
- `local\decoctions\mutagen73.ws`
- `local\decoctions\mutagen74.ws`

Reason:

- W3EE already defines Tiara and throwing knives.
- The mutagen files depend on a vanilla-style `W3Mutagen_Effect` ownership path that is not visible in this priority stack.

Added Sword and Axe effect enum values to active higher-priority `effectTypes.ws` copies:

- `modIcyOcean`
- `modNobsReflex`
- `modW3EE`

Added values:

- `EET_Bindweed`
- `EET_Brock`
- `EET_Devries`
- `EET_DrunkennessPlus`
- `EET_Fisstech`
- `EET_Gadwall`
- `EET_Kiss`
- `EET_Lapwing`
- `EET_Rook`
- `EET_Shrike`
- `EET_StamPhiltre`
- `EET_Steroids`
- `EET_TirNaLia`
- `EET_Virga`
- `EET_VitalityRaise`
- `EET_Willow`
- `EET_WivesTears`
- `EET_Wolf`
- `EET_Wolverine`

Ported minimal drinking-system hooks:

- Added `playerDrinkingManager : PlayerDrinkingManager` to active `mod0000_MergedFiles` `r4Player.ws`.
- Initialized `playerDrinkingManager` during `OnSpawned`.
- Added `OnWasted()` to active W3EE `unconscious.ws`.

## Backups

Created backups under:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\SwordAxe_11556_patches_20260624_064844`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\SwordAxe_11556_disable_duplicates_20260624_065006`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\SwordAxe_11556_effecttypes_20260624_065213`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\SwordAxe_11556_drinking_hooks_20260624_065419`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\SwordAxe_11556_onwasted_20260624_065435`

## Verification

Smoke compile passed:

`SmokePassed_StillRunningAfter45s`

## Rule Learned

Compatibility patches can still expose hidden core-system ownership issues. Prefer:

1. Apply only patches matching installed mods.
2. Skip optional patches for absent mods.
3. Treat `inventoryComponent.ws`, `playerWitcher.ws`, `r4Player.ws`, `PlayerAbilityManager.ws`, and `effectTypes.ws` as high-risk.
4. Prefer small hook ports over replacing active W3EE/merged core files.
