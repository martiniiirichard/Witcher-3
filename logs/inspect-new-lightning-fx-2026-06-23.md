# New Lightning FX Inspection

Date: 2026-06-23

Source:
- Nexus mod 2985
- Downloaded archives:
  - `C:\Users\marti\Downloads\New Lightning Effect - Next Gen Version-2985-3-0-1780800527.7z`
  - `C:\Users\marti\Downloads\New Lightning FX - Alternative Script For Weathers-2985-3-0-1780921783.7z`

Current installed state:
- Active mod folder:
  `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modnewlightningfx`
- Active DLC folder:
  `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\DLC\dlcnewlightningfx`
- Menu XML:
  `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\r4game\user_config_matrix\pc\NewLightningFX.xml`
- XML is registered in both:
  - `dx11filelist.txt`
  - `dx12filelist.txt`
- `mods.settings` contains `[modnewlightningfx]`.

Configuration check:
- `C:\Users\marti\OneDrive\Documents\The Witcher 3\dx12user.settings` has:
  - `modDebugInfo=false`
  - `modDebugMode=false`

Notes:
- The previously observed parchment debug overlay was caused by New Lightning FX debug settings.
- The current user settings have debug info and debug mode disabled.
- The installed `weathers_list.ws` is the weather-aware/expanded version and has a prior Codex backup:
  `weathers_list.ws.codex-backup-static-weather-list-20260623-120605`

Cleanup:
- A duplicate-looking `modNewLightningFX` folder appeared during inspection.
- On this filesystem, moving the camel-case path also moved the active lowercase mod path, meaning Windows treated them as the same underlying folder for this operation.
- The mod was immediately restored under the lowercase `modnewlightningfx` name used by `mods.settings`.
- Final state has one active lightning mod folder: `modnewlightningfx`.

Risk notes:
- Compile risk is already proven low because this mod has passed launch previously.
- Main risks are visual intensity, camera shake/reaction annoyance, and interactions with dense weather/cloud mods.
- Keep `modDebugInfo=false` and `modDebugMode=false` unless explicitly debugging lightning behavior.

Pending verification:
- Optional storm/weather smoke test after future weather changes.
