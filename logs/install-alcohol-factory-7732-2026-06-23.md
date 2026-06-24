# Alcohol Factory 7732

Date: 2026-06-23

## Installed

- Archive: `AlcoholFactory-7732-3-7-1743864885.zip`
- Mod folder: `modAlcoholFactory`
- DLC folder: `dlcalcoholfactory`

## Skipped

- `modAlchemy_Primer_AlcoholFactory_Patch-7732-3-7-Alchemy1-12-1-1770522977.zip`

Reason: this optional patch is for Alchemy Primer. Alchemy Primer is not installed in the current stack, and the patch replaces `AlchemyExtensions.GetRecipes`, so it should not be added without the dependency.

## Load Order

Added to both active `mods.settings` files:

- `modAlcoholFactory` priority `226`

## Script Notes

- Main script: `mods\modAlcoholFactory\content\scripts\local\alcoholfactory.ws`
- Script defines quest functions for distillery/alcohol recipe behavior.
- No shared base game script replacement was enabled by the main install.
- No Script Merger pass was required.

## Backup

Created rollback backup:

```text
C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\AlcoholFactory_7732_20260623_235023
```

## Verification

- DX12 launch smoke passed: game stayed running for 45 seconds.

## Risk

Compile is clean. In-world behavior should eventually be tested by reaching the distillery flow and confirming recipes/items are added correctly.
