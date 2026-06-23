# Install - Restored Content - Ciri's Fate - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/8152`
- File ID: `67533`
- Archive: `C:\Users\marti\Downloads\Ciri's Fate-8152-3-0-1-1764655192.zip`

## Assessment

`Restored Content - Ciri's Fate` restores late-game Ciri/Tedd Deireadh related content. This is a story/quest content mod, so the risk profile is higher than visual-only mods even though it contains no scripts.

The downloaded archive contains:

- `mods\modswallow`
- `dlc\dlcswallow`

It contains no `.ws` script files and no `.xml` menu files.

Install instructions indicate the mod should have priority. Known compatibility notes from the page are favorable for Brothers in Arms, but unknown compatibility remains for mods editing `q502_avallach` or Tedd Deireadh quest files.

## Installed

- `modswallow`
- `dlcswallow`

`mods.settings` backup:

- `C:\Games\The Witcher 3\mods.settings.codex-backup-ciris-fate-20260623-150429`

Priority:

- `modswallow`: `162`

## Verification

Static verification:

- Installed mod and DLC folders exist.
- `modswallow` contains `0` `.ws` script files.
- `modswallow` contains `0` `.xml` menu files.
- No Script Merger run was required.

## Pending

Needs launch smoke testing.

Functional validation requires a save near the relevant late-game Ciri/Tedd Deireadh content path. If issues appear there, inspect conflicts involving `q502_avallach` and Tedd Deireadh quest bundle assets.
