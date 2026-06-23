# Download triage - low-risk batch - 2026-06-23

## Goal

Pause the input/menu crash investigation and start integrating the newest large download batch by installing the easiest, lowest-conflict candidates first.

## Installed

Installed asset-only or no-script folders:

- `mod_triss_earrings_fix`
- `modTrissCBTrueDress`
- `modMorgueLightsFix`
- `modDandelionScarfFix`
- `modCatHoodFix`
- `modredanianroyalship`
- `modLampOnPlayersBoat_NoCityLight`
- `modUnseenMonsters`
- `modAdditionalArmorStandsNoUni`
- `dlcNamesFromThePath`

`mods.settings` was backed up before editing:

- `C:\Games\The Witcher 3\mods.settings.codex-backup-low-risk-batch-20260623-142227`

New priorities appended:

- `mod_triss_earrings_fix`: `140`
- `modTrissCBTrueDress`: `141`
- `modMorgueLightsFix`: `142`
- `modDandelionScarfFix`: `143`
- `modCatHoodFix`: `144`
- `modredanianroyalship`: `145`
- `modLampOnPlayersBoat_NoCityLight`: `146`
- `modUnseenMonsters`: `147`
- `modAdditionalArmorStandsNoUni`: `148`

## Verification

Static verification passed after install:

- All installed folders exist under the game `Mods` or `DLC` directories.
- Installed batch contains `0` `.ws` script files.
- Installed batch contains `0` `.xml` menu files.
- No Script Merger run was required for this batch.

## Deferred

Deferred despite being downloaded because they need more inspection against W3EE Redux, E3 HUD, Better Icons, mod menu configuration, gameplay balance, or quest bundle conflicts:

- UI/icon/font/menu-facing: Better Icons duplicate/update, Advanced Icons for Witcher Gear, Easier to Read, Main/Menu Strings, QuickLoad, Sort Everything, Colored Map Markers, Instant Tooltips.
- Gameplay/economy/combat: Balanced Alcohol Prices, Enhanced Herbalism, Essential Weapon Rework, Crossbow Rework, Better Torches, No Stair Rolling, Bomb Aiming, Improved Horse Controls, Improved Fist Fight, NPC targeting/Axii fixes, Counterattack Fixes.
- Quest/story/cutscene restorations: Ciri Witcher Ending Restoration variants, Last Wish Final Scene Restoration, Ciri Scene Restored, Memory of Iris, Corvo Bianco Guests/Collection.
- Script or config touchers: Progress on the Path, Cinematic Fast Travel, Selected Bomb for Monster Nests, Additional Stash Locations, Loot in Water, Menu Organizer, Tweaks.

## Notes

This was intentionally conservative. The next strongest move is to inspect the no-script-but-gameplay bundle candidates first, then handle script/config mods one at a time with Script Merger and launch checks.
