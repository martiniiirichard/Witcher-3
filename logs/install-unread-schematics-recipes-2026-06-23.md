# Install - Unread Schematics and Recipes - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/10419`
- Archive: `C:\Users\marti\Downloads\Unread Schematics and Recipes - Next-Gen-10419-1-3-1764868968.7z`

## Assessment

The downloaded mod includes full replacements for:

- `game\gui\menus\alchemyMenu.ws`
- `game\gui\menus\craftingMenu.ws`

Those files are already overridden by W3EE Redux / W3EE and Better Icons. Installing the archive as-is would risk replacing W3EE/Better Icons menu logic with a less compatible full-file override.

## Install Approach

Installed a compatibility version of `modUnreadSchematicsAndRecipes`:

- Used the current `modBetterIcons2025_NextGen_W3EE` versions of `alchemyMenu.ws` and `craftingMenu.ws` as the base.
- Added the unread-marker hooks from mod `10419`:
  - `IsUnreadSchematicOrRecipe(...)` for `isNew` in alchemy and crafting lists.
  - `RemoveUnreadSchematicOrRecipe(...)` when viewing an alchemy recipe or crafting schematic.
- Kept the original local wrapper script:
  - `local\UnreadSchematicsAndRecipes.ws`

## Installed

- `modUnreadSchematicsAndRecipes`

`mods.settings` backup:

- `C:\Games\The Witcher 3\mods.settings.codex-backup-unread-schematics-20260623-144453`

Priority:

- `modUnreadSchematicsAndRecipes`: `155`

## Verification

Static verification:

- Installed folder exists.
- Contains `3` `.ws` files.
- Contains `0` `.xml` menu files.
- Hot-file owners for `alchemyMenu.ws` and `craftingMenu.ws` are now:
  - `modW3EE`
  - `modBetterIcons2025_NextGen_W3EE`
  - `modUnreadSchematicsAndRecipes`
- `modUnreadSchematicsAndRecipes` has the highest priority of those owners and contains the Better Icons/W3EE base scripts plus unread-marker hooks.

## Pending

Needs a game launch compile test. If it fails, likely areas to inspect:

- `@wrapMethod(W3PlayerWitcher)` signatures in `UnreadSchematicsAndRecipes.ws`.
- Any Script Merger output for `alchemyMenu.ws` or `craftingMenu.ws`.
- Menu behavior in alchemy/crafting after opening newly learned recipes or schematics.
