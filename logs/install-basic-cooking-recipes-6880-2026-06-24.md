# Basic Cooking Recipes 6880 - 2026-06-24

Source: https://www.nexusmods.com/witcher3/mods/6880

Installed archive:

- `C:\Users\marti\Downloads\Basic Cooking Recipes Next Gen-6880-2-2-1718388433.zip`

Installed payload:

- `DLC\dlcBasicCookingRecipes`
- `mods\modBasicCookingRecipes`

Settings added to both active `mods.settings` files:

```ini
[modBasicCookingRecipes]
Enabled=1
Priority=230
```

Compatibility decision:

- The mod page notes the Next-Gen version edits `alchemyManager.ws` and `alchemyTypes.ws`.
- In this stack, `modW3EE` already owns those files at priority 21 and already maps `cookedItemType = edibles` to W3EE's `EACIT_Edible` category.
- `modBasicCookingRecipes` was intentionally placed after W3EE at priority 230 so it contributes the DLC recipe/vendor/loot data without replacing W3EE's alchemy scripts.
- The downloaded Sword and Axe Basic Cooking Recipes patch was inspected. It only contained `alchemyTypes.ws`, and applying it as the active owner would not be appropriate in the current W3EE-owned script stack.

Verification:

- Effective script owner for `game\gameplay\alchemy\alchemyManager.ws`: `modW3EE`.
- Effective script owner for `game\gameplay\alchemy\alchemyTypes.ws`: `modW3EE`.
- DX12 smoke test passed; process remained running after 45 seconds.

Follow-up:

- In-game validation should check whether the recipes appear under the Edibles tab and whether multi-output recipes produce the expected quantity.
