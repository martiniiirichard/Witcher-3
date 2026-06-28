# Audit: E3 HUD Stack Ownership

Date: 2026-06-28

## Goal

Verify whether the active E3 HUD folders are redundant with each other or whether they form an intentional layered UI stack.

## Active Folders

| Folder | File shape | Role |
| --- | --- | --- |
| `modE3HUD` | 1 bundle, 1 texture cache, 7 string files, no scripts. | Base E3 HUD asset/string/cache layer. |
| `mod0_E3HUD_W3EER_NG` | 15 scripts, 1 bundle, 1 metadata store. | W3EE Redux / E3 HUD compatibility layer. Owns current HUD/menu scripts and many W3EE-sensitive SWFs. |
| `modE3HUDColorLoad` | 1 bundle, 1 metadata store, no scripts. | Optional colored loading-screen override. |

## Bundle Index Evidence

`mod0_E3HUD_W3EER_NG` wins 18 indexed UI assets at priority `10`, including:

- `gameplay\gui_new\guirsrc\r4default.guiconfig`
- core alchemy, character, common, crafting, deathscreen, inventory, journal, meditation, worldmap SWFs
- core HUD SWFs such as `hud.redswf`, `hud_buffs.redswf`, `hud_radialmenu.redswf`, and `hud_wolfstatbars.redswf`

`modE3HUD` contributes 61 indexed assets at priority `12`, including:

- E3 menu resources
- glossary, HUD, loading, and other UI SWFs not all replaced by the W3EE compatibility layer
- localized strings and texture cache

`modE3HUDColorLoad` contributes 10 indexed loading-screen SWFs at priority `11`, winning them over base `modE3HUD`.

## Script Evidence

Only `mod0_E3HUD_W3EER_NG` contains scripts:

- HUD modules:
  - `hudModuleEnemyFocus.ws`
  - `hudModuleInteractions.ws`
  - `hudModuleMinimap2.ws`
  - `hudModuleRadialMenu.ws`
  - `hudModuleWolfHead.ws`
- Menus:
  - `commonMenu.ws`
  - `glossaryBestiaryMenu.ws`
  - `inventoryMenu.ws`
  - `mapMenu.ws`
  - `meditationClockMenu.ws`
- Inventory components:
  - `guiBaseInventoryComponent.ws`
  - `guiContainerInventoryComponent.ws`
  - `guiPlayerInventoryComponent.ws`
- Local helpers:
  - `e3hudAnnotations.ws`
  - `menuConfig.ws`

## Decision

Keep `modE3HUD` and `mod0_E3HUD_W3EER_NG` as a pair.

They are not duplicate folders:

- `modE3HUD` supplies the base UI asset/string/cache layer.
- `mod0_E3HUD_W3EER_NG` supplies the W3EE-compatible script and panel layer.

Keep `modE3HUDColorLoad` unless the colored loading-screen look is unwanted or active mod count pressure becomes severe. It is a low-risk cosmetic override, not a script concern.

## Practical Rule

When a smaller UI mod loses a SWF to this stack, that is usually intentional. E3 HUD is the selected UI owner for this build, while W3EE remains the selected gameplay owner.
