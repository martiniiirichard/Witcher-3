# Inspect - BGM, Kaer Morhen Armory Rubble, Benis Toussaint Lighting

Date: 2026-06-26

## BGMv3 Mixed

Decision: removed from active download flow by quarantining the archive.

Moved:

- From: `C:\Users\marti\Downloads\BGMv3 mixed Ver 2-9028-2-1713517286.zip`
- To: `C:\Users\marti\OneDrive\Documents\New project\Witcher-3\downloads-quarantine\removed-visual-risk\BGMv3 mixed Ver 2-9028-2-1713517286.zip`

Reason: grass/foliage visual risk against the current foliage stack. This is not worth stacking unless we do a deliberate grass pass later.

## Kaer Morhen Armory Rubble Removed

Source archive:

- `C:\Users\marti\Downloads\Kaer Morhen Armory Rubble Removed-5813-1-2-1708274171.rar`

Extracted candidate:

- `modKMArmoryRubbleRemoved`
- Content-only: `blob0.bundle`, `buffers0.bundle`, `metadata.store`
- Script files: `0`

Bundle inspection found 12 files. Important paths:

- `levels\kaer_morhen\kaer_morhen_valley\q403_arsenal_rubble\q403_arsenal_nonpermanent\nonpermanent_rubble.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_interior\q403_avallach_chamber\q403_avallach_chamber.w2l`
- several Kaer Morhen castle interior/global lighting layers

Compared against active Kaer stack:

- `modkaer_morhen_extended`: 0 exact bundle path overlaps
- `mod_KaerMorhenEnhanced`: 0 exact bundle path overlaps

Decision: installed as a narrow selective Kaer Morhen patch.

Installed:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modKMArmoryRubbleRemoved`

Load order:

```ini
[modKMArmoryRubbleRemoved]
Enabled=1
Priority=264
```

Backup:

- `backups\km-armory-rubble-removed-20260626-*\mods.settings.before`

Verification:

- DX12 launch smoke passed. `witcher3.exe` stayed alive after 55 seconds.

Residual risk:

- This proves no immediate launch/content load failure. It does not visually prove the armory scene, Avallach chamber, or Kaer Morhen lighting are perfect. In-world check later: visit Kaer Morhen armory/arsenal and Avallach chamber after relevant story state.

## Benis Toussaint Lighting Overhaul

Source archive:

- `C:\Users\marti\Downloads\Benis Toussaint Lighting Overhaul-11820-1-1-4-5-1770077045.rar`

Extracted candidate:

- `modtoussaintw4New`
- Content-only: `blob0.bundle`, `metadata.store`
- Script files: `0`

Bundle inspection found 40 files. The payload broadly changes Blood and Wine environment definitions:

- `dlc\bob\data\environment\definitions\sunny\*.env`
- `dlc\bob\data\environment\definitions\foggy\*.env`
- `dlc\bob\data\environment\definitions\rainy\*.env`
- `dlc\bob\data\environment\definitions\quests\q704\*.env`
- `dlc\bob\data\fx\environment\weather\weather_bob.csv`
- `dlc\bob\data\levels\bob\bob.w2w`

Exact overlaps with current active weather/Toussaint stack:

- `mod_FilterlessToussaint`: 2 exact overlaps
  - `dlc\bob\data\environment\definitions\sunny\sunny_bob_v7.env`
  - `dlc\bob\data\fx\environment\weather\weather_bob.csv`
- `modRealisticWeather4`: 1 exact overlap
  - `dlc\bob\data\environment\definitions\foggy\fog_tm_pois.env`
- `modPromotionalAtmosphereLighting`: 0 exact overlaps
- `modNewToussaintClouds1_3`: 0 exact overlaps

Decision: deferred. Treat this as a deliberate Toussaint lighting/weather pass, not a quick content add.

Reason:

- It would directly override active Filterless Toussaint and Realistic Weather behavior.
- It changes `weather_bob.csv`, which is exactly the kind of file that can quietly alter weather transitions, rain/storm behavior, and downstream weather-script expectations.
- It touches `bob.w2w`, so this is broader than a simple lighting texture replacement.

Strong next move if revisited:

- Compare it visually against the current stack in Beauclair day, Beauclair night, rain, fog, Toussaint interiors, and q704/fairy tale scenes.
- Only install if we intentionally choose Benis as the Toussaint lighting winner, then place it after Filterless Toussaint/Realistic Weather or remove the redundant Toussaint pieces it supersedes.

## Benis Follow-Up Diff

Compared against the current active Toussaint/weather winners:

- `weather_bob.csv`: real text changes, not just a repack.
- `sunny_bob_v7.env`: large binary profile change versus Filterless Toussaint.
  - Benis length: `181229`
  - Filterless length: `198751`
  - Shared bytes different: about `67.76%`
- `fog_tm_pois.env`: tiny binary profile change versus Realistic Weather.
  - Same file length: `94381`
  - Shared bytes different: about `0.02%`

Weather table behavior:

- Filterless Toussaint makes normal Toussaint weather mostly one mid-cloud look:
  - `WT_Clear`: `0.0`
  - `WT_Light_Clouds`: `0.0`
  - `WT_Mid_Clouds`: `0.85`
  - `WT_Fog`: `0.08`
- Benis spreads probability back across multiple daytime/fog states:
  - `WT_Clear`: `0.4`
  - `WT_Light_Clouds`: `0.3`
  - `WT_Mid_Clouds`: `0.4`
  - `WT_Fog`: `0.1`
  - adds `WT_Fog2`: `0.1`

Payload concentration:

- `21` files: q704 fairy-tale / Dettlaff quest lighting.
- `6` files: sunny/daylight profiles.
- `3` files: fog profiles.
- `2` files: q702 wight quest lighting.
- `2` files: rain profiles.
- `2` files: Toussaint interior cubemaps.
- `1` file: Blood and Wine world definition, `bob.w2w`.
- `1` file: Toussaint weather probability/effect table, `weather_bob.csv`.

Interpretation:

- Full high-priority Benis install would visibly change everyday Toussaint weather away from the current Filterless Toussaint look.
- Low-priority Benis install might preserve current Filterless/Realistic Weather overlapping winners while still adding unique q704/q702/rain/interior/cutscene profiles, but `bob.w2w` means that is still a world-level visual change and should be tested deliberately.
