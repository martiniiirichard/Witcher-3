# Time of the Sword and Axe 8258 Install

Date: 2026-06-24

## Mod

Nexus: `https://www.nexusmods.com/witcher3/mods/8258`

Installed archive:

- `C:\Users\marti\Downloads\Time of the Sword and Axe-8258-0-4b-1700804814.7z`

Manual reviewed:

- `C:\Users\marti\Downloads\Time of the Sword and Axe - PDF Manual-8258-0-4-1704416398.zip`

## Installed Files

- `mods\modexpansionzero`
- `mods\modSharedImports` replaced with the version shipped by 8258
- `DLC\dlcexpansionzero`
- `bin\config\r4game\user_config_matrix\pc\expansionzero.xml`

Added to both filelists:

- `bin\config\r4game\user_config_matrix\pc\dx11filelist.txt`
- `bin\config\r4game\user_config_matrix\pc\dx12filelist.txt`

Entry added:

```ini
[modexpansionzero]
Enabled=1
Priority=228
```

The low priority is intentional for the first pass so Gwent Redux, W3EE Redux, Better Icons, E3 HUD, Nobs Reflex, and existing merged files keep precedence unless we explicitly merge.

## Backup

Created install backup under:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\TimeOfSwordAndAxe_8258_20260624_003528`

Note: the backup command hit long-path copy errors while backing up two nested `modSharedImports` files, but the install copy completed and the current build still compiles.

## Gwent Rule

Per the manual, the Gwent card XML should not be merged with Gwent overhaul mods.

For this build:

- Gwent Redux should win.
- Sword and Axe quests may still work.
- special Gwent card rewards from Sword and Axe may be missing.

## Script Conflict Inventory

Static scan found 34 overlapping script files out of 91 shipped by `modexpansionzero`.

Major owners involved:

- `mod0000_MergedFiles`
- `modW3EE`
- `modGwentRedux`
- `modBrothersInArms`
- `modNobsReflex`
- `mod0_E3HUD_W3EER_NG`
- `modBetterIcons2025_NextGen_W3EE`
- `modExtraSkillSlotsNextGen`
- `modShadesOfIron`
- `modAMM`
- `modFriendlyMeditation`
- `modIcyOcean`
- `modUnreadSchematicsAndRecipes`
- `mod__hoods`

High-risk overlaps include:

- `game\player\playerWitcher.ws`
- `game\player\r4Player.ws`
- `game\components\inventoryComponent.ws`
- `game\gameplay\ability\PlayerAbilityManager.ws`
- `game\gameplay\effects\effectTypes.ws`
- `game\gameplay\effects\gameEffectManager.ws`
- `game\gui\menus\gwintManager.ws`
- `game\gui\menus\inventoryMenu.ws`
- `game\gui\hud\modules\hudModuleRadialMenu.ws`

## Verification

Smoke compile passed after install:

`SmokePassed_StillRunningAfter45s`

## Next Step

Script Merger was launched to inspect conflicts.

Do not assume all Sword and Axe script features are active yet. The install is launch-safe, but many features may be shadowed until the relevant scripts are merged or selectively ported.
