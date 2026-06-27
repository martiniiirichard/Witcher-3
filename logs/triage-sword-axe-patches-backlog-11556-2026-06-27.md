# Sword and Axe Compatibility Patch Backlog Triage - 11556

Date: 2026-06-27

## Result

No new install action is recommended.

The useful compatibility pieces from 11556 were already applied and fixed:

- `Sword and Axe and Extra Skill Slots`
- `Sword and Axe and Extra-REDUX gwent patch`

## Active / Keep

The current Time of the Sword and Axe integration is launch-safe because prior fixes:

- disabled duplicate/incompatible Expansion Zero local scripts
- added missing Sword/Axe effect enum values to active higher-priority effect type owners
- ported minimal drinking-system hooks into active W3EE/merged script owners

## Skip

| Download | Decision |
| --- | --- |
| `inventoryComponent-11556-*` | Skip. `inventoryComponent.ws` is a hot core file currently owned by `mod0000_MergedFiles` with W3EE/BiA/Shades/Gwent compatibility. Do not replace it raw. |
| `Basic Cooking Recipes patch-11556-*` | Skip. Basic Cooking is now installed, but this patch only targets `alchemyTypes.ws`; W3EE owns that script lane. Apply only if a specific Basic Cooking + ToSA error appears and we manually graft the needed delta. |

## Guardrail

For Time of the Sword and Axe patches, prefer selective hook ports over raw script replacement. Treat `inventoryComponent.ws`, `playerWitcher.ws`, `r4Player.ws`, `PlayerAbilityManager.ws`, `alchemyTypes.ws`, and `effectTypes.ws` as high-risk.
