# Corvo Bianco MCME Variants

Installed: 2026-06-22

Source:
- https://www.nexusmods.com/witcher3/mods/3287

Archives:
- `CorvoBianco_NPC_Relocation-3287-4-0-4-1688097859.zip`
- `CorvoBianco_NPC_Sleeping_Arrangement-3287-4-0-5-1764309347.zip`

Selected variants:
- NPC relocation: `Baron - Dettlaff - Priscilla - Sorceresses - Syanna / Replace Yennefer with Syanna`
- Sleeping arrangement: `Yennefer as the love interest / Yennefer in the master bedroom - Ciri in the guest bedroom`

Installed changes:
- Replaced `mods/modSpawnCompanions/content/scripts/game/mcm/job/MultiCompanionModNPCManager.ws`.
- Replaced `mods/modSpawnCompanions/content/scripts/game/mcm/job/MultiCompanionModJobManager.ws`.

Validation:
- Game launched and user confirmed pass.

Notes:
- These two patch files are mutually exclusive variant choices, not cumulative folders.
- The sleeping arrangement archive produced a stale/unopenable extracted path under the long repo staging folder. Re-extracting to a short temp path allowed the selected file to copy cleanly.
- No duplicate script paths outside `modSpawnCompanions`, so Script Merger was not required.
