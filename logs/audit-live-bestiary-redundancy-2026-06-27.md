# Audit: Live Bestiary Redundancy

Date: 2026-06-27

Question:

- Is `modLiveBestiary` redundant because its original script is disabled and E3 HUD owns the bestiary menu?

Result:

- Keep it while the Live Bestiary feature is desired.

Active settings:

| Mod | Enabled | Priority |
| --- | --- | --- |
| `modLiveBestiary` | `1` | `130` |

Current payload:

- `Mods\modLiveBestiary\lbTable.csv`
- `Mods\modLiveBestiary\content\blob0.bundle`
- `Mods\modLiveBestiary\content\metadata.store`
- `Mods\modLiveBestiary\content\scripts.disabled-by-codex\game\gui\menus\glossaryBestiaryMenu.ws`
- `DLC\DLCLiveBestiary\content\dlc\globals\lbTable.csv`

Compatibility strategy:

- The original Live Bestiary script is intentionally disabled.
- `mod0_E3HUD_W3EER_NG\content\scripts\game\gui\menus\glossaryBestiaryMenu.ws` owns the active E3/W3EE-compatible bestiary menu behavior.
- That active script reads `LoadCSV( "dlc\globals\lbTable.csv" )`.
- `DLCLiveBestiary\content\dlc\globals\lbTable.csv` supplies that virtual path without creating malformed direct children under the game `DLC` root.
- Current `dx12user.settings` has `livebestiray=true`, matching the E3 HUD typo used by the script/config.

Conclusion:

This is an intentional compatibility split. `modLiveBestiary` is not a script owner in the current stack; it is the data/content layer feeding the E3/W3EE-compatible bestiary path.
