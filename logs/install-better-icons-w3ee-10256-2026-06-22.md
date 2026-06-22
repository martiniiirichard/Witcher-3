# Better Icons - Definitive Edition W3EE Install - 2026-06-22

## Goal
Install the W3EE-specific Better Icons package as the first pass, without adding generic Next Gen, Vlad UI, Friendly HUD, or E3 Better Icons compatibility patches.

## Installed Download
- `Better Icons - Definitive Edition (Next Gen) W3EE-10256-W3EE-1-4-2i-1767827107.7z`

## Installed Game Files
- `mods\modBetterIcons2025_NextGen_W3EE`
- `bin\config\r4game\user_config_matrix\pc\modBetterIcons.xml`

## Menu Filelist
Added `modBetterIcons.xml;` to:
- `bin\config\r4game\user_config_matrix\pc\dx11filelist.txt`
- `bin\config\r4game\user_config_matrix\pc\dx12filelist.txt`

## Priority Decision
Lower numeric priority wins in `mods.settings`.

- `modBetterIcons2025_NextGen_W3EE` placed below the E3 HUD W3EE patch pair:
  - `mod0_E3HUD_W3EER_NG`
  - `modE3HUD`
- Placed above `modReduxW3EE` and `modW3EE`.

This preserves the E3 HUD patch on files it must own, while allowing Better Icons W3EE to win against base W3EE on its icon/script files.

## Script Overlap Observed
Better Icons W3EE overlaps with W3EE on several UI/gameplay script paths and overlaps with `mod0_E3HUD_W3EER_NG` on:
- `game\gui\hud\modules\hudModuleRadialMenu.ws`
- `game\gui\menus\commonMenu.ws`
- `game\gui\menus\glossaryBestiaryMenu.ws`
- `game\gui\_old\components\guiBaseInventoryComponent.ws`

No Script Merger pass was performed before first launch because the current priority order allows the E3 HUD W3EE patch to keep its critical script files.

## Validation
- Archive contents inspected before install.
- First launch exposed missing W3EE popup callback methods because Better Icons W3EE overrides `alchemyMenu.ws` and `craftingMenu.ws`.
- Added the missing W3EE callback surface to Better Icons W3EE:
  - `IngredientSelectionPopupChangeIngredient`
  - `GetRequiredIngredientQuantityForPopup`
  - `GetAlchemistInventoryComponent`
  - `GetCraftsmanInventoryComponent`
- Second launch exposed a `ReplaceGridIngredient` signature mismatch.
- Updated Better Icons W3EE `ReplaceGridIngredient` in both `alchemyMenu.ws` and `craftingMenu.ws` to accept W3EE's optional popup item parameter.
- DX12 direct launcher started the game.
- `witcher3` process remained alive and responding after the initial launch window.

## Backup
- Install backup: `backups\better-icons-w3ee-10256-20260622-151540`
- Callback fix backup: `backups\better-icons-w3ee-10256-scriptfix-20260622-151748`
- ReplaceGridIngredient fix backup: `backups\better-icons-w3ee-10256-replacegridfix-20260622-151859`

## Deferred
- `E3.UI.and.HUD.Revamped.-.Better.Icons.Patch.zip`
- Generic Next Gen Better Icons package
- Vlad UI compatibility patch
- Friendly HUD compatibility patch

The E3 Better Icons patch should only be considered after confirming whether icons display correctly with the W3EE package alone.
