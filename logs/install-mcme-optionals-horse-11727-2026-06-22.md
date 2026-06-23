# MCME Optionals and Horse Riding 11727

Installed: 2026-06-22

Sources:
- MCME optionals: https://www.nexusmods.com/witcher3/mods/3287
- Horse Riding For Companions: https://www.nexusmods.com/witcher3/mods/11727

Archives:
- `Enable_Collisions-3287-4-0-6-1772743803.zip`
- `Extended_Cerys_Romance-3287-4-0-4-1688098207.zip`
- `Horse Riding For Companions-11727-1-0-0-1768583997.rar`

Installed changes:
- Replaced `mods/modSpawnCompanions/content/scripts/game/SpawnCompanionsSCMCC.ws` with the Enable Collisions optional file.
- Replaced `DLC/DLCmod_spawn_companions/content/blob0.bundle` and `metadata.store` with the Extended Cerys Romance optional DLC content.
- Added `mods/modnpcrideshorse`.
- Added `[modnpcrideshorse]` to `mods.settings` at priority `52`.

Validation:
- Game launched and user confirmed pass.

Deferred:
- Corvo Bianco NPC Relocation.
- Corvo Bianco NPC Sleeping Arrangement.

Notes:
- This subset did not create duplicate `.ws` paths outside MCME itself.
- Horse Riding For Companions requires MCME 4.0.6 and is bundle-only in this install, so it did not need Script Merger.
- Corvo Bianco relocation and sleeping arrangement are mutually exclusive variant patches and should be selected separately.
