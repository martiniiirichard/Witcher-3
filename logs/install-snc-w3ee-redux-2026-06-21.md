# Install Log - SNC W3EE Redux - 2026-06-21

## Mod

- Nexus: https://www.nexusmods.com/witcher3/mods/12218
- Name: `(SNC) Standarised Naming Convention for W3EE Redux`
- Version: `1.0`
- Archive: `C:\Users\marti\Downloads\Standarised Naming Convention - W3EE Redux-12218-1-0-1778788363.zip`

## Instructions Read

The mod page says it applies Faen's Standardised Naming Convention to W3EE Redux and can be installed manually by extracting the file and placing it in the main game directory.

Requirement listed:

- `W3EE Redux`

Recommended, not required:

- SNC Witcher Gear
- SNC Potions
- SNC Oils
- SNC Bombs
- SNC Mutagens
- SNC Runestones & Glyphs
- Grammar on the Path
- Names from the Path

## Archive Structure

The archive contained a nested root folder:

```text
Standarised Naming Convention - W3EE Redux/mods/mod_SNC_W3EERedux
```

It contains localization/string files only:

- `.w3strings`
- `localization/en.csv`

No scripts were present, so Script Merger should not be required for this mod.

## Backup

Created before install:

```text
C:\Users\marti\OneDrive\Documents\New project\Witcher-3\backups\pre-snc-w3ee-redux-20260620-234942
```

## Installed

Installed to:

```text
C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\mod_SNC_W3EERedux
```

## Load Order

Placed above Redux so its naming strings override W3EE Redux strings:

```ini
[mod_SNC_W3EERedux]
Enabled=1
Priority=1

[modSharedImports]
Enabled=1
Priority=2

[modReduxW3EE]
Enabled=1
Priority=3

[modW3EE]
Enabled=1
Priority=4

[modW3EELocalization1]
Enabled=1
Priority=5

[modW3EELocalization2]
Enabled=1
Priority=6

[modW3EELocalization3]
Enabled=1
Priority=7

[modW3EELocalization4]
Enabled=1
Priority=8
```

## Verification

- `mod_SNC_W3EERedux` folder exists.
- Expected `.w3strings` files exist.
- `localization/en.csv` exists.
- Active `mods.settings` updated.

## Next Validation

Launch the game and confirm:

- No startup/script errors.
- Inventory/crafting item names use the standardized naming pattern.
