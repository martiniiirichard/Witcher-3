# Reputation System 9383

Date: 2026-06-24

## Installed

Installed W3EE Redux main file:

- `mods/mod00ReputationSystem_W3EE_REDUX`
- `DLC/dlcreputationsystem`
- `bin/config/r4game/user_config_matrix/pc/modReputationSystem.xml`

Source archive:

- `C:/Users/marti/Downloads/Reputation System W3EE_REDUX-9383-W3EER-1-42i-RS-2-5c-1770459724.zip`

## Compatibility patch

Applied the RS + FOCES + W3EE Redux patch onto FOCES:

- `mods/mod00FlorenEconomySystem_W3EE_REDUX`

Patch source:

- `C:/Users/marti/Downloads/RS - FOCES - W3EE_REDUX Patch-8707-RS-2-5c-FOCES-4-8d-W3EER-1-42i-1770460001.zip`

This is intentional because FOCES owns the shared economy/menu paths at the top of the load order. The patch carries the Reputation System hooks into the FOCES owner so the two systems do not fight over the same files.

## Settings

Added to both active `mods.settings` files:

```ini
[mod00ReputationSystem_W3EE_REDUX]
Enabled=1
Priority=2
```

Relevant top priority order:

```ini
[mod00FlorenEconomySystem_W3EE_REDUX]
Priority=0

[mod0000_MergedFiles]
Priority=1

[mod00ReputationSystem_W3EE_REDUX]
Priority=2
```

FOCES stays above Reputation because the RS+FOCES patch installs Reputation-aware scripts into FOCES. Reputation's own matching script paths are therefore not expected to win.

## Page notes

The page describes Reputation System as restoring CDPR's cut reputation concept. Geralt's choices and behavior affect regional/faction reputation, which can influence activities such as shops, betting, negotiation, dialogue, and stats display. Requires Hearts of Stone and Blood and Wine.

## Verification

- Launch smoke test: passed.
- Result: game stayed running after 45 seconds.

## Residual risk

- This is broad and overlaps FOCES economy behavior.
- Smoke test only proves scripts compile and the game reaches runtime.
- Later in-game checks:
  - Reputation menu/settings appears.
  - Character stats reputation display.
  - Shop/betting/negotiation modifiers.
  - A known reputation-changing quest or combat scenario.
  - FOCES currency display still behaves correctly after Reputation integration.
