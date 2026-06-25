# Fix Stuck Quest Items 7173

Source: https://www.nexusmods.com/witcher3/mods/7173

Installed archive:
- `C:\Users\marti\Downloads\Fix Stuck Quest Items-7173-2-0-0-1762796162.zip`

Installed files:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modFixStuckQuestItems`

Settings:
- `[modFixStuckQuestItems]`
- `Enabled=1`
- `Priority=250`

Notes:
- Version `2.0.0` is an annotation-based build. Nexus description states this version is merge-free and intended to be broadly compatible.
- Archive contains a single local annotation script: `FixStuckQuestItems_anno.ws`.
- Behavior: fixes quest items that remain stuck in the quest inventory tab by removing the quest tag when appropriate. The script runs from `CR4InventoryMenu.OnConfigUI()` when opening the player inventory.

Verification:
- DX12 smoke test passed: game stayed running after 45 seconds.
- No Script Merger pass required.

Risk:
- Low compile risk because it wraps an inventory menu method and does not replace base scripts.
- Functional behavior is retroactive inventory cleanup, so verify in-game later by opening inventory on an existing save with stuck quest items.
