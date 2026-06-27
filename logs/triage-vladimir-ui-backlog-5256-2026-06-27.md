# Vladimir UI Backlog Triage - 5256

Date: 2026-06-27

## Result

Do not install the 5256 backlog files into the current stack.

Vladimir UI is a full alternate UI owner. The current selected UI owner is E3 HUD with the W3EE Redux compatibility layer:

- `modE3HUD`
- `mod0_E3HUD_W3EER_NG`
- `modBetterIcons2025_NextGen_W3EE`

## Skip

| Download | Decision |
| --- | --- |
| `Vladimir UI (For 4.04-NextGen)` | Skip. Full UI stack replacement; conflicts with the selected E3 HUD direction. |
| `W3 Enhanced Edition Patch` | Skip. Patch is for Vladimir UI + W3EE, not E3 HUD + W3EE Redux. |
| `Gwent Redux - Patch for Vladimir UI` | Skip. Gwent Redux is installed, but this patch targets Vladimir UI, which is not installed. |
| `Gwent Redux - Vanilla Spy Effect - Patch for Vladimir UI` | Skip. Same reason. |
| `Extra Skill Slots and Mutations Patch` | Skip in this package context. `modExtraSkillSlotsNextGen` is already installed and fixed through its own W3EE-compatible adjustments; this 5256 patch is part of the Vlad UI ecosystem. |
| `Main Menu Background Replacer` | Skip for now. Large cosmetic menu replacement from the Vlad UI lane; revisit only if we intentionally redesign the main menu presentation. |

## Guardrail

Do not mix full HUD/UI owners casually. E3 HUD and Vladimir UI both want to own large SWF/UI surfaces. Patches from one UI stack should not be applied to the other unless we are doing a deliberate manual port.
