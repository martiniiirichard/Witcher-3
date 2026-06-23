# No Journal Sounds 1424 Manual Merge

Source: https://www.nexusmods.com/witcher3/mods/1424

## Files

- Download: `C:\Users\marti\Downloads\No Journal Sounds-1424-1-31-0-1.zip`
- Extracted for inspection only: `C:\Users\marti\AppData\Local\Temp\codex-journal-sounds-1424`
- Backup: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\no-journal-sounds-1424-20260623-180128`

## Decision

Did not install the shipped `modNoJournalSounds` folder.

Reason: the archive is a Witcher 3 1.31-era script mod that ships full replacements for:

- `content\scripts\game\components\inventoryComponent.ws`
- `content\scripts\game\gui\hud\modules\hudModuleJournalUpdate.ws`

Those files are heavily modified in the current Next Gen W3EE/E3 HUD/Better Icons stack. Installing the old full scripts would be high risk.

Instead, manually ported only the intended sound-event changes.

## Manual Changes

Patched active merged inventory script:

- `Mods\mod0000_MergedFiles\content\scripts\game\components\inventoryComponent.ws`
- Muted the bestiary/new journal sound by changing `theSound.SoundEvent("gui_ingame_new_journal")` to an empty sound event.

Patched HUD notification script:

- `Mods\modBetterIcons2025_NextGen_W3EE\content\scripts\game\gui\hud\modules\hudModuleJournalUpdate.ws`
- Mirrored the same change into `Mods\modW3EE\content\scripts\game\gui\hud\modules\hudModuleJournalUpdate.ws` so future merge passes do not accidentally reintroduce the sounds.

Muted journal/HUD sound events:

- `gui_ingame_quest_active`
- `gui_ingame_new_journal`
- `gui_ingame_quest_success`
- `gui_ingame_quest_fail`
- `gui_ingame_level_up`
- `gui_ingame_new_mappin`
- `gui_ingame_new_reward_item`

## Verification

- Confirmed all target sound events are now empty-string assignments in the active patched files.
- DX12 compile smoke passed.
- The game process stayed running after 45 seconds and was then stopped manually by Codex.

## Risk

This should be low-risk because it changes only sound event string assignments. The main functional risk is subjective: journal, quest, level-up, map pin, and reward notifications may now feel too quiet.
