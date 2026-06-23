# Menu Label Cleanup - Swords and Meditation

Date: 2026-06-23

## Issue

The in-game Mods menu wrapped `Swords and Meditation` into three lines and overlapped the next menu entry, `Brothers In Arms`.

## Change

Shortened the English `modSwordscampfire` menu title strings in:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modSwordscampfire\content\en.w3strings`

Patched string ids:

- `2114064002`: `Swords and Meditation` -> `Swords`
- `2114064003`: `Swords and Meditation` -> `Swords`

String id `2114064004` was already `Swords`.

## Backup

A timestamped backup was created next to the live file:

`en.w3strings.codex-backup-short-menu-<timestamp>`

## Note

This follows the same technique used for Random Encounters Reworked: when the menu XML points at a localized key, patch the `.w3strings` entry directly instead of relying on XML ordering or spacing.
