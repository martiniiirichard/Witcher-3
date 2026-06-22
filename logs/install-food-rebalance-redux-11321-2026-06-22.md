# Food Rebalance For W3EE Redux 11321 Install

Date: 2026-06-22

## Source

- Food Rebalance: https://www.nexusmods.com/witcher3/mods/11321
- Main file: `modFoodRebalanceRedux-11321-1-0-1765128047.zip`
- BiA compatibility patch: https://www.nexusmods.com/witcher3/mods/12221
- Patch file used: `W3EER - Food Rebalance - BiA Compatibility Patch-12221-1-0-1778850191.zip`

## Decision

Installed the main compatibility patch only, not the optional `with My Tweaks` variant.

Reason:

- The main patch preserves original Food Rebalance behavior.
- The optional variant is a balance fork that removes max vitality/stamina bonuses and changes regen/recipe prices.
- Current stack already has W3EE Redux, BiA Ultimate, and several balance-touching mods, so the least-opinionated compatibility path is preferred.

## Runtime Changes

Installed:

- `mods/modFoodRebalanceRedux`
- `mods/mod0000_W3EER_FoodRebalance_BiA_Patch`

Updated `C:\Games\The Witcher 3\mods.settings`:

```ini
[mod0000_MergedFiles]
Enabled=1
Priority=1

[mod0000_W3EER_FoodRebalance_BiA_Patch]
Enabled=1
Priority=2

[mod000_Patch_BIA-W3EER]
Enabled=1
Priority=3
```

`modFoodRebalanceRedux` is enabled later in the order at priority 30. The compatibility patch is intentionally above W3EE/BiA/Food Rebalance so it wins bundled item-data conflicts.

## Backup

- `backups/food-rebalance-redux-11321-20260622-121902`

## Inspection Notes

- Both archives contain bundled content only.
- No `.ws` script files were present.
- No Script Merger step required.
- Non-script overlap is expected through `blob0.bundle` and `metadata.store`; this is handled by priority.

## Verification

- Confirmed both runtime mod folders exist.
- Confirmed load order is updated.
- Launched via direct DX12 launcher.
- Game reached main window with no script compilation error.
