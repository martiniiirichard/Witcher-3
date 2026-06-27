# Install: Food Rebalance + Lighter Bombs Compatibility

Date: 2026-06-27

## Goal

Keep W3EE/BiA Food Rebalance as the owner of food/drink economy balance while preserving the useful part of Lighter Bombs: lower bomb casing weight.

## Installed Custom Mod

`mod000000_W3EER_FoodRebalance_LighterBombsCompat`

Versioned source:

`custom-mods/mod000000_W3EER_FoodRebalance_LighterBombsCompat`

Live installed folder:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\mod000000_W3EER_FoodRebalance_LighterBombsCompat`

## Runtime Asset

Packed bundle contains one file:

`gameplay\items\def_item_edibles.xml`

The source XML comes from `mod0000_W3EER_FoodRebalance_BiA_Patch`, with only these edits:

- `Bomb casing`: `weight="0.7"` to `weight="0.2"`
- `Bomb casing_Stash`: `weight="0.7"` to `weight="0.2"`

## Settings

Backups:

`settings-backups/food-lighter-compat-20260627-1226`

Applied settings:

```ini
[mod000000_W3EER_FoodRebalance_LighterBombsCompat]
Enabled=1
Priority=6

[modlighterbombsW3eeRedux]
Enabled=0
Priority=7

[mod0000_W3EER_FoodRebalance_BiA_Patch]
Enabled=1
Priority=8
```

Lower numeric priority wins in this install. The custom compatibility mod now wins `def_item_edibles.xml`, while the original broad Lighter Bombs edibles bundle is disabled.

## Verification

- `wcc_lite pack` succeeded.
- `wcc_lite metadatastore` succeeded.
- Installed live mod folder is content-only: `blob0.bundle` and `metadata.store`.
- No Script Merger pass is required because this is a bundled XML-only compatibility patch.
