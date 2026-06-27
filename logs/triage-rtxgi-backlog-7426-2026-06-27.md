# RTXGI / RT Settings Backlog Triage - 7426

Date: 2026-06-27

## Result

No new install action is recommended for the remaining 7426 downloads.

The useful dependency piece was already installed:

- RTXGI unlocker DLL from `RTXGI unlocker and setting auto-updater-7426-4-04c-1739728925(1).zip`

## Active / Keep

| Item | State |
| --- | --- |
| RTXGI unlocker DLL | Installed earlier. Required by several RT/RTXGI override mods. |
| `bin\config\platform\pc\RT_ImprovedReflectionsAndShadows.ini` | Installed from Improved RT Reflections and Shadows 8865. |
| `bin\config\platform\pc\BlueFix_RTXMirrors.ini` | Installed from Ray Bleach 8890. |

## Skip / Do Not Apply Automatically

| Download | Decision |
| --- | --- |
| `Complete RT Ultra dx12user.settings-*` | Skip for now. This is a full DX12 graphics preset and would overwrite many local performance/visual choices. |
| Duplicate RTXGI unlocker archives | Already installed. No action. |

## Guardrail

Treat `dx12user.settings` presets as graphics-profile changes, not normal mod installs. Apply them only when deliberately tuning performance/visuals, with a backup and a before/after launch check.
