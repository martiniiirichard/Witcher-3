# Mod Settings Decisions

Date started: 2026-06-26

Purpose: one living reference for mod-menu settings we have reviewed, what we picked, and why. This should grow as we inspect each menu in-game, from XML, from scripts, and from Nexus/GitHub documentation.

Generated inventory:

- `docs/mod-menu-option-inventory.csv`
- `docs/mod-settings-recommendations.csv`
- `docs/mod-settings-recommendations-guide.md`
- `docs/w3ee-settings-deep-pass.md`
- `docs/mod-redundancy-candidates.md`
- Current inventory size: 3,670 menu rows
- Mod option rows: 2,672
- System option rows: 998

Review workflow:

1. Parse active menu XML from `bin/config/r4game/user_config_matrix/pc`.
2. Cross-reference current values from `dx12user.settings`.
3. Inspect local scripts when labels are unclear.
4. Check Nexus/GitHub docs, images, and posts when local context is not enough.
5. Record the chosen value, reason, and risk here.
6. Only apply setting changes after a deliberate decision.

## Target Experience

Goal: immersive, difficult, completionist-friendly W3EE playthrough.

The desired line is not "maximum punishment". It is a world that pushes back, but still rewards knowledge, preparation, and good routing:

- Combat and survival should stay hard enough that preparation, potions, scouting, and choosing fights matter.
- Money should feel scarce early and still meaningful later, but not become a chore once Geralt has reputation, buyer knowledge, and dismantling discipline.
- Reputation should affect prices and social feedback so the world remembers Geralt's choices.
- Crafting all grandmaster gear, collecting all mutagens, doing all quests, and exploring the whole map must remain practical.
- Encounter and economy settings should add pressure and texture without flooding the map, breaking quests, or turning repeatable systems into passive money farms.

## Ownership Rules

These rules keep overlapping mods from all steering the same system at once.

| System | Preferred owner | Reason |
| --- | --- | --- |
| Core combat, alchemy, toxicity, skills, mutagens, witcher gear, and baseline economy difficulty | W3EE Redux | It is the foundation mod. Other settings should extend it, not fight it. |
| Base-game fixes, restored consistency, and broad compatibility patches | Brothers in Arms | It should usually win direct bugfix/content conflicts unless a specific content mod is intentionally selected. |
| Region/faction memory and price response to reputation | Reputation System | This directly matches the "world reflects my reputation" goal. |
| Regional currencies and exchange friction | Florens - Orens - Crowns Economy System | Best fit for making money feel local and political rather than generic. |
| Item value curves, durability penalties, crafting/repair/dismantle cost multipliers | W3EE's LFE layer | It is already integrated into W3EE scripts and should be tuned conservatively. |
| Passive banking/investment | Vivaldi Investments | Optional flavor; cap tightly so it does not bypass the money struggle. |
| Repeatable exploration pressure, contracts, bounties, ambushes, ecosystem behavior | Random Encounters Reworked | It owns world dynamism; W3EE still owns how dangerous combat feels. |
| Camera/HUD ergonomics | Immersive Cam plus E3/W3EE-compatible UI stack | Use atmosphere where safe, but visibility remains part of W3EE balance. |

## Economy And Reputation

Sources used:

