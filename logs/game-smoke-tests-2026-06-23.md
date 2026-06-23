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

