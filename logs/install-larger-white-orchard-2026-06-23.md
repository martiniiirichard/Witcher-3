# Install - Larger White Orchard - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/9022`
- File ID: `56064`
- Archive: `C:\Users\marti\Downloads\Larger White Orchard (1.32)-9022-1-01-1718911610.7z`

## Assessment

`Larger White Orchard` is a terrain/world visual mod. The archive name includes `1.32`, but the Nexus file entry is tagged as Next-Gen compatible.

The downloaded archive contains:

- `modLargerWhiteOrchard\content\blob0.bundle`
- `modLargerWhiteOrchard\content\buffers0.bundle`
- `modLargerWhiteOrchard\content\texture.cache`
- `modLargerWhiteOrchard\content\metadata.store`

It contains no scripts, XML menu files, or config files.

The active stack already includes tree/LOD and world visual mods, so the main risk is visual/worldspace overlap rather than compile failure. It was installed late so its White Orchard-specific assets can win.

## Installed

- `modLargerWhiteOrchard`

`mods.settings` backup:

- `C:\Games\The Witcher 3\mods.settings.codex-backup-larger-white-orchard-20260623-150001`

Priority:

- `modLargerWhiteOrchard`: `160`

## Verification

Static verification:

- Installed folder exists.
- Contains `0` `.ws` script files.
- Contains `0` `.xml` menu files.
- Contains `1` `texture.cache`.
- No Script Merger run was required.

## Pending

Needs visual/worldspace smoke testing in White Orchard.
