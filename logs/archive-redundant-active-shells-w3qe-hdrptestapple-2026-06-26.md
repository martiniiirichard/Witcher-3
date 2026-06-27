# Archive Redundant Active Shells - W3QE and HDRP Test Apple

Date: 2026-06-26

## Goal

Remove two low-value active mod folders from the game scan path after redundancy review:

- `modW3QE`
- `modHDRPTestApple`

This was an archive move, not a deletion.

## Decisions

### `modW3QE`

Archived because the only real mod payload was already disabled:

- `content\blob0.bundle.disabled-by-codex-internal-test`

That bundle previously caused the no-window startup hang documented in:

- `logs\investigate-w3qe-9360-startup-hang-2026-06-24.md`

The remaining folder only had `metadata.store` plus the disabled bundle, so keeping it enabled created scan/audit clutter without restoring the broken scene.

Important: `DLC\dlcW3QE` was left in place.

### `modHDRPTestApple`

Archived because it is an HDRP test utility, not part of the required HDRP stack.

The required HDRP folders remain active separately, including the BiA HDRP patch.

## Changes

Moved to:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_disabled_mods\archive-20260626-redundancy-cleanup\Mods-active-shells`

- `modW3QE`
- `modHDRPTestApple`

Updated:

`C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`

```ini
[modW3QE]
Enabled=0
Priority=241

[modHDRPTestApple]
Enabled=0
Priority=179
```

Backups:

- `backups\archive-redundant-active-shells-20260626\mods.settings.before`
- `backups\archive-redundant-active-shells-20260626\mods.settings.after`

## Verification

- `modW3QE`: `Enabled=0`
- `modHDRPTestApple`: `Enabled=0`
- Enabled `mods.settings` entries without physical active folder: `0`
- `DLC\dlcW3QE` still exists.
- `DLC\DLCVolumetricCloudsBootstrap` still exists.

## Rollback

Move the folder back from `Mods-active-shells` to the game `Mods` directory and set the relevant `mods.settings` entry back to `Enabled=1`.
