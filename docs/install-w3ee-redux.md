# W3EE Redux 1.46 Install Runbook

## Goal

Install W3EE Redux 1.46 on the clean local GOG GOTY install with enough logging and rollback points to debug script conflicts.

## Current State

- Game root exists.
- No `mods` folder was detected.
- No `Documents\The Witcher 3` folder was detected.
- Stock `dx12filelist.txt` and `dx11filelist.txt` were detected.

## Artifacts Needed

Download these manually from Nexus into local `downloads/`:

- `Community Patch - Shared Imports` from https://www.nexusmods.com/witcher3/mods/2110
- `Redux for W3EE (NextGen)` from https://www.nexusmods.com/witcher3/mods/5802

Nexus file downloads require login, so keep the archives local-only and out of Git.

Do not install `Redux for W3EE (OldGen)` into a Next-Gen 4.x game install. DX11 launch mode is not the same thing as OldGen; OldGen targets the pre-Next-Gen game branch.

## Install Steps

1. Launch The Witcher 3 once from GOG/REDlauncher, then exit at the main menu.
2. Confirm `Documents\The Witcher 3` now exists.
3. Back up:
   - `bin\config\r4game\user_config_matrix\pc\dx12filelist.txt`
   - `bin\config\r4game\user_config_matrix\pc\dx11filelist.txt`
   - `Documents\The Witcher 3`
4. Extract Community Patch - Shared Imports into the game root.
5. Extract W3EE Redux NextGen into the game root.
6. Copy Redux `input.settings` into `Documents\The Witcher 3`.
7. Add these menu entries to the relevant file list:

```text
ImmCamMenu.xml;
LFE.xml;
modFHUDConfig.xml;
modMoreQuickSlots.xml;
ReduxGaunterMode.xml;
W3EnhancedEdition.xml;
```

For the default GOG launch path, update `dx12filelist.txt`. If launching DX11, update `dx11filelist.txt` as well.

8. If `Documents\The Witcher 3\mods.settings` is created later, ensure `modReduxW3EE` has priority over `modW3EE`.
9. Launch the game and capture any script compilation error text/screenshots.
10. If the game starts, run `DefaultReduxSettings()` in console or set W3EE mod options manually.

## First Debug Checks

- Missing dependency: confirm `mods\modSharedImports` exists.
- Menu options missing: confirm the XML entries are in `dx12filelist.txt` or `dx11filelist.txt`.
- Input issues: confirm Redux `input.settings` landed in `Documents\The Witcher 3`.
- Script conflict: run Script Merger only after the two-mod baseline fails or after adding more mods.

## Save Guidance

A new game is the cleanest path. For an existing save, back up the save first, unequip gear, drink Potion of Clearance, save, install, apply Redux defaults, drink another Potion of Clearance, then redistribute skills.
