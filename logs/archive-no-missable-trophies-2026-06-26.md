# Archive No Missable Trophies

Date: 2026-06-26

## Decision

The user approved removing `modNoMissableTrophies` from the active stack.

This was archived, not deleted.

## Moved

Archive location:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_disabled_mods\archive-20260626-redundancy-cleanup\NoMissableTrophies`

Moved from `Mods`:

- `modNoMissableTrophies`

Moved from `DLC`:

- `dlcNoMissableTrophies`
- `dlcNoMissableMutagens`

## Settings

Updated:

`C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`

```ini
[modNoMissableTrophies]
Enabled=0
Priority=154
```

Backups:

- `backups\archive-no-missable-trophies-20260626\mods.settings.before`
- `backups\archive-no-missable-trophies-20260626\mods.settings.after`

## Verification

- `modNoMissableTrophies`: `Enabled=0`
- Enabled `mods.settings` entries without physical active folder: `0`

## Rollback

Move the archived `Mods` and `DLC` folders back to the game root and set `[modNoMissableTrophies] Enabled=1`.
