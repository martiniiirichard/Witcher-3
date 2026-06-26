# W3EE Settings Deep Pass

Date: 2026-06-26

Scope:

- `W3EnhancedEdition.xml`
- `docs/mod-settings-recommendations.csv`
- Local W3EE scripts under `mods/modW3EE`
- W3EE Redux source page: <https://www.nexusmods.com/witcher3/mods/5802>

No live settings were changed.

## Summary Decision

Keep the current W3EE/Redux baseline. W3EE is the foundation layer for combat, alchemy, toxicity, progression, economy pressure, inventory discipline, damage, and scaling. Other mods should add texture around it, not override its core balance.

This is especially important because the target playthrough is difficult and immersive but still completionist-friendly. The goal is not to make every slider harsher; it is to keep preparation, positioning, money decisions, and reputation meaningful while still allowing all quests, all grandmaster gear, all mutagens, and full-map exploration.

## Group Recommendations

| Group | Area | Recommendation | Why |
| --- | --- | --- | --- |
| `SCOptionCW` | Stamina costs/recovery | Keep current stamina-pressure baseline. | Forces deliberate attacks, blocks, counters, and movement without obviously blocking completionist play. |
| `SCOptionIN` | Injuries | Keep low-intrusion injury baseline. | Injuries add consequence, but low chance and quiet messaging avoid constant friction over a long run. |
| `SCOptionCR` | Finishers/dismemberment | Keep finishers manual/earned. | Rewards vulnerability windows without automating combat or adding camera interruptions. |
| `SCOptionCA` | Vigor | Keep current vigor pressure. | Preserves sign/resource discipline without making signs unusable. |
| `SCOptionCM` | General targeting/control | Keep current targeting/control baseline. | Feel-sensitive. Current improved/camera-driven setup has passed play checks. |
| `EECombatStance` | Combat stance | Keep enabled/current. | Supports deliberate W3EE combat and target readability. |
| `EEAimAssist` | Aim assist | Keep off/current. | Hard immersive play favors manual aim; re-enable only if bombs/crossbow become annoying rather than challenging. |
| `EnhancedTargeting` | Soft lock | Keep current soft-lock weights. | Camera-weighted targeting avoids hard-lock behavior that can fight W3EE positioning. |
| `SCOptionCE` | Enemy aggression/difficulty behavior | Keep high enemy aggression baseline. | Enemy pressure is central to the difficult experience. |
| `SCOptionCE1-10` | Enemy class profiles | Keep current profiles. | Human/monster profiles are interdependent; tune only from controlled combat tests. |
| `SCOptionSkills` | Talents/progression | Keep current progression baseline. | Skill gain and mutagen scaling affect long-run completion balance. |
| `SCOptionPrepAlch` | Alchemy | Keep current W3EE alchemy baseline. | Alchemy is a core W3EE system; avoid convenience creep unless prep becomes tedious rather than strategic. |
| `SCOptionTox` | Toxicity | Keep current toxicity baseline. | Toxicity is a core tradeoff and should not be softened without potion/decoction tests. |
| `SCOptionPrepMed` | Meditation/preparation | Keep current baseline. | Supports planning-before-risk witcher fantasy; tune only if it obstructs quest flow. |
| `SCOptionAnims` | Animations | Keep immersive animations unless they waste too much time. | Immersion-positive, but repeated looting/crafting friction can matter in a completionist run. |
| `SCOptionVisuals` | Visual effects | Keep current if readability holds. | Visuals are subordinate to combat readability and menu stability. |
| `NightSightMenu` | Night sight | Coordinate with darker nights. | Night vision and darker nights must be tuned together. |
| `SCOptionHUD` | W3EE HUD | Coordinate with E3/FHUD. | W3EE HUD options overlap with the E3/Friendly HUD stack. |
| `SCOptionInv` | Inventory/economy discipline | Keep current. | Weight, quest item handling, loot radius, and money behavior affect scarcity and ergonomics. |
| `SCOptionEx` | Exploration | Keep current. | Exploration friction should exist but not slow full-map completion. |
| `SCOptionScaling` | Scaling | Keep current. | Casual scaling changes can invalidate W3EE progression. |
| `SCOptionH` | Health modifiers | Keep current. | Health multipliers shape time-to-kill and should be benchmarked before changes. |
| `SCOptionD` | Damage modifiers | Keep current. | Damage multipliers are the sharpest balance lever; W3EE/Redux should remain the anchor. |

## Settings To Revisit Only After Testing

| Area | Test trigger | Possible adjustment |
| --- | --- | --- |
| Stamina | If fights feel slow because Geralt is constantly empty rather than tactically constrained. | Slightly reduce global stamina cost or regen pressure, not individual enemy difficulty. |
| Injuries | If injuries are too invisible to matter. | Enable messages before raising injury chance. |
| Aim assist | If bombs/crossbow feel physically awkward rather than skill-based. | Enable limited aim assist instead of changing combat difficulty. |
| Alchemy/toxicity | If potion/decoction use feels blocked rather than costly. | Adjust the narrow alchemy/toxicity setting causing friction; do not broadly soften W3EE. |
| Animations | If repeated looting/crafting becomes a chore. | Disable or shorten the specific animation class. |
| Inventory/economy | If grandmaster crafting becomes grindy after merchant/reputation testing. | Prefer dismantle/crafting relief over global sell-price increases. |
| Scaling | If specific regions become pointless or impossible. | Tune region/level behavior only with save-specific evidence. |

## Relationship To Other Mods

W3EE Redux's source page now distinguishes the full version from a light version that omits bundled add-ons such as More Quick Slots, Friendly HUD, AQOOM, and Immersive Camera. Our current working stack uses W3EE scripts that already contain hooks for Friendly HUD, Immersive Cam, Quick Slots, and AQOOM-style behavior.

That does not mean every related external folder is safe to delete. It means UI/control/camera add-ons are redundancy candidates and should be reviewed as an integrated stack before removal.

Strong rule: W3EE is the gameplay owner. If another mod changes combat, alchemy, mutagens, toxicity, skills, progression, or base economy, it needs a W3EE-specific compatibility reason to stay.
