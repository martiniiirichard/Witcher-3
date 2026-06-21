# OneDrive Junction Move - 2026-06-21

## Goal

Move the active Witcher 3 config/save folder out of OneDrive while preserving the path the game expects.

## Before

Windows Documents known folder:

```text
C:\Users\marti\OneDrive\Documents
```

Active Witcher 3 folder:

```text
C:\Users\marti\OneDrive\Documents\The Witcher 3
```

## Backup

Created before moving:

```text
C:\Users\marti\OneDrive\Documents\New project\Witcher-3\backups\pre-onedrive-junction-20260620-225912
```

## After

Real folder:

```text
C:\Games\The Witcher 3
```

Game-visible junction:

```text
C:\Users\marti\OneDrive\Documents\The Witcher 3 -> C:\Games\The Witcher 3
```

## Verification

- Old OneDrive path is a junction/reparse point.
- Junction target is `C:\Games\The Witcher 3`.
- `mods.settings` resolves correctly from both paths.
- W3EE Redux load order is preserved.

## Rollback

To roll back manually:

1. Make sure the game is closed.
2. Delete only the junction at `C:\Users\marti\OneDrive\Documents\The Witcher 3`.
3. Move `C:\Games\The Witcher 3` back to `C:\Users\marti\OneDrive\Documents\The Witcher 3`.
