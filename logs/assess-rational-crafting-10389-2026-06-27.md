# Assess - Rational Crafting 10389

Date: 2026-06-27

Source archive:

- `C:\Users\marti\Downloads\Rational Crafting-10389-1-1-1-1761991819.zip`

Nexus:

- https://www.nexusmods.com/witcher3/mods/10389

## Payload

Extracted for inspection only:

- `mods\modRationalCrafting\content\blob0.bundle`
- localization strings
- `mods\modRationalCrafting\content\scripts\game\gui\menus\craftingMenu.ws`
- `mods\modRationalCrafting\content\scripts\local\modRationalCrafting.ws`

The local script adds one helper:

- `modRCSetCategory(craftedItemName, l_GroupTag)`

The helper categorizes runes/glyphs by tags before falling back to the normal item category key.

## Conflict Read

The risky file is:

- `game\gui\menus\craftingMenu.ws`

Current active stack already has this path in:

- `modW3EE`
- `modBetterIcons2025_NextGen_W3EE`
- `modUnreadSchematicsAndRecipes`
- `modexpansionzero`

The Rational Crafting file is a full menu override, not a narrow `wrap`/`add` script. Size comparison:

- W3EE: `151846` bytes
- Better Icons W3EE: `71460` bytes
- Unread Schematics and Recipes: `71686` bytes
- Expansion Zero: `49456` bytes
- Rational Crafting candidate: `48792` bytes

That shape suggests an older or alternate full-file base. Installing it directly would probably either lose the feature to current higher-priority owners or break/undo W3EE/E3 HUD/crafting-menu compatibility.

## Decision

Do not install now.

Reason: the value is modest compared with the merge risk. It would require a deliberate manual graft into the current active crafting menu, and the target file is already a known hot zone for Better Icons, Unread Schematics, Expansion Zero, and W3EE Redux.

## Revisit Only If

- The current crafting UI is confusing enough that rationalized categories are worth manual merge time.
- We decide to drop one of the current crafting-menu owners.
- A W3EE/E3/Better Icons compatible patch appears.
