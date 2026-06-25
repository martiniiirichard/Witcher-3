# Honey Workshop in Corvo Bianco 8658

Date: 2026-06-24

## Installed

- Installed DLC payload:
  - `DLC/dlchoneyworkshop`
- Installed script mod:
  - `mods/modHoneyWorkshop`
- Source archive:
  - `C:/Users/marti/Downloads/HoneyWorkshop-8658-2-4-1768333423.zip`

## Settings

Added to both active `mods.settings` files:

```ini
[modHoneyWorkshop]
Enabled=1
Priority=233
```

## Script inspection

The mod contains one local script:

- `local/honeysoldfloren.ws`

It adds three unique quest functions:

- `AddItemQuestHoneySoldFloren`
- `RecalHoneyInChestAfterReturnToBob`
- `AddItemQuestExtHiveReset`

No core script replacement, class override, or duplicate installed symbol was found.

## In-game behavior

The page describes this as a Corvo Bianco honey workshop that produces honeycombs, purifies them into honey, and sells honey for Florens. The generated Florens are added to the stash in the current version.

Expected availability condition:

- Blood and Wine required.
- Corvo Bianco garden must be upgraded.
- `Contract: The Apiarian Phantom` must be completed.

## Verification

- Launch smoke test: passed.
- Result: game stayed running after 45 seconds.

## Residual risk

- Content was not visually verified in Corvo Bianco.
- Because activation is quest/property gated, verify later on a save where the garden is upgraded and `Contract: The Apiarian Phantom` is complete.
