# Safe Batch: Mirror Reward + Memory Of Making Love - 2026-06-26

## Installed

### Master Mirror Reward - BiA Patch

Archive:

- `C:\Users\marti\Downloads\modMirrorReward_BiA3-6499-2-3c-1770519583.zip`

Installed folder:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\mod0MirrorReward_BiA3`

Payload:

- `content\blob0.bundle`
- `content\metadata.store`

Risk:

- Low. Bundle-only, no scripts.
- Installed as a BiA-specific reward patch and placed at priority `3` so it can win over broad BiA content when paths overlap.

### Memory Of Making Love

Archive:

- `C:\Users\marti\Downloads\memoryofmakinglove-9089-2-4a-1770653991.zip`

Installed folders:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modMemoryOfMakingLove`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\DLC\dlcmemoryofmakinglove`

Payload:

- `modMemoryOfMakingLove\content\scripts\local\memoryofmakinglove.ws`
- `dlcmemoryofmakinglove\content\blob0.bundle`
- `dlcmemoryofmakinglove\content\metadata.store`

Script notes:

- Adds wrappers to `W3EyeOfLoki.OnUsed` and `W3EyeOfLoki.OnHidden`.
- Adds quest helper functions for memory scene checks/teleport return.
- Adds saved fields/method to `CR4Player` for recording and returning to the player's previous location.
- Does not duplicate an existing active `.ws` path, so Script Merger is not expected to create a merge for it.

Risk:

- Medium-low. It is a standalone local script, not a broad override, but it still requires a launch compile check.

## Settings

Added to:

- `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`

Entries:

```ini
[mod0MirrorReward_BiA3]
Enabled=1
Priority=3

[modMemoryOfMakingLove]
Enabled=1
Priority=263
```

## Backups

- `backups\mirror-reward-bia3-6499-20260626-135121`
- `backups\memoryofmakinglove-9089-20260626-135244`

## Verification

- Confirmed installed folders exist.
- Confirmed `mod0MirrorReward_BiA3` has zero scripts.
- Confirmed `modMemoryOfMakingLove` has one active script: `local\memoryofmakinglove.ws`.
- No Script Merger cleanup is expected for this batch.
- DX12 launch/compile smoke test passed: `witcher3.exe` remained running after ~55 seconds and was then closed.

## Deferred From This Pass

- `BGMv3 mixed Ver 2-9028-2-1713517286.zip`: deferred because earlier grass audit warned against old grass visual mods on top of the current modern foliage stack.
- `Kaer Morhen Armory Rubble Removed-5813-1-2-1708274171.rar`: deferred because the Kaer Morhen area is already owned by multiple world/layout mods and should be reviewed selectively.
- `Benis Toussaint Lighting Overhaul-11820-1-1-4-5-1770077045.rar`: deferred because the lighting/weather stack is already complex and this should be handled as a visual pass, not a quick safe install.
