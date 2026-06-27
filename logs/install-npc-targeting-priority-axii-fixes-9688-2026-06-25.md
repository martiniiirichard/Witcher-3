# NPC Targeting Priority and Axii Fixes - 9688

Date: 2026-06-25

Source:
- https://www.nexusmods.com/witcher3/mods/9688

Archive:
- `C:\Users\marti\Downloads\NPC targeting priority and Axii fixes-9688-1-4-1-1771377437.7z`

Installed:
- Used the `Ver NG` package only.
- Installed folder:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modNPCTargetingPriorityAndAxiiFixes`

Settings:
- Enabled in both active `mods.settings` files:
  - `C:\Games\The Witcher 3\mods.settings`
  - `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`
- Entry:

```ini
[modNPCTargetingPriorityAndAxiiFixes]
Enabled=1
Priority=254
```

Touched scripts:
- `game\gameplay\damage\damageManagerProcessor.ws`
- `game\gameplay\effects\effectManager.ws`
- `game\gameplay\effects\effects\critical\confusedEffect.ws`
- `game\gameplay\effects\effects\skill\axiiGuardMe.ws`
- `game\npc\npc.ws`
- `local\modNPCTargetingPriorityAndAxiiFixes.ws`

Fix applied:
- First compile failed because these global helpers were already present in the W3EE graft helper:
  - `UnforceTargetsAxiiGuardMe`
  - `FixConfusionCriticalState`
- Existing duplicate location:
  - `mods\modW3EE\content\scripts\local\codex_w3ee_graft_helpers.ws`
- Disabled the redundant helper file from 9688:
  - `local\modNPCTargetingPriorityAndAxiiFixes.ws.disabled-by-codex-duplicate-w3ee-graft`

Settings cleanup:
- During enablement, a PowerShell replacement mistake briefly created orphan `$11` and `$10` lines in both `mods.settings` files.
- Removed only those orphan lines and their orphan priority lines.
- Created backups before cleanup:
  - `mods.settings.codex-backup-fix-orphan-dollar-lines-9688-*`

Verification:
- DX12 launch passed after disabling the duplicate helper:
  - visible full-screen `The Witcher 3` window
  - rect `0,0,1920,1080`
  - memory settled around 5914 MB
  - no script compilation dialog

Notes:
- Recommended dependency `modFixCritEffAnim` was already installed and enabled.
- No Script Merger action was needed after the duplicate helper was removed.
- This mod had been present in settings previously as a disabled entry, likely from an earlier partial attempt.
