# Safe Batch: DWS, Fast Travel Pack, Killing Monsters Cloak

Date: 2026-06-22

Installed:
- Dynamic Witcher Schematics for W3EE Redux
  - Archive: `Dynamic Witcher Schematics for W3EE Redux-5826-1-32-1657832016.7z`
  - Folder: `mods/modDynamicWitcherSchematics`
- Fast Travel Pack
  - Archive: `Fast Travel Pack-7202-2-0-1-1764407323.zip`
  - Folders: `mods/modFastTravelPack`, `dlc/dlcFastTravelPack`
  - Menu: `bin/config/r4game/user_config_matrix/pc/FastTravelPack.xml`
- Killing Monsters Cloak
  - Archive: `Killing Monsters Cloak-4751-3-3-1769130189.zip`
  - Folders: `mods/mod_KillingMonstersCloak`, `dlc/dlc_KillingMonstersCloak`

Configuration:
- Added `FastTravelPack.xml;` to both `dx11filelist.txt` and `dx12filelist.txt`.
- Appended Killing Monsters Cloak `ToggleCloak` bindings to `C:\Games\The Witcher 3\input.settings`.
- Added explicit `mods.settings` entries:
  - `modDynamicWitcherSchematics` at priority `118`
  - `modFastTravelPack` at priority `119`
  - `mod_KillingMonstersCloak` at priority `120`

Menu polish:
- Shortened WPI's mod menu label from localized `Mods.wpi_name` to literal `Pocket Items` in `WPI.xml`.
- Reason: the original `Wearable Pocket Items` title wrapped in the Mods menu and visually overlapped `Fast Travel Pack`.

Backups:
- `tools/backups/before-safe-batch-dws-ftp-kmc-20260622-223903`

Validation:
- New active scripts from this batch are local-only:
  - `modFastTravelPack/content/scripts/local/ftpack_modMenu.ws`
  - `mod_KillingMonstersCloak/content/scripts/local/mod_KillingMonstersCloak_Annotations.ws`
  - `mod_KillingMonstersCloak/content/scripts/local/mod_KillingMonstersCloak_Keybind.ws`
- `mods.settings` after install: 120 sections, 120 priorities, no duplicate sections/priorities.
- User confirmed game launch passed.
