# Game Smoke Testing Workflow

Use this workflow after installing or changing any mod that can affect scripts, menus, weather, spawning, travel, bestiary, UI, or save loading.

## Rule

When Codex says "hands off", do not click or type until Codex reports back. Witcher 3 accepts foreground input only, and Windows can send test commands to the wrong app if focus changes.

## Standard Test Loop

1. Launch with the direct DX12 launcher:
   - `tools\direct-launchers\Witcher3DirectDX12.exe`
2. Capture a baseline screenshot after the game window appears.
3. Skip any update/cinematic prompt if present.
4. For route/location-specific tests, open the offline map utility first:
   - `C:\Users\marti\OneDrive\Desktop\Witcher 3 Interactive Map.lnk`
5. Use the map to choose the target region, nearby marker, and fallback route before teleporting or enabling all pins.
6. Load into a save or start the current test scenario.
7. Run targeted console commands.
8. Capture screenshots after each important command or menu state.
9. Close the game cleanly or stop the process if it is stuck.
10. Record the result in `logs\game-smoke-tests-YYYY-MM-DD.md`.

## Useful Console Commands

Travel:

- `gotoNovigrad`
- `gotoSkellige`
- `gotoKaerMohren`
- `gotoProlog`
- `gotoPrologWinter`

Fast travel and map visibility:

- `AllowFT(1)`
- `ShowAllFT(1)`
- `ShowPins(1)`

Weather:

- `changeweather(WT_Clear)`
- `changeweather(WT_Light_Rain)`
- `changeweather(WT_Rain_Storm)`
- `changeweather(WT_Heavy_Clouds_Dark)`
- `changeweather(WT_q501_Storm)`
- `makeitrain`
- `stoprain`

Time:

- `settime(1,6,0,0)`
- `settime(1,12,0,0)`
- `settime(1,22,0,0)`

Bestiary and glossary:

- `activateAllGlossaryBeastiary`

## Result Categories

- Pass: game loads and the targeted feature behaves plausibly.
- Pass with notes: game loads, but there is visual oddness, warnings, or uncertain behavior.
- Fail: script compile error, crash, missing dependency dialog, unusable menu, or broken save load.
- Not tested: blocked by missing save state, missing visual confirmation, or unreliable input focus.

## Evidence To Keep

For each meaningful run, log:

- Date and time.
- Mod or change being tested.
- Launcher used.
- Save or location tested.
- Offline map route/marker used, when relevant.
- Commands used.
- Screenshots captured.
- Pass/fail result.
- Any suspected root cause and next action.
