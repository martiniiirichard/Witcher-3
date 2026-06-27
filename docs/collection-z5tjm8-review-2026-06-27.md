# Nexus Collection z5tjm8 Visible Review

Source: https://www.nexusmods.com/games/witcher3/collections/z5tjm8/mods

Date: 2026-06-27

Scope: Nexus exposed 177 visible mod rows in the logged-in in-app browser. The collection page advertised more total mods than were available in the rendered table, so this is a visible-page review, not a perfect Vortex export.

## High Confidence Installed Or Covered

- Brothers In Arms - Ultimate Edition: installed as `modBrothersInArms` plus BiA DLC folders.
- Brothers In Arms - HD Reworked Project Compatible Patch: installed/covered by active BiA/HDRP compatibility layers including `mod000000aHDRP_BiA`.
- The Witcher 3 HD Reworked Project NextGen Edition: installed as HDRP multi-part folders.
- Better Icons - Definitive Edition: installed as `modBetterIcons2025_NextGen_W3EE`.
- Hoods: installed as `mod__hoods` and `dlc__hoods`.
- Gameplay Mimics Fix - Next Gen: installed as `modGameplayMimicsFix`.
- Fast Travel Pack: installed as `modFastTravelPack` and `dlcFastTravelPack`.
- Corvo Bianco Guests Extended: installed as `modCorvoBiancoGuestsExtended` and DLC.
- Witcher 3 Quests Extended: DLC retained; reduced script shell intentionally archived after compatibility review.
- Restored Content - Shrines of Verna: installed as a split compatibility setup with `modshrinesofverna`, `dlcshrinesofverna`, and `modVernaShrine_Everlasting`.
- Live/Actual Bestiary behavior: covered by `modLiveBestiary`; original script disablement is intentional because E3/W3EE-compatible behavior wins.
- Standardised Naming Convention: covered by `mod_SNC_W3EERedux`.
- No Missable Trophies / Mutagens: intentionally archived after approval.
- Bald Mountain Oak Tree LOD Fix, Beauclair NPC Spawn Fix, Dandelion Scarf Fix, VGX-style tiny fixes: intentionally removed/archived as low-value or redundant cleanup.
- More Quick Slots, Friendly HUD, Immersive Cam, AQOOM-style behavior: W3EE-owned integrated hooks/menus are already present; avoid adding standalone copies.

## Interesting Candidates To Consider Later

- Blood Trails: immersive tracking; likely content/script-light, but check overlap with W3EE combat/blood effects.
- All Containers Glow without Witcher Senses: convenience UI; may reduce intended W3EE difficulty/immersion.
- Better Torches Next-Gen: possibly redundant with `modNaturalTorchlight`; compare visuals before adding.
- Better Vision of Camera LOOK DOWN / Smooth Camera Motion / Smooth Camera Zoom: likely overlaps Immersive Cam/W3EE camera controls; only add if current camera still bothers you.
- Dynamic Minimap Zoom: likely overlaps E3 HUD/W3EE HUD behavior; high merge risk relative to value.
- Characters Hi-Res Shadows - Next Gen: visual candidate, but inspect for RTX/HDRP overlap.
- Blood And Steel / Critical Slow Motion Combat REDUX / Stronger Monster Status Effects: gameplay/combat changes; high risk with W3EE balance.
- Brew With A View: overlaps Friendly Meditation and W3EE alchemy/meditation systems; high risk.
- Rational Crafting / Richer Merchants / Well Stocked Craftsmen / Better Gold: economy/crafting candidates, but likely overlap W3EE Redux economy, Floren Economy, and reputation goals.
- Viper Venomous Silver Sword Schematic Restored: small restoration candidate; likely easier than broad economy/gameplay mods.
- Roach Gwent Card for Everyone: small Gwent unlock candidate; check against Gwent Redux first.
- Additional Armor Stands / Additional Stash Locations / Extra Stashes: housing/QoL candidates; verify Corvo Bianco and stash conflicts first.

## Defer Or Avoid Unless There Is A Specific Want

- Standalone All Quest Objectives On Map: avoid unless W3EE/AQOOM-style integrated behavior is insufficient.
- More Quick Slots standalone: avoid; W3EE already owns this integration.
- Auto Take All: likely redundant with `modAutoLootRedux` and can undercut W3EE scarcity.
- Auto Roll / More reasonable fall injury / Smooth Movement / Improved Horse Controls: movement changes can be good, but should be tested one at a time because they touch feel and input.
- Path Of The Tough: broad overhaul; not appropriate on top of W3EE Redux without a dedicated compatibility plan.
- Tweaks Collection: broad balancing bundle; inspect individual tweaks before adding.
- Better Vanilla lighting Changes / More Shadows for Toussaint / New Clouds / New Toussaint Clouds / Realistic Rain Textures: defer to deliberate weather/lighting passes because we already run weather, Toussaint, rain, cloud, and HDRP layers.
- Adult Fatality: combat/gore logic likely script-heavy; possible with work, but not a low-risk add.
- Faction Appearance Project / Humans of the Continent / large appearance packs: high bundled non-text conflict potential with current appearance stack.
- E3 visual identity mods: only add if you actually want that style; we previously removed E3 Quen variants and are not chasing E3 visuals by default.

## Strong Next Move

Do not batch-install from this collection. We already have many of its core/value mods or stronger W3EE-compatible equivalents. The safest line is to pick one candidate at a time from the "Interesting Candidates" section, starting with small restoration/QoL mods before touching camera, combat, economy, or lighting.
