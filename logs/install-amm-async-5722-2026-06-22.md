# AMM Async Loading Patch Checkpoint

Date: 2026-06-22

## Mod

- Nexus: `https://www.nexusmods.com/witcher3/mods/5722`
- Archive: `AMM patch - asynchronous loading-5722-1-0-1620645327.zip`

## Install Decision

Did not overwrite `modAMM/content/scripts/local/AMM.ws`.

Reason: the archive contains a full replacement `AMM.ws`, but the current installed AMM file already includes later edits from the active stack, including Shades of Iron and Swords on Roach support. A wholesale replacement would likely remove those integrations.

Instead, the async-loading behavior was grafted into the current installed `AMM.ws`.

## Runtime Changes

Patched:

- `mods/modAMM/content/scripts/local/AMM.ws`

Graft summary:

- Converted `CAMM` to a `statemachine class`.
- Added `CAMM` `Waiting` and `Loading` states.
- Added `CAMM_RoachRefresher` state machine.
- Added async wrapper functions:
  - `RefreshAppearance()`
  - `RefreshRoach()`
- Preserved immediate implementations as:
  - `RefreshAppearanceImmediate()`
  - `RefreshRoachImmediate()`

## Backup

Runtime backup created before patch:

- `backups/amm-async-5722-20260622-100514`

## Verification

- Confirmed the installed AMM file contains the async state-machine graft.
- Confirmed the file no longer contains literal escape artifacts from the patching pass.
- Launched with the direct DX12 launcher.
- User confirmed the game is good after launch.

Next step: commit this working checkpoint before installing additional mods.
