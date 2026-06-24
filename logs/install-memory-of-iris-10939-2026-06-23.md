# Memory of Iris / Iris Rose Fix 10939

Date: 2026-06-23

Source:
- https://www.nexusmods.com/witcher3/mods/10939

Download:
- `C:\Users\marti\Downloads\Memory of Iris-10939-0-1-1749825659.zip`

Intent:
- Makes Olgierd wear Iris' rose in the final Hearts of Stone scene if the player gave it to him.

Install:
- Installed `mods\modolgierd_rose`.
- Enabled `modolgierd_rose` in both known `mods.settings` copies:
  - `C:\Games\The Witcher 3\mods.settings`
  - `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`
- Assigned priority `188`.

Compatibility notes:
- Archive contains bundled content only:
  - `blob0.bundle`
  - `buffers0.bundle`
  - `en.w3strings`
  - `info.json`
  - `metadata.store`
- No Witcher scripts were installed.
- No Script Merger pass required.
- Broad Iris/Olgierd references exist in AMM, Live Bestiary, and companion mods, but pre-install search did not identify another installed mod explicitly overriding the same final-scene Olgierd entity behavior.

Backup:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\memory-of-iris-10939-20260623-193713`

Verification:
- DX12 smoke test passed: `witcher3.exe` stayed alive for 45 seconds after install.

Gameplay check:
- Later, validate the final Hearts of Stone scene after giving Olgierd Iris' rose. Startup smoke cannot verify conditional scene appearance.
