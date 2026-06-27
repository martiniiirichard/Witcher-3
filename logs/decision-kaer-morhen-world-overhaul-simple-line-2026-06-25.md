# Decision - Kaer Morhen World Overhaul Simple Line

Date: 2026-06-25

## Decision

Keep the highest-content Kaer Morhen world overhaul active and avoid stacking competing world overhauls.

Active:

```ini
[modkaer_morhen_extended]
Enabled=1
Priority=259

[mod_KaerMorhenEnhanced]
Enabled=1
Priority=260
```

Disabled:

```ini
[modkaermorhenrestoredtoitsancientsplendor]
Enabled=0
Priority=259
```

## Reason

Kaer Morhen Extended Edition 11934 appears to add the most content and has the largest unique world footprint: expanded fortress areas, basement/crypt/mine-style assets, additional occlusion/terrain/foliage, and broader castle interior/exterior layers.

Kaer Morhen Enhanced 10978 is a functional overlay rather than a competing full world overhaul, so it remains useful alongside Extended.

Kaer Morhen Restored To Its Ancient Splendor 9563 overlaps heavily with Extended on core world/collision/occlusion/terrain/castle layers. Stacking both is likely to produce hidden overrides, map/collision issues, or partial content loss. Manual REDkit merging can be revisited later, but it is tabled for now.

## Backup

Before locking the config, the active settings file was backed up to:

- `backups/kaer-morhen-final-simple-line-20260625/mods.settings.before`

## Next Test

When testing Kaer Morhen in-world, use Extended as the baseline and check:

- castle exterior traversal
- castle interior traversal
- second floor/basement/crypt/mine content
- KME bed/stash/stands/tables/bookshelves/fast travel
- any falling-through-world, invisible-wall, or occlusion problems
