# Install - Debug Photomode Config / Assess Script-Heavy Batch

Date: 2026-06-28

## Installed

### Debug Console and Unlocked Photomode `7172`

Archive:

- `C:\Users\marti\Downloads\Debug Console and Unlocked Photomode-7172-4-02-1679939306.zip`

Current state before this pass:

- Debug console was already enabled in:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\base\general.ini`
- Existing value:
  - `DBGConsoleOn=true`

Change made:

- Installed:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\platform\pc\UnlockedPhotomode.ini`

Installed contents:

```ini
[Game]
AllowPhotomodeFreeMovement=true

[Streaming]
UseCameraForStreamingOverride=true
```

Backup:

- `settings-backups\debug-console-photomode-7172-20260628-090015\UnlockedPhotomode.ini.source`

Notes:

- Config-only change.
- No mod folder installed.
- No `mods.settings` change.
- No Script Merger action required.

## Deferred

### NOBs SlowMo `10286`

Archives inspected:

- `C:\Users\marti\Downloads\modNOBsSlowMoNextgen-10286-2-31-1739410104.zip`
- `C:\Users\marti\Downloads\NOBsSlowMoPatches-10286-2-31-1739410514.zip`

Reason:

- Replaces `content\scripts\local\W3EE - Effects.ws`.
- That file is already owned by `modW3EE` and `modNobsReflex`.
- Needs a manual effect-system compatibility pass if we ever want slow-motion behavior.

### Community Patch - Besserwisser and Nitpicker `3163`

Archive inspected:

- `C:\Users\marti\Downloads\Community Patch - Besserwisser and Nitpicker-3163-2-1-1592429912.rar`

Reason:

- Ships script replacements for:
  - `game\actor.ws`
  - `game\gameplay\items\spells\aardEntity.ws`
  - `game\player\playerWitcher.ws`
  - `game\player\r4Player.ws`
- These are major W3EE/AMM/Expansion Zero/current merged hot paths.
- Also includes bundled content and a `content0` bundle payload.
- Do not install raw.

### Shields `2356`

Archive inspected:

- `C:\Users\marti\Downloads\Shields-2356-1-10a-1554850379.rar`

Reason:

- Adds DLC/config, but also replaces major scripts:
  - `PlayerAbilityManager.ws`
  - `guiTooltipComponent.ws`
  - `playerWitcher.ws`
  - `r4Player.ws`
  - `arrowProjectile.ws`
- Current stack already has W3EE, Expansion Zero, Extra Skill Slots, Friendly Meditation, AMM, Nobs Reflex, Shades of Iron, and economy/reputation tooltip owners in these lanes.
- Do not install raw.

### Reasonable Senses Configurable / Main Menu Strings `10463`

Archive inspected:

- `C:\Users\marti\Downloads\Main - Menu Strings version-10463-1-0-1-1741608341.7z`

Reason:

- The archive name is misleading; it contains `modReasonableSensesConfigurable` plus menu support.
- Adds many Witcher-sense highlight scripts and a `gameplayEntity.ws` hook.
- This can undercut the current W3EE exploration/difficulty direction and should only be considered if Witcher-sense readability becomes a real problem.

## Validation

- No enabled mod count or load-order change.
- Script Merger required: no.
- DX12 launch smoke: passed. `witcher3.exe` was running and responsive after 45 seconds, then closed cleanly.
