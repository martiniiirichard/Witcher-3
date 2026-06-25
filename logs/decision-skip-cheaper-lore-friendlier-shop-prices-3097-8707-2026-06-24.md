# Decision: Skip Cheaper Lore Friendlier Shop Prices

Date: 2026-06-24

## Mods evaluated

- Cheaper Lore Friendlier Shop Prices `3097`
  - `C:/Users/marti/Downloads/Cheaper Lore Friendlier Shop Prices-3097-4-04-1-1700091456.7z`
- FOCES pre-merge CLFSP patch from `8707`
  - `C:/Users/marti/Downloads/Cheaper Lore Friendlier Shop Prices Pre-Merge-8707-CLFSP-4-04-1-FOCES-4-8d-1767278482.zip`

## Decision

Do not install CLFSP in the current stack.

## Reason

The standalone `3097` mod adds a helper:

```witcherscript
ModLoreFriendlierShopPricesGetItemPriceBase(itemName)
```

That helper returns the item's XML/base price through `dm.GetItemPrice(itemName)`.

The FOCES pre-merge patch wires that helper into shop/crafting/alchemy/inventory UI scripts so buy prices use base XML price and are then multiplied by FOCES regional currency logic.

However, the currently installed FOCES + Reputation integration already includes a deeper LFE economy layer:

- `LFEGetCategoryMult`
- `LFEGetQualityMult`
- `LFEGetDurabilityMult`
- `LFEGetSellingMult`
- `LFEGetCraftMult`
- `GetInventoryItemBasePriceModified(...)`
- `GetItemSellPrice(...)`

Those functions account for category, quality, durability, selling/buying context, crafting, difficulty, FOCES regional currency, and Reputation modifiers.

The CLFSP pre-merge files are older/shorter than the currently installed FOCES + Reputation-patched files and would likely downgrade or overwrite parts of the active RS+FOCES integration.

## Future rule

If prices feel wrong in-game, tune FOCES/Reputation config or targeted multipliers instead of installing CLFSP over the current economy stack.

Only revisit CLFSP if a newer patch explicitly targets:

- FOCES 4.8d or later
- W3EE Redux 1.42i or later
- Reputation System 2.5c or later
- The active Gwent Redux/BiA patched stack
