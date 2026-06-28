# Mod Redundancy Candidates

Date: 2026-06-26

Purpose: track mods that may be redundant, low-value, or already superseded. This is advisory only. Do not delete, disable, or reprioritize anything without explicit approval.

## Rules

- W3EE Redux owns core gameplay.
- Brothers in Arms owns broad bugfix/restoration compatibility.
- If a mod only duplicates W3EE/BiA behavior, it is a removal candidate.
- If a mod is content-only and harmless, removal is optional and should be based on value/clutter.
- If a mod required manual compatibility work and is currently stable, prefer caution.

## Candidates To Review Before Removal

| Candidate | Evidence | Risk if removed | Recommendation |
| --- | --- | --- | --- |
| `modE3HUD` vs `mod0_E3HUD_W3EER_NG` | Both active. `modE3HUD` is large asset/string bundle; `mod0_E3HUD_W3EER_NG` contains W3EE/E3 HUD scripts and compatibility work. | Removing the wrong one may break HUD assets or scripts. | Do not delete now. Treat as a paired stack until we prove which folder provides assets versus compatibility scripts. |
| Standalone Friendly HUD / More Quick Slots / Immersive Cam / AQOOM style behavior | Follow-up audit found no active standalone folders named `modMoreQuickSlots`, `modFHUD`, `modFriendlyHUD`, `modImmersiveCam`, or `modAQOOM`. Active menus are W3EE-integrated XML: `modMoreQuickSlots.xml`, `modFHUDConfig.xml`, and `ImmCamMenu.xml`. | Deleting the menu XML would break W3EE-integrated add-on configuration. Adding standalone versions later would create real duplication. | Do not remove these W3EE-owned menus. Avoid adding standalone copies on top of W3EE. See `docs/ui-control-overlap-audit.md`. |
| Kaer Morhen world-overhaul test folders | Current `mods.settings` has the Kaer Morhen overhaul entries disabled, and no matching live folders remain in the active `Mods` scan path. | No gameplay risk from absent disabled folders; the risk is stale notes causing us to chase already-resolved cleanup. | No file action needed. Keep disabled settings entries as historical rollback markers unless we later decide to prune disabled `mods.settings` sections. |
| `modshrinesofverna` + `modVernaShrine_Everlasting` | Confirmed split compatibility setup: `modshrinesofverna` keeps bundled/world/localization assets, its duplicate local scripts are disabled, and `modVernaShrine_Everlasting` supplies the improved vitality effect. `dlcshrinesofverna` remains installed. | Removing either may remove world/content/localization assets or the intended Everlasting effect behavior. | Keep. This is an intentional manually split compatibility pair, not redundancy. |
| HDRP stack | Confirmed active official multi-part HDRP install plus compatibility layers: `mod00000HDReworkedProject`, `modHDReworkedProject` through `modHDReworkedProject4`, `mod000000aHDRP_BiA`, and `modATrueFiresHDReworkedProjectCompatibility`. | Removing a part may degrade textures or undo BiA/True Fires/HDRP compatibility. | Keep. These are install volumes/patch layers, not duplicate folders. See `logs/audit-hdrp-redundancy-status-2026-06-27.md`. |
| `modWitcher3RFGUnshaved` plus disabled RFG folder | Active unshaved variant and disabled alternate exist. | Disabled folder should not compile; active folder is the chosen visual preference. | Keep active unshaved variant. Disabled alternate can be archived later if we clean backups. |
| Low-value disabled folders from prior cleanup | Several `DISABLED_*low-value-cleanup*` folders remained. | No gameplay risk while disabled, but clutter makes audits noisier. | Archived on 2026-06-26. See `logs/archive-disabled-redundant-mod-folders-2026-06-26.md`. |

## Already Low Confidence For Removal

These are not good removal candidates right now:

- `mod0000_MergedFiles`: required script merge output.
- `mod000_Patch_BIA-W3EER`: core compatibility patch.
- `mod00FlorenEconomySystem_W3EE_REDUX` and `mod00ReputationSystem_W3EE_REDUX`: match the target economy/reputation goals.
- `modRandomEncountersReworked`: matches the exploration-pressure goal.
- `modBrothersInArms`: primary bugfix/restoration owner.
- `modW3EE`, `modReduxW3EE`, `modW3EELocalization*`: core stack.
- W3EE-owned add-on menus: `ImmCamMenu.xml`, `modFHUDConfig.xml`, `modMoreQuickSlots.xml`.

