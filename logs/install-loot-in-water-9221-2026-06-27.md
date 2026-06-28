# Install: Loot In Water - Next Gen 4.04 (9221)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/9221
Archive: `C:\Users\marti\Downloads\Loot In Water (Next-Gen 4.04)-9221-0-3-1718965649.zip`

## Decision

Installed after inspection.

## Why

The mod is behavior-sensitive because it modifies death/loot behavior, but current inspection found no active mod owner for its key script path:

- `game/behavior_tree/tasks/high_level/btTaskDeath.ws`

That means this is not currently a script-merge collision with W3EE, BiA, or another active mod. The archive is explicitly a Next-Gen 4.04 package.

## Install

Installed:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modLootInWater`

Added to `mods.settings`:

```ini
[modLootInWater]
Enabled=1
Priority=151
```

Backup path:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\loot-in-water-9221-20260627-225352`

## Validation

- Enabled mod count after install: 197.
- Enabled duplicate priority count stayed at the known baseline of 6.
- `modLootInWater` is the only active mod owner found for `btTaskDeath.ws`.
- DX12 game launched and remained responding for 40 seconds.

## Residual Risk

This still needs an in-game behavior check: kill or find a lootable enemy in water and confirm loot behavior works without odd death-state issues.
