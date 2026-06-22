# E3 Better Icons Patch Graft - 2026-06-22

## Goal
Apply the E3 UI/HUD Revamped Better Icons patch safely on top of the current E3 HUD + W3EE Redux + Better Icons W3EE stack.

## Source Download
- `E3.UI.and.HUD.Revamped.-.Better.Icons.Patch.zip`

## Why This Was Not Installed Blindly
The archive targets the generic Better Icons folder:
- `mods\modBetterIcons2025_NextGen`

Our active install uses:
- `mods\modBetterIcons2025_NextGen_W3EE`

Also, the active radial menu script is currently owned by:
- `mods\mod0_E3HUD_W3EER_NG`

So copying the archive directly would either target the wrong folder or fail to affect the active radial menu. The full patch scripts also risk dropping W3EE/FriendlyHUD-derived code from the current files.

## Applied Graft
Patched active radial menu:
- `mods\mod0_E3HUD_W3EER_NG\content\scripts\game\gui\hud\modules\hudModuleRadialMenu.ws`

Added Better Icons radial icon path calls to the active E3 HUD radial script:
- crossbow/ranged weapon icon path
- pocket/quickslot icon path

Patched active journal update file:
- `mods\modBetterIcons2025_NextGen_W3EE\content\scripts\game\gui\hud\modules\hudModuleJournalUpdate.ws`

Added selected E3 journal formatting:
- quest update text sizing
- level-up color styling
- experience update color/title sizing
- map-pin update text sizing

## Validation
- Did not install generic Better Icons.
- Did not install Vlad UI or Friendly HUD patches.
- Did not replace full radial/journal scripts.
- DX12 direct launcher started the game.
- `witcher3` process remained alive and responding after the initial launch window.

## Backup
- Script graft backup: `backups\e3-better-icons-patch-10256-20260622-152303`

## Deferred
The full patch's other E3 journal text-size changes were not copied wholesale. If the visual pass shows a specific journal popup still mismatched, graft that individual block rather than overwriting the active script.
