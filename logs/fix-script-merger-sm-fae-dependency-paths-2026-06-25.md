# Fix - Script Merger SM-FAE Dependency Paths

Date: 2026-06-25

## Symptom

SM-FAE Script Merger showed the `Dependency Locations` dialog with red paths for:

- `KDiff3.exe`
- `quickbms.exe`
- `witcher3.bms`
- `wcc_lite.exe`

The dialog used relative paths like:

- `Tools\KDiff3\KDiff3.exe`
- `Tools\QuickBMS\quickbms.exe`
- `Tools\QuickBMS\witcher3.bms`
- `Tools\wcc_lite\bin\x64\wcc_lite.exe`

## Cause

The helper files were present, but `tools\sm-fae-0.9.7\WitcherScriptMerger.dll.config` used relative tool paths.

That can fail when Script Merger is launched from a shortcut or taskbar entry whose `Start in` folder is not:

`C:\Users\marti\OneDrive\Documents\New project\Witcher-3\tools\sm-fae-0.9.7`

## Local Fix Applied

Updated the local ignored config file:

`tools\sm-fae-0.9.7\WitcherScriptMerger.dll.config`

Configured absolute paths for:

- `GameDirectory`
- `VanillaScriptsDirectory`
- `ModsDirectory`
- `KDiff3Path`
- `QuickBmsPath`
- `QuickBmsPluginPath`
- `WccLitePath`

Validation confirmed all configured paths exist.

## Git Decision

Do not commit the SM-FAE config file itself.

Reasons:

- `tools/` is ignored by `.gitignore`
- the config contains machine-specific absolute paths
- the tool bundle is local runtime state, not portable project source

This log preserves the fix pattern for future rebuilds or new machines.
