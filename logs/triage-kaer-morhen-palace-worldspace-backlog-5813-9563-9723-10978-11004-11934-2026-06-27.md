# Kaer Morhen / Palace Worldspace Backlog Triage

Date: 2026-06-27

## Scope

- `5813` - Kaer Morhen Armory Rubble Removed
- `9563` - Kaer Morhen Restored To Its Ancient Splendor
- `9723` - Kaer Morhen's Bastion Restored
- `10978` - Kaer Morhen Enhanced
- `11004` - Full Access To An Expanded Beauclair Palace
- `11934` - Kaer Morhen Extended Edition

## Current State

Do not treat these as normal install backlog items. This cluster is a deferred worldspace/content-loader project.

Current live scan:

- `Mods\modKMArmoryRubbleRemoved` existed but was disabled in `mods.settings`.
- `DLC\dlcKaerMorhenEnhanced` exists.
- `Mods\mod_KaerMorhenEnhanced` is not present and is disabled in `mods.settings`, so Kaer Morhen Enhanced's script/string half is not currently active.
- The large Kaer Morhen world overhauls and Palace Extended are disabled in `mods.settings`.

## Action

Archived the disabled Kaer Morhen rubble folder out of the active `Mods` scan path:

- From: `Mods\modKMArmoryRubbleRemoved`
- To: `_CodexArchivedMods\modKMArmoryRubbleRemoved.disabled-settings-20260627`

No active enabled mod was removed.

## Decisions

### Keep Deferred

- `11934` Kaer Morhen Extended Edition
- `9563` Kaer Morhen Restored To Its Ancient Splendor
- `9723` Kaer Morhen's Bastion Restored
- `11004` Full Access To An Expanded Beauclair Palace

These are not Script Merger problems. They are cooked worldspace, collision, occlusion, terrain, DLC/package, and content-loader risk.

### Do Not Stack Blindly

The large Kaer Morhen packages overlap the same world region. Load order can choose winners, but it will not truly merge castle geometry, collision, occlusion, and terrain edits. Combining them properly would be REDkit/world-layer work.

### Revisit Only As A Dedicated Pass

If we reopen this cluster, do it deliberately:

1. Free loader budget by archiving lower-value content mods.
2. Pick one Kaer Morhen world base.
3. Restore only the matching mod/DLC pair.
4. Launch test.
5. Load an in-world Kaer Morhen save and check traversal, collision, interiors, map/menu stability, and utility interactions.
6. Only then consider adding narrow patches like rubble cleanup.

## Why This Matters

This stack has already shown no-window launch hangs and Kaer Morhen loading/visual uncertainty. The current strongest line is to keep the stable game stack clean and not let disabled worldspace experiments remain in the active mod scan path.

## Status

- Disabled shell archived: `5813`.
- Large worldspace mods remain deferred.
- No scripts changed.
- No launch test run in this triage pass.
