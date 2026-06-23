# Install - Utilities, Mods Menu Category, HD Tree LOD

Date: 2026-06-23

## Utility Tools Staged

Staged utility bundle:

`tools\sm-fae-0.9.7`

Source:

`C:\Users\marti\Downloads\SM-FAE FULL 0.9.7 release candidate 2-8405-0-9-7-1732762713.7z`

Useful executables found:

- `WitcherScriptMerger.exe`
- `Tools\KDiff3\kdiff3.exe`
- `Tools\QuickBMS\quickbms.exe`
- `Tools\wcc_lite\bin\x64\wcc_lite.exe`

Staged menu filelist helper:

`tools\menu-filelist-updater\tw3-menu-filelist-updater.exe`

Source:

`C:\Users\marti\Downloads\tw3-menu-filelist-updater-7171-v1-1-1706381076.exe`

These tool folders are ignored by Git and were not committed.

Desktop shortcut update:

- `C:\Users\marti\OneDrive\Desktop\Witcher 3 Script Merger.lnk` now points to `tools\sm-fae-0.9.7\WitcherScriptMerger.exe`.
- The older `tools\script-merger-0.6.5` install remains available as a fallback.

## Mods Installed

Installed to the game `mods` folder:

- `mod_ModsMenuCategory`
- `modHDTreeBillboards`
- `modHDTreeBillboardsBnW`

Sources:

- `C:\Users\marti\Downloads\Mods Menu Category-10578-2-1-1745319248.zip`
- `C:\Users\marti\Downloads\HD Tree LOD Billboards-3739-0-3-1562750425.zip`
- `C:\Users\marti\Downloads\HD Tree LOD Billboards for Blood and Wine-3739-0-1-1569567981.zip`

## Load Order

Added to:

`C:\Games\The Witcher 3\mods.settings`

```ini
[mod_ModsMenuCategory]
Enabled=1
Priority=129

[modHDTreeBillboards]
Enabled=1
Priority=130

[modHDTreeBillboardsBnW]
Enabled=1
Priority=131
```

Created a timestamped backup of `mods.settings` before editing.

## Verification

Static checks:

- `mod_ModsMenuCategory`: 18 files, 0 scripts.
- `modHDTreeBillboards`: 1 file, 0 scripts.
- `modHDTreeBillboardsBnW`: 1 file, 0 scripts.
- No Script Merger work expected.
- Game `dlc` root stayed clean; only the known pre-existing `DLCScabbards` package lacks metadata.

Runtime smoke:

- Launched `Witcher3DirectDX12.exe`.
- `witcher3.exe` was alive and responding after 45 seconds.
- Closed the game after the smoke test.

## Deferred

Still deferred because they need isolated visual/render testing:

- NextgenBetterFX
- Dense Rainfall
- Realistic Rain
- Realistic Weather
- Skellige Winter Weather
- Promotional Atmosphere Lighting
- Filterless Toussaint
- RT/RTXGI tweaks
- HD Reworked partial downloads
