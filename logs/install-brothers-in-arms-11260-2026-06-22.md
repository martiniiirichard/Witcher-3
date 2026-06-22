# Brothers In Arms Ultimate Edition 11260 Install

Date: 2026-06-22

## Source

- Nexus: https://www.nexusmods.com/witcher3/mods/11260
- Main file: `Brothers In Arms - Ultimate Edition-11260-3-1-2-1772472350.zip`
- Optional LOD file: `Brothers In Arms - LOD Fixes-11260-3-1-0-lod-1770398542.zip`
- W3EER compatibility patch: `W3EER - BiA Compatibility Patch.zip`
- Related add-on already downloaded: `New Hairstyles and - BiA-4400-3-0-2-1771845621.zip`

## Runtime Changes

Installed:

- `mods/modBrothersInArms`
- `mods/modZBrothersInArmsLOD`
- `mods/mod000_Patch_BIA-W3EER`
- `mods/mod_sharedutils_menudescriptors`
- `mods/modNewHairstylesAndBeards` BiA add-on overwrite
- `dlc/dlcBrothersInArms1`
- `dlc/dlcBrothersInArms2`
- `dlc/dlcBrothersInArms3`
- `bin/config/r4game/user_config_matrix/pc/BrothersInArms.xml`

Updated:

- `dx11filelist.txt` and `dx12filelist.txt` now include `BrothersInArms.xml;`
- `C:\Games\The Witcher 3\mods.settings` now loads `mod0000_MergedFiles` first and `mod000_Patch_BIA-W3EER` second.

## Compatibility Patch Instructions Applied

Deleted from BiA after installing the compatibility patch:

- `mods/modBrothersInArms/content/scripts/game/gameplay/damage/damageManagerProcessor.ws`
- `mods/modBrothersInArms/content/scripts/game/gameplay/projectile/signs/signProjectiles.ws`

Ignored non-mergeable conflicts where the compatibility patch is expected to win by priority.

## Manual Merge Notes

Script Merger/KDiff3 failed to emit output reliably, so the two documented script merges were created manually in:

- `mods/mod0000_MergedFiles/content/scripts/game/components/inventoryComponent.ws`
- `mods/mod0000_MergedFiles/content/scripts/game/vehicles/vehicleComponent.ws`

Merge strategy:

- `vehicleComponent.ws`: clean W3EE + BiA three-way merge.
- `inventoryComponent.ws`: W3EE + BiA three-way merge, then replaced `SingletonItemGetMaxAmmo` with the BiA/Shades-compatible body so Shades of Iron `GetCurioWatcher().GetAdditionalAmmo(itemID)` is preserved.
- Removed the BiA/Shades `EET_Mutagen03` ammo branch from the merged inventory script because this installed W3EE Redux build does not define that enum, causing compile failure.

Preserved required behavior:

- W3EE potion removal in `SingletonItemRemoveAmmo`.
- BiA `ManageSingletonItemsBonus` current/max ammo logic.
- Shades of Iron CurioWatcher ammo bonus.

## Backup

- `backups/brothers-in-arms-11260-20260622-112353`

## Verification

- Confirmed `mod0000_MergedFiles` contains the two merged scripts.
- Confirmed merged scripts have no conflict markers.
- Confirmed `mods.settings` priority order starts with:
  - `mod0000_MergedFiles`
  - `mod000_Patch_BIA-W3EER`
  - existing stack shifted down by one.
- First launch produced compile error:
  - `Error [mod0000_mergedfiles]game\components\inventoryComponent.ws(6082): I dont know any 'EET_Mutagen03'`
- Removed the incompatible `EET_Mutagen03` branch.
- Relaunched via direct DX12 launcher; game reached main window with no script compilation error.
