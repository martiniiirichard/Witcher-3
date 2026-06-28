# Witcher 3 Mod Status Taxonomy

Generated: 2026-06-25

This file defines the status language used for the Witcher 3 mod backlog and install ledger.

Related files:

- `backlog/witcher3-mod-download-backlog-2026-06-25.md` - downloaded archive backlog grouped by source
- `backlog/witcher3-downloads-last-2-weeks-2026-06-25.csv` - raw download inventory
- `backlog/witcher3-install-status-ledger-2026-06-25.csv` - first-pass install/decision ledger built from logs

## Status Categories

| Category | Meaning | Next action |
|---|---|---|
| Installed standard path | Installed through normal mod/DLC/config copy plus normal Script Merger where needed. No known custom graft beyond routine merge resolution. | Keep unless later testing fails. |
| Installed with adjustments / partial | Installed, but with options removed, files disabled, or scope reduced to avoid conflicts. | Keep exact notes; re-check before related mods. |
| Installed with manual merge/graft | Installed by editing or grafting script/data behavior into the active stack instead of using the package as-is. | High-change-risk; preserve local changes and avoid blind reinstall. |
| Removed / quarantined | Tried or previously present, then disabled/quarantined because it failed launch, conflicted, or was low value. | Do not re-enable without a specific retest plan. |
| Skipped / do not install now | Assessed and intentionally skipped due to redundancy, incompatibility, missing dependency, or low value. | Leave out unless priorities change. |
| Deferred | Not rejected, but postponed because it needs more inspection, dependencies, or manual work. | Revisit from backlog. |
| Assessed / audited | Inspected, compared, or documented. May or may not be installed; see the specific log. | Use as decision context. |
| Troubleshooting / validation | Crash/merge/test record, not an install decision by itself. | Use to explain stack behavior and future fixes. |
| Download triage | Batch-level scan of downloads. | Promote individual mods into a more specific status after inspection. |

## Current Ledger Counts

- Assessed / audited: 33
- Deferred: 2
- Download triage: 2
- Fix / restoration applied: 5
- Installed standard path: 130
- Installed with adjustments / partial: 7
- Installed with manual merge/graft: 3
- Reference / notes: 10
- Removed / quarantined: 3
- Skipped / do not install now: 8
- Troubleshooting / validation: 12

## Important Caveat

This is a first-pass classification from log names and known workflow conventions. The individual log file remains the source of truth for exact file changes, conflicts, and validation results.
