# Ice Breath Backlog Triage - 1257 / 4138 / 7302

Date: 2026-06-27

## Result

No new install action is recommended.

The active Ice Breath path is the newer Next Gen mod:

- `modIceBreath`
- `DLCIceBreath`
- `IceBreath.xml`
- shared Bootstrap registry entry: `modCreate_CIceBreathMod()`

## Active / Keep

| Mod | Reason |
| --- | --- |
| Ice Breath Next Gen 7302 | Current active implementation. Includes dialogue/cutscene handling and weather support for Skellige Winter Weather, Realistic Weather, Immersive Lighting, and More Variable Weather. |

## Skip / Legacy Or Superseded

| Download | Decision |
| --- | --- |
| `Ice Breath Menu v2.0.3-1257-*` | Skip. Older/base menu line; active Next Gen package already installed and registered `IceBreath.xml`. |
| `playerWitcher.ws IceBreath_AMM merge 1.30 and above-1257-*` | Skip. Old direct `playerWitcher.ws` merge file is unsafe in the current W3EE/AMM/merged stack. |
| `DLC Ice-1257-*` | Skip. Current active DLC is `DLCIceBreath` from the Next Gen package. |
| `Skellige Snow Weather-1257-*` | Skip unless doing a dedicated weather pass. Current weather stack already has newer Skellige winter/weather handling. |
| `Skellige Ice Breath Compatibility - Next Gen-4138-*` | Skip. Older compatibility patch would replace the current 1.06 Ice Breath script with an older/smaller file and risk losing newer behavior. |

## Guardrail

Do not downgrade Ice Breath to an older `1257`/`4138` script. If Ice Breath breaks later, patch the active `7302` implementation or the Bootstrap registry rather than replacing it with a legacy `playerWitcher.ws` merge.
