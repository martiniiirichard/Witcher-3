# Mod Install Triage Process

Date: 2026-06-27

Purpose: standardize how new backlog mods and deferred fixes are reviewed before touching the live Witcher 3 install.

## Source Lessons

Sinitar's TW3 guide reinforces several rules that match this stack:

- Run Script Merger after each few gameplay/UI/script mods, then launch the game and verify compilation plus basic feature behavior.
- Merge `.ws` and `.xml` conflicts when appropriate, but do not merge `.csv` files.
- Graphics/model/texture conflicts are usually load-order ownership decisions, not script-merge problems.
- If a merge causes trouble, remove the problematic merge output and rerun Script Merger rather than blindly editing more files.

External references:

- Sinitar TW3 guide: https://www.sinitargaming.com/tw3.html
- Script Merger: https://www.nexusmods.com/witcher3/mods/484
- Script Merger FAE: https://www.nexusmods.com/witcher3/mods/8405

## Current Stack Owners

These owners should usually win unless we make an explicit exception:

- W3EE Redux: gameplay baseline, alchemy, skills, economy-sensitive scripts.
- Brothers in Arms: broad restoration/bugfix baseline.
- E3 HUD + W3EE Redux E3 compatibility layer: HUD/menu owner.
- Better Icons W3EE/E3 patches: inventory/alchemy/crafting icon UI owner.
- Gwent Redux: Gwent owner.
- Floren Economy + Reputation System: economy/reputation owner.
- HDRP/BiA/True Fires/weather stack: visual owner, with exact-path inspection before adding more.

## Intake Checklist

For every backlog or deferred mod:

1. Identify source page, downloaded archive, and required dependencies.
2. Confirm Next-Gen/W3EE/BiA/E3/Gwent compatibility claims.
3. Extract to `tmp\inspect-*`; never install directly from archive.
4. Inventory:
   - `mods`
   - `DLC`
   - `bin\config\r4game\user_config_matrix\pc`
   - `input.settings`
   - scripts, bundles, XML, CSV, SWF/REDSWF, texture cache
5. Classify risk:
   - `safe-content`: content-only, no exact hot-zone collision.
   - `load-order-owner`: bundled non-text or SWF/REDSWF conflict; choose a winner.
   - `script-graft`: older full-script override, but feature may be portable as a small block.
   - `hot-zone`: touches W3EE/BiA/E3/Better Icons/Gwent/economy files.
   - `defer`: value does not justify current merge/loader risk.
6. Check exact-path overlap against active folders and the bundle conflict index.
7. If scripts changed, run Script Merger/compile smoke before any further mod.
8. If only bundles changed, still launch smoke when the mod is large or world/DLC-heavy.
9. Document the decision in `logs/` and update `docs/mod-backlog.md`.
10. Commit documentation and config/game-file changes in focused checkpoints.

## Hard Rules For This Build

- Do not merge `.csv` files in Script Merger. Treat them as data-owner decisions.
- Do not let old full vanilla scripts override W3EE Redux. Graft small marked blocks into the active winner when justified.
- Do not add standalone Friendly HUD, More Quick Slots, AQOOM, or Immersive Cam copies unless we intentionally replace W3EE-owned integrations.
- Do not stack broad economy/crafting mods on top of Floren Economy/Reputation/W3EE without a value comparison.
- Do not add new weather/Toussaint/cloud/rain mods without exact-path inspection against the current visual stack.
- Do not install mods with `blob0.bundle` payloads that previously reproduced the no-window startup hang unless we intentionally free loader budget and isolate the test.

## Current Environment Notes

- The game is still installed under `C:\Program Files (x86)`, which is less ideal for a very large manual mod setup because permissions and launcher behavior can be noisier.
- `ModLimitAdjuster.asi` is present under `bin\x64`.
- `dinput8.dll` is present, so ASI loading is configured.
- The newer Script Merger FAE toolset exists in `tools\sm-fae-0.9.7`.

## Backlog Order

Prefer this install/review order:

1. Small restoration/QoL mods with no scripts.
2. Content-only quest/location additions that do not hit known startup-hang patterns.
3. Narrow script mods with tiny helper functions and clear W3EE-compatible graft points.
4. Visual mods only after exact-path comparison.
5. Economy/crafting/combat/UI overhauls last, and only as deliberate compatibility passes.

## Abort Criteria

Stop and rollback/disable the candidate if any occur:

- No-window startup hang.
- Compile errors in W3EE/BiA/E3 hot-zone scripts.
- Menu Organizer XML error returns.
- Script Merger reports a broad full-file conflict in a current owner file and the feature is not worth a manual graft.
- The mod only wins by overriding a higher-value owner such as W3EE, BiA, E3 HUD, Better Icons, Gwent Redux, or Floren Economy.
