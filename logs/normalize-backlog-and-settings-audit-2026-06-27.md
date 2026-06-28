# Normalize Backlog And Settings Audit

Date: 2026-06-27

## Goal

Reduce backlog noise after the recent triage passes and verify that `mods.settings` still matches the physical `Mods` folder.

## Backlog Normalization

Updated:

- `backlog/witcher3-downloads-last-2-weeks-2026-06-25.csv`
- `backlog/witcher3-mod-download-backlog-2026-06-25.md`
- `backlog/witcher3-install-status-ledger-2026-06-25.csv`
- `backlog/witcher3-status-taxonomy-2026-06-25.md`

Result:

- Raw download rows normalized from recent decision logs: 160
- Remaining rows still marked `triage`: 277

Current download backlog status counts:

- `triage`: 277
- `installed-standard-or-script-merged`: 66
- `skipped`: 59
- `installed-partial-or-adjusted`: 15
- `deferred`: 8
- `installed-with-manual-graft`: 8
- `quarantined-or-disabled`: 3
- `reference`: 1

## Settings Repair

Restored the missing `mods.settings` entry for:

```ini
[modSelectedBombForMonsterNests]
Enabled=1
Priority=267
```

Reason:

- Physical folder existed.
- Install log recorded this mod as installed and launch-tested.
- The current `mods.settings` file had lost the entry.

Backup:

- `backups/normalize-backlog-and-settings-20260627/mods.settings.before-selected-bomb-restore`

## Disabled Folder Cleanup

Archived disabled physical folder:

- From: `Mods/modlighterbombsW3eeRedux`
- To: `_CodexArchivedMods/modlighterbombsW3eeRedux.disabled-superseded-by-custom-compat-20260627`

Reason:

- `modlighterbombsW3eeRedux` is disabled in `mods.settings`.
- It is superseded by `mod000000_W3EER_FoodRebalance_LighterBombsCompat`.
- Leaving a disabled physical folder in `Mods` adds scan clutter without benefit.

## Final Mods Settings Audit

Final state:

- Settings sections: 229
- Enabled entries: 194
- Physical `Mods` folders: 194
- Enabled entries missing physical folder: 0
- Disabled entries with physical folder: 0
- Physical folders without settings entry: 0
- Duplicate enabled priorities: 6

Duplicate priority groups still present:

| Priority | Mods |
| --- | --- |
| `0` | `mod00FlorenEconomySystem_W3EE_REDUX`, `modWoodlandSpirit` |
| `6` | `modleadOre`, `mod000000_W3EER_FoodRebalance_LighterBombsCompat` |
| `10` | `mod0_E3HUD_W3EER_NG`, `mod0BiA_ASL_Compatibility` |
| `22` | `modReduxW3EE`, `modMenuOrganizerNG_IMM_MrCK` |
| `124` | `modDilatedPupils`, `modtoussaintw4New` |
| `265` | `modAWitcherCanHideAnother`, `modVVSSDiagramRestoredVerCNextGen` |

## Recommendation

Do not renumber duplicate priorities blindly. In this stack, several duplicate priorities are intentional local priority bands where exact file conflicts are controlled by file ownership, previous manual merges, or low-risk content layering.

Next useful cleanup pass:

1. Continue normalizing the remaining 277 `triage` rows from existing logs.
2. Then run Script Merger GUI and a launch test.
3. Only renumber duplicate priorities if a specific conflict needs a deterministic winner.
