# Colored Subtitles 7523 install

Date: 2026-06-24
Mod: https://www.nexusmods.com/witcher3/mods/7523
Downloaded archive: `C:\Users\marti\Downloads\Colored Subtitles (NextGen)-7523-2-0-1725933554.zip`

## Installed

- Copied `Mods\modSubtitleColors` to game `mods\modSubtitleColors`.
- Copied `modsubtitleColor.xml` to `bin\config\r4game\user_config_matrix\pc`.
- Added `modsubtitleColor.xml;` to both `dx12filelist.txt` and `dx11filelist.txt`.
- Added `[modSubtitleColors] Enabled=1 Priority=236` to both active `mods.settings` files.

## Compatibility decisions

- Disabled `modSubtitleColors\content\scripts\game\gui\hud\modules\hudModuleDialog.ws` because the active dialogue HUD file is owned by `mod00FlorenEconomySystem_W3EE_REDUX` / Reputation / W3EE. Letting the full Colored Subtitles dialogue file win would drop FOCES/Reputation dialogue economy hooks.
- Disabled `subtitleColor_Annot.ws` because it wraps several `CR4ScriptedHud` methods that are not present in the active W3EE HUD script. Kept a small replacement `subtitleColor_AddFields.ws` with only the needed `@addField` declarations for `CR4HudModuleDialog` and `CR4HudModuleSubtitles`.
- Kept the full `hudModuleSubtitles.ws`; no other installed mod owns that script path.
- Manually merged the small subtitle/dialogue color calls into active FOCES `hudModuleDialog.ws`, preserving the FOCES one-time Bram exchange gold highlight.

## Compile fixes exposed during test

After installing, old priority/winner-file issues surfaced because several mods ship their own `r4Game.ws` or GUI component files that do not win priority:

- Patched active FOCES `r4Game.ws` with shared fields/init for `ESSConfig essconfig` and `NobReflexOptionHandler Roptions`, because Extra Skill Slots and Nobs Reflex helper files reference `theGame.essconfig` / `theGame.Roptions` but their own `r4Game.ws` files do not win.
- Changed FOCES `Experience().AwardGeneralXP(true)` to `Experience().AwardGeneralXP(rewrd.experience)` to match the active W3EE function signature.
- Patched E3 HUD old container component to use direct item tags for weapon runes / armor upgrades instead of helper functions hidden by the active base class.
- Patched active FOCES `guiPlayerInventoryComponent.ws` with W3EE `forbiddenItemList` field and filter check, because W3EE `itemSelectionPopup.ws` expects it.

## Verification

Launch smoke after fixes: passed. `witcher3.exe` remained running after 45 seconds and was terminated by Codex.

## Notes

Generalizable rule: when multiple mods ship `game\r4Game.ws`, only the highest-priority winner supplies fields on `CR4Game`. Helpers in losing mods still compile and can reference fields that no longer exist. Prefer adding tiny field/init bridges to the active winning `r4Game.ws` over changing priority or enabling broad old replacements.
