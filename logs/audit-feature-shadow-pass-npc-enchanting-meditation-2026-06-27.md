# Audit: Feature Shadow Pass - NPC Targeting, Enchanting, Friendly Meditation

Date: 2026-06-27

## Goal

Review script-heavy mods where file ownership alone is misleading. The key question is whether the intended behavior is represented in the active winning scripts.

## NPC Targeting Priority and Axii Fixes

Mod: `modNPCTargetingPriorityAndAxiiFixes`

Status: keep, no change.

Evidence:

- Helper functions are active in `modW3EE\content\scripts\local\codex_w3ee_graft_helpers.ws`:
  - `AddHitReactionForCriticalEffects`
  - `UnforceTargetsAxiiGuardMe`
  - `FixConfusionCriticalState`
- Active W3EE/Nobs/MergedFiles scripts contain the mod-specific call sites/comments for Confusion, Axii Guard Me, and target unforce behavior.
- The duplicate local helper file in the source mod remains disabled intentionally.

Decision: no priority move. This is a grafted compatibility setup, not a dead mod.

## All Gear Enchanting Based On Sockets

Mod: `modAllGearEnchantingBasedOnSockets`

Status: fixed.

Prior state:

- The main enchanting menu behavior was already grafted into:

`modBetterIcons2025_NextGen_W3EE\content\scripts\game\gui\menus\enchantingMenu.ws`

- However, the active inventory component still came from W3EE and required 3 sockets, with only swords and armor visible. That could hide the very items the mod is supposed to expose.

Fix applied to active W3EE component:

`modW3EE\content\scripts\game\gui\_old\components\guiEnchantingInventoryComponent.ws`

Changes:

- `REQUIRED_SLOTS_COUNTS` changed from `3` to `1`.
- Added `boots`, `gloves`, and `pants` to the enchanting item filter.
- Added `maxslots = _inv.GetSlotItemsLimit( item );`
- Adjusted the not-enough-sockets warning to use the item's slot limit.

Backup:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\all-gear-enchanting-component-graft-20260627-234435`

Validation:

- DX12 launch smoke passed; `witcher3.exe` stayed running and responding for 45 seconds.

Remaining check:

- At the runewright/enchanting menu, verify boots, gloves, pants, and 1-2 socket gear appear and only valid enchantments can be applied.

## Friendly Meditation

Mod: `modFriendlyMeditation`

Status: keep, but likely partial.

Evidence:

- The config object is grafted into the active merged `playerWitcher.ws`:
  - `fMeditationConfig : CModFMeditationConfig`
  - `fMeditationConfig = new CModFMeditationConfig in this;`
  - `fMeditationConfig.Init();`
- Its menu XML/input/settings/string assets are installed.
- But many actual Friendly Meditation behavior scripts still lose to W3EE/E3/Nobs:
  - meditation state files
  - meditation camera hooks
  - player input hooks
  - `r4Player` camera request helpers

Decision: do not blindly reprioritize Friendly Meditation. A deeper port is possible, but it would touch meditation states, camera behavior, input handling, and W3EE prep-meditation behavior.

Recommended test before deeper port:

- Open the Friendly Meditation menu.
- Try fast-forwarding meditation with the bound input.
- Check whether the custom camera and campfire options do anything.
- If only the menu appears but behavior is missing, schedule a dedicated Friendly Meditation graft pass.
