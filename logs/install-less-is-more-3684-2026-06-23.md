# Install - Less Is More 3684

Date: 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/3684?tab=description`
- Installed archive: `C:\Users\marti\Downloads\Less Is More Next Gen-3684-4-1671742956.zip`

## Installed

- `Mods\modLessIsMore`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modLessIsMore]
Enabled=1
Priority=173
```

## Compatibility Check

This mod overrides:

- `content\scripts\engine\sound.ws`

The only existing active mod touching this file was:

- `modW3EE`

The downloaded Next-Gen `sound.ws` already includes the W3EE sound-threat additions, including:

- `useSoundValue`
- `sound_threat_settings.csv`
- W3EE monster sound weighting logic

Because of that, it was installed as a high-priority override rather than manually patching `modW3EE`.

## Behavior

The shipped Next-Gen preset is:

- 10 minutes music on
- 3 minutes music off

Controlled by:

```witcherscript
default lim_playDuration = 600.0;
default lim_muteDuration = 180.0;
```

## Backup

Created:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\less-is-more-20260623-173707`

Also created a timestamped `mods.settings` backup.

## Verification

- Static check confirmed `lim_` toggle logic is present.
- Static check confirmed W3EE `useSoundValue` / `sound_threat_settings.csv` logic is preserved.
- DX12 compile smoke passed: `witcher3.exe` stayed alive after 45 seconds.
- Test process was closed after verification.
