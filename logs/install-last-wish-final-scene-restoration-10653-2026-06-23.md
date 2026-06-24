# The Last Wish Final Scene Restoration 10653

Date: 2026-06-23

Source:
- https://www.nexusmods.com/witcher3/mods/10653

Download:
- `C:\Users\marti\Downloads\The Last Wish Final Scene Restoration-10653-1-1-1754997890.zip`

Intent:
- Restores cut dialogue/content in the final scene of The Last Wish quest.

Install:
- Installed `mods\modlastwishrestoration`.
- Enabled `modlastwishrestoration` in both known `mods.settings` copies:
  - `C:\Games\The Witcher 3\mods.settings`
  - `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`
- Assigned priority `184`.

Compatibility notes:
- Archive contains bundled content only:
  - `blob0.bundle`
  - `buffers0.bundle`
  - `en.w3strings`
  - `info.json`
  - `metadata.store`
  - `texture.cache`
- No Witcher scripts were installed.
- No Script Merger pass required.
- Pre-install search did not find another installed mod explicitly touching `sq202_10_ending_djinn`.

Backup:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\last-wish-restoration-10653-20260623-192342`

Verification:
- DX12 smoke test passed: `witcher3.exe` stayed alive for 45 seconds after install.

Gameplay check:
- Later, validate in The Last Wish final scene. Startup smoke cannot verify restored scene timing, camera, subtitles, or dialogue flow.
