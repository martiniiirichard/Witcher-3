# Geralt The Master Cook 4809

Date: 2026-06-24

## Installed

- Installed DLC payload only:
  - `DLC/dlcgeralt_the_master_cook`
- Source archive:
  - `C:/Users/marti/Downloads/Geralt The Master Cook-4809-2-1-4-1598353459.7z`

## Deliberately skipped

- Did not install `Mods/modgeralt_the_master_cook`.

Reason: the mod page says the script/mod portion is not needed when another mod, such as W3EE Lazarus or Ghost Mode, already adds a food/drink alchemy tab. This stack already has W3EE ownership of `alchemyManager.ws` and `alchemyTypes.ws`, with `"edibles"` mapped to the W3EE `EACIT_Edible` enum. Installing the script portion would compete with W3EE/BCR alchemy ownership and likely create avoidable script conflicts.

## Script inspection

`modgeralt_the_master_cook` contains two scripts:

- `game/gameplay/alchemy/alchemyManager.ws`
- `game/gameplay/alchemy/alchemyTypes.ws`

Those scripts add an `EACIT_Edibles` enum path and cooked-item quantity behavior. W3EE already parses `cookedItemQuantity` and maps the `edibles` recipe type, so the DLC data can be loaded without replacing W3EE alchemy scripts.

## Verification

- Launch smoke test: passed.
- Result: game stayed running after 45 seconds.

## Residual risk

- In-game recipe availability still needs a content check at the relevant merchants/books.
- If a specific recipe appears but crafts the wrong quantity, revisit a targeted W3EE-compatible quantity hook rather than installing the full `Mods` script folder.
