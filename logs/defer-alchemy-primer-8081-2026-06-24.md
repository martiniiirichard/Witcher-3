# Alchemy Primer 8081 Deferred

Date: 2026-06-24

## Decision

Deferred Alchemy Primer 8081 for this stack.

The mod is not a safe drop-in for the current W3EE Redux build. It attempts to own large parts of the alchemy, skill, inventory, tooltip, and menu script surface that are already heavily owned by W3EE Redux, E3 HUD, Better Icons, Nobs Reflex, Quest Item Equipment, Alcohol Factory, and merged core files.

## What Was Tried

- Installed main Alchemy Primer files from `Alchemy Primer-8081-1-12-1-1768345333.7z`.
- Added `PrimerMenu.xml` to the DX11 and DX12 user config file lists.
- Added Primer input bindings to the active Witcher 3 input settings.
- Installed available compatibility patch files:
  - `Alchemy-v1.12.1_BIDE-v1.8.3 NG Patch-12308-1-0-0-1780592692.7z`
  - `modAlchemy_Primer_QuestItemEquipment_Patch-7955-2-8b-Alchemy1-12-1-1770522925.zip`
  - `modAlchemy_Primer_AlcoholFactory_Patch-7732-3-7-Alchemy1-12-1-1770522977.zip`
- Tried targeted fixes for:
  - duplicate dominance effect classes
  - missing `EET_PotionDigestion`
  - W3EE final method overrides
  - `UnequipSkill` signature mismatch
  - Primer full `playerWitcher.ws` and `PlayerAbilityManager.ws` overrides

## Failure Mode

Even after the official compatibility patches, the compiler still produced more than 200 errors. The dominant categories were:

- Primer `AlchemySkills.ws` accessing private W3EE `W3PlayerAbilityManager` fields and private methods.
- Primer alchemy menu APIs conflicting with the active W3EE/Better Icons/E3 HUD menu stack.
- Inventory and tooltip signature mismatches such as `GetItemEncumbrance`.
- Duplicate or hidden dominance effect classes across W3EE and Nobs Reflex.
- Better Icons BIDE patch calling a different `ReplacingBetterIcons` signature than our installed Better Icons stack exposes.

This is a porting project, not a normal install.

## Cleanup Applied

- Disabled `modPrimer` in both active `mods.settings` files.
- Disabled `modAlchemyBIDEPatch` in both active `mods.settings` files.
- Renamed `mods/modPrimer/content/scripts` to `scripts.disabled-by-codex`.
- Renamed `modAlchemyBIDEPatch/content/scripts` to `scripts.disabled-by-codex`.
- Disabled accidentally nested compatibility patch folders:
  - `mods/modAlcoholFactory/modAlcoholFactory.disabled-by-codex`
  - `mods/modQuestItemEquipment/modQuestItemEquipment.disabled-by-codex`
- Restored W3EE `playerAbilityManager.ws` from backup.
- Corrected dominance class ownership:
  - `modNobsReflex` keeps the higher-priority visible definitions.
  - duplicate `modW3EE` dominance classes are commented out.

## Backups

Key backups created under:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\AlchemyPrimer_8081_20260624_000350`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\AlchemyPrimer_compat_patches_20260624_001756`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\AlchemyPrimer_fix_dominance_owner_nobs_20260624_002344`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\AlchemyPrimer_fix_dominance_owner_w3ee_20260624_002344`

## Verification

Smoke compile passed after rollback:

`SmokePassed_StillRunningAfter45s`

## Future Rule

Do not retry Alchemy Primer 8081 as a normal mod install in this build.

Only revisit it if we are willing to create a dedicated compatibility fork/patch that ports Primer onto the current W3EE Redux + Better Icons + E3 HUD + Nobs Reflex stack.
