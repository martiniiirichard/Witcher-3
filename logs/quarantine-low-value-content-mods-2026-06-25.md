# Quarantine: low-value content-only mods

Date: 2026-06-25

## Decision

The user approved removing the following low-value/cosmetic content-only mods to reclaim loader budget:

- `mod_bald_tree_fix`
- `mod_beauclair_npc_spawn_fix`
- `mod_VGXVillageCutsceneBright`
- `modDandelionScarfFix`
- `modolgierd_rose`
- `modKnightHips`
- `modKnightPendant`

These were quarantined rather than deleted.

## New folder names

- `DISABLED_mod_bald_tree_fix.disabled-by-codex-low-value-cleanup-20260625`
- `DISABLED_mod_beauclair_npc_spawn_fix.disabled-by-codex-low-value-cleanup-20260625`
- `DISABLED_mod_VGXVillageCutsceneBright.disabled-by-codex-low-value-cleanup-20260625`
- `DISABLED_modDandelionScarfFix.disabled-by-codex-low-value-cleanup-20260625`
- `DISABLED_modolgierd_rose.disabled-by-codex-low-value-cleanup-20260625`
- `DISABLED_modKnightHips.disabled-by-codex-low-value-cleanup-20260625`
- `DISABLED_modKnightPendant.disabled-by-codex-low-value-cleanup-20260625`

Both `mods.settings` files were updated to `Enabled=0` for these sections.

## Loader impact

Active physical mod folders reduced from `203` to `196`.

Combined with the earlier E3 Quen cleanup, this recovered `10` active folder slots total.

## Verification

DX12 launch smoke test passed after quarantine:

- visible window at about `15s`
- title: `The Witcher 3`
- private memory reached about `4521 MB` at the first visible-window observation

