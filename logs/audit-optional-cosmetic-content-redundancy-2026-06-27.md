# Audit: Optional Cosmetic / Flavor Content Redundancy

Date: 2026-06-27

## Goal

Review the active low-risk flavor mods previously marked as "future trim only if needed." These are not core systems, but they can still be legitimate map, estate, ship, outfit, or NPC appearance payloads.

## Result

No removal action recommended right now.

These mods are optional from a gameplay perspective, but they are not dead shells.

## Current Read

| Mod | Current evidence | Recommendation |
| --- | --- | --- |
| `modAdditionalArmorStandsNoUni` | 2 indexed bundled assets, both currently winning. | Keep. Corvo/display-room enrichment and not shadowed. |
| `modMorgueLightsFix` | 6 of 7 indexed bundled assets winning; one overlap loses to `modBoatRaces`. | Keep. Mostly active small visual fix. |
| `modLampOnPlayersBoat_NoCityLight` | 5 of 6 indexed bundled assets winning; one overlap loses to `modBoatRaces`. | Keep. Mostly active boat lighting flavor. |
| `modredanianroyalship` | 43 of 44 indexed bundled assets winning; one overlap loses to `modmanticor`. | Keep. Large active content payload. |
| `modBaratheon` | 3 indexed bundled assets, all winning. | Keep. Active Tailory option. |
| `modZ_GrammarOfThePath` | String-only polish package. | Keep unless the naming/string stack feels too noisy. |
| `modViola`, `modSuzy`, `modNarcissa1`, `modBertha1`, `modTouCourt1` | Small active appearance-content bundles; selected variants were documented during the Brothel/Addicted pass. | Keep unless we intentionally simplify NPC appearance variants. |
| `modLessIndignantNPCs` | One active script. | Keep. Not a shell; should be reviewed only if NPC reaction behavior feels off. |
| `modDandelionScarfFix` | Already disabled and physical folder is missing from active `mods`. | No action. Previously handled. |

## Rule

This group is a good future trim list only if we need to reduce loader pressure or visual clutter. It is not a cleanup batch today.
