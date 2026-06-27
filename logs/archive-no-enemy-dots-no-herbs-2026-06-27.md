# Archive: No Enemy Dots And No Herbs

Date: 2026-06-27

Archived folder:

- From: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modNoEnemyDotsAndNoHerbs`
- To: `archived-mods/redundant-shadowed-no-enemy-dots-no-herbs-20260627-130748/modNoEnemyDotsAndNoHerbs`

Configuration:

- `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`
- Changed `[modNoEnemyDotsAndNoHerbs]` from `Enabled=1` to `Enabled=0`.
- Kept priority `204`.
- Before/after copies are stored in the archive folder.

Evidence:

- The mod contains one bundled asset:
  - `gameplay/gui_new/swf/hud/hud_minimap2.redswf`
- No active scripts, DLC folder, menu XML, or input bindings were present.
- `modE3HUD` owns the same SWF earlier in load order at priority `12`.
- `modNoEnemyDotsAndNoHerbs` was priority `204`, so its HUD SWF was not active in the current E3 HUD stack.

Hash/size check:

| Mod | Bytes | SHA256 prefix |
| --- | ---: | --- |
| `modNoEnemyDotsAndNoHerbs` | 569319 | `92309D1B8F46A274` |
| `modE3HUD` | 890073 | `740575C56C6954D2` |

Conclusion:

This was a losing HUD override. Because the current UI preference is E3 HUD, keeping the folder enabled added active mod count without changing the visible minimap/HUD behavior.

