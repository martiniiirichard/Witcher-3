# Attack Collision Overhaul - Leshens 10530

Date: 2026-06-23

Source:
- https://www.nexusmods.com/witcher3/mods/10530

Download:
- `C:\Users\marti\Downloads\Attack Collision Overhaul - Leshens - W3EE-10530-0-2-1741367222.zip`

Intent:
- Improves attack collision behavior for Leshen-family enemies, including Leshens, Spriggans, Hym, and Miasmal style enemies.

Install:
- Installed `mods\modACO-Leshens`.
- Enabled `modACO-Leshens` in both known `mods.settings` copies:
  - `C:\Games\The Witcher 3\mods.settings`
  - `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`
- Assigned priority `183`, immediately after `modACO-Giants`.

Compatibility notes:
- Archive contains bundled content only:
  - `blob0.bundle`
  - `buffers0.bundle`
  - `en.w3strings`
  - `info.json`
  - `metadata.store`
- No Witcher scripts were installed.
- No Script Merger pass required.
- The mod page recommends priority over W3EE for W3EE Redux setups. It is loaded late for that reason.

Backup:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\aco-leshens-10530-20260623-191657`

Verification:
- DX12 smoke test passed: `witcher3.exe` stayed alive for 45 seconds after install.

Gameplay check:
- Later, test combat against Leshen/Spriggan/Hym/Miasmal style enemies to confirm improved collision behavior and no animation/combat oddities.
