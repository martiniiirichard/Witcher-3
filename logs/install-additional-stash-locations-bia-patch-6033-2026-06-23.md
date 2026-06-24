# Additional Stash Locations + BiA Compatibility Patch 6033

Date: 2026-06-23

## Installed

Base dependency:

- Archive: `Additional Stash Locations - Next Gen-2034-1-404-1689964849.zip`
- Mod folder: `modAdditionalStashLocations`

Compatibility patch:

- Archive: `mod0BiA_ASL_Compatibility - Next-Gen-6033-BiA-Next-Gen-2-1-1682687497.zip`
- Mod folder: `mod0BiA_ASL_Compatibility`

## Load Order

Added to both active `mods.settings` files:

- `mod0BiA_ASL_Compatibility` priority `8`
- `modAdditionalStashLocations` priority `224`

The compatibility patch is intentionally placed near the early BiA/W3EER patch group so its bundle changes can override the relevant map pin/hub data.

## Manual Script Merge

`modAdditionalStashLocations` ships a full copy of:

```text
content\scripts\game\player\playerWitcher.ws
```

That file would collide with the existing W3EE/AMM/Friendly Meditation/Extra Skill Slots merged player script. Instead of enabling the full ASL copy, this file was disabled:

```text
mods\modAdditionalStashLocations\content\scripts\game\player\playerWitcher.ws.disabled-by-codex
```

Kept active:

```text
mods\modAdditionalStashLocations\content\scripts\local\extraStashSpawner.ws
```

Added the ASL spawn call to the active merged player file:

```text
mods\mod0000_MergedFiles\content\scripts\game\player\playerWitcher.ws
```

Inserted after `super.OnSpawned( spawnData );`:

```witcherscript
spawnMyLovelyStashes(); // Additional Stash Locations
```

## Backup

Created rollback backup:

```text
C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\ASL_BIA_6033_20260623_234120
```

## Verification

- DX12 launch smoke passed: game stayed running for 45 seconds.

## Notes

- The Nexus page for `6033` is a compatibility patch for Brothers in Arms and Additional Stash Locations.
- ASL was downloaded but not installed before this step.
- No Script Merger GUI pass was required because the player script change was manually reduced to the one required helper call.