- Local menu XML: `modReputationSystem.xml`, `modFlorenEconomySystem.xml`, `LFE.xml`, `VivaldiInvestments.xml`
- Local scripts: `mod00FlorenEconomySystem_W3EE_REDUX/content/scripts/local/reputationSystemSettings.ws`, `questWorldFlorenMod.ws`, and `modW3EE/content/scripts/local/LFEOptions.ws`
- Nexus: [Reputation System](https://www.nexusmods.com/witcher3/mods/9383) says the mod restores CDPR's cut reputation concept and lets Geralt's choices/behaviors influence activities in different regions.
- Nexus: [Florens - Orens - Crowns Economy System](https://www.nexusmods.com/witcher3/mods/8707) says Florens, Orens, Ducats, and Crowns become usable regional currencies with prices/incomes adjusted by exchange value.

### Current Recommendation

| Setting area | Recommendation | Why |
| --- | --- | --- |
| Reputation System | Enable, default offsets, visible feedback on while learning. | Defaults are asymmetric in the right direction: hated/disliked penalties are stronger than liked/respected bonuses. This supports consequence without making good reputation a money printer. |
| Reputation UI toggles | Keep char stats, item stats, betting, negotiation, dialogue, and Scoia'tael display enabled for now. | We need visible feedback while calibrating. Later, switch toward `Rep_MinUI` if the UI feels too gamey. |
| Reputation offsets | Keep defaults: hated `-25`, disliked `-10`, liked `10`, respected `20`, max `20`. | Strong enough to matter, capped enough to avoid destabilizing W3EE pricing. |
| Floren auto-convert | Prefer On. | Prevents currency desync and preserves the regional-money fantasy without adding bookkeeping pain. |
| Floren convert from stash/horse inventory | Prefer On unless it creates obvious exploit behavior. | The script explicitly includes horse inventory in exchange calculations. With our hoarding/crafting goal, ignoring stash/horse money would create annoying false scarcity. |
| LFE sell multiplier | Keep low, current `0.2`. | Keeps selling from becoming the dominant money solution. Rewards the right buyer/reputation layer more than blanket vendor dumping. |
| LFE buy multiplier | Keep current `1.0`. | Lets W3EE difficulty and regional/reputation systems carry the pressure instead of globally inflating everything. |
| LFE durability curve | Keep current `0.2/0.6/0.8/0.9`. | Damaged loot should sell poorly, which rewards repair/dismantle decisions and prevents every sword pickup from being clean profit. |
| LFE dismantle multiplier | Keep current `0.5` initially. | Supports dismantling as a viable crafting route without making it free. Revisit if grandmaster crafting feels grindy rather than earned. |
| LFE category/quality multipliers | Keep all at `1.0` until we have merchant test data. | Category tuning is powerful and easy to overfit. Use it only after we observe real vendor prices. |
| Vivaldi Investments | Keep conservative defaults: max sim days `365`, max balance `10`. | Flavor is fine; passive income should not replace contracts, looting, crafting, and merchant routing. |

Redundancy watchlist:

- W3EE/LFE, Reputation System, Florens economy, and Vivaldi Investments all touch money. Keep their roles distinct: LFE handles base value math, Reputation handles social price response, Florens handles currency/exchange context, Vivaldi handles small optional investment flavor.
- Do not raise global sell prices to solve poverty. First test whether reputation, right-buyer routing, and dismantling already create the intended late-game easing.
- If money remains too tight for grandmaster completion, first consider targeted dismantle/crafting relief, not broad merchant sell boosts.

## Random Encounters Reworked

Sources used:

- Local menu XML: `modRandomEncountersReworked.xml`
- Local scripts: `modRandomEncountersReworked/content/scripts/local/rer_scripts.min.ws`
- Nexus: [Random Encounters Reworked](https://www.nexusmods.com/witcher3/mods/5018) describes generated contracts, bounties, ambushes, hunts, ecosystem simulation, and events that react to player actions.
- GitHub: [Aelto/tw3-random-encounters-reworked](https://github.com/Aelto/tw3-random-encounters-reworked) documents contracts, bounties, ecosystem behavior, trophies, and a complete mod menu.
- RER Bible: [Summary](https://aelto.github.io/tw3-random-encounters-reworked/rer-bible/) is the setting reference to use when reviewing the 762-option menu.

### Current Recommendation

| Setting area | Recommendation | Why |
| --- | --- | --- |
| Mod enabled | On. | It supports exploration pressure and replayable world activity. |
| Main difficulty | Keep current/default unless live testing shows encounter bloat. | W3EE already makes fights dangerous. RER should add uncertainty and texture, not become the main combat difficulty slider. |
| Level scaling | Prefer automatic. | Keeps RER aligned with the current run instead of forcing static level math that may fight W3EE progression. |
| External factors impact | Keep modest/default. | Sounds, corpses, and ecosystem behavior should matter, but not constantly dogpile the player. |
| Day/night frequency | Keep default first. | We want pressure while exploring, but the map should still breathe. Tune only after timed travel tests. |
| Cancel spawns near quest markers | On. | Completionist run needs quest safety more than maximum chaos. |
| Big city spawns | Off. | Cities are social/economic hubs; random combat there risks immersion and quest/menu disruption. |
| Encounter loot | On, but monitor economy. | Hunting should pay, but if it becomes a farming loop, lower rewards before lowering encounter quality. |
| Only known bestiary creatures | On for immersion. | Geralt's knowledge and bestiary progression should matter. This also reduces early-game monster nonsense. |
| Hide next notifications | On if currently enabled. | Keeps the world less mechanical; rely on clues, tracks, and encounters. |
| Action camera scenes | Off unless explicitly desired. | We already have camera/UI complexity. Avoid cinematic interrupts until the gameplay layer is stable. |

Redundancy watchlist:

- RER can generate money, trophies, loot, and contracts. If economy gets too generous, tune RER rewards before weakening the reputation/currency systems.
- RER difficulty and W3EE difficulty are not interchangeable. Prefer W3EE for enemy lethality and RER for encounter cadence, creature mix, and wilderness pressure.
- Quest safety settings should stay conservative because the run is completionist.

## Immersive Cam

Sources used:

- Local menu XML: `ImmCamMenu.xml`
- Local scripts: `modW3EE/content/scripts/local/immersiveCamConfig.ws`
- Nexus: [Immersive Cam](https://www.nexusmods.com/witcher3/mods/689) documents the in-game Options/Mods/Immersive Cam menu and keybind tuning.
- Nexus docs: [Immersive Cam docs](https://www.nexusmods.com/witcher3/mods/689?tab=docs&topic_id=7760103) confirm positive offset moves the camera right and higher zoom moves the camera closer.
- Nexus: [Immersive Camera for Next Gen](https://www.nexusmods.com/witcher3/mods/8387) notes close-camera transition fixes and renames the second preset to "Immersive", which matches the kind of label cleanup we made locally.

Decision: keep W3EE Immersive Cam enabled and use Immersive Cam presets as the baseline. Avoid vanilla close camera overriding it unless we intentionally want vanilla camera behavior.

Reason: Immersive Cam gives stronger atmosphere, but W3EE combat still needs readable camera distance and peripheral awareness.

### Recommended Baseline

| Tab | Setting | Picked value | Why |
| --- | --- | --- | --- |
| Exploration | Field Of View | 65 | Wider than default for awareness without heavy distortion. |
| Exploration | Interior Camera Matches Exterior Camera | On | Keeps indoor and outdoor camera behavior consistent. |
| Exploration | Exploration Offset | 0.25 | Mild right-shoulder framing. |
| Exploration | Exploration Zoom | 1.10-1.35 | Immersive without getting cramped. |
| Exploration | Exploration Height | 0.55-0.65 | Keeps Geralt grounded while preserving horizon visibility. |
| Sprint | Sprint Cam Based Upon | Exploration Settings | Keeps sprinting visually consistent with walking/exploration and avoids jarring camera shifts. |
| Sprint | Custom Sprint Base Offset | 0 | Only used for Custom sprint mode; leave neutral while using Exploration Settings. |
| Sprint | Custom Sprint Base Zoom | 0 | Only used for Custom sprint mode; leave neutral unless sprinting feels wrong. |
| Sprint | Custom Sprint Base Height | 0 | Only used for Custom sprint mode; leave neutral unless sprinting feels wrong. |
| Combat | Preset | Immersive Cam | Prefer readable combat over maximum cinematic closeness. |
| Horseback | Preset | Immersive Cam | If Roach feels cramped, raise ride distances toward 3.0. |
| Sailing | Preset | Immersive Cam | Keep Sail Pitch around 25. |
| Witcher Sense | Preset | Immersive Cam | Keep Witcher Sense Zoom enabled for focused investigation. |
| Examine Clue | Preset | Immersive Cam | Close framing works well for clue inspection. |
| Aim / Throw | Preset | Vanilla or Immersive Cam | Use Vanilla if bombs/crossbow feel awkward. |
| Igni Stream | Preset | Immersive Cam | Switch only this tab to Vanilla if the stream blocks target visibility. |

### Setting Meanings

| Setting family | Meaning |
| --- | --- |
| FOV | Wider/narrower view. Higher shows more peripheral vision but can add distortion. |
| Offset | Horizontal camera shoulder position. Higher moves right; lower/negative moves left. |
| Zoom / Depth | Camera distance. Higher generally moves closer; lower pulls back. |
| Height | Vertical camera position. Higher raises the camera; lower drops it closer to Geralt. |
| Interior Match | If enabled, interiors reuse the exploration camera instead of switching to a separate indoor camera. |
| Sprint Cam Based Upon | Chooses whether sprinting uses exploration, vanilla sprint, or custom sprint-only values. |
| Combat Lock | If enabled, combat camera avoids vanilla zoom-in/zoom-out behavior. |
| Horse distances | Separate camera distance values for walk/trot, canter, gallop, and mounted combat. |
| Sail Pitch | How far the sailing camera can tilt skyward. |
| Witcher Sense Zoom | Enables the dedicated focused Witcher Sense camera. |
| Aim Rotate | Whether Geralt auto-rotates toward camera direction while aiming/throwing. |

Practical rule: use Immersive Cam for atmosphere, but do not over-tighten combat, aiming, or Igni. W3EE is already more punishing than vanilla, so visibility is part of balance.

## Review Queue

High-value menus to review next:

| Priority | Menu XML | Reason |
| --- | --- | --- |
| 1 | `W3EnhancedEdition.xml` | Core gameplay overhaul. Many settings affect balance, difficulty, HUD, and addon behavior. |
| 2 | `modRandomEncountersReworked.xml` | 762 options; can affect spawn density, ambush frequency, bounty loops, performance, and balance. Nexus posts mention menu/config and spawn behavior issues, so this needs careful review. |
| 3 | `BrothersInArms.xml` | Large compatibility/bugfix mod; should usually preserve fixes unless a setting conflicts with W3EE/Redux. |
| 4 | `DarkerNights.xml` | Visual/immersion settings with direct gameplay visibility impact. |
| 5 | `modFHUDConfig.xml` / `e3hud.xml` | UI visibility and HUD behavior; high impact on usability. |
| 6 | `modMoreQuickSlots.xml` | Gameplay ergonomics; can affect balance and controller usability. |
| 7 | `AMM.xml` / `AMMRoach.xml` | Mostly appearance; lower gameplay risk but many options. |
| 8 | `modMenuOrganizer_IMM_MrCK.xml` | Keep stable. It controls menu organization and has caused startup/menu errors when misconfigured. |

Known parser note:

- `modInterfaceAnim.xml` contains malformed XML tolerated by the game but not strict parsers: an extra closing `</Var>` near the end. The generated inventory strips that only in memory; active game files were not changed for inventory generation.
