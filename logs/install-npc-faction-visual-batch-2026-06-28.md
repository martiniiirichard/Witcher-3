# Install - NPC / Faction Visual Batch

Date: 2026-06-28

## Installed

### BW NPCs AIO - Regis No Eyes `7072`

Archive:

- `C:\Users\marti\Downloads\02 - BW NPCS - AIO - Regis NO EYES-7072-1-1-1723999812.zip`

Installed folder:

- `mod023zzjayBW_NPCs_Regis_No_Eyes`

Payload:

- `content\blob0.bundle`
- `content\metadata.store`
- `content\texture.cache`

Reason:

- Content/texture-only.
- Bundle scan found 20 assets and no overlap with the existing enabled bundle index.

Load order:

```ini
[mod023zzjayBW_NPCs_Regis_No_Eyes]
Enabled=1
Priority=200
```

### Faction Appearance Project `5669`

Archive:

- `C:\Users\marti\Downloads\Faction Appearance Project-5669-4-02-1744380426.rar`

Installed folder:

- `modFactionAppearanceProject`

Payload:

- `content\blob0.bundle`
- `content\buffers0.bundle`
- `content\metadata.store`
- `content\texture.cache`

Reason:

- Content/texture-only.
- Bundle scan found 302 assets with 4 overlaps against the prior enabled bundle index, mainly `modBrothersInArms` and `modHDReworkedProject`.
- Low enough overlap to try as a visual/faction enrichment candidate.

Load order:

```ini
[modFactionAppearanceProject]
Enabled=1
Priority=201
```

### Temeria Faction Overhaul `10161`

Archive:

- `C:\Users\marti\Downloads\TemeriaFactionOverhaul-10161-1-5-1776004218.zip`

Installed folder:

- `modfactionimprovementstemeria`

Payload:

- `content\blob0.bundle`
- `content\buffers0.bundle`
- `content\en.w3strings`
- `content\metadata.store`
- `content\texture.cache`

Reason:

- Content/texture/string-only.
- Bundle scan found 221 assets with 12 overlaps against the prior enabled bundle index.
- Accepted as a faction-visual candidate; watch Temerian/Blue Stripes/Nilfgaard-adjacent scenes for visual oddities.

Load order:

```ini
[modfactionimprovementstemeria]
Enabled=1
Priority=202
```

## Deferred From This Batch

### zzjay NPCs `7051`

Deferred because it overlaps named appearance choices already in the current stack:

- `modCerys_5app02_S`
- `modNakedCollection`
- `modYenFace`

This may still be useful, but should be handled as a deliberate named-NPC appearance decision rather than a broad install.

### Vegetation Billboards Remastered `8956`

Deferred despite zero exact overlap in the older bundle index.

Reason:

- It is a broad 346-asset vegetation pass.
- Current visuals already include HDRP, HD tree billboards, Better Grass AO, Realistic Weather, and dense lighting/weather work.
- Best handled during a deliberate foliage/performance/LOD pass.

## Validation

- Enabled mods after install: `203`
- Enabled priority range: `0..202`
- Duplicate enabled priorities: `0`
- Invalid enabled priorities: `0`
- Script files installed: none.
- Script Merger required: no.
- DX12 launch smoke: passed. `witcher3.exe` was running and responsive after 50 seconds, then closed cleanly.

## Residual Risk

- Compile risk is effectively none.
- Visual risk remains: check Blood and Wine NPCs, Novigrad/Temerian faction NPCs, guards, and faction-heavy scenes during normal play.
