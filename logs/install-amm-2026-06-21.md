# AMM Install Log - 2026-06-21

## Goal

Install Appearance Menu Mod (AMM) on the current W3EE Redux Next-Gen stack, using the available AMM compatibility patch for W3EE Redux.

## Game Paths

- Game root: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY`
- User config root: `C:\Games\The Witcher 3`
- Documents junction: `C:\Users\marti\OneDrive\Documents\The Witcher 3` -> `C:\Games\The Witcher 3`

## Archives Used

- `AMM 4.04 Scripts and Horse Mod-780-4-04-1689807822.rar`
- `AMM 4.0 Menu Inputs and DLCs-780-4-03-1684511560.rar`
- `AMM and W3EE Redux NextGen 1.39b-8627-1-0-1699875365.7z`

## Installed Files

- `mods\modAMM`
- `mods\mod00AMMW3EEReduxNG139b`
- `dlc\DLCAMM`
- `dlc\DLCAMMHORSE`
- `bin\config\r4game\user_config_matrix\pc\AMM.xml`
- `bin\config\r4game\user_config_matrix\pc\AMMRoach.xml`

## Config Changes

- Prepended AMM input bindings into `C:\Games\The Witcher 3\input.settings`.
- Inserted AMM menu entries into:
  - `bin\config\r4game\user_config_matrix\pc\hidden.xml`
  - `bin\config\r4game\user_config_matrix\pc\input.xml`
- Added AMM menu files to:
  - `bin\config\r4game\user_config_matrix\pc\dx11filelist.txt`
  - `bin\config\r4game\user_config_matrix\pc\dx12filelist.txt`

## Load Order

`C:\Games\The Witcher 3\mods.settings`:

```ini
[mod00AMMW3EEReduxNG139b]
Enabled=1
Priority=1

[mod_SNC_W3EERedux]
Enabled=1
Priority=2

[modAMM]
Enabled=1
Priority=3

[modSharedImports]
Enabled=1
Priority=4

[modReduxW3EE]
Enabled=1
Priority=5

[modW3EE]
Enabled=1
Priority=6

[modW3EELocalization1]
Enabled=1
Priority=7

[modW3EELocalization2]
Enabled=1
Priority=8

[modW3EELocalization3]
Enabled=1
Priority=9

[modW3EELocalization4]
Enabled=1
Priority=10
```

## Repair Applied

AMM's `hidden.xml` snippet included invalid raw `<u>` markup inside the `HeadEnabled` `displayName` XML attribute:

```xml
Show Head - <u>This only works when body is hidden<u>
```

This was changed to:

```xml
Show Head - This only works when body is hidden
```

AMM's `modAMM\content\scripts\game\player\states\combatSword.ws` also referenced `W3Mutagen21_Effect`, but the installed W3EE `mutagen21.ws` has that class commented out. This caused launch-time script compilation to fail:

```text
Error [modamm]game\player\states\combatsword.ws(1014): Unknown type 'W3Mutagen21_Effect' for property 'mutagen'.
```

Applied a minimal compatibility fix to AMM's winning `combatSword.ws`:

- Removed `var mutagen : W3Mutagen21_Effect;`
- Removed the light special attack `EET_Mutagen21` heal block.
- Removed the heavy special attack `EET_Mutagen21` heal block.

Backup:

- `backups\amm-combatSword-mutagen-fix-20260621\combatSword.ws.pre-mutagen-fix`

The next launch progressed farther and exposed two missing-method errors caused by older winning AMM/compatibility scripts shadowing newer W3EE Redux methods:

```text
Error [modw3ee]game\gameplay\ability\playerabilitymanager.ws(4276): Could not find function 'SetMutationSpentMutagens'
Error [modw3ee]game\behavior_tree\tasks\horse\bthorse.ws(597): Could not find function 'ShouldRest'
```

Applied minimal W3EE Redux 1.46 compatibility grafts:

- Added W3EE's mutation bookkeeping vars and `SetMutationSpentMutagens(itemString, quantity)` to `mod00AMMW3EEReduxNG139b\content\scripts\game\player\playerWitcher.ws`.
- Added W3EE's `shouldHorseRest`, `ShouldRest()`, and `SetHorseRest(...)` timer to `modAMM\content\scripts\game\vehicles\horse\horseManager.ws`.

Backup:

- `backups\amm-w3ee-missing-methods-20260621\playerWitcher.ws.pre-missing-methods`
- `backups\amm-w3ee-missing-methods-20260621\horseManager.ws.pre-missing-methods`

## Verification

- Confirmed installed mod/DLC/menu files exist.
- Confirmed `dx12filelist.txt` includes `AMM.xml;` and `AMMRoach.xml;`.
- Confirmed all four menu XML files parse successfully:
  - `hidden.xml`
  - `input.xml`
  - `AMM.xml`
  - `AMMRoach.xml`
- Confirmed current load order keeps `mod00AMMW3EEReduxNG139b` above AMM and W3EE Redux.
- Confirmed AMM's patched `combatSword.ws` no longer references `W3Mutagen21_Effect`.
- Confirmed the winning `playerWitcher.ws` now includes `SetMutationSpentMutagens`.
- Confirmed the winning `horseManager.ws` now includes `ShouldRest`.

## Next Validation

Launch the game and verify:

- No script compilation error on startup.
- Main menu loads.
- Existing save or new game loads.
- AMM menu appears in Options.
- AMM hotkeys/menu inputs respond.

Do not commit this branch until the launch test succeeds.
