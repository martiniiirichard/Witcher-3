# Food Rebalance vs Lighter Bombs Audit

Date: 2026-06-27

## Files Compared

Normalized bundle extracts were staged under:

`tools/tmp/food-rebalance-compare-20260627/_norm_food_only`

Important files:

- `modFoodRebalanceRedux__gameplay__abilities__effects.xml`
- `mod0000_W3EER_FoodRebalance_BiA_Patch__gameplay__abilities__effects.xml`
- `modFoodRebalanceRedux__gameplay__items__def_item_cooking_recipes.xml`
- `mod0000_W3EER_FoodRebalance_BiA_Patch__gameplay__items__def_item_cooking_recipes.xml`
- `modFoodRebalanceRedux__gameplay__items__def_item_edibles.xml`
- `mod0000_W3EER_FoodRebalance_BiA_Patch__gameplay__items__def_item_edibles.xml`
- `modlighterbombsW3eeRedux__gameplay__items__def_item_edibles.xml`
- `modW3EE__gameplay__items__def_item_edibles.xml`

## Runtime Winners

Lower numeric priority wins in this stack.

- `effects.xml`: `mod0000_W3EER_FoodRebalance_BiA_Patch`
- `def_item_cooking_recipes.xml`: `mod0000_W3EER_FoodRebalance_BiA_Patch`
- `def_item_edibles.xml`: `modlighterbombsW3eeRedux`

## Findings

The W3EE/BiA Food Rebalance patch is not a weak cosmetic patch. It carries meaningful gameplay and compatibility changes:

- Stronger/harsher bleed and poison values than base Food Rebalance.
- BiA-compatible entries such as Axii/stopping effect wiring.
- Recipe metadata/stat changes that appear compatibility-oriented.

`modlighterbombsW3eeRedux` is the real balance concern. It wins the entire `def_item_edibles.xml` file, so it changes more than bomb weights:

- Bomb casing weight is reduced.
- Empty bottle and bomb casing categories/descriptions/tags differ.
- Many food and drink prices are lower.
- Several food/drink quality tiers and stat tiers change.

## Recommendation

For the user's target experience, keep the W3EE/BiA Food Rebalance patch as the intended balance owner. Do not treat `modFoodRebalanceRedux` as a simple removal until dependency behavior is verified.

Applied resolution:

- Created `custom-mods/mod000000_W3EER_FoodRebalance_LighterBombsCompat`.
- Packed one bundled runtime file: `gameplay/items/def_item_edibles.xml`.
- Source XML is based on `mod0000_W3EER_FoodRebalance_BiA_Patch`.
- Only intended gameplay edit: `Bomb casing` and `Bomb casing_Stash` weight changed from `0.7` to `0.2`.
- Installed the packed content folder to the live game `Mods` directory.
- Set `mod000000_W3EER_FoodRebalance_LighterBombsCompat` to `Enabled=1`, `Priority=6`.
- Set `modlighterbombsW3eeRedux` to `Enabled=0`, `Priority=7`.

This preserves challenge and avoids silently softening the food/drink economy while still encouraging bomb use.
