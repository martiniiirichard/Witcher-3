# Extra Skills Slots Next Gen 12249

Date: 2026-06-23

## Source

- https://www.nexusmods.com/witcher3/mods/12249

## Installed Download

- `C:\Users\marti\Downloads\Extra Skills Slots Next Gen-12249-1-1779652136.rar`

## Installed Game Folder

- `mods\modExtraSkillSlotsNextGen`

The bundled readme refers to `modSlotsOnly`, but the archive's actual folder is `modExtraSkillSlotsNextGen`.

## Load Order

Added to both active `mods.settings` copies:

- `modExtraSkillSlotsNextGen`: priority `213`

## Backup

Backup path:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\ExtraSkillSlots_12249_20260623_231459`

Backed up:

- Both active `mods.settings` copies.
- Active merged `playerWitcher.ws`.

## Conflict Surface

The mod overlaps major W3EE/Redux hot zones:

- `game\gameplay\ability\PlayerAbilityManager.ws`
- `game\gui\menus\characterMenu.ws`
- `game\player\playerWitcher.ws`
- `game\r4Game.ws`
- local debug/config/notification/uninstall helper scripts

The page also warns about `panel_character.redswf` conflicts. The local archive did not expose that file directly in the content listing, but the gameplay/UI script surface remains high risk.

## Compatibility Fixes

Initial errors:

- `ResetMutationsDev` did not take the optional bool argument used by Extra Skill Slots local scripts.
- `theGame.essconfig` was missing from the active `CR4Game` provider.
- `ESSInitUnistall` was unavailable on the active ability manager.

Fixes:

- Patched active `mods\modNobsReflex\content\scripts\game\r4Game.ws`:
  - added `public var essconfig : ESSConfig;`
  - initialized it with `essconfig = new ESSConfig in this; essconfig.ESSInit();`
- Patched Extra Skill Slots local support scripts:
  - changed `ResetMutationsDev(true)` / `ResetMutationsDev(mutagens)` calls to no-argument `ResetMutationsDev()`.
  - disabled the uninstall-only `ESSInitUnistall(...)` call because the active W3EE ability manager does not expose that function.

Technique learned:

- For script mods layered onto W3EE/Redux, do not assume the new mod's full `r4Game.ws`, `playerWitcher.ws`, or `PlayerAbilityManager.ws` will be the active class provider. Patch the active winning provider when the error is a missing class member, and avoid pulling in an entire older core script unless compile errors force it.

## Verification

- DX12 compile/smoke test passed after the compatibility fixes; process stayed alive for 45 seconds and was killed manually.

## Residual Risk

- This is compile-clean, not functionally verified.
- First load of an existing save may reset the build; the readme says this is expected because new skill slot IDs are used.
- `essuninstall()` is not fully reliable in this stack because its `ESSInitUnistall` call was disabled to avoid a compile failure.
- In-world validation required:
  - Open character panel.
  - Confirm extra base/BaW slots render.
  - Confirm mutation panel extra slots render.
  - Confirm W3EE/Redux skill behavior still works.
  - Confirm the game handles an existing save build reset gracefully.
