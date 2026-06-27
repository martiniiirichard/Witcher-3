# Install - Enhanced Herbalism 7269

Date: 2026-06-25

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/7269`
- Archive: `C:\Users\marti\Downloads\Enhanced Herbalism-7269-2-0-0-1762800663.zip`

## Page / Package Notes

Current version is DLC-based and advertises broad compatibility because it no longer edits vanilla files.

Archive contents:

- `dlc/dlcEnhancedHerbalism/content/blob0.bundle`
- `dlc/dlcEnhancedHerbalism/content/metadata.store`

No `.ws` scripts, no `mods.settings` entry, and no Script Merger work needed.

Package strings indicate it adds herb loot XML definitions:

- `dlc\dlcenhancedherbalism\data\gameplay\items\def_loot_herbs.xml`
- `dlc\dlcenhancedherbalism\data\gameplay\items_plus\def_loot_herbs.xml`
- `dlc\dlcenhancedherbalism\dlcenhancedherbalism.reddlc`

## Install

Installed:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\dlc\dlcEnhancedHerbalism`

Backup folder:

- `backups/enhanced-herbalism-7269-20260625`

No previous install was present.

## Verification

DX12 launch smoke test passed:

- launched through `tools/direct-launchers/Witcher3DirectDX12.exe`
- after 60 seconds `witcher3.exe` had a visible `The Witcher 3` window
- process responding, working set ~1.69 GB

## Remaining Test

In-game harvest behavior still needs practical validation:

- pick a few herb nodes
- confirm the modded quantity/loot behavior appears
- confirm no conflict with W3EE's alchemy/herb economy expectations
