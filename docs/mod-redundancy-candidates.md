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
| `modkaer_morhen_extended` plus disabled backup of the same mod | Active folder exists, and a disabled backup folder of the same size also exists. | Active folder may be the selected working version after prior testing; disabled folder is backup clutter but not compiled. | Candidate for later archive cleanup only, not gameplay removal. Confirm commit/log history first. |
| `modshrinesofverna` + `modVernaShrine_Everlasting` | We previously had duplicate class/function conflicts. Current `modshrinesofverna` has local scripts disabled so Everlasting can win parts of the implementation. | Removing either may remove content or compatibility split. | Keep for now. Documented as a manually split compatibility pair. |
| `modHDReworkedProject`, `modHDReworkedProject2`, `modHDReworkedProject3`, `modHDReworkedProject4`, `mod00000HDReworkedProject`, `mod000000aHDRP_BiA` | Multiple HDRP folders are active. Some are likely official parts/patches/load-order layers, not duplicates. | Removing a part may degrade textures or undo BiA/HDRP compatibility. | Do not treat as redundant until checked against HDRP install instructions/file manifests. |
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
| `modNoEnemyDotsAndNoHerbs` | One bundled SWF: `gameplay\gui_new\swf\hud\hud_minimap2.redswf`. It loses to `modE3HUD` priority `12`; no active scripts or menu XML found in the folder. | Archive unless we intentionally leave E3 HUD and redesign minimap behavior. |
| `modNG_modUndiesVanillaFix` | Its two underwear mesh assets lose to `modNG_modNudeUndies_M_MFla_B` priority `207`; this folder is priority `211`. | Archived after user approval on 2026-06-27. |
| `modNewVaginas` | Its 18 common female body texture assets lose to `modWitcher3RFGUnshaved` priority `57`; `modNewVaginas` is priority `58`. User preference is the unshaved RFG variant. | Archived after user approval on 2026-06-27. |
| `modFoodRebalanceRedux` | Its three bundled item/ability XML assets lose to `mod0000_W3EER_FoodRebalance_BiA_Patch` and `modlighterbombsW3eeRedux`. | Do not archive as a simple no-effect mod yet. The W3EE/BiA patch appears to carry the intended harsher status-effect behavior, but `modlighterbombsW3eeRedux` currently wins `def_item_edibles.xml` and changes many food/drink prices, categories, qualities, and bomb-casing weight. Needs a balance decision. |

### Not Removal Candidates Despite Shadowed Assets

| Item | Why It Looked Redundant | Why To Keep |
| --- | --- | --- |
| `mod__hoods` | Its inventory SWF loses to E3 HUD. | Hoods' items/scripts still matter; the SWF loss was already accepted to preserve E3/W3EE inventory UI. |
| `modLiveBestiary` | Its original bestiary SWF loses to E3 HUD. | This is intentional; Live Bestiary contributes data/content while E3/W3EE-compatible UI behavior wins. |
| `modEvents` | Its bundled world/content rows are shadowed by BiA/Boat Races in the old index. | It still has active scripts: `events_journal.ws` and `events_modMenu.ws`. Keep unless the Events feature is unwanted. |
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

Do not remove `modFoodRebalanceRedux` until we confirm whether the compatibility patch fully depends on its DLC/bundle presence or merely supersedes it. The safer near-term candidate is not removal; it is a controlled priority/manual-merge pass for `modlighterbombsW3eeRedux`.

### Needs Decision: Remove Or Re-Prioritize

| Candidate | Evidence | Decision Needed |
| --- | --- | --- |
| `modRRTCHARDX12eyes` | Companion eyes fix for `modRTCHARDX12`; current priority is `182` vs parent `183`, so the eyes fix should win under lower-number-wins rules. | Keep for now. Only revisit if visual inspection shows eye artifacts or a fresh index contradicts this. |

### Resolved: Archived

| Candidate | Resolution | Evidence |
| --- | --- | --- |
| `modDynamicWitcherSchematics` | Archived on 2026-06-27 and disabled in `mods.settings`. | It contains only two bundled content files. After unpacking, all four recipe XML paths were shadowed by lower-priority winners: `modleadOre`, `mod000_Patch_BIA-W3EER`, or `modW3EE`. Named recipe item blocks were identical to the winners except `DWSTestItem`, a hidden/no-drop/no-show test item. No scripts, DLC folder, menu XML, or input bindings were present. |

### Resolved: Keep

| Candidate | Resolution | Evidence |
| --- | --- | --- |
| `mod0BiA_ASL_Compatibility` | Keep with `modAdditionalStashLocations`. | Fresh bundle unpack showed the compatibility patch wins the overlapping `bob.w2em` and `novigrad.w2em` hub files at priority `10`; base ASL stays later at priority `226` and still contributes Skellige hub data plus two stash level files. The two overlapping patch files differ from base ASL by hash and size, so the patch is not a duplicate no-effect folder. |
