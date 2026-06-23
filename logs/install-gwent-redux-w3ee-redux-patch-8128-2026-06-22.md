# Gwent Redux + W3EE Redux Patch

Sources:
- https://www.nexusmods.com/witcher3/mods/4287
- https://www.nexusmods.com/witcher3/mods/8128?tab=files
- https://www.nexusmods.com/witcher3/mods/2109?tab=files

Installed archives:
- `Gwent Redux (Next-Gen v4.04)-4287-NEXT-GENv4-04-1691430518(1).zip`
- `PatchGwent Redux-W3EE_REDUX-8128-0-1-1681556759.7z`
- `modBootstrap-v.0.5-NEXT-GEN-2109-v0-5-NEXT-GEN-1771092575.zip`
- `modBootstrap-registry-2109-1-0-1554756443.zip`

Installed game folders:
- `mods/modGwentRedux`
- `mods/modPatchGwentRedux_W3EE_W3EERedux`
- `mods/modBootstrap`
- `mods/modBootstrap-registry`
- `DLC/dlcBootstrap`

Configuration:
- Added `modGwentReduxConfig.xml` to `bin/config/r4game/user_config_matrix/pc`.
- Added `modGwentReduxConfig.xml;` to both `dx11filelist.txt` and `dx12filelist.txt`.
- Added `mods.settings` entries:
  - `modPatchGwentRedux_W3EE_W3EERedux` at priority 2.
  - `modGwentRedux` at priority 3.
  - `modBootstrap` and `modBootstrap-registry` after the existing stack.
- Existing top-of-stack XML patch mods were shifted down by two priorities.

Script handling:
- Gwent Redux ships full overrides for:
  - `game/components/inventoryComponent.ws`
  - `game/gameParams.ws`
  - `game/gui/menus/gwintBaseMenu.ws`
  - `game/gui/menus/gwintManager.ws`
  - `game/gui/_old/components/guiTooltipComponent.ws`
  - `game/player/playerWitcher.ws`
- The full Gwent Redux `content/scripts` folder was renamed to `scripts.disabled-by-codex`.
- A minimal live `content/scripts` folder was recreated with only:
  - `game/gui/menus/gwintBaseMenu.ws`
  - `game/gui/menus/gwintManager.ws`
- The heavier conflict files remain disabled for now to protect the existing W3EE/AMM/Shades/BiA/Reflex merged work.

Validation:
- Launched through `tools/direct-launchers/Witcher3DirectDX12.exe`.
- Startup/script compile passed; `witcher3` remained running and responding after the launch window.

Rollback:
- Backup created under `backups/4287-8128-gwent-redux-20260622-194747/`.

Reusable lesson:
- For large overhaul mods with full script copies, enable only unique/non-conflicting script files first. Leave broad overrides parked until a concrete compile or gameplay need proves they must be grafted into `mod0000_MergedFiles`.