## Next Redundancy Audit

1. Build an asset/script ownership map for the E3 HUD stack.
2. Check whether any active UI/control folder is only an old standalone copy now superseded by W3EE Redux.
3. Review active duplicate/paired content mods with disabled backups.
4. Only then propose a removal batch for user approval.

## Cleanup Completed

2026-06-26:

- Archived disabled/superseded/failed-test folders out of active `Mods` and `DLC` scan paths.
- Archived the disabled standard `modWitcher3RFG` folder; the selected active variant remains `modWitcher3RFGUnshaved`.
- Archived normal-named folders that were already `Enabled=0` in `mods.settings`, including the disabled Kaer Morhen test layers and `modLessIsMore`.
- Verified there are no enabled `mods.settings` entries missing physical active folders after cleanup.
- Archived `modW3QE` reduced shell and `modHDRPTestApple` test utility. See `logs/archive-redundant-active-shells-w3qe-hdrptestapple-2026-06-26.md`.
- Archived `modNoMissableTrophies`, `dlcNoMissableTrophies`, and `dlcNoMissableMutagens` after user approval. See `logs/archive-no-missable-trophies-2026-06-26.md`.

## Future Trim Only If Needed

These are active, low-risk flavor/polish additions. User preference is to keep them for now because they are nice additions, but they are reasonable future removal candidates if loader budget, visual clutter, or debugging pressure requires a leaner stack:

- `modAdditionalArmorStandsNoUni`
- `modMorgueLightsFix`
- `modLampOnPlayersBoat_NoCityLight`
- `modZ_GrammarOfThePath`
- Brothel/Addicted appearance variants: `modViola`, `modSuzy`, `modNarcissa1`, `modBertha1`, `modTouCourt1`
- `modBaratheon`

Do not remove these as generic cleanup without another approval pass.

## Shadowed Bundle Audit - 2026-06-27

Rule verified from prior logs: lower numeric `mods.settings` priority wins in this stack.

This pass used `tools/tmp/bundle-conflict-index-20260625/enabled-bundle-assets.csv`, so it covers the active bundle index from that audit date. Treat the result as strong evidence for older installed mods, but refresh the bundle index before a large cleanup batch.

### Strong Removal Candidates

These appear to be active but functionally shadowed by other active mods. Do not remove without approval, but these are good cleanup candidates.

| Candidate | Evidence | Recommendation |
| --- | --- | --- |
| `modAtmosphericNights` | One bundled asset: `fx\demos_and_temp_fx\darkness_upon_us.env`. It loses to `modDarkerNights` priority `237`; `modAtmosphericNights` is priority `238`. | Archived after user approval on 2026-06-27. |
| `modNoEnemyDotsAndNoHerbs` | One bundled SWF: `gameplay\gui_new\swf\hud\hud_minimap2.redswf`. It loses to `modE3HUD` priority `12`; no active scripts or menu XML found in the folder. | Archived on 2026-06-27 because E3 HUD is the chosen HUD owner. |
| `modNG_modUndiesVanillaFix` | Its two underwear mesh assets lose to `modNG_modNudeUndies_M_MFla_B` priority `207`; this folder is priority `211`. | Archived after user approval on 2026-06-27. |
| `modNewVaginas` | Its 18 common female body texture assets lose to `modWitcher3RFGUnshaved` priority `57`; `modNewVaginas` is priority `58`. User preference is the unshaved RFG variant. | Archived after user approval on 2026-06-27. |
| `modFoodRebalanceRedux` | Its three bundled item/ability XML assets lose to `mod0000_W3EER_FoodRebalance_BiA_Patch` and `mod000000_W3EER_FoodRebalance_LighterBombsCompat`. | Archived on 2026-06-27 after verifying the W3EE/BiA patch and custom lighter-bombs compatibility mod supersede its active runtime files. |

### Not Removal Candidates Despite Shadowed Assets

