# Mod Settings Decisions

Date started: 2026-06-26

Purpose: one living reference for mod-menu settings we have reviewed, what we picked, and why. This should grow as we inspect each menu in-game, from XML, from scripts, and from Nexus/GitHub documentation.

Generated inventory:

- `docs/mod-menu-option-inventory.csv`
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
