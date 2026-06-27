# Archive: Food Rebalance Redux Base Folder

Date: 2026-06-27

Archived folder:

- From: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modFoodRebalanceRedux`
- To: `archived-mods/redundant-superseded-food-rebalance-redux-20260627-131644/modFoodRebalanceRedux`

Configuration:

- `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`
- Changed `[modFoodRebalanceRedux]` from `Enabled=1` to `Enabled=0`.
- Kept priority `48`.
- Before/after copies are stored in the archive folder.

Reason:

The base Food Rebalance folder was superseded by the active W3EE/BiA compatibility layer and our custom lighter-bombs compatibility layer.

Runtime file ownership:

| Food Rebalance file | Active winner |
| --- | --- |
| `gameplay/abilities/effects.xml` | `mod0000_W3EER_FoodRebalance_BiA_Patch` priority `8` |
| `gameplay/items/def_item_cooking_recipes.xml` | `mod0000_W3EER_FoodRebalance_BiA_Patch` priority `8` |
| `gameplay/items/def_item_edibles.xml` | `mod000000_W3EER_FoodRebalance_LighterBombsCompat` priority `6` |

Named-entry checks:

| File | Result |
| --- | --- |
| `def_item_cooking_recipes.xml` | Winner contains the same 22 named records as base Food Rebalance. |
| `def_item_edibles.xml` | Winner contains the same 109 named records as base Food Rebalance. |
| `effects.xml` | Winner intentionally replaces base bleeding variants with W3EE/BiA-compatible Silver Dust bleeding variants and carries BiA target-effect wiring. |

Balance intent preserved:

- Keep `mod0000_W3EER_FoodRebalance_BiA_Patch` as the food/effect balance owner.
- Keep `mod000000_W3EER_FoodRebalance_LighterBombsCompat` as the edibles owner with only bomb casing weight lowered.
- Keep `modlighterbombsW3eeRedux` disabled so it does not soften broad food/drink prices and tiers.

No Script Merger pass is required because this is bundled XML content only.
