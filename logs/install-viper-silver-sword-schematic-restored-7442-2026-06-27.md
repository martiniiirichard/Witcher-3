# Install - Viper Venomous Silver Sword Schematic Restored 7442

Date: 2026-06-27

Source:

- Nexus: https://www.nexusmods.com/witcher3/mods/7442
- Archive: `C:\Users\marti\Downloads\Version C-7442-1-0-1672156393.rar`

## Decision

Installed.

Reason: small content-only restoration mod with no script files and no exact active indexed owner for its three bundled paths.

## Installed Folder

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modVVSSDiagramRestoredVerCNextGen`

## Load Order

Added to active `mods.settings` files:

```ini
[modVVSSDiagramRestoredVerCNextGen]
Enabled=1
Priority=265
```

## Payload

QuickBMS unpacked three bundled files:

- `dlc\ep1\data\gameplay\container_definitions\autogen\ep1_viper_silver_sword_schematic_chest.w2ent`
- `dlc\ep1\data\gameplay\items_plus\def_loot_containers.xml`
- `dlc\ep1\levels\novigrad\ep1\living_world\poi\ep1_poi_26\loot.w2l`

The loot XML adds/restores Viper steel/silver sword and schematic loot records, including:

- `custom_ep1_viper_silver_sword_schematic`
- `EP1 Viper School silver sword schematic`

## Conflict Check

No exact active indexed owners were found for the three bundled paths in `tools/tmp/bundle-conflict-index-20260625/enabled-bundle-assets.csv`.

No active live Mod folder file matched those paths during direct scan.

## Backup

- `backups\viper-schematic-7442-install-20260627-140950\mods.settings.before`

## Verification

DX12 direct-launch smoke after install:

- `witcher3.exe` running after 65 seconds
- visible window: `True`
- responding: `True`
- working set: about `1637.2 MB`

No Script Merger action was needed because there are no `.ws` scripts.
