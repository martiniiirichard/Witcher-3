# Triage - Legacy Script and Redundant Downloads

Date: 2026-06-26

## Installed This Pass

- `WaterwheelFIXED-9206-1-1-1718019750.7z`
  - Installed as `modwaterwheel2`.
  - Reason: one narrow content layer, no scripts.
  - Separate install log: `logs\install-waterwheel-fixed-9206-2026-06-26.md`

## Skipped / Deferred

### No Journal Sounds 1424

Archive:

- `C:\Users\marti\Downloads\No Journal Sounds-1424-1-31-0-1.zip`

Decision: skip.

Reason:

- Old script replacement mod from 2016.
- Replaces:
  - `game\components\inventoryComponent.ws`
  - `game\gui\hud\modules\hudModuleJournalUpdate.ws`
- High collision risk with W3EE, E3 HUD, Better Icons, and our merged UI stack.

### Jump In Water Mods

Archives:

- `C:\Users\marti\Downloads\Enable Jumping in Water-7221-1-3-1705444930.rar`
- `C:\Users\marti\Downloads\Jump in Shallow Water 1.3-659-1-3.zip`

Decision: skip for now.

Reason:

- Both replace movement/player scripts:
  - `game\player\r4Player.ws`
  - `game\explorations\exploration_movement_system\exploration_substates\explorationStateJump.ws`
- High collision risk with W3EE and the newly installed `A Witcher Can Hide Another`, which also adds exploration/skating mechanics.

### Immersive Rewards 4438

Archive:

- `C:\Users\marti\Downloads\Immersive Rewards-4438-0-1-1582586746.7z`

Decision: skip.

Reason:

- Archive installs as `modFloren`.
- `modFloren` is already intentionally disabled because `mod00FlorenEconomySystem_W3EE_REDUX` replaces that economy/reward lane.
- Re-enabling it would be a step backward from the current W3EE Redux-compatible economy setup.

### Yellow Mutagens 7250

Archive:

- `C:\Users\marti\Downloads\Yellow Mutagens-7250-3-01-1718465651.zip`

Decision: skip.

Reason:

- Old mutagen/UI script replacement mod.
- Replaces:
  - `game\components\inventoryComponent.ws`
  - `game\gui\menus\characterMenu.ws`
  - `game\player\playerWitcher.ws`
- High collision risk with W3EE's mutagen/toxicity/character-menu stack.

### Darker Nights Patch 3151

Archive:

- `C:\Users\marti\Downloads\Darker Nights PATCH (UPatch-Compatible Smooth transitions with Friendly Meditation Patch)-3151-2-1.zip`

Decision: skip.

Reason:

- Old compatibility patch that replaces broad scripts:
  - `game\gui\main_menu\ingameMenu.ws`
  - `game\player\r4Player.ws`
  - `game\player\states\unconscious.ws`
  - `game\r4Game.ws`
  - `game\environmentManager.ws`
  - `game\player\playerWitcher.ws`
  - `game\player\states\meditation\meditationWaiting.ws`
- Current stack already has active modern entries:
  - `modDarkerNights`
  - `modAtmosphericNights`
  - `modFriendlyMeditation`

### Vlad Gwent Board Concept 7087

Archive:

- `C:\Users\marti\Downloads\Concept Ver-7087-1-0a-1667968189.zip`

Decision: skip.

Reason:

- Content-only, but replaces exactly:
  - `gameplay\gui_new\swf\gwint\gwint_game.redswf`
- This exact SWF is also owned by `modGwentRedux`.
- If the concept board wins, it can override Gwent Redux UI behavior. If it loses, it contributes nothing.

### Cheaper Lore Friendlier Shop Prices Pre-Merge 8707

Archive:

- `C:\Users\marti\Downloads\Cheaper Lore Friendlier Shop Prices Pre-Merge-8707-CLFSP-4-04-1-FOCES-4-8d-1767278482.zip`

Decision: defer to a manual economy merge pass.

Reason:

- This is not a standalone mod. It is a pre-merge script patch for `mod00FlorenEconomySystem`.
- Our active economy mod is `mod00FlorenEconomySystem_W3EE_REDUX`.
- Candidate script overlap with the active W3EE Redux economy mod is partial:
  - `inventoryMenu.ws`: active `4995` lines, candidate `4394` lines, `931` line diff count.
  - `guiTooltipComponent.ws`: active `2634` lines, candidate `2317` lines, `585` line diff count.
- Candidate also adds or patches files not present in the active mod path:
  - `alchemyMenu.ws`
  - `craftingMenu.ws`
  - `guiShopInventoryComponent.ws`

Strong next move if revisited:

- Treat this as a focused economy merge, not a normal install.
- Compare against the active W3EE Redux FOCES scripts and manually port only the pricing behavior we actually want.
