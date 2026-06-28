# Assess - Potions Tab Expanded and Unreasonable Plot Redesigned

Date: 2026-06-28

## Potions Tab Expanded `7007`

Archives inspected:

- `C:\Users\marti\Downloads\Potions Tab Expanded-7007-1-01-1674937735.7z`
- `C:\Users\marti\Downloads\Potions Tab Expanded Adaptations-7007-1-02-1675252766.7z`

Payload:

- Main mod: `modPotionsTabExpanded`
- Content-only bundle, no scripts.
- Unpacked `blob0.bundle` contains only:
  - `gameplay\gui_new\swf\inventory\panel_inventory.redswf`

Current conflict lane:

- `modE3HUD`
- `mod0_E3HUD_W3EER_NG`
- `mod__hoods`
- `modW3EE`

Decision:

- Deferred.
- Although it has no scripts, it replaces the same inventory SWF already owned by the current E3/W3EE/Hoods UI stack. Installing it raw would be a silent UI override, not a safe additive mod.

## Unreasonable Plot Redesigned `10014`

Archive inspected:

- `C:\Users\marti\Downloads\mod00UnreasonablePlotRedesigned-10014-2-0b-1770434739.zip`

Payload:

- `content\scripts\game\gui\inventoryContext.ws`
- `content\scripts\game\quests\quest_function.ws`
- `content\scripts\game\quests\functions\tutorial.ws`
- `content\scripts\local\UnreasonablePlotRedesigned.ws`
- 17 language `.w3strings` files plus CSV sources.
- `blob0.bundle` with quest/scene/world edits, including Baron, Ciri, Skellige berserkers, Radovid assassination wrap-up, Gwent card meta, and HoS finale files.

Current conflict lane:

- `inventoryContext.ws` already exists in `modexpansionzero` and `modW3EE`.
- `quest_function.ws` already exists in `mod0000_MergedFiles`, `mod00FlorenEconomySystem_W3EE_REDUX`, `mod00ReputationSystem_W3EE_REDUX`, and `modW3EE`.
- `tutorial.ws` already exists in `modW3EE`.

Decision:

- Deferred as a dedicated compatibility project.
- This is not a quick content add. Raw installation would introduce broad script and quest-content ownership changes across current W3EE/economy/reputation hot paths.

## Outcome

- No game files changed for either candidate.
- No Script Merger action required.
- Keep both out of the active stack unless we intentionally schedule a UI compatibility pass (`7007`) or a quest/restoration compatibility pass (`10014`).
