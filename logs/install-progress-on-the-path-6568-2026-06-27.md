# Progress on the Path - W3EE Redux (6568)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/6568
Archive: `C:\Users\marti\Downloads\Progress on the Path - W3EE Redux-6568-6-0-0-7-1731236903.zip`

## Decision

Installed with a manual graft instead of copying the full script set directly.

The mod is a completion/progress tracker, not a leveling or economy rebalance. It marks craftable/collected progress in relevant menus and adds hotkeys for updating and previewing progress.

## Install Notes

- Installed `modProgressOnThePath`.
- Installed `bin\config\r4game\user_config_matrix\pc\modProgressOnThePath.xml`.
- Did not overwrite existing SharedUtils folders, because the current stack already has active SharedUtils modules from Random Encounters Reworked and other mods.
- Disabled the raw Progress `craftingMenu.ws` as `craftingMenu.ws.disabled-by-codex`.
- Grafted `PotP_GetCollectedStringForCrafting(...)` into the active Better Icons / W3EE crafting menu layer:
  - `mods\modBetterIcons2025_NextGen_W3EE\content\scripts\game\gui\menus\craftingMenu.ws`
- Added `modProgressOnThePath.xml;` to both DX11 and DX12 user config filelists.
- Added Progress on the Path settings to `user.settings` and `dx12user.settings`.
- Added default hotkeys to `input.settings`:
  - `NumPad5`: `UpdateProgressOnThePath`
  - `NumPad6`: `DisplayProgressPreview`
- Added the input actions to `input.xml`.
- Added `[modProgressOnThePath]` to `mods.settings` at enabled priority `120`.

Backup path:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\progress-on-the-path-6568-20260627-215530`

## Validation

- Enabled mod count after install: 195.
- Enabled missing physical folders: none found during the pre-install checkpoint.
- Enabled duplicate priority count stayed at the known baseline of 6.
- Progress XML appears once in both DX11 and DX12 filelists.
- Progress's raw `craftingMenu.ws` is disabled, so it does not add a fifth script owner for `game\gui\menus\craftingMenu.ws`.
- Better Icons active crafting menu contains exactly one `PotP_GetCollectedStringForCrafting` graft.
- DX12 game launched and remained responding for 40 seconds after script compilation.

## Residual Risk

This still needs an in-game menu check after loading a save: confirm the Progress on the Path menu opens, hotkeys do not conflict, and crafting/collection labels display correctly. The compile/startup smoke test passed.
