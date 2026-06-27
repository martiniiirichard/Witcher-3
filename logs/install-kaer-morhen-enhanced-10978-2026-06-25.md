# Install: Kaer Morhen Enhanced 10978

Date: 2026-06-25

Source:

- Nexus: https://www.nexusmods.com/witcher3/mods/10978
- Archive: `C:\Users\marti\Downloads\Kaer Morhen Enhanced-10978-1-6-1-1776375310.zip`

## Mod summary

Kaer Morhen Enhanced adds Corvo Bianco-style utility interactions to Kaer Morhen:

- bookshelves / library buff
- alchemy tables / alchemy buff
- mutagen dismantling tables
- armor and sword stands
- bed in Geralt's room
- fast travel point

The Nexus description identifies it as Next-Gen compatible and made with REDkit.

## Install contents

Installed:

- `mods\mod_KaerMorhenEnhanced`
- `dlc\dlcKaerMorhenEnhanced`

The mod includes one script:

- `mods\mod_KaerMorhenEnhanced\content\scripts\local\KaerMorhenEnhanced.ws`

Script surface:

- `class W3QuestCond_IsGearsRewardsEnabled extends CQuestScriptedCondition`
- `quest function BookshelvesBooks`
- `quest function KME_DecreaseFactQuest`
- wraps `W3Effect_BookshelfBuff.OnEffectAdded`
- wraps `Unconscious.OnEnterState`

Pre-install scan found no duplicate symbol names and no duplicate relative script-file path with active mods. Wrapped targets exist in the active/base script stack.

## Settings

Added/enabled in both `mods.settings` files:

```ini
[mod_KaerMorhenEnhanced]
Enabled=1
Priority=260
```

Active physical mod folder count after install: `197`.

## Verification

DX12 launch smoke test passed.

Observed sequence:

- brief visible script/compiler-style window around `12s-18s`
- main `The Witcher 3` window visible at about `24s`

No compile error was reported.

