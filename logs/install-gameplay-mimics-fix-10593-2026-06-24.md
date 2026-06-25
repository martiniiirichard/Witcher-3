# Gameplay Mimics Fix 10593

Source: https://www.nexusmods.com/witcher3/mods/10593

Installed archive:
- `C:\Users\marti\Downloads\Gameplay Mimics Fix-10593-2-1-1772495836.zip`

Installed files:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modGameplayMimicsFix`

Settings:
- `[modGameplayMimicsFix]`
- `Enabled=1`
- `Priority=251`

Disabled old package:
- `mods\modEnableMimics_blinking` -> disabled with `disabled-by-codex-replaced-by-10593` suffix
- `DLC\DLCEnableMimics` -> disabled with `disabled-by-codex-replaced-by-10593` suffix
- `[modEnableMimics_blinking]` left in both `mods.settings` files but set to `Enabled=0`, `Priority=174`

Reasoning:
- Nexus page describes version `2.0` as merge-free via annotations.
- The old active `modEnableMimics_blinking` package shipped full base script replacements (`actor.ws`, `npc.ws`, `player.ws`) plus a scene/DLC trigger for mimics/high-resolution shadows.
- The new mod is a single annotation script and explicitly separates mimic fixes from high-resolution shadows, reducing script replacement risk.

Expected behavior:
- Fixes facial mimics wrongly applied to dead bodies.
- Adds blinking animations to NPCs in gameplay.
- Adds missing Geralt blinking after spawn-like states.

Verification:
- DX12 smoke test passed: game stayed running after 45 seconds.
- No Script Merger pass required.

Future note:
- Prefer annotation rewrite mods over old full script replacement packages when they cover the same behavior.
- If a future mod expects the old `DLCEnableMimics` scene trigger, this replacement choice should be revisited, but current active mod stack should not need it.
