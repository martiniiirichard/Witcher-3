# Audit - Weather and Visual Stack

Date: 2026-06-27

Purpose: review active weather, lighting, cloud, rain, night, fire, terrain, and high-resolution visual mods for redundancy before moving into the backlog mod list.

## Method

- Parsed active `mods.settings` entries containing weather/visual keywords.
- Compared active bundle ownership against `tools/tmp/bundle-conflict-index-20260625/enabled-bundle-assets.csv`.
- Ran a direct filesystem inventory for newer/script/cache-only visual mods that the old bundle index does not fully see.
- No removals or priority edits were made during this pass.

## High-Level Result

No clean visual/weather removal candidate was found in this pass.

The current visual stack is layered, but most overlaps are intentional:

- HDRP/BiA owns broad texture and bugfix compatibility.
- E3/W3EE and NextGen Better FX override selected effects.
- Rain/weather/cloud mods touch different asset classes.
- Toussaint lighting is deliberately layered so existing winners keep exact conflicts while Benis contributes unique files.
- Darker Nights and No Artificial Player Light affect different layers.
- True Fires and Natural Torchlight are an intentional split because the Natural Torchlight script behavior is grafted into merged files.

## Active Stack Summary

| Area | Active owner(s) | Redundancy read |
| --- | --- | --- |
| HDRP / broad texture stack | `mod00000HDReworkedProject`, `modHDReworkedProject*`, `mod000000aHDRP_BiA`, `modZBrothersInArmsLOD` | Keep. Official multi-part texture payload plus compatibility/LOD layers. |
| Rain particles/textures | `modDenseRainfall`, `modRealisticRainV3` | Keep. Dense Rainfall owns rain particle `.w2p`; Realistic Rain owns rain/water textures. They do not exact-conflict in the old bundle index. |
| Weather tables/profiles | `modRealisticWeather4`, `modSkelligeWinterWeather`, `modPromotionalAtmosphereLighting` | Keep. Realistic Weather wins one Skellige weather table; Skellige Winter still wins snow/terrain texture payload; PAL wins many quest/atmosphere profiles. |
| Toussaint lighting/weather | `mod_FilterlessToussaint`, `modRealisticWeather4`, `modtoussaintw4New`, `modNewToussaintClouds1_3` | Keep for now. Benis is low-priority and contributes unique Blood and Wine lighting while losing exact conflicts to existing winners. Needs visual QA. |
| Clouds | `modNewClouds3_0`, `modNewToussaintClouds1_3`, `modVolumetricCloudsBootstrap1_31` | Keep. New Clouds and New Toussaint Clouds provide cloud textures; Volumetric Clouds Bootstrap has entity/script/DLC behavior and only two low-priority losses to BiA. |
| Nights / darkness | `modDarkerNights`, `modNoArtificialPlayerLight`, `modNaturalTorchlight` | Keep. `modAtmosphericNights` was already archived because Darker Nights shadowed it. Current three affect different darkness/light-source layers. |
| Fire / torches | `modTrueFires`, `modATrueFiresHDReworkedProjectCompatibility`, `modNaturalTorchlight` | Keep. True Fires wins many torch/fire entities; Natural Torchlight is retained for merged script/menu behavior; HDRP compatibility patch is required. |
| Grass / trees / terrain | `modBetterGrassAO`, `modHDTreeBillboards`, `modHDTreeBillboardsBnW`, `modenvironmentoverhaul` | Keep. Environment Overhaul is partially shadowed by HDRP, but still wins 295 indexed assets and was intentionally placed as a terrain/vegetation layer. |
| Ray tracing / reflection fixes | `modRTCHARDX12`, `modRRTCHARDX12eyes`, `modRTWaterReflectionColorFix` | Keep. Eyes companion patch wins over parent eye material files. RT Water Reflection is script-only because its bundle was disabled after startup-hang testing. |

## Notable Evidence

Bundle-index ownership highlights:

- `modDenseRainfall`: 2 indexed assets, 2 wins, 0 losses.
- `modRealisticRainV3`: 5 indexed assets, 5 wins, 0 losses.
- `modRealisticWeather4`: 8 indexed assets, 8 wins, 0 losses.
- `modSkelligeWinterWeather`: 65 indexed assets, 64 wins, 1 loss to Realistic Weather.
- `modPromotionalAtmosphereLighting`: 145 indexed assets, 130 wins, 15 losses.
- `modNewClouds3_0`: 7 indexed assets, 7 wins, 0 losses.
- `modNewToussaintClouds1_3`: 2 indexed assets, 2 wins, 0 losses.
- `modBetterGrassAO`: 148 indexed assets, 148 wins, 0 losses.
- `modenvironmentoverhaul`: 829 indexed assets, 295 wins, 534 losses. This is heavy overlap, but not dead.
- `modTrueFires`: 604 indexed assets, 454 wins, 150 losses.
- `modNaturalTorchlight`: 1 indexed asset, 1 win in the old index, but its important script logic lives in `mod0000_MergedFiles`.

Direct inventory filled gaps for mods not visible in the old bundle index:

- `modtoussaintw4New`: 1 bundle + metadata, content-only Benis Toussaint layer.
- `modnewlightningfx`: scripts, strings, cache, and metadata; weather-compatible script was previously installed.
- `modHDTreeBillboards` / `modHDTreeBillboardsBnW`: texture cache-only.
- `modNoArtificialPlayerLight`: script/string-only.
- `modRTWaterReflectionColorFix`: script-only active state; bundle remains disabled because it caused startup hang.

## Decisions

- Do not archive anything from this visual/weather stack right now.
- Keep the current rain pairing: Dense Rainfall for denser particle effect, Realistic Rain V3 for rain/water texture look.
- Keep the current Toussaint layering. If Toussaint looks wrong later, the decision point is not removal-by-default; it is choosing a Toussaint visual owner between Filterless Toussaint, Benis, Realistic Weather, and New Toussaint Clouds.
- Keep Natural Torchlight despite apparent overlap with True Fires because its behavior was manually merged.
- Keep Environment Overhaul despite heavy texture overlap because it still wins a meaningful asset set and matches the visual richness goal.

## Visual QA Backlog

Use in-game testing later, not blind cleanup:

1. Toussaint: Beauclair day, Beauclair night, rain/fog, interiors, q702 wight area, q704 fairy-tale/Dettlaff scenes.
2. Rain/storm: compare Velen/Novigrad/Skellige under normal rain and storm.
3. Skellige: verify snow/terrain and weather table behavior.
4. Night traversal: verify Darker Nights + No Artificial Player Light does not become unplayable without constant torch use.
5. Fire/torch: verify True Fires visuals with Natural Torchlight menu/script behavior.
6. Terrain/grass/tree distance: verify HDRP + Better Grass AO + Environment Overhaul + HD Tree Billboards do not produce obvious pop-in or texture mismatches.

## Next Move

Proceed to backlog mods with this baseline:

- New weather/lighting mods should be treated as deliberate visual-owner decisions, not quick installs.
- New rain/cloud/Toussaint mods need exact-path checks against the current stack before install.
- New texture mods can be installed only if they either win meaningful unique assets or clearly replace a current owner by design.
