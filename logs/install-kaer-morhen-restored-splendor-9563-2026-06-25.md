# Install - Kaer Morhen Restored To Its Ancient Splendor 9563

Date: 2026-06-25

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/9563`
- Archive: `C:\Users\marti\Downloads\Kaer Morhen restored to its ancient slpendor-9563-1-8-1729435430.zip`
- Installed folder: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modkaermorhenrestoredtoitsancientsplendor`

## Install Notes

Installed as a separate mod folder. No files were merged into `mod_KaerMorhenEnhanced`.

Updated active config:

- `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`

Added/confirmed:

```ini
[modkaermorhenrestoredtoitsancientsplendor]
Enabled=1
Priority=259
```

Current installed Kaer Morhen Enhanced remains active:

```ini
[mod_KaerMorhenEnhanced]
Enabled=1
Priority=260
```

Backup created:

- `backups/kaer-morhen-splendor-9563-20260625/mods.settings.before`

## Risk Model

This mod has no `.ws` scripts, so Script Merger is not relevant. The risk is content/world-layer behavior:

- interior objects from Kaer Morhen Enhanced may be embedded, floating, blocked, or hidden by restored geometry
- collision/occlusion from the restored world may affect access to KME utility objects
- the mod adds a large content payload, but only one active mod folder

## Verification

Active physical mod folder count after install: 198.

DX12 smoke test passed:

- launched through `tools/direct-launchers/Witcher3DirectDX12.exe`
- `witcher3.exe` opened a responding main window titled `The Witcher 3`
- observed working set after 35 seconds: ~1.70 GB

## Next Verification

In-world Kaer Morhen test still needed:

- castle interior traversal
- bed/stash/stands/tables from Kaer Morhen Enhanced
- bookshelves/library buff
- fast travel marker
- Wolf gear-related interior/exterior spots if convenient

If visual placement or collision problems appear, temporarily disable one of the two Kaer Morhen mods to determine whether the issue is Splendor alone or interaction between Splendor and KME.
