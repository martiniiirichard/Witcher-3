# Install/Test - Kaer Morhen Extended Edition 11934 as World Base

Date: 2026-06-25

## Goal

Maximize Kaer Morhen content without breaking the map.

## Decision

Use Kaer Morhen Extended Edition 11934 as the active Kaer Morhen world-content base and keep Kaer Morhen Enhanced 10978 as the functional overlay.

Do not stack Extended 11934 and Splendor 9563 at the same time. They overlap heavily on core world/collision/occlusion/terrain/castle layers. Load order would likely choose one world graph over the other rather than truly combining both.

## Active Configuration

Updated:

- `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`

Configured:

```ini
[mod_KaerMorhenEnhanced]
Enabled=1
Priority=260

[modkaermorhenrestoredtoitsancientsplendor]
Enabled=0
Priority=259

[modkaer_morhen_extended]
Enabled=1
Priority=259
```

Installed:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modkaer_morhen_extended`

Backup:

- `backups/kaer-morhen-extended-11934-base-test-20260625/mods.settings.before`

## Why This Line

Extended has the larger unique content footprint:

- basement/crypt-style assets
- Kikimore/mine assets
- `levels\kaer_morhen\kaer_morhen_valley\mine2\mine_out.w2l`
- `levels\kaer_morhen\merged_geometry.w2l`
- extra occlusion/terrain/source foliage
- broader castle/interior/exterior layer set

Kaer Morhen Enhanced is mostly utility/functionality:

- bed
- stash
- armor/sword stands
- alchemy/crafting tables
- bookshelves/library buff
- fast travel marker

This makes Extended + Enhanced a cleaner high-content stack than Splendor + Extended.

## Verification

Active physical mod folder count after install/configuration: 199.

DX12 launch smoke test passed:

- launched through `tools/direct-launchers/Witcher3DirectDX12.exe`
- `witcher3.exe` opened a responding main window titled `The Witcher 3`
- observed working set after 40 seconds: ~1.70 GB

## Remaining Risk

Launch success does not prove the map is clean. In-world validation is still required.

Test points:

- Kaer Morhen exterior traversal
- castle interior traversal
- second floor/basement/crypt/mine areas from Extended
- KME bed/stash/stands/tables/bookshelves/fast travel
- doors and collision around restored/expanded areas
- occlusion issues such as disappearing towers/walls/floors

If Extended is visually worse than Splendor, revert by re-enabling `modkaermorhenrestoredtoitsancientsplendor` and disabling `modkaer_morhen_extended`.
