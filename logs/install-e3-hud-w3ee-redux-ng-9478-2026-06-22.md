# E3 HUD + W3EE Redux NG Patch Install - 2026-06-22

## Goal
Install E3 HUD for the W3EE Redux NG stack using the minimal Nexus path, without introducing the broader GitHub Revamped/Nudel script bundle.

## Installed Downloads
- `E3 Hud and UI 1.2-2996-1-2.rar`
- `E3 UI Nudel Update Patch for W3EE Redux NG 1.40-9478-1-0-3-1728405522.7z`

## Installed Game Files
- `mods\modE3HUD`
- `mods\mod0_E3HUD_W3EER_NG`
- `DLC\dlc_e3`
- `bin\config\r4game\user_config_matrix\pc\e3hud.xml`

## Required Install Adjustment
Per the 9478 instructions, removed:
- `mods\modE3HUD\content\scripts`

The removed scripts were backed up before deletion.

## Priority Decision
Lower numeric priority wins in `mods.settings`.

- `mod0_E3HUD_W3EER_NG` placed above `modE3HUD`.
- Both placed above `modReduxW3EE` and `modW3EE`.
- Existing merge and W3EE compatibility patches remain above the E3 HUD pair.

## Compile Fixes
The first launch failed because `mod0_E3HUD_W3EER_NG` shadows W3EE HUD/inventory scripts but did not preserve a few W3EE helper members expected by lower-priority W3EE scripts.

Patched:
- `mods\mod0_E3HUD_W3EER_NG\content\scripts\game\gui\hud\modules\hudModuleMinimap2.ws`
  - restored W3EE helper state/methods:
    - `SetIsInDlg`
    - `SetIsInCombat`
    - `SetIsInFocus`
    - `GetMinimapDuringFocusCombat`
    - `SetMinimapDuringFocusCombat`
- `mods\mod0_E3HUD_W3EER_NG\content\scripts\game\gui\_old\components\guiPlayerInventoryComponent.ws`
  - restored W3EE `forbiddenItemList` member and item-name filter check.

## Validation
- Base E3 HUD scripts were deleted as instructed.
- Active patch scripts were scanned for the missing symbols from the first compile error.
- DX12 direct launcher started the game after the compatibility patch.
- `witcher3` process remained alive and responding after the initial launch window.

## Backup
- Initial install backup: `backups\e3-hud-w3ee-redux-ng-9478-20260622-145822`
- Script fix backup: `backups\e3-hud-w3ee-redux-ng-9478-scriptfix-20260622-150150`

## Deferred
- GitHub Revamped/Nudel base and optional patches were not installed in this pass.
- Branch should be merged only after in-game HUD/menu validation.
