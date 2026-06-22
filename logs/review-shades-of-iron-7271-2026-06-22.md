# Shades of Iron Review - 2026-06-22

## Nexus Page

- `https://www.nexusmods.com/witcher3/mods/7271`

## Archive Found

- `Shades of Iron v2.0 - Game Version 4.04-7271-Final-1732825923(1).zip`

Duplicate also exists:

- `Shades of Iron v2.0 - Game Version 4.04-7271-Final-1732825923.zip`

## Page Notes

Nexus page identifies the mod as:

- `Shades of Iron v2.0 - Content Pack (Nextgen Upgraded)`
- Version: `Final`
- Last updated: `2024-11-28`
- DLC requirements:
  - Hearts of Stone
  - Blood and Wine
- Nexus requirement:
  - Hoods

The page describes it as a large additional content pack with new armors, weapons, enemies, and gameplay mechanics. Install instructions say to put the DLC and Mod folders into the game directory and run Script Merger.

The page also lists related mods that require Shades of Iron:

- `AMM and SoI - Appearances Menu Mod and Shades of Iron (next gen updated)`
- `Shades of Iron - W3EE Redux - Compatibility Patch (WIP)`

## Archive Layout

Adds one mod folder:

- `Mods\modShadesOfIron`

Adds three DLC folders:

- `dlc\dlcShadesChests`
- `dlc\dlcShadeWatcher`
- `dlc\dlc_ShadesOfIron`

Script files:

- `game\actor.ws`
- `game\components\inventoryComponent.ws`
- `game\gui\menus\inventoryMenu.ws`
- `game\gui\_old\components\guiTooltipComponent.ws`
- `local\CNewNPCshades.ws`
- `local\curio_watcher.ws`
- `local\items_shades.ws`
- `local\previewer.ws`
- `local\shades_main.ws`
- `local\spawney.ws`

## Risk Classification

High.

Reason:

- Very large content pack.
- Ships full overrides for core game scripts.
- Directly collides with W3EE script paths.
- Touches actor, inventory, inventory menu, and tooltip systems.
- Current branch is `codex/hoods`; Hoods should be merged first because Shades of Iron requires it.

## Pre-Install Conflict Inventory

Staged SoI files that directly collide with installed W3EE scripts:

```text
game\actor.ws
  conflicts with modW3EE\content\scripts\game\actor.ws

game\components\inventoryComponent.ws
  conflicts with modW3EE\content\scripts\game\components\inventoryComponent.ws

game\gui\menus\inventoryMenu.ws
  conflicts with modW3EE\content\scripts\game\gui\menus\inventoryMenu.ws

game\gui\_old\components\guiTooltipComponent.ws
  conflicts with modW3EE\content\scripts\game\gui\_old\components\guiTooltipComponent.ws
```

This is especially sensitive because W3EE already rewrites `inventoryMenu.ws` and changes the inventory menu class to `WmkCR4InventoryMenu`.

## Decision

Do not install Shades of Iron yet.

Recommended sequence:

1. Merge the verified `codex/hoods` branch to `main`.
2. Download/review `AMM and SoI - Appearances Menu Mod and Shades of Iron (next gen updated)` if AMM integration is wanted.
3. Locate/download/review `Shades of Iron - W3EE Redux - Compatibility Patch (WIP)` before installing SoI into this W3EE Redux stack.
4. Create a new branch from updated `main`.
5. Install SoI and any required compatibility patch together.
6. Run Script Merger.
7. Expect manual script conflict work before launch.

Installing raw Shades of Iron without the W3EE Redux compatibility patch is likely to break the current W3EE inventory/actor systems.
