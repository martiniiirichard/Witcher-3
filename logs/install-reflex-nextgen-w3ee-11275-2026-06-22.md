# Reflex NextGen W3EE install

Date: 2026-06-22

Branch: `codex/reflex-nextgen-w3ee-11275`

## Source archives

- `C:\Users\marti\Downloads\modMenuStrings-3650-1-0-1556948614.7z`
- `C:\Users\marti\Downloads\NGNobsToolTipGenerator-11426-1-1-0-1765750315.7z`
- `C:\Users\marti\Downloads\NGNobsReflexes-11275-1-5-7-1765750539.7z`
- `C:\Users\marti\Downloads\NGNobsReflexesPatch-11275-1-5-7-1765750575.7z`

## Installed mods

- `modMenuStrings`
- `modNobsToolTipHandaler`
- `modNobsReflex`

## Configuration

Added to `C:\Games\The Witcher 3\mods.settings` after `modSharedImports`:

```ini
[modNobsToolTipHandaler]
Priority=13

[modNobsReflex]
Priority=14

[modMenuStrings]
Priority=15
```

Added `ReflexSettings.xml;` to both:

- `bin\config\r4game\user_config_matrix\pc\dx11filelist.txt`
- `bin\config\r4game\user_config_matrix\pc\dx12filelist.txt`

Added Reflex input bindings to the existing user `input.settings`, preserving previous bindings:

- `IK_P=(Action=ReflexPlayerInput)`
- `IK_Pad_LeftThumb=(Action=ReflexPlayerInput)`

## Merge model

The Nexus posts were important here. The broad instruction to choose Reflex over W3EE is unsafe for W3EE Redux. Reflex ships several vanilla-derived full-file replacements. When those replaced W3EE files, W3EE helpers and structs disappeared and produced cascades such as missing `Options()`, `Combat()`, `GetNPCStats()`, `SAttributeTooltip.attributeType`, and `ETS_*` values.

Reusable rule learned:

- For Reflex vs W3EE Redux core script conflicts, use W3EE as the base.
- Graft only Reflex-specific hooks into the W3EE file.
- Treat giant missing-function cascades as evidence that a core W3EE file was overwritten by a stale vanilla-derived mod file.

## Manual fixes applied

- `modNobsReflex\content\scripts\game\r4Game.ws`
  - Rebuilt from W3EE `r4Game.ws`.
  - Grafted Reflex option handler field, `ETS_Reflex` timescale source, and `ReflexOptionsPopulate()`.

- `modNobsReflex\content\scripts\game\types.ws`
  - Rebuilt from W3EE `types.ws`.
  - Added `ETS_Reflex`.

- `modNobsReflex\content\scripts\game\gameplay\effects\effectTypes.ws`
  - Rebuilt from W3EE `effectTypes.ws`.
  - Added Reflex-specific effect enum values.

- `modNobsReflex\content\scripts\game\gameplay\effects\gameEffectManager.ws`
  - Rebuilt from W3EE `gameEffectManager.ws`.
  - Grafted mappings for `EET_Reflex`, `ReflexEffect`, and `W3Effect_ReflexSlowMo`.

- `modNobsReflex\content\scripts\game\npc\npc.ws`
  - Rebuilt from W3EE `npc.ws`.
  - Grafted Reflex `LatentReflex()` calls into `OnPreAttackEvent`.

- `modNobsReflex\content\scripts\game\gameplay\damage\damageManagerProcessor.ws`
  - Rebuilt from W3EE `damageManagerProcessor.ws`.
  - Grafted Reflex `ManageReflexApplication(attackAction)` before W3EE damage reduction.

- `modNobsReflex\content\scripts\game\player\playerInput.ws`
  - Rebuilt from W3EE `playerInput.ws`.
  - Grafted `ReflexPlayerInput` listener and `OnCommReflexInput()`.

- `mod00AMMW3EEReduxNG139b\content\scripts\game\player\playerWitcher.ws`
  - Added Reflex effect field/getter.
  - Added combat start setup for `EET_Reflex`.
  - Added combat end cleanup.

- `modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws`
  - Rebuilt from W3EE `characterMenu.ws`.
  - Grafted only Nobs tooltip handler field/init/getter.
  - This preserved W3EE's `OnIncreaseSkillLVL`, `OnDecreaseSkillLVL`, and public `PopulateDataForMutagenTab()`.

## Specific debugging patterns learned

- `Unable to parse value` on many W3EE effects meant Reflex's stale `effectTypes.ws` had removed W3EE effect enum values.
- Unknown `W3Mutagen##_Effect` types can mean W3EE has the file but comments out the class. Do not assume copying the file fixes it.
- A massive list of missing W3EE functions usually traces back to `r4Game.ws` being overwritten.
- Missing NPC stats, movement helpers, and `SAttributeTooltip.attributeType` usually points to stale `types.ws`.
- Private/public errors in W3EE UI often mean a vanilla-derived menu file is overriding the W3EE menu.

## Verification

- Game compile/startup passed.
- User confirmed in-game validation passed.

## Backup

- `C:\Users\marti\OneDrive\Documents\New project\Witcher-3\backups\reflex-nextgen-w3ee-11275-20260622-165446`
