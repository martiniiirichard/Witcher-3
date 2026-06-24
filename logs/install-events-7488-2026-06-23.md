# Events 7488

Date: 2026-06-23

## Installed

- Archive: `Events-7488-2-0-1-1764411098.zip`
- Mod folder: `modEvents`
- DLC folder: `dlcEvents`
- Menu XML: `bin\config\r4game\user_config_matrix\pc\Events.xml`

## Load Order

Added to both active `mods.settings` files:

- `modEvents` priority `223`

## Menu Filelists

Added the required XML entry to both game config filelists:

- `dx11filelist.txt`
- `dx12filelist.txt`

Entry:

```text
Events.xml;
```

## Compatibility Notes

- The archive includes `mod_sharedutils_menudescriptors`, but the installed copy was byte-for-byte identical, so no separate dependency action was needed.
- Brothers in Arms already defines and registers `EVENTS_MenuDescriptor` in `bia_modDescriptions.ws`.
- The standalone Events descriptor caused:

```text
Error [modevents]local\events_moddescriptions.ws(1): Class 'EVENTS_MenuDescriptor' already defined.
```

Fix applied:

```text
mods\modEvents\content\scripts\local\events_modDescriptions.ws.disabled-by-codex
```

This preserves the active Events scripts for menu settings and journal categorization while avoiding the duplicate descriptor already supplied by Brothers in Arms.

## Backup

Created rollback backup:

```text
C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\Events_7488_20260623_233533
```

## Verification

- First launch exposed the duplicate `EVENTS_MenuDescriptor` error.
- After disabling the duplicate descriptor file, DX12 launch smoke passed: game stayed running for 45 seconds.

## Risk

Events writes event/quest state through facts from the mod menu. The Nexus page warns against updating an existing Events/BIA-embedded Events setup mid-playthrough. Current install compiles, but in-world behavior should be tested before relying on affected quest state.
