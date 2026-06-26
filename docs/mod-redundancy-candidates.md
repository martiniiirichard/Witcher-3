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
| Low-value disabled folders from prior cleanup | Several `DISABLED_*low-value-cleanup*` folders remain. | No gameplay risk while disabled, but clutter makes audits noisier. | Candidate for later archive move outside `mods`, only with approval. |

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
