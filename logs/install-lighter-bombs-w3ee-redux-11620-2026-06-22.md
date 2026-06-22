# Lighter Bombs W3EE Redux 11620

Source: https://www.nexusmods.com/witcher3/mods/11620?tab=description

Installed archive:
- `Lighter bombs W3ee Redux-11620-1-0-1766490924.zip`

Installed game folder:
- `mods/modlighterbombsW3eeRedux`

Configuration:
- Added `[modlighterbombsW3eeRedux]` to `mods.settings`.
- Assigned `Priority=3`, below `modleadOre` and above the W3EE/Food Rebalance XML patches.

Contents:
- `modlighterbombsW3eeRedux/content/blob0.bundle`
- `modlighterbombsW3eeRedux/content/metadata.store`
- `modlighterbombsW3eeRedux/content/scripts/game/components/inventoryComponent.ws.disabled-by-codex`

Bundle paths:
- `gameplay/items/def_item_edibles.xml`

Conflict notes:
- `def_item_edibles.xml` is also owned by W3EE, Food Rebalance Redux, and `mod0000_W3EER_FoodRebalance_BiA_Patch`.
- The bundle must outrank those mods for the casing/edibles weight changes to apply.
- The archive shipped a full `inventoryComponent.ws`, but the current stack already uses a hand-merged `mod0000_MergedFiles` version for W3EE/BiA/Shades compatibility.
- The shipped loose script was renamed to `.disabled-by-codex`; only the intended bomb-weight line was grafted into the active merged script.

Manual script graft:
- File: `mods/mod0000_MergedFiles/content/scripts/game/components/inventoryComponent.ws`
- In `GetItemEncumbrance`, bomb encumbrance changed from `1.f + skill bonuses` to `0.5f + skill bonuses`.

Validation:
- Launched through `tools/direct-launchers/Witcher3DirectDX12.exe`.
- Startup/script compile passed; `witcher3` remained running and responding after the launch window.

Rollback:
- Backup created under `backups/11620-lighter-bombs-20260622-172631/`.

Reusable lesson:
- If a small mod ships a full copy of a heavily merged script, avoid replacing the active merged script. Disable the shipped loose script and graft the minimal behavior delta into `mod0000_MergedFiles`.
