# Wearable Pocket Items Redux 11599

Date: 2026-06-22

Source:
- https://www.nexusmods.com/witcher3/mods/11599
- Download: `Wearable Pocket Items Redux - Next Gen-11599-1-5-5-1771305577.7z`

Installed:
- `mods/mod_WPI_Redux`
- `bin/config/r4game/user_config_matrix/pc/WPI.xml`

Configuration:
- Added `WPI.xml;` to `dx11filelist.txt` and `dx12filelist.txt`.
- Added `[mod_WPI_Redux]` to `C:\Games\The Witcher 3\mods.settings` at priority `117`.

Compatibility strategy:
- Disabled WPI's broad script overrides under `mods/mod_WPI_Redux/content/scripts/game` as `.disabled-by-codex`.
- Kept only `mods/mod_WPI_Redux/content/scripts/local/WPI.ws` active inside the mod folder.
- Grafted the marked `//modWPI` hooks into active merged winners in `mod0000_MergedFiles`.

Merged hook targets:
- `game/gameplay/poster.ws`
- `game/gameplay/interactive/monsterNestEntity.ws`
- `game/gameplay/items/itemEntity.ws`
- `game/gameplay/items/throwables/petards/petard.ws`
- `game/gui/menus/menuBase.ws`
- `game/player/playerAiming.ws`
- `game/player/playerWitcher.ws`
- `game/player/r4Player.ws`
- `game/quests/quest_function.ws`

Backups:
- `tools/backups/before-wpi-redux-11599-20260622-221801`
- `tools/backups/before-wpi-graft-20260622-222022`

Validation:
- Confirmed only `local/WPI.ws` remains active in `mod_WPI_Redux`.
- Confirmed WPI hooks are present in the merged script layer.
- Direct DX12 launch passed by user confirmation.
