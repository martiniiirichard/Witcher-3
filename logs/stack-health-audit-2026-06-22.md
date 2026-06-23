# Stack Health Audit

Date: 2026-06-22

Result:
- Repository clean before audit: `main...origin/main`.
- `mods.settings` section count: 106.
- Duplicate `mods.settings` sections: none.
- Duplicate priorities: none.
- Missing priority numbers: none.
- Max priority: 106.

Safety disables verified:
- BASE `quest_function.ws` is disabled as `quest_function.ws.disabled-by-codex`.
- `modSpawnCompanions` `r4Player.ws` is disabled as `r4Player.ws.disabled-by-codex`.
- `modSpawnCompanions` `npc.ws` is disabled as `npc.ws.disabled-by-codex`.

Critical merged files verified:
- `mod0000_MergedFiles/content/scripts/game/player/r4Player.ws`
- `mod0000_MergedFiles/content/scripts/game/npc/npc.ws`
- `mod0000_MergedFiles/content/scripts/game/components/inventoryComponent.ws`
- `mod0000_MergedFiles/content/scripts/game/vehicles/vehicleComponent.ws`

Known active duplicate script paths:
- Existing W3EE/BiA/Shades/AMM/E3HUD/BetterIcons/NobsReflex conflicts remain present by design.
- Key broad conflicts are covered by `mod0000_MergedFiles` or earlier manual patches.
- No new appearance-batch-specific active duplicate script paths were found.

Other checks:
- `dinput8.dll` and `ModLimitAdjuster.asi` are present in both `bin/x64` and `bin/x64_dx12`.
- User config filelists include AMM, Better Icons, Reflex, Gwent Redux, and Modular Eyes entries for both DX11 and DX12.
- Current `modSpawnCompanions` Corvo manager files match the pre-8841 backup by file size, so the selected Corvo Bianco variants appear preserved after 8841.

Recommendation:
- Continue with small cosmetic/content mods first.
- Treat any future MCME, BASE, W3EE, E3HUD, Better Icons, AMM, or NobsReflex overwrite as high-risk and re-run this audit pattern afterward.
