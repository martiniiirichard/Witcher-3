# Witcher 3 Mod Backlog

This backlog tracks mods worth considering later, plus mods that should stay deferred unless there is a specific gameplay or visual goal.

## Link Policy

When a mod came from a Nexus collection table and the table did not expose the exact mod ID, store:

- the source collection URL
- title, uploader, and category
- a Nexus search link for follow-up

Replace search links with direct mod links when we inspect/install the candidate.

Source collection reviewed: https://www.nexusmods.com/games/witcher3/collections/z5tjm8/mods

## Candidates To Consider

| Mod | Source | Why Consider | Risk / Notes | Status |
| --- | --- | --- | --- | --- |
| [Blood Trails](https://www.nexusmods.com/witcher3/mods/8065) | z5tjm8, Scoutbr0, Immersion | Strong fit for tracking, hunting, and difficult immersive play. | Check overlap with W3EE blood/combat effects before install. | Backlog |
| [Viper Venomous Silver Sword Schematic Restored - Next Gen](https://www.nexusmods.com/witcher3/mods/7442) | z5tjm8, konyme, Alchemy and Crafting | Small restoration candidate; likely better value/risk than broad crafting mods. | Verify against W3EE item/progression changes. | Backlog |
| [Roach Gwent Card for Everyone](https://www.nexusmods.com/witcher3/mods/10898) | z5tjm8, paulr0013, Gwent | Small unlock/QoL candidate. | Check against Gwent Redux before install. | Backlog |
| [Additional Armor Stands](https://www.nexusmods.com/witcher3/search/?gsearch=Additional%20Armor%20Stands&gsearchtype=mods) | z5tjm8, djkovrik, Immersion | Good fit if we want Corvo Bianco/display-room enrichment. | Installed as `modAdditionalArmorStandsNoUni` at priority `150`; content-only. | Installed |
| [Extra Stashes](https://www.nexusmods.com/witcher3/search/?gsearch=Extra%20Stashes&gsearchtype=mods) | z5tjm8, MerseyRockoff, Immersion | Useful QoL if storage friction becomes annoying. | Covered for now by `modAdditionalStashLocations` plus `mod0BiA_ASL_Compatibility`; do not add another stash mod unless storage still feels bad. | Covered |
| [Richer Merchants](https://www.nexusmods.com/witcher3/mods/8212) | z5tjm8, shiv4444, Tweaks | Supports goal of being rewarded for selling to proper buyers. | Likely overlaps Floren economy/reputation and W3EE economy. Review values first. | Backlog |
| [Well Stocked Craftsmen](https://www.nexusmods.com/witcher3/mods/3002) | z5tjm8, Partoutatix, Tweaks | Could support long-term grandmaster crafting goals. | Economy/crafting overlap. Needs deliberate balance review. | Backlog |
| [Characters Hi-Res Shadows - Next Gen](https://www.nexusmods.com/witcher3/mods/10591) | z5tjm8, TheRealArdCarraigh, Visuals and Graphics | Potential visual upgrade. | Check RTX/HDRP overlap and performance. | Backlog |
| [Vampires Have No Shadows](https://www.nexusmods.com/witcher3/mods/1749) | z5tjm8, djkovrik, Immersion | Strong lore/immersion idea. | Check if it touches broad entity/material bundles. | Backlog |
| [Professional Witcher Belt and Items](https://www.nexusmods.com/witcher3/mods/5911) | z5tjm8, Bjorn18, Immersion | Visual immersion candidate if it does not fight AMM/equipment visuals. | Appearance stack is already dense. Inspect file paths first. | Backlog |

## Deferred Unless Specifically Wanted

| Mod / Group | Source | Reason To Defer |
| --- | --- | --- |
| [All Containers Glow without Witcher Senses](https://www.nexusmods.com/witcher3/search/?gsearch=All%20Containers%20Glow%20without%20Witcher%20Senses&gsearchtype=mods) | z5tjm8 | Convenience feature, but it undercuts W3EE-style exploration difficulty. |
| [All Quest Objectives On Map](https://www.nexusmods.com/witcher3/search/?gsearch=All%20Quest%20Objectives%20On%20Map&gsearchtype=mods) | z5tjm8 | Standalone AQOOM-style behavior is likely redundant with W3EE-integrated hooks. |
| [More Quick Slots - Better Radial Menu - Quick Inventory](https://www.nexusmods.com/witcher3/search/?gsearch=More%20Quick%20Slots%20Better%20Radial%20Menu%20Quick%20Inventory&gsearchtype=mods) | z5tjm8 | Avoid standalone copy; W3EE already owns this integration. |
| Camera mods: Better Vision of Camera LOOK DOWN, Smooth Camera Motion, Smooth Camera Zoom | z5tjm8 | Likely overlap Immersive Cam/W3EE camera controls. Only revisit for a specific camera complaint. |
| Movement mods: Auto Roll, Smooth Movement, Improved Horse Controls, More reasonable fall injury | z5tjm8 | These change input/feel; install one at a time only after deciding the current movement problem. |
| Lighting/weather mods: Better Vanilla lighting Changes, More Shadows for Toussaint, New Clouds, New Toussaint Clouds, Realistic Rain Textures | z5tjm8 | We already have HDRP, weather, Toussaint, rain, and cloud layers. Treat as deliberate weather pass only. |
| Combat/system mods: Blood And Steel, Critical Slow Motion Combat REDUX, Stronger Monster Status Effects, Adult Fatality | z5tjm8 | High script/balance risk with W3EE combat. Not low-risk additions. |
| Economy/crafting bundles: Better Gold, Rational Crafting, Tweaks Collection | z5tjm8 | Broad balance overlap with W3EE Redux, Floren economy, reputation, and crafting goals. Rational Crafting was inspected on 2026-06-27 and deferred because it ships a full `craftingMenu.ws` override in a current hot zone. See `logs/assess-rational-crafting-10389-2026-06-27.md`. |
| Appearance packs: Faction Appearance Project, Humans of the Continent, broad face/eye/body packs | z5tjm8 | Current appearance stack already has many bundled non-text conflicts. Add only for a specific visual target. |
| Path Of The Tough | z5tjm8 | Broad overhaul on top of W3EE Redux; not compatible with the current design direction without a dedicated plan. |

## Already Covered Or Intentionally Not Backlogged

- Brothers In Arms, HDRP, Better Icons, Hoods, Fast Travel Pack, Corvo Bianco Guests Extended, Shrines of Verna, Standardised Naming Convention, Live Bestiary behavior, and W3EE-owned UI/control hooks are already installed or covered.
- No Missable Trophies / Mutagens were intentionally archived.
- Tiny fix mods previously removed as low-value or redundant are not re-added to the backlog unless a bug reappears.
