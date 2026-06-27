# Archive: Dynamic Witcher Schematics

Date: 2026-06-27

Archived folder:

- From: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modDynamicWitcherSchematics`
- To: `archived-mods/redundant-shadowed-dynamic-witcher-schematics-20260627-130039/modDynamicWitcherSchematics`

Configuration:

- `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`
- Changed `[modDynamicWitcherSchematics]` from `Enabled=1` to `Enabled=0`.
- Kept priority `120`.
- Before/after copies are stored in the archive folder.

Evidence:

- The mod has no scripts, DLC folder, menu XML, or input bindings.
- Live folder contained only:
  - `content/blob0.bundle`
  - `content/metadata.store`
- Unpacked bundle contributed four recipe XML paths:
  - `gameplay/items/def_item_crafting_recipes.xml`
  - `dlc/ep1/data/gameplay/items/def_item_crafting_recipes.xml`
  - `dlc/dlc10/data/gameplay/items/dlc10_wolf_recipes.xml`
  - `dlc/bob/data/gameplay/items/def_item_crafting_recipes.xml`

Winning active owners:

| Path | Active winner |
| --- | --- |
| `gameplay/items/def_item_crafting_recipes.xml` | `modleadOre` |
| `dlc/ep1/data/gameplay/items/def_item_crafting_recipes.xml` | `modW3EE` |
| `dlc/dlc10/data/gameplay/items/dlc10_wolf_recipes.xml` | `mod000_Patch_BIA-W3EER` |
| `dlc/bob/data/gameplay/items/def_item_crafting_recipes.xml` | `modleadOre` |

Named item comparison:

| Path | Result |
| --- | --- |
| `gameplay/items/def_item_crafting_recipes.xml` | Dynamic and winner match on 307 shared named item blocks. Dynamic adds only `DWSTestItem`, tagged `NoShow`, `NoDrop`, and `EncumbranceOff`. |
| `dlc/ep1/data/gameplay/items/def_item_crafting_recipes.xml` | Dynamic and winner match on 22 named item blocks. |
| `dlc/dlc10/data/gameplay/items/dlc10_wolf_recipes.xml` | Dynamic and winner match on 48 named item blocks. |
| `dlc/bob/data/gameplay/items/def_item_crafting_recipes.xml` | Dynamic and winner match on 89 named item blocks. |

Conclusion:

This was an active no-effect folder in the current load order. Archiving it reduces active mod count without removing gameplay behavior from the current stack.
