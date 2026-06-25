# Witcher Lore Collection - 7236

Date: 2026-06-24

Source:
- https://www.nexusmods.com/witcher3/mods/7236

Installed archive:
- `C:\Users\marti\Downloads\Witcher Lore Collection-7236-2-0-1-1764408820.zip`

Installed paths:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modWitcherLoreCollection`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\DLC\dlcWitcherLoreCollection`

Settings:
- Added `[modWitcherLoreCollection]` with `Enabled=1`, `Priority=255` to both active `mods.settings` files.

Notes:
- Nexus description/posts say WLC 2.0+ is Next-Gen, REDkit rebuilt, merge-free, and can be used with Brothers in Arms Next-Gen. It restores cut books/documents, glossary content, and missing bestiary entries.
- Initial launch produced:
  - `Property 'SORT_WEIGHT_01' already exists in class 'CR4GlossaryBooksMenu'`
- Cause:
  - `modBrothersInArms\content\scripts\local\anno\bia_glossaryBooksMenu_anno.ws` already adds `SORT_WEIGHT_01`.
  - WLC's `wlc_glossaryBooksMenu_anno.ws` added the same field.
- Fix:
  - Backed up WLC annotation file.
  - Removed only the duplicate WLC `@addField( CR4GlossaryBooksMenu ) private var SORT_WEIGHT_01 : int;` line.
  - Left WLC's assignment/use of `SORT_WEIGHT_01` intact so it reuses the field already added by BiA.

Verification:
- DX12 launch smoke passed: game remained running after 60 seconds.

Residual risk:
- Best experience requires a new game for every placed/restored document, but existing saves should still work and may get some retroactive entries.
- Rare bundled non-text conflicts should favor the existing overhaul/BiA stack; worst case is losing a specific restored document, not breaking scripts.
