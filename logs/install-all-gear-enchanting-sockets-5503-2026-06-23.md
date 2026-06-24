# All Gear Enchanting Based On Sockets 5503

Date: 2026-06-23

## Installed

- Archive: `All Gear Enchanting Based On Sockets-5503-1-2-1743865146.zip`
- Mod folder: `modAllGearEnchantingBasedOnSockets`

## Skipped

- `modAllGearEnchantingBasedOnSockets_FStashPatch-5503-1-2-1741449758.zip`

Reason: this optional patch is for Friendly Stash. Friendly Stash is not installed in the current stack.

## Load Order

Added to both active `mods.settings` files:

- `modAllGearEnchantingBasedOnSockets` priority `225`

## Manual Script Merge

The mod ships a full copy of:

```text
content\scripts\game\gui\menus\enchantingMenu.ws
```

The current stack already has active `enchantingMenu.ws` owners from W3EE and Better Icons W3EE. To avoid replacing W3EE-specific enchantment logic, the mod's full script file was disabled:

```text
mods\modAllGearEnchantingBasedOnSockets\content\scripts\game\gui\menus\enchantingMenu.ws.disabled-by-codex
```

The socket-based `canApply` recalculation from this mod was manually merged into:

```text
mods\modBetterIcons2025_NextGen_W3EE\content\scripts\game\gui\menus\enchantingMenu.ws
```

Specifically, `OnSelectItem(...)` now recalculates runeword/glyphword applicability against the selected item's enhancement slot count and ingredient availability, while preserving W3EE's previous-tier runeword requirement in `OnSelectEnchantment(...)`.

## Backup

Created rollback backup:

```text
C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\AllGearEnchantingSockets_5503_20260623_234601
```

## Verification

- DX12 launch smoke passed: game stayed running for 45 seconds.

## Risk

This is compile-clean, but the actual behavior should eventually be tested at the runewright/enchanting menu with armor and weapons that have different socket counts. The merge intentionally preserves W3EE enchantment progression rules.
