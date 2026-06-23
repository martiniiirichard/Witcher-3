# Assessment - Sort Everything / Minor Tweaks patch - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/5468`
- Downloaded archive: `C:\Users\marti\Downloads\UD-SE-Minor Tweaks-Extras-Patch - Next-Gen-5468-2-6d-1768319756.zip`
- Related downloaded archive: `C:\Users\marti\Downloads\Sort Everything - Next Gen-1710-1-44-1689965693.zip`

## Assessment

The downloaded `5468` file is not a simple standalone install. It appears to be a patched `modSortEverything` package with extra grouping/minor tweak behavior and a user config XML.

Archive contents include:

- `Mods\modSortEverything`
- `bin\config\r4game\user_config_matrix\pc\modSortEverything.xml`
- `inventoryMenu.ws`
- `glossary\glossaryEncyclopediaMenu.ws`
- `glossaryBestiaryMenu.ws`
- `journalQuestMenu.ws`
- `modseGroupItems.ws`
- `modSortInvItems.ws`

It contains:

- `6` `.ws` files
- `1` XML config file

## Current Stack Conflicts

The patch touches hot menu files already owned by important active mods:

- `inventoryMenu.ws`
  - `mod0_E3HUD_W3EER_NG`
  - `modShadesOfIron`
  - `modW3EE`
- `glossaryBestiaryMenu.ws`
  - `mod0_E3HUD_W3EER_NG`
  - `modBetterIcons2025_NextGen_W3EE`
  - `modW3EE`
  - Live Bestiary area was previously handled manually
- `journalQuestMenu.ws`
  - `modW3EE`
- `glossaryEncyclopediaMenu.ws`
  - `modW3EE`

The plain `Sort Everything - Next Gen` archive is also downloaded, but it additionally includes `alchemyMenu.ws` and `craftingMenu.ws`, which would collide with the recent Better Icons/W3EE/Unread Schematics compatibility work.

## Decision

Deferred.

Do not install this raw. It is useful, but the safe path is a manual compatibility patch based on the current highest-priority menu scripts, similar to the approach used for `modUnreadSchematicsAndRecipes`.

## Strongest Install Path Later

If we decide to add it:

1. Use the `5468` patched package rather than the plain Sort Everything archive.
2. Install/copy only after building compatibility versions of the hot menu scripts from the current active winners.
3. Preserve:
   - W3EE menu behavior
   - E3 HUD menu changes
   - Better Icons bestiary/menu changes
   - Shades of Iron inventory changes
   - Live Bestiary compatibility
   - Unread Schematics alchemy/crafting compatibility
4. Add `modSortEverything.xml` to the user config matrix.
5. Run Script Merger and launch compile test.
6. Smoke test inventory, journal, bestiary, glossary, shops, crafting, and alchemy.

## Notes

This is not redundant, but it is high-friction. It should be handled as a dedicated compatibility task, not as part of the quick browser-cleanup install pass.
