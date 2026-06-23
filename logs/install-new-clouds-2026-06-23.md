# Install - New Clouds - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/3315`
- File ID: `48434`
- Archive: `C:\Users\marti\Downloads\New Clouds 3.0-3315-3-0-1680189337.rar`

## Assessment

`New Clouds` is a visual texture replacer. The downloaded archive contains:

- `modNewClouds3_0\content\blob0.bundle`
- `modNewClouds3_0\content\metadata.store`
- `modNewClouds3_0\content\texture.cache`

It contains no scripts, XML menu files, or config files.

The active stack already includes several weather/lighting mods, so the install order should allow `New Clouds` to win cloud texture conflicts. It was installed after the current weather and testing-helper priorities.

## Installed

- `modNewClouds3_0`

`mods.settings` backup:

- `C:\Games\The Witcher 3\mods.settings.codex-backup-new-clouds-20260623-145408`

Priority:

- `modNewClouds3_0`: `157`

## Verification

Static verification:

- Installed folder exists.
- Contains `0` `.ws` script files.
- Contains `0` `.xml` menu files.
- Contains `1` `texture.cache`.
- No Script Merger run was required.

## Pending

Needs visual smoke testing in a few weather states, especially clear, cloudy, storm/rain, and Skellige winter conditions.
