# Assessment - UI Sound Effects Cleaning and Redesign 6421

Date: 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/6421?tab=description`
- Local download found:
  - `C:\Users\marti\Downloads\Less Is More tweaked-6421-1-1-1645636423.zip`

## Finding

The downloaded file is not the main UI sound effects redesign package. It is an optional `Less Is More` timing variant:

- `modLessIsMore_Tweaked\content\scripts\engine\sound.ws`

The main UI sound redesign asset archive was not found in Downloads during this pass.

## First Attempt

Temporarily copied the tweaked `sound.ws` over the active installed file:

`Mods\modLessIsMore\content\scripts\engine\sound.ws`

The tweak changes Less Is More timing from:

```witcherscript
default lim_playDuration = 600.0;
default lim_muteDuration = 180.0;
```

to:

```witcherscript
default lim_playDuration = 240.0;
default lim_muteDuration = 360.0;
```

It still included the W3EE sound-threat hooks:

- `useSoundValue`
- `sound_threat_settings.csv`

## First Rollback

The Codex smoke process exited during the compile window, so the optional tweak was rolled back to the previously working Less Is More script from:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\less-is-more-tweaked-6421-20260623-174701`

Current active values are again:

```witcherscript
default lim_playDuration = 600.0;
default lim_muteDuration = 180.0;
```

The user later reported the game loaded, confirming the restored known-good Less Is More state is working.

## Outcome

This first attempt left no active 6421 changes.

## Applied On Request

The user later explicitly asked to apply 6421. The same optional tweak was applied again, this time intentionally kept after a clean smoke test.

Active file replaced:

`Mods\modLessIsMore\content\scripts\engine\sound.ws`

Current active timing:

```witcherscript
default lim_playDuration = 240.0;
default lim_muteDuration = 360.0;
```

This means:

- 4 minutes music on
- 6 minutes music off

The script still includes W3EE sound-threat hooks:

- `useSoundValue`
- `sound_threat_settings.csv`

Backup for the final applied state:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\less-is-more-tweaked-6421-applied-20260623-175040`

Verification:

- DX12 compile smoke passed: `witcher3.exe` stayed alive after 45 seconds.
- Test process was closed after verification.

Safe current state:

- Keep `modLessIsMore` from mod 3684 installed.
- Its active `sound.ws` now uses the 6421 tweaked timing.

Need the main UI sound redesign archive before assessing the actual 6421 UI sound replacement.
