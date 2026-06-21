# Script Merger Setup - 2026-06-21

## Tool

- Archive: `Witcher Script Merger v0.6.5-484-0-6-5-1593771408.7z`
- Extracted to ignored local tool path:
  - `tools\script-merger-0.6.5`

The `tools` folder is ignored and should not be committed.

## Configured Paths

`WitcherScriptMerger.exe.config` was configured with:

```text
GameDirectory=C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY
VanillaScriptsDirectory=C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\content\content0\scripts
ModsDirectory=C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods
MergedModName=mod0000_MergedFiles
```

Enabled checks:

- scripts
- XML files
- bundle contents
- custom load order validation

## Use

Launch:

```powershell
Start-Process -FilePath "tools\script-merger-0.6.5\WitcherScriptMerger.exe" -WorkingDirectory "tools\script-merger-0.6.5"
```

Use Script Merger as a conflict detector before launch-testing script-heavy mods. Treat its result as advisory: W3EE Redux compatibility patches may still require manual review because older compatibility files can shadow newer W3EE methods.
