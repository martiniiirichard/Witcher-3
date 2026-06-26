# Mod Settings Recommendations Guide

Date started: 2026-06-26

Companion artifact:

- `docs/mod-settings-recommendations.csv`
- `docs/w3ee-settings-deep-pass.md`
- `docs/mod-redundancy-candidates.md`

Scope:

- Covers every active mod-menu row from `docs/mod-menu-option-inventory.csv`.
- Current row count: 2,672 mod settings.
- This is an advisory layer only. It does not change live game settings.
- The CSV is the broad first-pass inventory. Dedicated deep-pass docs supersede broad CSV wording for their specific mod/menu.

## How To Read The CSV

| Column | Meaning |
| --- | --- |
| `Priority` | Review tier. `P0` is highest gameplay risk/impact; `P4` is structural or internal. |
| `Status` | Whether the row has a recommendation, should not be touched, or has no gameplay action. |
| `CurrentValue` | Current value from `dx12user.settings` when available. |
| `PreferredValue` | Recommended target or "keep current/default" when the exact value should be preserved. |
| `Recommendation` | Short decision. |
| `Reason` | Why that decision fits the current mod stack and target experience. |
| `ReviewBasis` | Whether the recommendation came from local XML, scripts, source page notes, or broad rules. |

## Priority Tiers

| Tier | Meaning | Current count |
| --- | --- | --- |
| `P0` | Core gameplay, economy, reputation, BiA, W3EE, RER. Review first. | 1,175 |
| `P1` | Important UI, camera, control, visual readability, or balance-adjacent settings. | 635 |
| `P2` | Moderate-risk immersion/content systems or previously fragile mods. | 452 |
| `P3` | Mostly cosmetic/personal-preference settings. | 335 |
| `P4` | Structural separators, hidden initializer/version fields, or no-action rows. | 75 |

## Current Strong Line

The strongest line is conservative: preserve the working W3EE/BiA stack and only tune settings when they solve a specific observed problem.

1. W3EE Redux owns core difficulty, alchemy, toxicity, progression, skill economy, and baseline merchant pressure.
2. Brothers in Arms owns broad bugfix and compatibility behavior.
3. Reputation System owns region/faction consequences and social price response.
4. Florens - Orens - Crowns owns regional currency friction.
5. W3EE's LFE layer owns item value math, durability penalties, crafting, repair, and dismantle cost curves.
6. Random Encounters Reworked owns exploration pressure, contracts, bounties, ambushes, and ecosystem behavior.
7. UI/camera mods should support readability first, immersion second, cosmetics third.

## Recommended Review Order

| Order | Menu | Why |
| --- | --- | --- |
| 1 | `W3EnhancedEdition.xml` | Foundation layer. Highest risk if casually changed. |
| 2 | `modRandomEncountersReworked.xml` | 762 options. Can affect difficulty, loot, exploration pressure, and performance. |
| 3 | `BrothersInArms.xml` | Broad fix layer. Usually let BiA win unless a content decision says otherwise. |
| 4 | `LFE.xml` + `modReputationSystem.xml` + `modFlorenEconomySystem.xml` | Economy stack must stay coherent. |
| 5 | `modFHUDConfig.xml`, `e3hud.xml`, `modMoreQuickSlots.xml`, `ImmCamMenu.xml` | Readability and ergonomics. Needs visual testing. |
| 6 | `DarkerNights.xml`, lighting/weather options | Immersion gain with direct gameplay visibility risk. |
| 7 | Cosmetic systems such as AMM, Modular Eyes, swords-on-Roach/campfire, medallion visuals | Keep current unless visual tests show clipping, noise, or mismatch. |

## Early Decisions To Preserve

| Area | Recommendation | Why |
| --- | --- | --- |
| W3EE gameplay sliders | Keep current W3EE/Redux baseline. | They passed current launch/play checks and form the difficulty foundation. |
| Reputation System | Enable defaults and keep visible feedback while calibrating. | You want reputation to matter, and the default penalties are stronger than the bonuses. |
| LFE sell multiplier | Keep `0.2`. | Keeps money scarce and prevents looting swords from becoming the main income loop. |
| LFE buy multiplier | Keep `1.0`. | Avoids crude global inflation; reputation/currency should create the texture. |
| LFE dismantle multiplier | Keep `0.5` initially. | Supports crafting without making dismantling free. Revisit if grandmaster gear becomes grindy. |
| Floren auto-convert | Enable. | Preserves regional currency flavor without bookkeeping pain. |
| Floren stash/horse conversion | Enable unless exploit behavior appears. | Completionist hoarding should not create false scarcity. |
| Vivaldi Investments | Keep conservative caps. | Flavor is fine; passive income should not bypass the money game. |
| RER quest safety | Keep quest-marker spawn cancellation on and big-city spawns off. | Completionist run needs stable quest spaces. |
| RER loot | Enable, monitor economy. | Hunting should pay, but farming should not dominate. |
| RER known bestiary creatures | Enable. | Geralt's knowledge should matter. |

## Redundancy Watchlist

| Cluster | Risk | Recommendation |
| --- | --- | --- |
| W3EE/LFE + Reputation + Florens + Vivaldi | Too many money systems can stack into either poverty or passive wealth. | Keep roles distinct. Tune from merchant tests, not vibes. |
| W3EE combat + RER difficulty/scaling | RER can accidentally become the real difficulty mod. | W3EE owns lethality; RER owns encounter cadence and variety. |
| W3EE integrated add-ons + standalone UI/control mods | Duplicate menu/HUD/slot/camera features can create conflicts or noisy UX. | Prefer the W3EE-compatible install path unless a standalone feature clearly adds value. |
| E3 HUD + Friendly HUD + Better Icons + Menu Organizer | UI stack has already needed manual fixing. | Change only with screenshots and launch checks. |
| Appearance/body/texture mods | Non-mergeable conflicts can be harmless if the desired visual mod wins. | Treat these as visual decisions, not script problems, unless the game fails to launch. |

## Research Notes

Useful external references for future option reviews:

- [W3EE Redux](https://www.nexusmods.com/witcher3/mods/5802)
- [Random Encounters Reworked](https://www.nexusmods.com/witcher3/mods/5018)
- [RER GitHub](https://github.com/Aelto/tw3-random-encounters-reworked)
- [RER Bible](https://aelto.github.io/tw3-random-encounters-reworked/rer-bible/)
- [Reputation System](https://www.nexusmods.com/witcher3/mods/9383)
- [Florens - Orens - Crowns Economy System](https://www.nexusmods.com/witcher3/mods/8707)
- [Immersive Cam](https://www.nexusmods.com/witcher3/mods/689)

## Next Audit Pass

Start with `W3EnhancedEdition.xml` and convert its `P0` rows from broad recommendations into setting-by-setting decisions after reading the exact script behavior. That is the highest leverage because every other gameplay mod is downstream of W3EE.
