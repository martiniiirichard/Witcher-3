# Audit: Kaer Morhen And Verna Redundancy Status

Date: 2026-06-27

## Kaer Morhen World Overhaul Entries

Checked `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings` and the live `Mods` folder.

Current matching settings entries:

| Entry | Enabled | Live folder exists? |
| --- | --- | --- |
| `mod_KaerMorhenEnhanced` | `0` | No |
| `modkaermorhensbastionrestoredtoitsancientsplendor` | `0` | No |
| `modkaermorhenrestoredtoitsancientsplendor` | `0` | No |
| `modkaer_morhen_extended` | `0` | No |
| `modKMArmoryRubbleRemoved` | `0` | No |

Conclusion:

No live cleanup action is needed. These are disabled historical settings entries only. Prior logs record that Kaer Morhen Extended caused content-load/no-window startup hangs and was rolled back.

## Shrines Of Verna

Current matching settings entries:

| Entry | Enabled | Priority |
| --- | --- | --- |
| `modVernaShrine_Everlasting` | `1` | `230` |
| `modshrinesofverna` | `1` | `233` |

Live payload:

- `DLC\dlcshrinesofverna` exists and carries bundled world/localization assets.
- `Mods\modshrinesofverna` exists and carries bundled assets plus scripts.
- `Mods\modVernaShrine_Everlasting` exists and carries `content\scripts\local\effects\vitalityRaise.ws`.

Compatibility split:

- `modshrinesofverna\content\scripts\local\vitalityRaise.ws` is disabled as `vitalityRaise.ws.disabled-by-codex-everlasting-wins`.
- `modshrinesofverna\content\scripts\local\vernaShrine.ws` is disabled as `vernaShrine.ws.disabled-by-codex-tosa-owns`.
- `modVernaShrine_Everlasting` owns the improved vitality effect behavior.
- Time of the Sword and Axe owns the shrine interaction class.
- Shrines of Verna keeps world/content/localization assets.

Conclusion:

Keep the Verna pair. It is a deliberate compatibility split, not duplicate clutter.
