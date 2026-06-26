# Install - WaterwheelFIXED

Date: 2026-06-26

## Source

- Nexus ID: `9206`
- Archive: `C:\Users\marti\Downloads\WaterwheelFIXED-9206-1-1-1718019750.7z`

## Assessment

This is a very small Blood and Wine content fix.

Archive payload:

- `modwaterwheel2\content\blob0.bundle`
- `modwaterwheel2\content\metadata.store`
- `modwaterwheel2\content\texture.cache`
- `modwaterwheel2\content\info.json`

Bundle unpack found exactly one game file:

- `dlc\bob\data\levels\bob\quests\main_quests\q702_hunt\entities\q702_mill.w2l`

Risk profile:

- Script files: `0`
- Menu/XML files: `0`
- DLC folders: `0`
- Narrow world layer change for the q702 mill/waterwheel area.

## Installed

`mods.settings` already had a stale disabled entry and no physical mod folder was present.

Installed:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modwaterwheel2`

Load order:

```ini
[modwaterwheel2]
Enabled=1
Priority=242
```

Backup:

- `backups\waterwheelfixed-9206-20260626-*\mods.settings.before`

## Verification

- Script Merger not required: no scripts.
- DX12 launch smoke passed. `witcher3.exe` stayed alive after 55 seconds.

## Residual Risk

Launch proves the bundle loads. Visual/in-world proof requires checking the q702 mill/waterwheel location in Toussaint.
