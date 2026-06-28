# Normalize mods.settings Priorities - 2026-06-28

Problem:

SM-FAE Script Merger rejected or warned on `mods.settings` because:

- `modBoatRaces` had `Priority=-1`, outside SM-FAE's valid `0..9999` range.
- Several enabled mods shared duplicate priorities, making same-priority load order ambiguous to SM-FAE.

Initial invalid entry:

```ini
[modBoatRaces]
Enabled=1
Priority=-1
```

Duplicate groups found before normalization:

- `0`: `mod00FlorenEconomySystem_W3EE_REDUX`, `modWoodlandSpirit`, `modBoatRaces`
- `6`: `modleadOre`, `mod000000_W3EER_FoodRebalance_LighterBombsCompat`
- `7`: `modCommunityPatch_WorldMapFull`, `mod00MarlenaTheCook`
- `10`: `mod0_E3HUD_W3EER_NG`, `mod0BiA_ASL_Compatibility`
- `21`: `modMenuStrings`, `modLessmusic`
- `22`: `modReduxW3EE`, `modMenuOrganizerNG_IMM_MrCK`
- `124`: `modDilatedPupils`, `modtoussaintw4New`
- `265`: `modAWitcherCanHideAnother`, `modVVSSDiagramRestoredVerCNextGen`

Fix:

Renumbered all enabled mods to unique priorities `0..198`.

Ordering rule:

1. Sort by existing numeric priority.
2. Preserve existing file order inside duplicate groups.
3. Treat `modBoatRaces` as if its old sort priority was `-1`, so its original "load before priority-0 owners" intent is preserved while using the valid priority `0`.

Top of normalized order:

```text
0  modBoatRaces
1  mod00FlorenEconomySystem_W3EE_REDUX
2  modWoodlandSpirit
3  mod0000_MergedFiles
4  mod00ReputationSystem_W3EE_REDUX
5  mod0MirrorReward_BiA3
6  modPatchGwentRedux_W3EE_W3EERedux
7  modGwentRedux
8  modleadOre
9  mod000000_W3EER_FoodRebalance_LighterBombsCompat
10 modCommunityPatch_WorldMapFull
11 mod00MarlenaTheCook
12 mod0000_W3EER_FoodRebalance_BiA_Patch
13 mod000_Patch_BIA-W3EER
14 mod0_E3HUD_W3EER_NG
15 mod0BiA_ASL_Compatibility
```

Backups:

- `settings-backups\mods-settings-boat-races-priority-20260628-014417`
- `settings-backups\mods-settings-normalize-priorities-20260628-014736`

Verification:

- Enabled priority range is now `0..198`.
- No enabled mods have priorities outside `0..9999`.
- No enabled mods have duplicate priorities.
- SM-FAE reopened and responded after the change.

Risk:

This changes many numeric priority values, but preserves the effective order by sorting from the prior priority map. Disabled mods were not renumbered.
