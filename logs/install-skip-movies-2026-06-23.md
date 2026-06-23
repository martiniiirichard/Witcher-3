# Install - Skip Movies - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/358`
- File ID: `42626`
- Archive: `C:\Users\marti\Downloads\SkipMovies-358-4-0-1671032845.zip`

## Assessment

This is useful testing infrastructure because it reduces time spent waiting through startup and recap movie flows.

It overlaps conceptually with `moddisablestorybooks`, but is not fully redundant:

- `moddisablestorybooks` is an asset/bundle mod for storybook recap skipping.
- `modSkipMovies` replaces startup/recap movie menu scripts:
  - `game\gui\main_menu\mainRecapMoviesMenu.ws`
  - `game\gui\main_menu\mainStartupMoviesMenu.ws`

No currently installed mod was found overriding those two script files.

## Installed

- `modSkipMovies`

`mods.settings` backup:

- `C:\Games\The Witcher 3\mods.settings.codex-backup-skip-movies-20260623-144841`

Priority:

- `modSkipMovies`: `156`

## Verification

Static verification:

- Installed folder exists.
- Contains `2` `.ws` files.
- Contains `0` `.xml` menu files.
- Only `modSkipMovies` currently owns `mainRecapMoviesMenu.ws` and `mainStartupMoviesMenu.ws`.
- No Script Merger run was required based on current script ownership.

## Launch Test

User confirmed both storybook and movie skipping are fixed after install.

Expected ongoing benefit is faster startup and load-game testing flow.
