# Kaer Morhen Enhanced 10978 vs Kaer Morhen Restored 9563 Comparison

Date: 2026-06-25

## Mods Compared

- Installed: Kaer Morhen Enhanced 10978
  - `mods/mod_KaerMorhenEnhanced`
  - `dlc/dlcKaerMorhenEnhanced`
  - Active in `mods.settings` with `Enabled=1`, `Priority=260`
- Candidate: Kaer Morhen Restored To Its Ancient Splendor 9563
  - Archive: `C:\Users\marti\Downloads\Kaer Morhen restored to its ancient slpendor-9563-1-8-1729435430.zip`
  - Archive folder: `modkaermorhenrestoredtoitsancientsplendor`
  - Nexus page version: 1.8
  - Internal `info.json` version: 1.6

## Package Shape

Kaer Morhen Enhanced is a functional add-on. It adds custom DLC layers, utility objects, bookshelf buff logic, alchemy/crafting/stash/stand/bed/fast-travel layers, and one script file.

Kaer Morhen Restored is a large REDkit content/world restoration. It has no `.ws` gameplay scripts. It contains `blob0.bundle`, `buffers0.bundle`, `collision.cache`, `texture.cache`, many Kaer Morhen world layer references, meshes, entities, textures, and occlusion/terrain references.

## String-Based Package Comparison

Unique relevant resource strings found:

- Kaer Morhen Enhanced: 67
- Kaer Morhen Restored: 801
- Exact overlaps: 5

Meaningful exact layer overlaps:

- `levels\kaer_morhen\kaer_morhen_valley\castle_interior\castle_interior_addons.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_interior\loot.w2l`

Other exact overlaps were generic/location strings, not strong evidence of direct file collision:

- `kaer_morhen`
- `kaer_morhen_valley`
- `1s\new_locations\kaer_morhen\indoor\average\ironbound_chest.w2ents`

## Interpretation

This is not a normal Script Merger problem. There are no `.ws` scripts in the candidate mod. A true manual merge would mean REDkit/world-layer work: unpack or open the relevant Kaer Morhen layers, reconcile object placement/collision/loot/interior additions, and recook.

The good news is that the overlap is narrow. KME mostly adds custom DLC namespaced utility layers. Splendor mostly rebuilds/restores the vanilla Kaer Morhen world shell and collision/occlusion. These may coexist if KME's interactable layers sit on top of Splendor's restored environment.

The risk is visual or placement conflict, not script compilation:

- KME armor/sword stands, bed, stash, tables, or bookshelves may be embedded in, floating over, or blocked by Splendor's restored interior geometry.
- Splendor changes collision and occlusion, so an object that exists may be hard to reach or visually hidden.
- Splendor includes large world/collision/texture caches, so it may add loader pressure despite costing only one active mod folder.

## Recommended Test Line

Do not overwrite or combine files yet.

1. Install Splendor as its own mod folder.
2. Keep KME enabled.
3. Give KME later/higher practical priority than Splendor so functional objects are more likely to overlay the restored world, subject to how the current load order behaves.
4. Launch test first. This checks loader pressure and package validity.
5. In-world test at Kaer Morhen:
   - castle interior
   - stash/bed/stands/tables
   - bookshelves/library buff
   - fast travel marker
   - basic door/collision traversal
   - Wolf gear quest-adjacent interior/exterior areas if convenient
6. If visuals or collision are broken, compare with KME temporarily disabled. That distinguishes "Splendor itself is broken" from "KME functional layer conflicts with Splendor geometry."

## Decision

Worth testing. It is not obviously incompatible from package inspection. Manual merge should be treated as a fallback only if the stack launches but has object placement or collision defects.
