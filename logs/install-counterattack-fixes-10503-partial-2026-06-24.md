# Counterattack Fixes 10503 Partial Install

Source: https://www.nexusmods.com/witcher3/mods/10503

Date: 2026-06-24

## Page Notes

- Mod name: Counterattack Fixes (Classic and Next Gen)
- Download inspected: `Counterattack Fixes-10503-1-3-1778274602.7z`
- Archive includes OG and NG folders.
- The Nexus description lists four modules:
  - `GuaranteedHitWithRetaliatorySwordStrike`
  - `BlockingEnemyEffects`
  - `KnockingOutSpear`
  - `GraveHagAnim`

## Decision

Did not install the NG all-in-one folder as a standalone mod.

Reason: the NG all-in-one ships full replacements for high-conflict core scripts:

- `game\actor.ws`
- `game\gameplay\damage\damageManagerProcessor.ws`
- `game\player\r4Player.ws`

Those files are already owned by W3EE, merged files, Reflex, and other active combat mods. Installing the full module would create large Script Merger conflicts and risk overwriting W3EE Redux combat behavior.

## Installed Subset

Manually grafted only the `GuaranteedHitWithRetaliatorySwordStrike` behavior, because the author calls this the remaining highly recommended module.

Implemented behavior:

- Cache intended counter target via `IsCounterattackHitTarget`.
- Make `counter_attack_light` search for that tagged target instead of missing nearby enemies.
- Apply the helper hit-reaction logic from `modCounterattackFixes.ws`.

Patched files:

- `mods\modW3EE\content\scripts\game\actor.ws`
- `mods\mod0000_MergedFiles\content\scripts\game\player\r4Player.ws`

Added helper:

- `mods\modW3EE\content\scripts\local\modCounterattackFixes.ws`

Skipped for now:

- Blocking enemy effects during counterattack.
- Spear counter/disarm behavior.
- Grave Hag tongue animation override.

Those are more invasive and should be revisited only if we see a concrete issue in testing.

## Backups

Created timestamped backups next to patched files:

- `actor.ws.codex-backup-counterattack-fixes-10503-<timestamp>`
- `r4Player.ws.codex-backup-counterattack-fixes-10503-<timestamp>`

## Compile Fix

First compile reported:

```text
Error [modw3ee]game\actor.ws(5367): I dont know any 'attackAnimNameForParryCounter'
```

Fix: added `attackAnimNameForParryCounter : name` as a top-level `CActor` field near `counterAttackAnimTable`.

## Verification

- Confirmed no standalone `modCounterattackFixes_AllInOne` folder was installed.
- Confirmed no `modCounterattackFixes` entry exists in active `mods.settings`.
- DX12 smoke test passed after the field fix: game stayed running after 45 seconds and was killed manually.
