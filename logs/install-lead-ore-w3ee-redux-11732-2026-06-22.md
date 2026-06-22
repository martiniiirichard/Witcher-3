# Lead Ore 11732

Source: https://www.nexusmods.com/witcher3/mods/11732?tab=description

Installed archive:
- `Lead Ore-11732-1-0-1768557826.zip`

Installed game folder:
- `mods/modleadOre`

Configuration:
- Added `[modleadOre]` to `mods.settings`.
- Assigned `Priority=2`, directly below `mod0000_MergedFiles`.
- Existing priorities from `mod0000_W3EER_FoodRebalance_BiA_Patch` downward were shifted by one.

Contents:
- `modleadOre/content/blob0.bundle`
- `modleadOre/content/metadata.store`
- No loose scripts, menus, input bindings, or DLC folder.

Bundle paths:
- `dlc/bob/data/gameplay/items/def_item_alchemy_recipes_dye.xml`
- `dlc/bob/data/gameplay/items/def_item_crafting_recipes.xml`
- `gameplay/items/def_item_crafting_recipes.xml`
- `gameplay/items/def_item_crafting_recipes_bolts.xml`
- `gameplay/items/def_item_ingredients.xml`

Conflict notes:
- W3EE owns all five XML paths.
- `mod000_Patch_BIA-W3EER` also owns `dlc/bob/data/gameplay/items/def_item_crafting_recipes.xml`, but that file was byte-identical to W3EE's copy, so no extra BiA merge was needed.
- Lead Ore needs to outrank W3EE/BiA XML for its recipe changes to apply, so priority 2 is intentional.

Validation:
- Launched through `tools/direct-launchers/Witcher3DirectDX12.exe`.
- Startup passed; `witcher3` remained running and responding after the launch window.

Rollback:
- Backup created under `backups/11732-lead-ore-20260622-172232/`.

Reusable lesson:
- Bundle-only XML mods can still conflict silently. Use QuickBMS to list bundle paths, compare against installed patch bundles, and set priority based on the exact files being overridden.
