# Audit: Feature Shadow Pass - Icy Ocean, Basic Cooking, Manticore

Date: 2026-06-28

## Goal

Check mods that look partially shadowed in Script Merger or loose-script ownership scans, then decide whether the installed feature is actually active through grafts, DLC bundles, or bundled content.

## Icy Ocean

Mod: `modIcyOcean`

Status: keep.

Evidence:

- The unique effect implementation is active:
  - `modIcyOcean\content\scripts\game\gameplay\effects\effects\damageOverTime\icyOceanEffect.ws`
  - Defines `W3Effect_IcyOcean extends W3DamageOverTimeEffect`.
- The active effect type/manager owners already contain the compatibility graft:
  - `EET_IcyOcean`
  - `case EET_IcyOcean : effects[effect] = new W3Effect_IcyOcean in this; break;`
  - `case "IcyOceanEffect" : type = EET_IcyOcean; break;`
  - `case EET_IcyOcean : effectName = 'IcyOceanEffect'; break;`
- Those hooks are present in both the active `modNobsReflex` copies and the W3EE copies.

Decision:

- Keep. The broad losing files are expected; the effect itself and required active hooks are present.
- No priority move or Script Merger action needed.

## Basic Cooking Recipes

Mod/DLC:

- `modBasicCookingRecipes`
- `dlcBasicCookingRecipes`

Status: keep, with caveat.

Evidence:

- `modBasicCookingRecipes` contains only two loose alchemy scripts:
  - `alchemyManager.ws`
  - `alchemyTypes.ws`
- Those scripts intentionally lose to W3EE.
- The relevant content payload is the DLC bundle:
  - `DLC\dlcBasicCookingRecipes\content\blob0.bundle`
  - `DLC\dlcBasicCookingRecipes\content\metadata.store`
- W3EE's active alchemy scripts already understand edible/cooking-style recipe categories (`EACIT_Edible`, `edibles`, `item_category_edibles`), so replacing W3EE with the mod's older alchemy scripts would be the worse move.

Decision:

- Keep the DLC.
- Leave `modBasicCookingRecipes` enabled for now because it documents the paired install and has not caused compile issues.
- Possible future cleanup: test whether recipes remain available with only `dlcBasicCookingRecipes` active. If yes, `modBasicCookingRecipes` may be an archive candidate, but do not remove it without that in-game recipe check.

## Full Manticore W3EE Redux Edit

Mod/DLC:

- `modmanticor`
- `dlcmant`

Status: keep.

Evidence:

- `modmanticor` has one broad loose script:
  - `content\scripts\game\temp.ws`
- That script intentionally loses to W3EE. It is a broad stock/debug-style script and should not beat W3EE.
- The useful payload is bundled and DLC content:
  - `modmanticor\content\blob0.bundle`
  - `modmanticor\content\en.w3strings`
  - `modmanticor\content\pl.w3strings`
  - `DLC\dlcmant\content\blob0.bundle`
- Bundle index evidence shows `modmanticor` contributes active world/journal/crafting/entity/level assets, including Blood and Wine crafting XML, quest/entity files, and level data for Kaer Morhen, Novigrad, Skellige, and Wyzima.

Decision:

- Keep. The script loss is intentional and safer; the feature payload lives in bundled/DLC content.
- No priority move or Script Merger action needed.

## Summary

No removals or live game-file edits were made in this pass.

Current redundancy read:

- `modIcyOcean`: active via unique effect script plus effect-manager grafts.
- `modBasicCookingRecipes`: DLC payload active; loose script shell is a future cleanup candidate only after recipe verification.
- `modmanticor`: active via bundles/DLC/strings; loose `temp.ws` loss is intentional.
