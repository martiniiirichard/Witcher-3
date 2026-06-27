# Reassess - Balanced Alcohol Prices 10295

Date: 2026-06-27

Source:

- https://www.nexusmods.com/witcher3/mods/10295
- `C:\Users\marti\Downloads\Balanced Alcohol Prices-10295-1-0-1-1761992119.zip`

## Why Revisited

Earlier logs showed Balanced Alcohol caused the no-window startup hang. Later loader-pressure testing showed it was not independently broken and could launch if the active content-folder pressure was reduced.

This pass rechecked whether it is worth enabling anyway.

## Payload

Content-only package:

- `mods\modBalancedAlcoholPrices\content\blob0.bundle`
- `mods\modBalancedAlcoholPrices\content\metadata.store`
- `mods\modBalancedAlcoholPrices\content\info.json`

QuickBMS unpacked:

- `gameplay\items\def_item_edibles.xml`
- `gameplay\items_plus\def_item_edibles.xml`

## Conflict / Value Read

The current build already has a deliberate edibles/food economy setup:

- `mod000000_W3EER_FoodRebalance_LighterBombsCompat` wins the main `def_item_edibles.xml` lane at priority `6`.
- It preserves W3EE/BiA Food Rebalance while applying only the desired lighter bomb casing weight change.
- `mod0000_W3EER_FoodRebalance_BiA_Patch` and W3EE also participate in this lane.

Balanced Alcohol would either:

- stay low-priority and be shadowed/no-op, while still adding a content bundle to a loader-pressure-sensitive stack; or
- be raised in priority and override the carefully chosen food/economy values.

Neither line is attractive.

## Decision

Keep disabled.

This is not a good install target for the current economy goal. If alcohol prices feel wrong later, tune the active W3EE/BiA/FOCES/LFE edibles and pricing path directly instead of adding another full edibles XML owner.
