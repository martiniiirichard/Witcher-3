# Assess: Next Backlog Candidates

Date: 2026-06-28

## Goal

Continue the backlog/redundancy pass by checking the next small or relevant candidates before asking for more downloads.

## Local Download Check

No matching local archives were found for:

- Roach Gwent Card for Everyone `10898`
- Blood Trails `8065`
- Richer Merchants `8212`
- Well Stocked Craftsmen `3002`
- Characters Hi-Res Shadows `10591`
- Vampires Have No Shadows `1749`
- Professional Witcher Belt and Items `5911`

No live folders for those exact candidates are active, except the current Gwent owner stack:

- `modGwentRedux`
- `modPatchGwentRedux_W3EE_W3EERedux`

## Blood Trails

Backlog link: `https://www.nexusmods.com/witcher3/mods/8065`

Current stack evidence:

- W3EE already has blood trail configuration and effects:
  - `Options().IsBloodTrailActive()`
  - `SCOptionVisuals/BloodTrail`
  - `W3EE - Injuries.ws` plays `cutscene_blood_trail`, `cutscene_blood_trail_02`, and `blood_trail_finisher`.
- Active W3EE/Merged player and actor scripts already contain blood trail hooks:
  - `BloodTrailForced`
  - `CBloodTrailEffect`
  - `blood_trail_horseriding`
- Random Encounters Reworked also has corpse/blood trail detail logic:
  - `RER_CorpseAndBloodTrailDetailsMaker`

Read:

- Do not prioritize this until we inspect the archive. It may still offer different tracking behavior, but the broad feature lane is already represented in W3EE/RER.
- If downloaded later, compare exact payload paths before install. Treat it as a potential overlap with W3EE visual/blood systems, not as a guaranteed safe immersion add.

## Roach Gwent Card For Everyone

Backlog link: `https://www.nexusmods.com/witcher3/mods/10898`

Current stack evidence:

- Gwent ownership is already dense:
  - `modGwentRedux`
  - `modPatchGwentRedux_W3EE_W3EERedux`
- The archive is not currently downloaded.

Read:

- Still a good small future candidate, but only after download/inspection.
- Key question: does it edit reward/card definition data that Gwent Redux already owns?
- If it is a tiny card unlock/reward tweak and does not replace broad Gwent Redux files, it is worth trying.

## Richer Merchants

Backlog link: `https://www.nexusmods.com/witcher3/mods/8212`

Current stack evidence:

- Active economy owner is already `mod00FlorenEconomySystem_W3EE_REDUX`, with merged W3EE inventory behavior.
- Active merchant funds logic currently includes:
  - `daysToIncreaseFunds = 5`
  - `GetFundsMax()` caps: broke `20`, poor `100`, average `300`, rich `1000`, rich quick-start `2500`
  - `IncreaseFunds()` scales restock by funds type and current economy modifiers.

Read:

- Do not add raw Richer Merchants on top of FOCES/W3EE.
- If merchants feel too poor, tune the existing FOCES/W3EE economy lane instead of stacking another merchant-money mod.
- This better supports the goal: struggle early, but be rewarded by reputation and selling to the right buyer.

## Well Stocked Craftsmen

Backlog link: `https://www.nexusmods.com/witcher3/mods/3002`

Current stack evidence:

- Archive not downloaded.
- The target goal is valid: long-run grandmaster crafting should be demanding without becoming blocked by vendor inventory pain.
- Current stack already has W3EE alchemy/crafting recipe logic and FOCES economy scripts in hot paths.

Read:

- More interesting than Richer Merchants, because it may address crafting supply without broadly increasing money.
- Needs archive inspection. If it is mostly vendor stock XML/entity data, it may be viable. If it replaces broad crafting/shop scripts, defer.

## Recommendation

Next download priority:

1. Roach Gwent Card for Everyone, if you want the Gwent completion nicety.
2. Well Stocked Craftsmen, if crafting supply feels too stingy.
3. Blood Trails only if we confirm it adds tracking behavior beyond W3EE/RER.

Skip or defer:

- Richer Merchants. Tune FOCES/W3EE economy instead.
