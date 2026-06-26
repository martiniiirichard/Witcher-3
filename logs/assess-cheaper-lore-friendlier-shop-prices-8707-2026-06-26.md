# Cheaper Lore Friendlier Shop Prices / FOCES Assessment

Date: 2026-06-26

## Sources

- Nexus page: https://www.nexusmods.com/witcher3/mods/8707
- Download inspected: `Cheaper Lore Friendlier Shop Prices-3097-4-04-1-1700091456.7z`
- Download inspected: `Cheaper Lore Friendlier Shop Prices Pre-Merge-8707-CLFSP-4-04-1-FOCES-4-8d-1767278482.zip`
- Active economy mod: `mod00FlorenEconomySystem_W3EE_REDUX`

## Decision

Do not install or graft CLFSP right now.

The active W3EE Redux FOCES install already owns the economy lane and is aligned with the target experience: regional currencies, regional buy/sell values, reputation-sensitive pricing, item category and quality effects, durability effects, and merchant/specialist logic.

CLFSP's core function is:

```witcherscript
function ModLoreFriendlierShopPricesGetItemPriceBase(itemName : name) : int
{
    var dm : CDefinitionsManagerAccessor;
    var priceBase : int;

    dm = theGame.GetDefinitionsManager();
    priceBase = dm.GetItemPrice(itemName);

    return priceBase;
}
```

The pre-merge patch then uses that function in shop UI purchase paths, mainly to force non-bolt vendor purchases toward raw XML definition price. That would bypass or partially flatten parts of the current W3EE/FOCES price pipeline rather than adding a richer pricing table.

## Why This Is Risky

- The pre-merge patch edits stale broad menu files:
  - `game/gui/menus/alchemyMenu.ws`
  - `game/gui/menus/craftingMenu.ws`
  - `game/gui/menus/inventoryMenu.ws`
  - `game/gui/_old/components/guiShopInventoryComponent.ws`
  - `game/gui/_old/components/guiTooltipComponent.ws`
- Two files overlap active W3EE Redux files with large diffs:
  - `inventoryMenu.ws`
  - `guiTooltipComponent.ws`
- The active FOCES/W3EE Redux pricing implementation already centralizes pricing in `game/components/inventoryComponent.ws` using:
  - `GetItemBasePrice`
  - `GetItemBasePriceAlt`
  - `GetItemSellPrice`
  - `GetItemBasePriceModified`
  - `GetInventoryItemBasePriceModified`
- Active logic already includes:
  - `LFEGetDurabilityMult`
  - `LFEGetCategoryMult`
  - `LFEGetQualityMult`
  - `GetAreaPriceMult`
  - `LFEGetSellingMult`
  - perk effects
  - difficulty modifiers
  - `GetFlorenModCostMult`
  - `GetFlorenModSellMult`
  - `GetFlorenModBaseMult`
  - merchant multiplier support

## Recommendation

Keep `mod00FlorenEconomySystem_W3EE_REDUX` as the economy authority.

If prices feel too punishing later, tune the active FOCES/W3EE Redux multipliers directly instead of installing CLFSP. That preserves the immersive economy model while giving us controlled balance changes.

## Status

- No game files changed.
- No Script Merger action required.
- CLFSP remains a reviewed/deferred candidate.
