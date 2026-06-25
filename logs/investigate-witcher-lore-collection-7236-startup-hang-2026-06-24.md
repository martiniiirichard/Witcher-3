# Witcher Lore Collection Startup Hang Investigation - 2026-06-24

## Mod

- Nexus: `7236`
- Active folder: `modWitcherLoreCollection`
- Local version: `2.0.0`
- Local `info.json` says the mod was cooked successfully and targets game version `27`.

## Original Failure

With the full mod active, the game entered the known startup headless-hang state:

- `witcher3.exe` alive
- `MainWindowHandle = 0`
- no visible `The Witcher 3` window
- memory parked around 4.1 GB

## Findings

The mod is not just scripts and strings. It contains:

- 17 `.w3strings` files
- 4 `.ws` scripts
- `metadata.store`
- `blob0.bundle`

The scripts touch high-conflict systems:

- `CR4GlossaryBooksMenu.PopulateListData`
- `CInventoryComponent.UpdateInitialReadState`
- `CInventoryComponent.AddBestiaryFromBook`
- `CNewNPC.AddBestiaryKnowledge`
- `CNewNPC.AddBestiaryKnowledgeEP2`
- console helpers `addwlc()` and `addglossary()`

However, disabling all WLC scripts did **not** fix the startup hang.

## Bundle Isolation

Disabling only `content\blob0.bundle` fixed the startup hang.

Current safe reduced state:

- WLC folder is active.
- WLC scripts are active.
- WLC strings are active.
- `content\blob0.bundle` is renamed to:
  `blob0.bundle.disabled-by-codex-internal-test`

Strict launch test passed in this reduced state:

- visible `The Witcher 3` window
- responding
- `1920x1080`
- stable through 90 seconds
- healthy memory path around 5.9 GB

## Bundle Contents

The disabled bundle contains 54 cooked assets, including:

- `.w2l` level/loot/noticeboard layers
- `.w2ent` quest/NPC/container entities
- `.w2phase` quest/living-world phases
- B&W and HoS level/quest files
- base-game Novigrad, Skellige, Kaer Morhen, Prologue, and quest assets

Notable high-risk assets include:

- `quests\part_2\q308_psycho.w2phase`
- `quests\part_2\quest_files\q206_berserkers\phases\q206_cerys_path.w2phase`
- `quests\secondary_npcs\nathanel_priest.w2ent`
- `quests\sidequests\no_mans_land\quest_files\sq106_killbill\characters\sq106_hammond.w2ent`
- multiple B&W and HoS `.w2l` quest/level overrides

## Interpretation

The headless launch is caused by the cooked REDkit bundle, not the scripts. The likely failure mode is a cooked asset/load-order/runtime incompatibility with the current large mod stack, not a WitcherScript compile issue.

The reduced install preserves strings and script-side glossary/bestiary/console behavior but likely loses the 2.0.0 REDkit feature where restored books/documents are placed into lore-friendly world locations.

## Decision

Keep WLC in reduced mode unless we decide to spend time repacking or asset-splitting the bundle. The safe reduced mode is currently launch-verified.
