# Triss Corvo Bianco Dialogue Fix - True Dress - 9287

Date: 2026-06-25

Source:
- https://www.nexusmods.com/witcher3/mods/9287

Archive:
- `C:\Users\marti\Downloads\Triss Corvo Bianco True Dress-9287-1-1718888918.rar`

Purpose:
- Fixes Triss's Corvo Bianco dialogue/dress mismatch by using the masquerade dress appearance referenced in dialogue.

Status:
- Already installed before this audit.
- Active folder:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modTrissCBTrueDress`

Settings:
- Enabled in both active `mods.settings` files:

```ini
[modTrissCBTrueDress]
Enabled=1
Priority=143
```

Files:
- `content\blob0.bundle`
- `content\buffers0.bundle`
- `content\metadata.store`
- `content\texture.cache`
- `content\info.json`

Notes:
- No scripts.
- No Script Merger work needed.
- `info.json` has `succesfullyCooked=false`, but the mod is already active and startup verification passed.

Verification:
- DX12 launch passed.
- Visible full-screen `The Witcher 3` window appeared.
- No script compilation dialog.
