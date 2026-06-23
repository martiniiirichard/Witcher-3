# Fix - New Lightning FX Debug Overlay

Date: 2026-06-23

## Symptom

An in-game parchment notification stayed visible with debug text such as:

- `Weather Infos`
- `World Positions`
- `Mod Menu Settings`
- `Debug Mode: true`

## Cause

`New Lightning FX` was running with debug options enabled in:

`C:\Games\The Witcher 3\dx12user.settings`

The active section had:

```ini
[NewLightningFX]
modDebugInfo=true
modDebugMode=true
```

## Fix

Created a timestamped backup of `dx12user.settings`, then changed only the debug flags:

```ini
[NewLightningFX]
modDebugInfo=false
modDebugMode=false
```

The mod itself remains enabled:

```ini
modStatus=true
modAllowStrike=true
modReactions=true
modCameraShake=true
```

## Note

This can also be changed in-game through:

`Options > Mods > New Lightning FX`

Use the recommended preset or manually disable `Debug Info` and `Debug Mode`.
