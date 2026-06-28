# Install: Community Patch - World Map Full (8259)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/8259
Archive: `C:\Users\marti\Downloads\Full-8259-1-0-2-1780403224.zip`

## Decision

Installed the Full variant as the winning world-map compatibility patch for the current E3 HUD + Colored Map Markers stack.

## Why

Community Patch - World Map is a compatibility resource for `panel_worldmap.redswf` conflicts. The Full variant includes the world-map compatibility base plus Smooth GUI, Colored Map Markers, and No World Map Levels behavior.

This is a deliberate exception to the normal "BiA wins direct conflicts" rule because the archive is a narrow compatibility bundle intended to combine world-map UI edits. It should win over E3 HUD / Colored Map Markers for this specific world-map asset instead of letting one raw UI owner shadow the others.

## Install

Installed:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modCommunityPatch_WorldMapFull`

Added to `mods.settings`:

```ini
[modCommunityPatch_WorldMapFull]
Enabled=1
Priority=7
```

Priority 7 places it above the active E3 HUD and Colored Map Markers UI layer:

- `mod0_E3HUD_W3EER_NG` at priority 10
- `modE3HUD` at priority 12
- `modBetterIcons2025_NextGen_W3EE` at priority 13
- `modColoredMapMarkers` at priority 14

Backup path:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\community-patch-world-map-8259-20260627-231114`

## Validation

- Archive contains one mod folder: `modCommunityPatch_WorldMapFull`.
- Archive contains only `blob0.bundle` and `metadata.store`; no `.ws` scripts and no menu XML.
- No loose `panel_worldmap.redswf` owner was present in the active `mods` folders.
- Compile/startup smoke test is still required after install.

## Residual Risk

The Full variant also includes No World Map Levels behavior. That is acceptable for now as an immersive map simplification, but it should be visually checked in game.

In-game checks:

- World map opens without menu corruption.
- Colored markers appear.
- Signpost icons and filters behave normally.
- Missing/hidden level labels are acceptable.
- Useful POP pins still display correctly.
