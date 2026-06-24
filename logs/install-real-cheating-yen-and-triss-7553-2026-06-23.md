# Real Cheating Yen and Triss 7553

Date: 2026-06-23

## Installed

- Archive: `RealCheatingYenAndTriss - Next-Gen ONLY-7553-2-1-1746902002.zip`
- Mod folder: `modRealCheatingYenAndTriss`
- Menu XML: `bin\config\r4game\user_config_matrix\pc\modRealCheatingYenAndTriss.xml`

## Load Order

Added to both active `mods.settings` files:

- `modRealCheatingYenAndTriss` priority `222`

## Menu Filelists

Added the required XML entry to both game config filelists:

- `dx11filelist.txt`
- `dx12filelist.txt`

Entry:

```text
modRealCheatingYenAndTriss.xml;
```

## Script Notes

- Contains one local script: `manage_cheatingyenandtrissfact.ws`
- Uses `@wrapMethod( CR4Game ) OnGiveReward`
- Uses `@wrapMethod( CR4HudModuleJournalUpdate ) OnTick`
- No Script Merger conflict was required during install.

## Backup

Created rollback backup:

```text
C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\RealCheatingYenAndTriss_7553_20260623_233107
```

## Verification

- DX12 launch smoke passed: game stayed running for 45 seconds.
