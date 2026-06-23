# Tweaks 2658

Date: 2026-06-23

Source:
- https://www.nexusmods.com/witcher3/mods/2658?tab=files

Downloads:
- `C:\Users\marti\Downloads\Tweaks (Next Gen version)-2658-5-1-2-1701864515.7z`
- `C:\Users\marti\Downloads\custom.ini-2658-5-1679771323.7z`

Intent:
- Adds more graphics and gameplay tweak options directly to the in-game menus.
- The optional `custom.ini` file is intended for settings that can be tested in-game but do not always save back cleanly.
- The Nexus files page notes the mod needs RTXGI Unlocker 7426; that dependency was already installed earlier.

Install:
- Copied Tweaks config files into:
  - `bin\config\base\general.ini`
  - `bin\config\base\rendering.ini`
  - `bin\config\r4game\user_config_matrix\pc\display.xml`
  - `bin\config\r4game\user_config_matrix\pc\gameplay.xml`
  - `bin\config\r4game\user_config_matrix\pc\graphics.xml`
  - `bin\config\r4game\user_config_matrix\pc\graphicsdx11.xml`
  - `bin\config\r4game\user_config_matrix\pc\hdr.xml`
  - `bin\config\r4game\user_config_matrix\pc\hud.xml`
- Added `bin\custom.ini`.
- Installed `mods\modTweaks` content files and strings.
- Enabled `modTweaks` in both known `mods.settings` copies:
  - `C:\Games\The Witcher 3\mods.settings`
  - `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`

Compatibility decision:
- The archive included `mods\modTweaks\content\scripts\game\gui\main_menu\ingameMenu.ws`.
- I intentionally omitted that script file from the installed mod.
- Reason: our W3EE stack already owns and customizes `game\gui\main_menu\ingameMenu.ws`, and the active W3EE file already contains the relevant RT/global illumination menu handling. Installing Tweaks' full script would risk replacing W3EE menu behavior for little expected gain.

Backup:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\tweaks-2658-20260623-185150`

Verification:
- DX12 smoke test passed: `witcher3.exe` stayed alive for 45 seconds after install.

Follow-up:
- Visually confirm the expanded options appear under the in-game settings menus.
- If an option appears but does not persist, test the value in-game and then place the stable value in `bin\custom.ini`.
