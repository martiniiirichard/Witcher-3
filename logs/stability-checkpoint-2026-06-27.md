# Stability Checkpoint - 2026-06-27

## Scope

Post-backlog-normalization validation before adding another mod batch.

## Checks

- Git repo was clean before validation: `main...origin/main [ahead 154]`.
- Active `mods.settings`: `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`.
- Enabled mod entries: `194`.
- Physical mod folders: `194`.
- Enabled entries missing physical folder: `0`.
- Physical folders without enabled settings entry: `0`.
- Duplicate enabled priorities: `6` known pairs.

## Known Duplicate Priority Pairs

- `0`: `mod00FlorenEconomySystem_W3EE_REDUX`, `modWoodlandSpirit`.
- `6`: `modleadOre`, `mod000000_W3EER_FoodRebalance_LighterBombsCompat`.
- `10`: `mod0_E3HUD_W3EER_NG`, `mod0BiA_ASL_Compatibility`.
- `22`: `modReduxW3EE`, `modMenuOrganizerNG_IMM_MrCK`.
- `124`: `modDilatedPupils`, `modtoussaintw4New`.
- `265`: `modAWitcherCanHideAnother`, `modVVSSDiagramRestoredVerCNextGen`.

## Launch Smoke

- Launched direct DX12 executable: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\x64_dx12\witcher3.exe`.
- Process stayed alive for the first 35 seconds, which is a positive compile/startup signal.
- No save-load or in-world test was performed during this checkpoint.

## Next Move

Load a stable save and verify menu/UI behavior in game. If it passes, this is a reasonable baseline before attempting another deferred mod.
