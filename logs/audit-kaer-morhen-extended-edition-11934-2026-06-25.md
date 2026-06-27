# Audit - Kaer Morhen Extended Edition 11934

Date: 2026-06-25

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/11934`
- Archive: `C:\Users\marti\Downloads\Kaer Morhen Extended Edition-11934-1-2-1772604141.7z`
- Extracted temp folder: `C:\Users\marti\AppData\Local\Temp\codex_km_extended_11934_inspect\modkaer_morhen_extended`

## Nexus Notes

Nexus page identifies the mod as version 1.2, REDkit-made. It expands Kaer Morhen's fortress and surroundings, restores the second floor and basement, adds TW1-inspired areas/landmarks, and says it can be installed at any point in the game.

## Archive Shape

Top-level mod folder:

- `modkaer_morhen_extended`

Content files:

- `blob0.bundle`
- `buffers0.bundle`
- `collision.cache`
- `texture.cache`
- `en.w3strings`
- `metadata.store`
- `info.json`

No `.ws` scripts were visible. Script Merger is not the relevant tool for this mod.

Internal `info.json` metadata:

```json
{
  "name": "kaer_morhen_extended",
  "modName": "kaer_morhen_extended",
  "version": "1.0",
  "succesfullyCooked": false,
  "dependencies": []
}
```

This does not match the Nexus version number, which is a caution flag but not proof of failure.

## Package Comparison

String-based relevant resource counts:

- Kaer Morhen Extended 11934: 952
- Kaer Morhen Restored To Its Ancient Splendor 9563: 801
- Kaer Morhen Enhanced 10978: 67

Exact overlaps:

- Extended vs Splendor: 70
- Extended vs Enhanced: 5

High-signal overlaps with Splendor include:

- `levels\kaer_morhen\kaer_morhen.w2w`
- `levels\kaer_morhen\kaer_morhen.grassmask`
- `levels\kaer_morhen\env_global_pbr\castle\env.w2l`
- `levels\kaer_morhen\fake_doors.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_exterior\castle_addons.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_exterior\castle_walls_entities.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_exterior\eating_area.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_exterior\main_keep.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_interior\castle_interior.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_interior\castle_interior_addons.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_interior\doors.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_interior\gameplay.w2l`
- `levels\kaer_morhen\kaer_morhen_valley\castle_interior\weather_volume.w2l`
- multiple `levels\kaer_morhen\occlusion_tiles\...`
- multiple `levels\kaer_morhen\terrain_tiles\...`

## Interpretation

Extended 11934 is not a safe additive install on top of Splendor 9563. It is another large Kaer Morhen world/collision/occlusion/terrain package that modifies the same region and many exact same layer paths.

This is different from Kaer Morhen Enhanced 10978, which is mostly a custom DLC/functionality layer and only lightly overlaps with Splendor.

## Recommendation

Treat Extended 11934 and Splendor 9563 as competing Kaer Morhen world overhauls.

Best next test, if we want to evaluate Extended:

1. Temporarily disable `modkaermorhenrestoredtoitsancientsplendor`.
2. Install `modkaer_morhen_extended`.
3. Keep `mod_KaerMorhenEnhanced` active.
4. Launch test.
5. Compare in-world with the Splendor baseline.

Do not stack Extended and Splendor unless we are intentionally doing a REDkit/world-layer manual merge later.
