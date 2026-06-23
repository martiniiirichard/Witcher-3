# Testing utility - skip storybook - 2026-06-23

## Goal

Install Nexus mod `816` as a testing utility to speed repeated load-game smoke tests by disabling storybook recap videos.

## Installed

- `moddisablestorybooks`

Archive:

- `C:\Users\marti\Downloads\Skip storybook-816-1-0.7z`

`mods.settings` backup:

- `C:\Games\The Witcher 3\mods.settings.codex-backup-skip-storybook-20260623-143351`

Priority:

- `moddisablestorybooks`: `154`

## Verification

Static verification passed:

- Folder exists under the game `Mods` directory.
- Contains `0` `.ws` script files.
- Contains `0` `.xml` menu files.
- No Script Merger run was required.

## Notes

This is not a debug console mod. It is useful testing infrastructure because it reduces friction when repeatedly loading saves during mod smoke tests.