| Item | Why It Looked Redundant | Why To Keep |
| --- | --- | --- |
| `mod__hoods` | Its inventory SWF loses to E3 HUD. Fresh 2026-06-27 audit confirmed `dlc__hoods`, Hoods keybind file, and active local scripts remain installed, with prior W3EE compatibility edits for dyeing and paperdoll animation. | Keep. Hoods' items/scripts/DLC still matter; the SWF loss was already accepted to preserve E3/W3EE inventory UI. |
| `modLiveBestiary` | Its original bestiary SWF loses to E3 HUD. | This is intentional; Live Bestiary contributes data/content while E3/W3EE-compatible UI behavior wins. |
| `modEvents` | Its bundled world/content rows are shadowed by BiA/Boat Races in the old index. Fresh 2026-06-27 audit confirmed it still has `dlcEvents`, registered `Events.xml`, active fact/journal scripts, and only the duplicate BiA-supplied descriptor script is disabled. | Keep unless the Events feature is unwanted. This is a script/menu/DLC feature layer, not a dead bundle folder. |
| `modNaturalTorchlight` | Its torch entity asset loses to `modTrueFires`. | Natural Torchlight script logic was manually grafted into `mod0000_MergedFiles`, and its menu XML is registered. Keep unless we intentionally remove that merged behavior. |
| `modAMM` | One horse entity asset loses to BiA. | AMM has active scripts/assets and the W3EE Redux compatibility patch. Keep while AMM is desired. |

### E3 HUD Ownership Notes

`modE3HUD` and `mod0_E3HUD_W3EER_NG` are not simple duplicates. They are the selected HUD stack:

- `modE3HUD` provides the base E3-style HUD assets and wins a few standalone panels.
- `mod0_E3HUD_W3EER_NG` wins most W3EE-sensitive panels and is the compatibility layer for the current W3EE Redux setup.
- `modE3HUDColorLoad` only wins loading-screen SWFs over the base E3 HUD layer.

The E3 stack competes with W3EE vanilla UI assets, Hoods inventory UI, Live Bestiary's original bestiary SWF, Extra Skill Slots' character SWF, and `modNoEnemyDotsAndNoHerbs`' minimap SWF. That does not make the E3 stack redundant; it means it is the active UI owner. Do not remove either `modE3HUD` or `mod0_E3HUD_W3EER_NG` unless we intentionally redesign the full UI stack.

### Food Rebalance Notes

Current active priority winners:

- `gameplay/abilities/effects.xml`: `mod0000_W3EER_FoodRebalance_BiA_Patch` wins over `modFoodRebalanceRedux`, W3EE, and BiA.
- `gameplay/items/def_item_cooking_recipes.xml`: `mod0000_W3EER_FoodRebalance_BiA_Patch` wins over `modFoodRebalanceRedux`.
- `gameplay/items/def_item_edibles.xml`: `modlighterbombsW3eeRedux` wins over both the W3EE/BiA Food Rebalance patch and base Food Rebalance.

For a difficult, balanced economy, the concerning overlap is `modlighterbombsW3eeRedux`. It owns the entire edibles file, not just bomb weights. It lowers or changes many food/drink prices and quality tiers while also making bomb casings lighter.

Resolution applied on 2026-06-27:

- Added custom compatibility mod `mod000000_W3EER_FoodRebalance_LighterBombsCompat`.
- It contains the W3EE/BiA Food Rebalance `def_item_edibles.xml` with only `Bomb casing` and `Bomb casing_Stash` weight changed from `0.7` to `0.2`.
- Set compatibility mod to `Enabled=1`, `Priority=6`.
- Set original `modlighterbombsW3eeRedux` to `Enabled=0`, `Priority=7`.

This preserves the intended bomb-use incentive without letting the older Lighter Bombs edibles file soften the broader food/drink economy.

`modFoodRebalanceRedux` was archived on 2026-06-27 after confirming it is content-only and its three bundled XML files are fully superseded:

- `effects.xml`: `mod0000_W3EER_FoodRebalance_BiA_Patch` wins.
- `def_item_cooking_recipes.xml`: `mod0000_W3EER_FoodRebalance_BiA_Patch` wins.
- `def_item_edibles.xml`: `mod000000_W3EER_FoodRebalance_LighterBombsCompat` wins.

