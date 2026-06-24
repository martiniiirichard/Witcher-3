# Attack Collision Overhaul - Giants 11686

Date: 2026-06-23

Source:
- https://www.nexusmods.com/witcher3/mods/11686

Download:
- `C:\Users\marti\Downloads\Attack Collision Overhaul - Giants-11686-0-1-1767827388.zip`

Intent:
- Improves attack collision behavior for giant-type enemies.

Install:
- Installed `mods\modACO-Giants`.
- Enabled `modACO-Giants` in both known `mods.settings` copies:
  - `C:\Games\The Witcher 3\mods.settings`
  - `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`
- Assigned priority `182`.

Compatibility notes:
- Archive contains bundled content only:
  - `blob0.bundle`
  - `buffers0.bundle`
  - `en.w3strings`
  - `info.json`
  - `metadata.store`
- No Witcher scripts were installed.
- No Script Merger pass required.
- The mod page notes W3EE/Redux also touch giant entities but should work if this mod has priority over W3EE. It is loaded late for that reason.

Backup:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\aco-giants-11686-20260623-191354`

Verification:
- DX12 smoke test passed: `witcher3.exe` stayed alive for 45 seconds after install.

Gameplay check:
- Later, test against giant/cyclops/ice giant style enemies to confirm the intended collision behavior and no animation/combat oddities.
