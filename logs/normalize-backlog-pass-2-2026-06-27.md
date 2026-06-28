# Backlog Normalization Pass 2 - 2026-06-27

## Scope

Normalized the remaining raw download backlog statuses after the first settings/backlog audit. This pass changed documentation artifacts only. No live game files were edited.

## Result

Remaining triage rows: 0.

## Status Counts

- assessed-or-audited: 27
- deferred: 59
- fix-applied: 1
- future-removal-candidate: 1
- installed-partial-or-adjusted: 20
- installed-standard-or-script-merged: 212
- installed-with-manual-graft: 23
- quarantined-or-disabled: 6
- reference: 4
- skipped: 81
- tooling-reference: 2
- troubleshooting-record: 1

## Main Decisions Captured

- Synced direct Nexus IDs from the install status ledger into the raw downloads CSV.
- Marked optional E3 HUD/Better Icons patches for Magic Spells, AQOOM, and extra Better Icons variants as skipped unless their dependency stack is intentionally added.
- Marked Script Merger, SM-FAE, SharedImports, and debug console entries as tooling/prerequisite/reference rather than gameplay backlog.
- Marked known manual grafts and safe batch installs as installed with the correct caveat rather than raw triage.
- Deferred unresolved broad-content or hot-script mods instead of treating them as installed.

## Verification

- Regenerated backlog/witcher3-mod-download-backlog-2026-06-25.md from the CSV.
- Confirmed BacklogStatus = triage count is zero after regeneration.
