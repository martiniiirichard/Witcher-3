# Download triage - contained fixes batch - 2026-06-23

## Goal

Continue after the first low-risk batch passed by installing another conservative set of downloaded mods with no scripts, no XML menu files, and no input/config edits.

## Installed

Installed folders:

- `dlcSheathe`
- `mod_beauclair_npc_spawn_fix`
- `mod_bald_tree_fix`
- `modZ_GrammarOfThePath`
- `modNoMissableTrophies`
- `dlcNoMissableTrophies`
- `dlcNoMissableMutagens`
- `modCorvoBiancoGuestsExtended`
- `dlcCorvoBiancoGuestsExtended`

`mods.settings` was backed up before editing:

- `C:\Games\The Witcher 3\mods.settings.codex-backup-contained-fixes-batch-20260623-142702`

New priorities appended:

- `mod_beauclair_npc_spawn_fix`: `149`
- `mod_bald_tree_fix`: `150`
- `modZ_GrammarOfThePath`: `151`
- `modNoMissableTrophies`: `152`
- `modCorvoBiancoGuestsExtended`: `153`

## Verification

Static verification passed after install:

- All installed folders exist under the game `Mods` or `DLC` directories.
- Installed batch contains `0` `.ws` script files.
- Installed batch contains `0` `.xml` menu files.
- No Script Merger run was required for this batch.

User launch smoke test passed after install.

## Deferred

Deferred for later:

- `mod000000aHDRP_BiA` because it should only be added if HDRP is intentionally part of the active visual stack.
- UI, menu, icon, input, and script-facing downloads remain parked for one-at-a-time handling.

## Notes

This batch is still conservative but touches more gameplay/content surfaces than the first batch. It should be launch-tested before stacking larger script or menu mods on top.
