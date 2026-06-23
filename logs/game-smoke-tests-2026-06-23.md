# Game Smoke Tests - 2026-06-23

## Foreground Control Test

Change under test:

- Validate that Codex can launch Witcher 3, focus the game window, send input, and capture screenshots for future mod testing.

Launcher:

- `tools\direct-launchers\Witcher3DirectDX12.exe`

Evidence:

- `C:\Users\marti\AppData\Local\Temp\witcher3-codex-window-test\before-input.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-codex-window-test\after-input.png`

Observed:

- Before input, Witcher 3 was focused and showing the update/settings reset notice with the `Space` skip prompt.
- After input, the game loaded into an active in-game interior scene with Geralt visible and HUD prompts active.
- No Witcher process was left running after the test.

Result:

- Pass.

Notes:

- This proves the workflow is viable when the user avoids mouse and keyboard input during the test window.
- The game displayed a settings reset notice, so future odd behavior should include a quick check of `dx12user.settings`.

## Reusable Next Test Template

Change under test:

- TBD

Launcher:

- `tools\direct-launchers\Witcher3DirectDX12.exe`

Commands:

- TBD

Screenshots:

- TBD

Observed:

- TBD

Result:

- Not tested.

Next action:

- TBD

## Current Stack Validation Attempt

Change under test:

- Baseline runtime check after Live Bestiary, weather/lighting stack, menu label fixes, and smoke-test workflow documentation.

Launcher:

- `tools\direct-launchers\Witcher3DirectDX12.exe`

Evidence:

- `C:\Users\marti\AppData\Local\Temp\witcher3-current-stack-smoke-20260623-123348\01-initial.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-current-stack-smoke-20260623-123348\02-after-space-skips.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-current-stack-smoke-20260623-123348\03-after-allowft.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-current-stack-smoke-20260623-123348\04-novigrad.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-current-stack-smoke-20260623-123348\05-novigrad-storm.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-current-stack-smoke-20260623-123348\06-novigrad-clear.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-current-stack-smoke-20260623-123348\07-after-bestiary-command.png`

Commands attempted:

- `AllowFT(1)`
- `gotoNovigrad`
- `changeweather(WT_Rain_Storm)`
- `changeweather(WT_Clear)`
- `activateAllGlossaryBeastiary`

Observed:

- Game launched and reached the main menu.
- The run continued into an active in-game interior save without a crash.
- The world map opened successfully and showed Novigrad with map markers visible.
- The game process was stopped after the run; no Witcher process was left running.
- Console command execution is not yet proven. The automated key sequence appears to have interacted with menus/map rather than reliably opening the console and executing every command.

Result:

- Pass with notes.

Next action:

- Improve the automation so it explicitly confirms console visibility before sending commands.
- Then rerun the weather and Live Bestiary checks from in-game state rather than treating this attempt as a full visual QA pass.

## Console Command Test From Loaded World

Change under test:

- Validate debug console access after the user manually loaded into a usable in-world save.

Evidence:

- `C:\Users\marti\AppData\Local\Temp\witcher3-console-world-test-20260623-132538\01-before-console.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-console-world-test-20260623-132538\02-after-backtick.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-console-world-test-20260623-132538\03-after-showpins.png`
- `C:\Users\marti\AppData\Local\Temp\witcher3-console-world-test-20260623-132538\05-after-settime-noon.png`

Commands tested:

- `ShowPins(1)`
- `settime(1,12,0,0)`

Observed:

- Backtick/tilde key opens the debug console from a loaded world state.
- The console prompt appears on the left side of the screen as `>`.
- Clipboard paste plus Enter successfully submits commands.
- Submitted command history was visible in green text for `ShowPins(1)` and `settime(1,12,0,0)`.
- `P` is not needed for console testing; in this run it typed into the already-open console after the previous command surface remained active.
- Game was left running for the user after the test.

Result:

- Pass.

Next action:

- Use backtick as the standard console key for future tests.
- For weather validation, load an outdoor save, open console with backtick, run `changeweather(...)`, close console with Escape, and screenshot after a short wait.
