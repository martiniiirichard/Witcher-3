# Less Music 9358 Install

Source: https://www.nexusmods.com/witcher3/mods/9358

## Files

- Download: `C:\Users\marti\Downloads\Less music-9358-4-1721417234.rar`
- Installed mod: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modLessmusic`
- Active settings file: `C:\Games\The Witcher 3\mods.settings`
- Backup: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\less-music-9358-20260623-175621`

## Decision

Installed `modLessmusic` as the active music-control mod and disabled `modLessIsMore`.

Reason: both mods override `content\scripts\engine\sound.ws`, so stacking them would leave Script Merger/game load order deciding the winner. Keeping `modLessIsMore` installed but disabled gives a clean rollback to the previous 6421 Less Is More setup.

Current active settings:

```ini
[modLessIsMore]
Enabled=0
Priority=173

[modLessmusic]
Enabled=1
Priority=175
```

## Compatibility Notes

The downloaded 9358 `sound.ws` preserves the W3EE sound-threat hooks that matter for this setup:

- `useSoundValue`
- `sound_threat_settings.csv`
- `UpdateThreatDamp`
- double-handed sword behavior driven by threat rating

The behavior difference from the prior active Less Is More 6421 tweak:

- Previous active timing: `lim_playDuration = 240.0`, `lim_muteDuration = 360.0`
- New active timing: `lim_playDuration = 600.0`, `lim_muteDuration = 600.0`
- Combat/monster hunt states are mapped to exploration music while music is active, then silence while muted.

## Verification

- DX12 compile smoke passed.
- The game process stayed running after 45 seconds and was then stopped manually by Codex.

## Rollback

If this feels worse in-game, disable `modLessmusic` and re-enable `modLessIsMore` in `mods.settings`.
