# Current Mode Script/Text Health Audit

Date: 2026-06-25

## Goal

Check whether the current Witcher 3 mod stack has lingering Script Merger, script compile, or bundled text issues.

## Current Result

The current stack passes a DX12 launch/compile smoke test.

Test:

- stopped any existing `witcher3.exe`
- launched `tools\direct-launchers\Witcher3DirectDX12.exe`
- waited 75 seconds

Observed:

- `witcher3.exe` was running
- main window title was `The Witcher 3`
- process was responding
- working set was about 1.7 GB

This strongly suggests there is no current fatal script compilation error.

## Static Checks

### Conflict Markers

Checked active merged/script text for common unresolved merge markers:

- `<<<<<<<`
- `=======`
- `>>>>>>>`
- `MERGE CONFLICT`

No real unresolved merge markers were found in `mod0000_MergedFiles`.

Broad scan noise existed from readme separators and normal log strings, but not actual merge markers.

### `mods.settings` Hygiene

Findings:

- enabled `mods.settings` entries: 247
- physical active mod folders: 199
- enabled entries with missing physical folders: 48
- physical active folders missing from `mods.settings`: 0

The missing-folder entries mostly come from old appearance-option entries that are no longer present as physical folders. They are probably not loaded by the game, but they make the config harder to reason about and may confuse manual audits.

Duplicate enabled priority values found:

- priority `0`: `mod00FlorenEconomySystem_W3EE_REDUX`, `modWoodlandSpirit`
- priority `7`: `mod00MarlenaTheCook`, `modlighterbombsW3eeRedux`
- priority `10`: `mod0_E3HUD_W3EER_NG`, `mod0BiA_ASL_Compatibility`
- priority `22`: `modMenuOrganizerNG_IMM_MrCK`, `modReduxW3EE`
- priority `259`: `modkaer_morhen_extended`, `modRTWaterReflectionColorFix`

These are not proven launch blockers, but duplicate priorities are a real load-order ambiguity. Cleaning them up would make future Script Merger/debugging passes cleaner.

### Merged Files

Current `mod0000_MergedFiles` contains merged scripts for:

- `components\inventoryComponent.ws`
- `gameplay\interactive\monsterNestEntity.ws`
- `gameplay\items\itemEntity.ws`
- `gameplay\items\throwables\petards\petard.ws`
- `gameplay\poster.ws`
- `gui\menus\menuBase.ws`
- `npc\npc.ws`
- `player\playerAiming.ws`
- `player\playerWitcher.ws`
- `player\r4Player.ws`
- `quests\quest_function.ws`
- `vehicles\vehicleComponent.ws`

Several `.codex-backup-*` files remain inside `mod0000_MergedFiles`. They do not end in `.ws`, so they should not compile, but they are housekeeping clutter.

### Script Path Overlap

Static scan found:

- duplicated `.ws` relative paths: 86
- duplicated `.ws` paths with a corresponding file in `mod0000_MergedFiles`: 6
- duplicated `.ws` paths without a corresponding merged file: 80

This does not automatically mean 80 broken merges. In this stack, many files are intentionally shadowed by priority, patched by a compatibility mod, or manually grafted into W3EE/merged files. The launch smoke test confirms none are currently fatal.

Still, the high-risk unresolved/shadowed areas for future debugging are:

- `playerWitcher.ws`: AMM / W3EE / NOBs / Friendly Meditation / Extra Skill Slots / Expansion Zero
- `r4Player.ws`: W3EE / Cape Hood Helmet Toggle / Icy Ocean / Friendly Meditation / Expansion Zero
- `playerInput.ws`: NOBs / W3EE / Cape Hood Helmet Toggle / Friendly Meditation / Expansion Zero
- `gameEffectManager.ws` and `effectTypes.ws`: NOBs / W3EE / Icy Ocean / Expansion Zero / Shrines
- `damageManagerProcessor.ws`: NOBs / W3EE / Expansion Zero / NPC Targeting Priority
- GUI inventory/menu files: FOCES / E3 HUD / Better Icons / W3EE / Expansion Zero
- `ingamemenu.ws` and `igmStructureCreator.ws`: Menu Organizer / W3EE / Friendly Meditation / Expansion Zero

## Script Merger Tooling Note

Tried launching both Script Merger builds with `--help`:

- `tools\sm-fae-0.9.7\WitcherScriptMerger.exe --help`
- `tools\script-merger-0.6.5\WitcherScriptMerger.exe --help`

Neither printed useful CLI output. Treat Script Merger as GUI-driven for conflict confirmation unless we find documented headless options later.

## Recommendation

No emergency merge fix is needed right now because the game launches cleanly.

Best next cleanup line:

1. Clean stale `mods.settings` entries whose folders no longer exist.
2. Normalize duplicate priorities so the load order is deterministic.
3. Remove non-compiled `.codex-backup-*` clutter from `mod0000_MergedFiles` only after backing it up elsewhere.
4. Run Script Merger GUI after the cleanup and capture screenshots/listings of remaining conflicts.
5. Do a second DX12 launch smoke test.

Do not start bulk-merging the 80 duplicate `.ws` paths just because a static scan sees overlap. That would be too blunt for the current W3EE stack.