The W3EE/BiA patch intentionally replaces base Food Rebalance bleeding entries with its own compatibility entries, and the recipe/edibles named item sets are covered by the active winners.

### Needs Decision: Remove Or Re-Prioritize

| Candidate | Evidence | Decision Needed |
| --- | --- | --- |
| `modRRTCHARDX12eyes` | Companion eyes fix for `modRTCHARDX12`; current priority is `182` vs parent `183`, so the eyes fix wins under lower-number-wins rules. Fresh unpack showed it overrides two parent eye material files with different hashes. | Keep. This is an active companion patch, not a redundancy candidate. |

## Weather / Visual Stack Audit - 2026-06-27

See `logs/audit-weather-visual-stack-2026-06-27.md`.

No safe removal candidate was found in the active weather/visual stack. Current read:

- Keep `modDenseRainfall` + `modRealisticRainV3`; they affect different rain layers.
- Keep `mod_FilterlessToussaint`, `modRealisticWeather4`, `modtoussaintw4New`, and `modNewToussaintClouds1_3` for now; this is an intentional Toussaint visual stack, not a simple duplicate.
- Keep `modDarkerNights`, `modNoArtificialPlayerLight`, and `modNaturalTorchlight`; they affect different night/light-source layers.
- Keep `modTrueFires` + `modATrueFiresHDReworkedProjectCompatibility` + Natural Torchlight's merged behavior.
- Keep HDRP, Better Grass AO, Environment Overhaul, HD Tree Billboards, RTCHARDX12, and RT Water Reflection script-only fix.

Rule going forward: new weather, lighting, cloud, rain, or Toussaint mods need exact-path inspection before install. These are visual-owner decisions, not routine backlog installs.

### Resolved: Archived

| Candidate | Resolution | Evidence |
| --- | --- | --- |
| `modDynamicWitcherSchematics` | Archived on 2026-06-27 and disabled in `mods.settings`. | It contains only two bundled content files. After unpacking, all four recipe XML paths were shadowed by lower-priority winners: `modleadOre`, `mod000_Patch_BIA-W3EER`, or `modW3EE`. Named recipe item blocks were identical to the winners except `DWSTestItem`, a hidden/no-drop/no-show test item. No scripts, DLC folder, menu XML, or input bindings were present. |

### Resolved: Keep

| Candidate | Resolution | Evidence |
| --- | --- | --- |
| `mod0BiA_ASL_Compatibility` | Keep with `modAdditionalStashLocations`. | Fresh bundle unpack showed the compatibility patch wins the overlapping `bob.w2em` and `novigrad.w2em` hub files at priority `10`; base ASL stays later at priority `226` and still contributes Skellige hub data plus two stash level files. The two overlapping patch files differ from base ASL by hash and size, so the patch is not a duplicate no-effect folder. |
| `modLessmusic` | Keep after priority correction. | Audit found it was enabled but losing `engine\sound.ws` to W3EE. Moved to priority `21` so it now wins the sound script while preserving W3EE sound-threat hooks. DX12 launch smoke passed. See `logs/audit-script-shadow-redundancy-pass-2026-06-27.md`. |
| `modBasicCookingRecipes` | Keep. | Its two alchemy scripts intentionally lose to W3EE, while `dlcBasicCookingRecipes` contributes recipe/vendor/loot data. |
| `modAllGearEnchantingBasedOnSockets` | Keep for now. | Main behavior was manually grafted into active Better Icons/W3EE enchanting logic; its remaining loose component loses to W3EE. Do not archive without a runewright behavior test. |
| `modmanticor` | Keep. | Its broad `temp.ws` intentionally loses to W3EE; useful payload is bundled/XML content. |
| `mod00ReputationSystem_W3EE_REDUX` | Keep. | Scripts lose to `mod00FlorenEconomySystem_W3EE_REDUX` by design; Floren Economy is the high-priority economy/reputation umbrella. |
| String/cache-only active mods | Keep. | Fresh pass found no stale active shell among no-script/no-bundle folders. HD Tree Billboards, TWCG Random OST, HD Ursine Concept, SNC W3EE Redux, Mods Menu Category, MenuStrings, Grammar of the Path, and W3EE localization folders all have legitimate string/cache/localization payloads. See `logs/audit-string-cache-shell-mods-2026-06-27.md`. |
