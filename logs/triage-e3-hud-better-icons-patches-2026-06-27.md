# E3 HUD / Better Icons Patch Backlog Triage

Date: 2026-06-27

## Result

No new install action is recommended for the leftover E3 HUD / Better Icons compatibility downloads.

The active UI path is already:

- `modE3HUD`
- `mod0_E3HUD_W3EER_NG`
- `modBetterIcons2025_NextGen_W3EE`
- `modE3HUDColorLoad` as an optional cosmetic loading-screen layer

## Active / Keep

| Mod | Reason |
| --- | --- |
| `modE3HUD` | Base E3 HUD asset/string layer. |
| `mod0_E3HUD_W3EER_NG` | W3EE Redux NG compatibility script layer for E3 HUD. |
| `modBetterIcons2025_NextGen_W3EE` | W3EE-specific Better Icons package. |
| `modE3HUDColorLoad` | Small loading-screen cosmetic layer. Keep unless the look is unwanted. |

## Skip / Wrong Target Patches

| Download | Decision |
| --- | --- |
| `E3-UI-and-HUD-Revamped-E32014UIandHUD_Revamped_MagicSpellsPatch.zip` | Skip. Only relevant if Magic Spells is installed. User explicitly did not want this patch without Magic Spells. |
| `E3.2014.UI.and.HUD.Revamped.-.Magic.Spells.Patch.zip` | Skip. Same reason. |
| `Friendly HUD Compatibility Patch-10256-*` | Skip. We are using W3EE-integrated Friendly HUD hooks, not standalone Friendly HUD as a separate UI owner. |
| `Vlad UI Compatibility Patch-10256-*` | Skip. We are not using Vlad UI as the selected HUD owner. |
| `E3-UI-and-HUDRevamped_NudelPatch_AQOOMPatch` / AQOOM patch variants | Skip. Standalone AQOOM is not installed; current AQOOM-style behavior is W3EE-integrated. |
| Extra `Better Icons Patch` archives from the GitHub release | Skip unless a specific UI symptom points back here. The current Better Icons W3EE package and prior manual fixes are launch-tested. |

## Guardrail

Compatibility patches are only safe when their target UI owner is active. In this stack:

- E3 HUD is active.
- W3EE Redux compatibility layer is active.
- Better Icons W3EE is active.
- Standalone Vlad UI, standalone Friendly HUD, standalone AQOOM, and Magic Spells are not active.

Do not install patches for inactive UI owners just because they mention E3 or Better Icons.
