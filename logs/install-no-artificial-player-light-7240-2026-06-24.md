# No Artificial Player Light - Next Gen - 7240

Date: 2026-06-24

Source:
- https://www.nexusmods.com/witcher3/mods/7240

Installed archive:
- `C:\Users\marti\Downloads\Menu - No Artificial Player and Cutscene Light-7240-2-08-1768843221.rar`

Installed paths:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modNoArtificialPlayerLight`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\r4game\user_config_matrix\pc\artificialplayerlight.xml`

Settings:
- Added `[modNoArtificialPlayerLight]` with `Enabled=1`, `Priority=256` to both active `mods.settings` files.
- Appended `artificialplayerlight.xml;` to DX12 file list:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\r4game\user_config_matrix\pc\dx12filelist.txt`

Notes:
- Page requirement block still lists Shared Imports, but the 2.08 changelog says the mod was rewritten so Shared Imports is no longer required.
- Script is annotation-only and wraps:
  - `CR4Game`
  - `CR4IngameMenu`
  - `CR4ScriptedHud`
  - `W3Potion_Cat`
- Static search found no duplicate fields/method names before install.
- Installed only DX12 menu file registration because this setup uses the DX12 executable.

Verification:
- DX12 launch smoke passed: game remained running after 60 seconds.

Residual risk:
- Visual behavior still needs in-game confirmation:
  - Mod menu entry appears.
  - Gameplay player light toggle behaves as expected.
  - Cutscene light toggle behaves as expected.
  - Cat potion correctly restores/removes the gameplay light behavior.
