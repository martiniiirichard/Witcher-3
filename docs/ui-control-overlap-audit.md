# UI And Control Overlap Audit

Date: 2026-06-26

Scope:

- W3EE-integrated add-ons: Friendly HUD, Immersive Cam, More Quick Slots, AQOOM-style hooks
- Active surrounding folders: E3 HUD, AMM, Live Bestiary, Menu Organizer
- Menu XML under `bin/config/r4game/user_config_matrix/pc`

No files were changed or disabled.

## Main Finding

There are no active standalone mod folders named:

- `modMoreQuickSlots`
- `modFHUD`
- `modFriendlyHUD`
- `modImmersiveCam`
- `modAQOOM`

The active menus for these systems are present, but they are W3EE-integrated add-on menus:

- `ImmCamMenu.xml`
- `modFHUDConfig.xml`
- `modMoreQuickSlots.xml`

W3EE scripts contain the actual Friendly HUD, Immersive Cam, Quick Slots, and AQOOM-style hooks. So these features are not redundant standalone installs right now. They are part of the W3EE stack.

## Active Folder Roles

| Folder | Payload | Likely role | Removal stance |
| --- | --- | --- | --- |
| `modW3EE` | 395 scripts plus menu/config integration. | Core W3EE gameplay and bundled add-on implementation. | Do not remove. |
| `modReduxW3EE` | Redux data/config layer. | W3EE Redux content layer. | Do not remove. |
| `modE3HUD` | Large bundle/cache/string payload, no scripts. | E3 HUD asset/base layer. | Do not remove unless we intentionally abandon E3 HUD. |
| `mod0_E3HUD_W3EER_NG` | 15 scripts plus small bundle. | W3EE/E3 HUD compatibility script layer. | Do not remove while using E3 HUD. |
| `modE3HUDColorLoad` | Small bundle. | E3 HUD loading screen/color patch. | Optional cosmetic; low priority cleanup candidate only if unwanted. |
| `modMenuOrganizerNG_IMM_MrCK` | Menu organizer scripts plus strings. | Infrastructure for organized mod menu. | Keep stable; prior menu XML errors make casual removal risky. |
| `modAMM` | Base AMM scripts/assets/strings. | Appearance Menu Mod base layer. | Keep if AMM features are desired. |
| `mod00AMMW3EEReduxNG139b` | One `playerWitcher.ws` script. | AMM/W3EE Redux compatibility patch. | Keep if AMM remains installed. |
| `modLiveBestiary` | Data table, bundle, disabled original bestiary script. | Live Bestiary data/content layer; script intentionally disabled in favor of E3/W3EE-compatible path. | Keep if Live Bestiary is desired. |

## What Is Actually Redundant?

Not the W3EE add-ons themselves. The active add-on menus are expected.

Potential redundancy or low-value areas are narrower:

| Candidate | Why it might be redundant | Why not remove yet |
| --- | --- | --- |
| `modE3HUDColorLoad` | Cosmetic E3 loading screen/color layer. | Small, likely harmless, and user may prefer the look. |
| AMM if user stops using AMM features | AMM adds appearance customization and causes script conflicts when unpatched. | It is currently working and desired for appearance control. |
| Live Bestiary if user does not want the feature | E3 HUD wins the bestiary script path, while Live Bestiary contributes data/content. | We intentionally installed the compatible arrangement; removing it may remove the feature. |
| Menu Organizer if mod menu count becomes manageable without it | It is infrastructure, not gameplay. | We previously hit XML/menu errors; removing it could destabilize menu organization. |

## Do Not Delete

Do not delete these without a specific rollback plan:

- `modW3EE`
- `modReduxW3EE`
- `mod0_E3HUD_W3EER_NG`
- `modE3HUD`
- `modMenuOrganizerNG_IMM_MrCK`
- `mod0000_MergedFiles`
- `mod000_Patch_BIA-W3EER`

## Practical Recommendation

Keep the current UI/control stack.

The next useful cleanup is not deleting Friendly HUD, Immersive Cam, More Quick Slots, or AQOOM. Those are W3EE-owned in this install. The next useful cleanup is:

1. Verify whether `modE3HUDColorLoad` adds enough value to keep.
2. Document AMM and Live Bestiary as intentional compatibility pairs.
3. Only revisit Menu Organizer if the mod menu itself breaks again.
4. Avoid adding standalone Friendly HUD, Immersive Cam, More Quick Slots, or AQOOM folders on top of W3EE; that would create real duplication.

## Reviewed Pair Decisions

These are the explicit keep/remove decisions for the current UI and utility stack.

| Item | Decision | Evidence | Risk if changed |
| --- | --- | --- | --- |
| `modE3HUD` + `mod0_E3HUD_W3EER_NG` | Keep as a pair. | `modE3HUD` is the large asset/cache/string layer with no scripts; `mod0_E3HUD_W3EER_NG` is the smaller W3EE/E3 script compatibility layer. | Removing only one side can leave either missing visual assets or incompatible HUD scripts. Only remove both if intentionally abandoning E3 HUD. |
| `modE3HUDColorLoad` | Optional cosmetic. Keep unless the look is unwanted. | Small bundle-only payload; no active script surface. | Low script risk. Removal should mainly affect loading screen/color presentation. |
| `modAMM` + `mod00AMMW3EEReduxNG139b` | Keep as a pair while AMM is desired. | `modAMM` is the base Appearance Menu Mod layer; `mod00AMMW3EEReduxNG139b` is a narrow W3EE Redux compatibility script patch. | Keeping AMM without the patch risks returning player script conflicts. Removing AMM loses appearance customization and dependent AMM content. |
| `modLiveBestiary` | Keep if the Live Bestiary feature is desired. | The data table and bundle remain active, while the original bestiary script is disabled so the E3/W3EE-compatible path can win. | Removing it should reduce script pressure, but it likely removes the Live Bestiary data/content contribution. |
| `modMenuOrganizerNG_IMM_MrCK` | Keep as infrastructure. | It owns menu organization scripts and strings for the current crowded mod menu stack. We previously had a Menu Organizer XML install error that needed correction. | Casual removal can make the options menu harder to reason about or break menu registration again. |

Strong rule: do not treat "a menu exists" as proof of a standalone duplicate. In this install, Friendly HUD, Immersive Cam, More Quick Slots, and AQOOM-style behavior are W3EE-owned unless a separate active mod folder proves otherwise.

## Cleanup Queue

Only these are realistic cleanup candidates from this group:

1. `modE3HUDColorLoad`, if the loading screen/color look is unwanted.
2. AMM and its W3EE Redux patch, only if appearance customization is no longer wanted.
3. Live Bestiary, only if the feature is not worth its data/content footprint.

The E3 HUD pair and Menu Organizer should not be removed as "cleanup"; they are structural choices. Changing either one is a deliberate UI-stack redesign and needs a launch test plus menu inspection afterward.
