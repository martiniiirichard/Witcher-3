# Florens - Orens - Crowns Economy System 8707

Date: 2026-06-24

## Installed

Installed the W3EE Redux main file:

- `mods/mod00FlorenEconomySystem_W3EE_REDUX`
- `DLC/dlcfloreneconomy`
- `bin/config/r4game/user_config_matrix/pc/modFlorenEconomySystem.xml`

Source archive:

- `C:/Users/marti/Downloads/mod00FlorenEconomySystem_W3EE_REDUX-8707-W3EER-1-42i-FOCES-4-8d-1767278451.zip`

Applied compatibility patch:

- `W3EER - Crowns Economy System - Brothers in Arms + Gwent Redux Patch.zip`

Patch source archive:

- `C:/Users/marti/Downloads/Patches for W3EER - BiA - Gwent Redux-8707-W3EER-1-42a-GR-4-04-BiA-2-72-FOCES-4-6f-1737179454.zip`

## Settings

Added/updated in both active `mods.settings` files:

```ini
[mod00FlorenEconomySystem_W3EE_REDUX]
Enabled=1
Priority=0
```

Priority `0` is intentional. This mod touches broad economy, inventory, shop, quest, scene, and `r4Game` scripts. If `mod0000_MergedFiles` with priority `1` wins those paths, FOCES is partially shadowed and will not function correctly.

## Superseded mod

Disabled older Immersive Rewards install:

- `mods/modFloren` -> `mods/modFloren.disabled-by-codex-foces-replaces`

Removed `[modFloren]` from both active `mods.settings` files.

Reason: FOCES is a newer, W3EE Redux-aware full economy system. It overlaps the same currency/reward layer as Immersive Rewards and should not be stacked with it.

## Skipped

Skipped Reputation System compatibility patch:

- `RS - FOCES - W3EE_REDUX Patch`

Reason: `modReputationSystem` was not installed. The patch includes Reputation System-specific scripts and should only be used if that mod is added.

Skipped Cheaper Lore Friendlier Shop Prices pre-merge:

- `Cheaper Lore Friendlier Shop Prices Pre-Merge`

Reason: optional adjacent compatibility layer, not needed for the base FOCES install, and it touches menu/shop scripts that are already conflict-heavy.

## Page notes

The page describes FOCES as making Florens, Orens, and Ducats usable currencies in corresponding regions, with regional pricing and income adjusted to reflect exchange rates. It is tagged Next-Gen compatible and versioned 4.8d.

## Verification

- Launch smoke test: passed.
- Result: game stayed running after 45 seconds.

## Residual risk

- This is a broad economy/menu overhaul. Smoke passing means scripts compile, not that all shop, crafting, Gwent, currency conversion, and quest reward flows behave correctly.
- Priority `0` means FOCES wins over some merged script outputs. Later Script Merger may show conflicts; do not blindly merge old `modFloren` or Immersive Rewards back in.
- In-game test targets:
  - Inventory currency display in Velen, Novigrad, Skellige, Toussaint.
  - Shop buying/selling with regional currency.
  - Crafting/alchemy payment display.
  - Bank currency exchange.
  - Gwent betting and Gwent Redux card purchase/reward flow.
