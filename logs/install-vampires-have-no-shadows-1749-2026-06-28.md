# Vampires Have No Shadows Install - 2026-06-28

Source: https://www.nexusmods.com/witcher3/mods/1749

Archive: `C:\Users\marti\Downloads\Vampires Have No Shadows - Next Gen-1749-1-43-1686041717.zip`

Installed folder: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modVampiresHaveNoShadows`

`mods.settings` entry:

```ini
[modVampiresHaveNoShadows]
Enabled=1
Priority=268
```

## Integration Decision

The archive ships a full `content\scripts\game\npc\npc.ws`, which is a hot file already owned by the current W3EE/BiA/merged stack. Do not let that raw file become the winner.

Safe install pattern used:

- keep the mod's unique helper script, `content\scripts\local\vampireChecker.ws`
- keep the mod enabled so the helper compiles
- leave `mod0000_MergedFiles` as the active `npc.ws` owner
- manually graft the small call into active merged `npc.ws` after the existing `NoShadows` ability check

Grafted call:

```witcherscript
// Vampires Have No Shadows
if( ShouldCastNoShadow( this ) )
{
    SetGroupShadows( false );
}
```

The helper removes shadows for vampires, specters, and named vampire/specter-adjacent cases such as katakan, ekimma/ekkima, bruxa, alp, fleder, garkain, graveir/gravier, Dettlaff, Regis, Oriana, ghosts, wraiths, and barghests.

Backup created before live edits:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\vampires-no-shadows-1749-20260628-010152`

## User Decisions Recorded

The same pass marked these backlog candidates as avoided:

- Roach Gwent Card for Everyone
- Well Stocked Craftsmen
- Blood Trails
- Richer Merchants

## Verification

Passed:

- `modVampiresHaveNoShadows\content\scripts\local\vampireChecker.ws` is present.
- `mod0000_MergedFiles\content\scripts\game\npc\npc.ws` contains the grafted `ShouldCastNoShadow( this )` call.
- `mods.settings` contains the enabled priority `268` entry.
- DX12 launch/compile smoke survived 55 seconds with the process responding.

Optional later check:

- in-game visual spot check against a vampire or specter
