# Audit: Script Shadow Redundancy Pass

Date: 2026-06-27

## Goal

Check active mods whose `.ws` files lose to lower-number priority owners. A losing script is not automatically redundant: many current features are intentionally supplied by DLC, bundled content, menu XML, or manual grafts into an active script owner.

## Finding: Fixed

### `modLessmusic`

Before this pass, `modLessmusic` was enabled at priority `177`, so its only file:

`content\scripts\engine\sound.ws`

lost to `modW3EE` at priority `23`. That means the Less Music timing behavior was probably not active even though the mod was enabled.

The installed Less Music script still contains the W3EE sound-threat hooks:

- `useSoundValue`
- `sound_threat_settings.csv`
- `UpdateThreatDamp`

It also contains the Less Music timing values:

- `lim_playDuration = 600.0`
- `lim_muteDuration = 600.0`

Action:

```ini
[modLessmusic]
Enabled=1
Priority=21
```

This lets `modLessmusic` win `sound.ws` while staying near the W3EE/Nobs script layer.

Backup:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\less-music-priority-fix-20260627-232735`

Validation:

- `modLessmusic` now wins `content\scripts\engine\sound.ws`.
- DX12 launch smoke passed; `witcher3.exe` stayed running and responding for 45 seconds.

## Keep: Looks Shadowed But Intentional

| Mod | Why it looks shadowed | Why to keep |
| --- | --- | --- |
| `mod00AMMW3EEReduxNG139b` | Its `playerWitcher.ws` loses to `mod0000_MergedFiles`. | This is expected for the AMM/W3EER manual compatibility stack; do not remove the AMM patch without a targeted AMM review. |
| `modReduxW3EE` | Its local uniques script loses to `mod000_Patch_BIA-W3EER`. | Expected core patch relationship. |
| `mod00ReputationSystem_W3EE_REDUX` | All ten scripts lose to `mod00FlorenEconomySystem_W3EE_REDUX`. | Expected: Floren Economy is the higher-priority economy/reputation umbrella. Keep both because reputation content/strings/DLC remain part of the target economy loop. |
| `modFriendlyMeditation` | Most broad scripts lose to E3 HUD/W3EE/Nobs/MergedFiles. | It still owns unique config and bed/meditation behavior files, plus menu XML and strings. Keep. |
| `modIcyOcean` | Its broad effect/player/swimming scripts lose to W3EE/Nobs/MergedFiles. | It still owns `icyOceanEffect.ws`; prior compatibility graft added the enum/manager hooks to active winners. Keep. |
| `modBasicCookingRecipes` | Its two alchemy scripts lose to W3EE. | Intentional install choice: DLC recipe/vendor/loot data remains active while W3EE alchemy scripts win. Keep. |
| `modmanticor` | Its broad `temp.ws` loses to W3EE. | Intentional install choice: Manticore payload is bundled/XML content; W3EE keeps the stock/debug script owner. Keep. |
| `modAllGearEnchantingBasedOnSockets` | Its `guiEnchantingInventoryComponent.ws` loses to W3EE and its full `enchantingMenu.ws` is disabled. | The real socket-based enchantment behavior was manually grafted into active Better Icons/W3EE enchanting logic. Keep for strings/rollback unless a later targeted test proves the loose losing component is unnecessary. |
| `modNPCTargetingPriorityAndAxiiFixes` | Its helper scripts lose to Nobs/W3EE/MergedFiles. | Prior conflict fix intentionally disabled duplicate helpers elsewhere; do not remove until an Axii/targeting behavior test confirms active graft coverage. |

## Next Pass

The next redundancy pass should focus on mods with active strings/config but no winning scripts or bundle paths. Those are usually either:

- menu/config-only helpers that should stay, or
- stale shell folders that can be archived after approval.
