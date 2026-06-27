# Ray Traced Water Reflections Fix - 11144

Date: 2026-06-25

Source:
- https://www.nexusmods.com/witcher3/mods/11144

Archive:
- `C:\Users\marti\Downloads\RT Water Reflection Fix-11144-1-05-1767469921.rar`

Purpose:
- Fixes water color mismatch when using Ray Traced Reflections.

Requirement:
- `Community Patch - Shared Imports`
- Already installed and enabled as:
  - `modSharedImports`
  - Priority `18`

Installed:
- Folder:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modRTWaterReflectionColorFix`

Settings:
- Enabled in both active `mods.settings` files:
  - `C:\Games\The Witcher 3\mods.settings`
  - `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`

```ini
[modRTWaterReflectionColorFix]
Enabled=1
Priority=259
```

Files:
- `content\scripts\local\RTWaterReflectionFix.ws`
- `content\metadata.store`
- `content\blob0.bundle`

Issue found:
- Full install caused the known bad no-window startup hang:
  - `MainWindowHandle=0`
  - `visible=False`
  - memory plateau around 4128 MB
- No script compilation dialog appeared.

Isolation:
- Disabled only:
  - `content\blob0.bundle.disabled-by-codex-startup-hang-test`
- Left the local script and metadata active.
- Script-only state launched successfully.

Final state:
- Keep `modRTWaterReflectionColorFix` enabled.
- Keep `blob0.bundle` disabled.
- This is a safe partial install unless later visual testing proves the disabled bundle is required.

Verification:
- DX12 launch passed for 72 seconds in final state:
  - visible full-screen `The Witcher 3`
  - rect `0,0,1920,1080`
  - memory around 5917 MB
  - no script compilation dialog

Notes:
- The functional script applies the RT/Radiance environment adjustment after loading.
- The tiny REDkit `blob0.bundle` is the only observed startup-hang trigger.
