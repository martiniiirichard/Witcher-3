# Decision: Skip E3 Combat Cam Shake / CCS (5736)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/5736
Archive: `C:\Users\marti\Downloads\CCS-5736-1-0-1621602618.rar`

## Decision

Skip.

## Why

The Nexus page identifies this as E3 Combat Cam Shake, a configurable combat camera-shake mod.

The archive is not a simple camera config package. It includes:

- `Mods/mod_CCS/content/scripts/game/gameplay/damage/damageManagerProcessor.ws`
- `Mods/mod_CCS/content/scripts/game/player/r4Player.ws`
- `Mods/mod_CCS/content/scripts/local/CSS.ws`
- `bin/config/r4game/user_config_matrix/pc/CCS.xml`

`r4Player.ws` and `damageManagerProcessor.ws` are high-risk script lanes in the current W3EE Redux, Brothers in Arms, Reflex, E3 HUD, and combat/effects stack. The stack already has camera and immersion behavior configured, so the value is not worth the merge risk.

## Status

No live game files changed.
