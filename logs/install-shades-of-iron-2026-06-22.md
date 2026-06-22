# Shades of Iron Install Checkpoint

Date: 2026-06-22

## Installed Archives

- `Shades of Iron v2.0 - Game Version 4.04-7271-Final-1732825923(1).zip`
- `AMM and SoI config for NEXT GEN update 1.0.2-7037-1-0-2-1672185866.zip`
- `SOI - EER - Patch-9971-v2-1735365638.zip`

## Runtime Changes

- Installed base SoI mod folder:
  - `mods/modShadesOfIron`
- Installed base SoI DLC folders:
  - `dlc/dlcShadesChests`
  - `dlc/dlcShadeWatcher`
  - `dlc/dlc_ShadesOfIron`
- Installed W3EE Redux/EER compatibility patch:
  - `mods/modShadesW3EEredux`
- Installed AMM + SoI config over existing AMM files:
  - `mods/modAMM/content/scripts/local/AMM.ws`
  - `bin/config/r4game/user_config_matrix/pc/AMM.xml`

## Load Order

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modShadesW3EEredux]
Enabled=1
Priority=14

[modShadesOfIron]
Enabled=1
Priority=15
```

## Manual Compatibility Decision

The SoI W3EE Redux patch includes a full replacement `game/player/playerWitcher.ws`, but that file does not include the active AMM/W3EE Redux hooks from `mod00AMMW3EEReduxNG139b`.

To avoid breaking AMM, the installed patch file was disabled:

- `mods/modShadesW3EEredux/content/scripts/game/player/playerWitcher.ws.disabled-by-codex`

Then the small SoI compatibility guard was grafted into the current winning `mod00AMMW3EEReduxNG139b` `playerWitcher.ws` around the Manticore/Red Wolf bomb-ammo set bonus block:

```witcherscript
if ( GetCurioWatcher().Check_alchemy_set() ) { /* SoI/W3EE alchemy set guard */ } else
```

## Backup

Runtime backup created before install:

- `backups/shades-of-iron-20260622-093311`

## Expected Script Merger Work

New collisions introduced by SoI:

- `game/actor.ws`: `modShadesOfIron` vs `modW3EE`
- `game/components/inventoryComponent.ws`: `modShadesOfIron` vs `modW3EE`
- `game/gui/_old/components/guiTooltipComponent.ws`: `modShadesOfIron` vs `modW3EE`
- `game/gui/menus/inventoryMenu.ws`: `modShadesOfIron` vs `modW3EE`
- `local/curio_watcher.ws`: `modShadesOfIron` vs `modShadesW3EEredux`

Existing baseline collisions remain from AMM/W3EE and W3EE Redux/W3EE.

## Verification

- Confirmed SoI mod and DLC directories exist in the game root.
- Confirmed `AMM.xml` parses as XML after install.
- Confirmed SoI priorities were appended to `mods.settings`.
- Confirmed the SoI guard exists in the active `mod00AMMW3EEReduxNG139b` `playerWitcher.ws`.
- Launched Script Merger for manual refresh/merge.
- User confirmed the post-merge state is good.

Next step: commit this working checkpoint before installing additional mods.
