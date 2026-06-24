# Friendly Meditation Next Gen 7343

Date: 2026-06-23

## Source

- https://www.nexusmods.com/witcher3/mods/7343

## Installed Download

- `C:\Users\marti\Downloads\modFriendlyMeditation-7343-0-9-8NGE-1716371869.zip`

## Installed Game Folder

- `mods\modFriendlyMeditation`

## Manual Config Integration

The readme warns not to replace `input.xml` when other mods add hotkeys. This install already had AMM and other menu/input entries, so I did the manual path instead of overwriting.

Changed game config:

- Copied `modFMeditationConfig.xml` into `bin\config\r4game\user_config_matrix\pc`.
- Added `modFMeditationConfig.xml;` to both `dx11filelist.txt` and `dx12filelist.txt`.
- Inserted the Friendly Meditation input rows into the existing `input.xml`:
  - `MeditationStop`
  - `HoldToMeditate`
  - `MeditationFastForward`
  - `ToggleSpawnCampFire`

Changed user settings:

- Prepended Friendly Meditation defaults into `user.settings`.
- Prepended Friendly Meditation defaults into `dx12user.settings`.
- Prepended Friendly Meditation keybinds into `input.settings`.

Added to both active `mods.settings` copies:

- `modFriendlyMeditation`: priority `203`

Backup path:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\FriendlyMeditation_7343_20260623_225135`

## Script Fix

Initial compile error:

- `Error [modfriendlymeditation]fmedconfig\modfmeditationconfig.ws(92): 'fMeditationConfig' is not a member of 'handle:W3PlayerWitcher'`

Cause:

- Friendly Meditation defines `W3PlayerWitcher.fMeditationConfig` in its own `playerWitcher.ws`, but the active winning script is the merged file under `mod0000_MergedFiles`, so the property was missing from the class that actually compiles.

Fix:

- Added `public var fMeditationConfig : CModFMeditationConfig;` to `mods\mod0000_MergedFiles\content\scripts\game\player\playerWitcher.ws`.
- Initialized it in `OnSpawned` with:
  - `fMeditationConfig = new CModFMeditationConfig in this;`
  - `fMeditationConfig.Init();`

Technique learned:

- When a mod error reports a missing member/function that exists in the mod's own version of a conflicted script, patch the active winning/merged script, not the losing source script. This preserves the current W3EE/AMM/NOB/E3 merged behavior while adding the minimum missing contract expected by the new mod.

## Verification

- `input.xml` parses as XML after manual hotkey insertion.
- DX12 smoke test passed after the merged `playerWitcher.ws` patch; process stayed alive for 45 seconds and was killed manually.

## Residual Risk

- This mod has a broad script surface: meditation states, player input, menu scripts, `playerWitcher`, `r4Player`, place of power, beds, and Quen.
- The compile smoke is clean, but in-world validation should test:
  - Mods menu shows Friendly Meditation.
  - Hold `N` starts meditation.
  - `Space` advances time where expected.
  - `End` toggles campfire spawning.
  - Normal W3EE meditation/menu behavior still works.
