# Immersive Rewards 4438

Date: 2026-06-24

## Installed

- Installed mod payload:
  - `mods/modFloren`
- Source archive:
  - `C:/Users/marti/Downloads/Immersive Rewards-4438-0-1-1582586746.7z`

## Settings

Added to both active `mods.settings` files:

```ini
[modFloren]
Enabled=1
Priority=234
```

## Compatibility handling

The archive ships old broad script replacements:

- `game/quests/quest_function.ws`
- `game/scenes/scene_functions.ws`

Those were not safe to use directly:

- `quest_function.ws` would shadow the active `mod0000_MergedFiles` version and lose W3EE/merged fixes.
- `scene_functions.ws` was older than the current Next-Gen base and lacked newer scene helpers.

Disabled original broad replacements:

- `mods/modFloren/content/scripts/game/quests/quest_function.ws.disabled-by-codex-old-broad-replacement`
- `mods/modFloren/content/scripts/game/scenes/scene_functions.ws.disabled-by-codex-old-broad-replacement`

Kept:

- `content/blob0.bundle`
- `content/metadata.store`
- `local/KuczOptions.ws`

Created a modern `scene_functions.ws` owner by copying the current Next-Gen `content0` file, then applying only Immersive Rewards' currency-exchange formula changes.

Patched active merged quest file:

- `mods/mod0000_MergedFiles/content/scripts/game/quests/quest_function.ws`

Patch scope:

- `BankCurrencyExchangeQuest`
- `BankCurrencyExchangeScene`

Both now use:

- `KuczGetOrenPrice()`
- `KuczGetFlorenPrice()`

## In-game behavior

The page describes reward changes where Temerian rewards use Orens, Nilfgaardian rewards use Florens, rich quest givers pay more, poor quest givers pay less, and Orens are revalued closer to canon.

## Verification

- Launch smoke test: passed.
- Result: game stayed running after 45 seconds.

## Residual risk

- This is an old 2020 reward-data mod, so content-level overlaps with W3EE, ToSA, BiA, Gwent Redux, or restored quests are possible.
- Need later in-game validation around banks/currency exchange and a few edited quest rewards.
