# Audit: AMM Stack Redundancy

Date: 2026-06-27

Question:

- Can `modAMM` or `mod00AMMW3EEReduxNG139b` be removed as redundant?

Result:

- Keep both.

Active settings:

| Mod | Enabled | Priority |
| --- | --- | --- |
| `mod00AMMW3EEReduxNG139b` | `1` | `15` |
| `modAMM` | `1` | `17` |

Installed supporting assets:

- `DLC\DLCAMM`
- `DLC\DLCAMMHORSE`
- `bin/config/r4game/user_config_matrix/pc/AMM.xml`
- `bin/config/r4game/user_config_matrix/pc/AMMRoach.xml`

Live `modAMM` payload:

- 6 active script files.
- 15 localization string files.
- Bundled content/metadata files.

Why this is not redundant:

- `modAMM` is the base Appearance Menu Mod implementation and provides the actual appearance menu feature.
- `mod00AMMW3EEReduxNG139b` is the W3EE Redux compatibility player script layer.
- Prior fixes manually patched AMM/W3EE mutation, horse rest, and combat sword issues.
- Tailory, New Hairstyles, Shades of Iron, and Swords on Roach were grafted into the active AMM scripts/menu XML instead of overwriting AMM wholesale.

Conclusion:

Do not remove AMM or its W3EE Redux patch as cleanup. This pair is a high-value but high-touch compatibility stack.
