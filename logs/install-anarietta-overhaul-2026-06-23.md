# Install - Anna Henrietta Overhaul - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/11636`
- File ID: `68200`
- Archive: `C:\Users\marti\Downloads\AnariettaOverhaul-11636-1-1-1-1766866072.zip`

## Assessment

`Anna Henrietta Overhaul` is a Blood and Wine NPC appearance/texture/model mod.

The downloaded archive contains:

- `modanariettaoverhaul\content\blob0.bundle`
- `modanariettaoverhaul\content\buffers0.bundle`
- `modanariettaoverhaul\content\collision.cache`
- `modanariettaoverhaul\content\metadata.store`
- `modanariettaoverhaul\content\texture.cache`

It contains no scripts, XML menu files, or config files.

## Current Stack Note

`mods.settings` already contained:

- `modAnarietta_plus`, priority `58`

But no matching installed folder exists under the game `Mods` directory. This appears to be a stale settings entry from an older/previous Anna Henrietta appearance mod.

The stale entry was left in place during this pass to avoid unrelated cleanup while installing the new linked archive.

## Installed

- `modanariettaoverhaul`

`mods.settings` backup:

- `C:\Games\The Witcher 3\mods.settings.codex-backup-anarietta-overhaul-20260623-153129`

Priority:

- `modanariettaoverhaul`: `166`

## Verification

Static verification:

- Installed folder exists.
- Contains `0` `.ws` script files.
- Contains `0` `.xml` menu files.
- Contains `1` `texture.cache`.
- No Script Merger run was required.

## Pending

Needs visual smoke testing on Anna Henrietta in Blood and Wine scenes.

Later cleanup candidate:

- Remove or disable stale `modAnarietta_plus` entry from `mods.settings` if confirmed unused.
