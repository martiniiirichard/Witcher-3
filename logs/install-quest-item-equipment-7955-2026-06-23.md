# Quest Item Equipment 7955

Date: 2026-06-23

## Installed

- Archive: `modQuestItemEquipment - Next-Gen-7955-2-8b-1770563470.zip`
- Mod folder: `modQuestItemEquipment`

## Skipped

- `modAlchemy_Primer_QuestItemEquipment_Patch-7955-2-8b-Alchemy1-12-1-1770522925.zip`

Reason: this optional patch is for Alchemy Primer. Alchemy Primer is not currently installed.

## Load Order

Added to both active `mods.settings` files:

- `modQuestItemEquipment` priority `227`

## Guarded Install

The mod ships full replacement scripts for major W3EE-sensitive systems:

- `playerWitcher.ws`
- `damageManagerProcessor.ws`
- `PlayerAbilityManager.ws`
- `characterMenu.ws`
- movement/sign/effect support files

To avoid replacing the current W3EE/AMM/Friendly Meditation/Extra Skill Slots stack, all scripts under:

```text
mods\modQuestItemEquipment\content\scripts\game
```

were disabled with `.disabled-by-codex`.

Kept active:

```text
mods\modQuestItemEquipment\content\scripts\local\questitemequipment.ws
```

## Manual Compatibility Fix

First compile attempt failed:

```text
Error [modquestitemequipment]local\questitemequipment.ws(53): Could not find function 'MutagensSyngergyBonusUpdateEX'
Error [modquestitemequipment]local\questitemequipment.ws(71): Could not find function 'MutagensSyngergyBonusUpdateEX'
```

Fix applied to active W3EE ability manager:

```text
mods\modW3EE\content\scripts\game\gameplay\ability\playerAbilityManager.ws
```

Added public bridge method:

```witcherscript
public final function MutagensSyngergyBonusUpdateEX() // modQuestItemEquipment
```

The bridge calls the existing W3EE `MutagensSyngergyBonusUpdate(...)` logic for each mutagen slot, preserving W3EE behavior while satisfying QIE's local wrapper calls.

## Backups

Created rollback backups:

```text
C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\QuestItemEquipment_7955_20260623_235804
C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\QuestItemEquipment_7955_fix_20260623_235937
```

## Verification

- First launch exposed the missing `MutagensSyngergyBonusUpdateEX` method.
- After adding the bridge method, DX12 launch smoke passed: game stayed running for 45 seconds.

## Risk

This is compile-clean in guarded mode, but the full QIE behavior may not be complete because the broad game-script replacements remain disabled. In-world testing should focus on acquiring/equipping QIE-supported quest items and confirming tags, quickslot behavior, and mutagen synergy effects work as expected.
