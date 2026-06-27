# Deferred Mod Worklist

Date: 2026-06-27

Purpose: track deferred or buggy areas using the current install triage process.

## Current Process

Use `docs/mod-install-triage-process.md` before retrying any item here.

## Fixed / Verified

| Area | Status | Notes |
| --- | --- | --- |
| Vivaldi Investments 12215 | Fixed installed DLC payload. | Active mod was present, but DLC `blob0.bundle` and `metadata.store` were zero bytes. Repaired from archive and DX12 smoke passed. See `logs/repair-vivaldi-investments-dlc-2026-06-27.md`. |
| Useful Place of Power Map Pin 11300 | Installed. | Tiny script-only map pin helper. DX12 smoke passed. See `logs/install-useful-place-of-power-map-pin-11300-2026-06-27.md`. |
| Selected Bomb for Monster Nests 7592 | Installed. | Tiny annotation wrapper over `CMonsterNestEntity.PlayerHasBombActivator()`. DX12 smoke passed. See `logs/install-selected-bomb-for-monster-nests-7592-2026-06-27.md`. |
| Fix Loot Sound 8316 | Already grafted. | Do not install raw. The useful Buckthorn/herb sound behavior is already patched into W3EE/Better Icons/container paths. See `logs/assess-small-fix-batch-2026-06-27.md`. |
| Fix sound of rotfiend exploding 11267 | Already grafted. | Do not install raw. The useful `SetSuppressHitSounds(true)` line is already patched into W3EE's active rotfiend explosion task. See `logs/assess-small-fix-batch-2026-06-27.md`. |
| Fix sounds of sword hits when adding effects 11267 | Already grafted. | Do not install raw. The active W3EE `actor.ws` contains the intended Codex 11267 sound behavior. See `logs/assess-script-hotfix-downloads-2026-06-27.md`. |

## Do Not Retry Raw

| Area | Why |
| --- | --- |
| Alchemy Primer 8081 | Porting project, not a normal install. It collides with W3EE, Better Icons, E3 HUD, Nobs Reflex, Quest Item Equipment, and Alcohol Factory. |
| Rational Crafting 10389 | Full `craftingMenu.ws` override in a current hot zone. |
| Advanced Icons for Witcher Gear 11339 | Cosmetic goal, but payload replaces B&W item XML already owned by W3EE/BiA/scabbard layers. |
| Balanced Alcohol Prices 10295 | Rechecked after loader-pressure finding. It owns full `def_item_edibles.xml` / `items_plus` edibles; low priority is no-op, high priority would override current Food Rebalance/Lighter Bombs/economy decisions. Keep disabled. |
| Improved Fist Fights 3703 | Full `r4Player.ws` and item XML changes; W3EE already intentionally changes fist-fight health behavior. |
| Sort Everything / Minor Tweaks | Useful but touches inventory, journal, bestiary, alchemy, and crafting hot-zone scripts. Needs manual compatibility patch. |
| Interface Animations 7353 | Script fixes were possible, but active DLC caused hard DX12 crash. Needs dedicated DLC/content crash pass. |
| Palace Extended 11004 | No scripts, but content/DLC install caused no-window launch failure. Only revisit after freeing loader budget. |
| Broad Kaer Morhen world stacks | Exact world-layer conflicts and prior startup/content failures. Keep the current simpler line unless we do REDkit/world-layer work. |
| No Stair Rolling 7774 | Full `explorationStateLand.ws` replacement. Diff only offered an older slope threshold while removing W3EE's falling-damage option gate. W3EE remains the better owner. |
| Bomb Aiming 9017 | Full `petard.ws` and `playerAiming.ws` replacements. These are W3EE combat/throwable hot files, so raw install is too risky. Reconsider only as a manual diff/graft if bomb aiming feels bad in play. |
| Life Steal Fix 5104 | Full `r4Player.ws` replacement. Too broad for W3EE/AMM/current player-state stack. |
| Superior Black Blood redesign 10416 | Full `damageManagerProcessor.ws` plus potion effect replacement. Too broad for W3EE/Nobs Reflex/current toxicity and damage stack. |
| Resistance to bleeding in necrophages and vampires 10416 | Full `baseEffect.ws` replacement. This is a core W3EE effect-system hot file; skip raw install unless we do a targeted manual compatibility pass. |
| Skellige Ice Breath Compatibility 4138 | Older Ice Breath script. Current Ice Breath Next Gen script already includes Skellige Winter Weather support plus newer dialogue/cutscene handling. |

## Partial / Special Active States

| Area | Current State |
| --- | --- |
| RT Water Reflection Fix 11144 | Script-only active. Bundle remains disabled because it causes no-window hang at current loader pressure. |
| Witcher Lore Collection 7236 | Active with `blob0.bundle` disabled per prior startup-hang isolation. |
| W3QE 9360 | Reduced/archived state after bundle startup-hang isolation. |
| Natural Torchlight | Important behavior is grafted into `mod0000_MergedFiles`; do not evaluate only by bundled asset ownership. |
| Live Bestiary | Original UI script/SWF losing to E3/W3EE is intentional; keep data/content behavior. |

## Good Future Candidates

These need download/inspection first:

| Mod | Link | Expected Risk |
| --- | --- | --- |
| Roach Gwent Card for Everyone | https://www.nexusmods.com/witcher3/mods/10898 | Small Gwent unlock candidate. Check Gwent Redux ownership. |
| Blood Trails | https://www.nexusmods.com/witcher3/mods/8065 | Strong immersion fit. Check VFX/blood/combat effect paths before install. |

## Future Compatibility Projects

These may be valuable, but should be deliberate projects:

- Sort Everything compatibility patch based on active E3/W3EE/Better Icons winners.
- Alchemy Primer compatibility fork, only if we decide to make that a major project.
- Palace/Kaer Morhen world-layer work, ideally with loader-budget reduction and possibly REDkit inspection.
- Economy tuning through existing FOCES/Reputation/LFE settings instead of stacking CLFSP/Richer Merchants blindly.
