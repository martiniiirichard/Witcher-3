# Script Merger Baseline Conflicts - 2026-06-21

## Context

Script Merger was opened after the stable `main` checkpoint containing:

- W3EE Redux
- AMM
- AMM + W3EE Redux compatibility patch
- Swords on Roach
- AMM + Swords on Roach compatibility patch

The game has already launched successfully with this stack.

## Result

Script Merger reports script conflicts in these paths:

- `game\gameplay\items\swords\witcherSword.ws`
  - `modAMM`
  - `modW3EE`
- `game\gameplay\items\throwables\throwable.ws`
  - `modAMM`
  - `modW3EE`
- `game\player\playerWitcher.ws`
  - `mod00AMMW3EEReduxNG139b`
  - `modAMM`
  - `modW3EE`
- `game\player\states\combatSword.ws`
  - `modAMM`
  - `modW3EE`
- `game\vehicles\horse\horseManager.ws`
  - `modAMM`
  - `modW3EE`
- `local\W3EE_Uniques.ws`
  - `modReduxW3EE`
  - `modW3EE`

## Current Priority Order

`C:\Games\The Witcher 3\mods.settings`:

```ini
[mod00AMMW3EEReduxNG139b]
Enabled=1
Priority=1

[mod_SNC_W3EERedux]
Enabled=1
Priority=2

[modAMM]
Enabled=1
Priority=3

[modSharedImports]
Enabled=1
Priority=4

[modReduxW3EE]
Enabled=1
Priority=5

[modW3EE]
Enabled=1
Priority=6

[modW3EELocalization1]
Enabled=1
Priority=7

[modW3EELocalization2]
Enabled=1
Priority=8

[modW3EELocalization3]
Enabled=1
Priority=9

[modW3EELocalization4]
Enabled=1
Priority=10

[modSwordsonroach]
Enabled=1
Priority=11
```

Lower priority number wins.

## Interpretation

Do not create automatic merges for this baseline just because Script Merger lists conflicts. These conflicts are expected in the current working stack.

Important prior fixes:

- `modAMM\content\scripts\game\player\states\combatSword.ws` was manually patched to remove references to W3EE-disabled `W3Mutagen21_Effect`.
- `mod00AMMW3EEReduxNG139b\content\scripts\game\player\playerWitcher.ws` was manually patched with W3EE Redux 1.46 mutation bookkeeping.
- `modAMM\content\scripts\game\vehicles\horse\horseManager.ws` was manually patched with W3EE Redux 1.46 `ShouldRest()` support.

Those manual compatibility edits are part of the current working runtime state. A careless merge could overwrite or bypass them.

## Decision

Treat this Script Merger view as the known baseline conflict set.

Before adding the next mod:

1. Refresh Script Merger and save/screenshot the baseline.
2. Install exactly one mod.
3. Refresh Script Merger again.
4. Focus only on new conflicts introduced by that mod.
5. Avoid merging existing baseline conflicts unless a new compile/runtime error proves the baseline priority resolution is insufficient.

If a future merge is created, ensure `mod0000_MergedFiles` is enabled with the highest priority before launch-testing.
