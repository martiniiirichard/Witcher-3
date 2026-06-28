# Decision: Skip Smooth Camera Motion (7155)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/7155
Archive: `C:\Users\marti\Downloads\Smooth Camera Motion-7155-1-0-1670978942.rar`

## Decision

Skip.

## Why

The archive ships a full replacement for:

- `modSmoothCameraMotion/content/scripts/game/player/player.ws`

That script path is too broad for a small camera polish change in the current stack. Camera behavior is already governed by W3EE and Immersive Cam settings, and we have a documented preferred immersive camera profile.

Only revisit this if there is a specific camera motion complaint that cannot be solved through the existing Immersive Cam options.

## Status

No live game files changed.
