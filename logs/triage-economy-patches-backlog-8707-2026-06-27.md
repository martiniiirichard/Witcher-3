# Economy Patch Backlog Triage

Date: 2026-06-27

## Scope

- Nexus page: https://www.nexusmods.com/witcher3/mods/8707
- `mod00FlorenEconomySystem_W3EE_REDUX-8707-W3EER-1-42i-FOCES-4-8d-1767278451.zip`
- `Patches for W3EER - BiA - Gwent Redux-8707-W3EER-1-42a-GR-4-04-BiA-2-72-FOCES-4-6f-1737179454.zip`
- `RS - FOCES - W3EE_REDUX Patch-8707-RS-2-5c-FOCES-4-8d-W3EER-1-42i-1770460001.zip`
- `Cheaper Lore Friendlier Shop Prices Pre-Merge-8707-CLFSP-4-04-1-FOCES-4-8d-1767278482.zip`
- Related older file: `Cheaper Lore Friendlier Shop Prices-3097-4-04-1-1700091456.7z`

## Current State

Keep the active economy stack:

- `mod00FlorenEconomySystem_W3EE_REDUX`
- `mod00ReputationSystem_W3EE_REDUX`
- FOCES W3EER/BiA/Gwent Redux patch
- RS + FOCES + W3EE Redux patch

This is already the strongest fit for the target economy: regional currencies, regional price pressure, reputation-sensitive prices, merchant specialization, difficulty-aware rewards, and a completionist-friendly path where selling and dismantling to the right buyer matters.

## Decision

Do not install `Cheaper Lore Friendlier Shop Prices` or the CLFSP pre-merge patch.

The cheaper-shop layer is not a richer economy system. It mainly pushes some shop paths back toward raw XML base item prices, which risks flattening or bypassing the active FOCES/W3EE/Reputation pricing pipeline.

## Why

- FOCES already owns the economy lane and is W3EE Redux-aware.
- Reputation has already been patched into the FOCES owner, so the two systems cooperate instead of competing over menu/shop scripts.
- The CLFSP pre-merge patch touches broad, conflict-heavy UI/shop files such as inventory, shop, tooltip, alchemy, and crafting menus.
- The active FOCES path already includes durability, category, quality, area, buy/sell, perk, difficulty, regional currency, and merchant multipliers.
- Installing CLFSP now would likely be a balance downgrade rather than a compatibility improvement.

## Future Tuning Rule

If prices feel too punishing later, tune the active FOCES/W3EE/Reputation multipliers directly. Do not stack another broad pricing mod unless we first decide to replace the current economy authority.

## Status

- Main FOCES W3EE Redux file: installed.
- W3EER/BiA/Gwent Redux patch: installed.
- Reputation compatibility patch: installed after Reputation System was added.
- CLFSP / Cheaper Lore Friendlier Shop Prices: reviewed and skipped.
- No game files changed in this triage pass.
