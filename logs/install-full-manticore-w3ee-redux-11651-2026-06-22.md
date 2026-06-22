# Full Manticore W3EE Redux Edit 11651

Source: https://www.nexusmods.com/witcher3/mods/11651?tab=description

Installed archive:
- `Full Manticore W3EE Redux Edit-11651-1-0-1767026819.zip`

Installed game folders:
- `DLC/dlcmant`
- `mods/modmanticor`

Configuration:
- Added `[modmanticor]` to `mods.settings`.
- Assigned `Priority=43`, below W3EE and the existing utility mods.

Reasoning:
- The Nexus page lists W3EE Redux as the required mod and Hearts of Stone/Blood and Wine as DLC requirements.
- The archive includes `modmanticor/content/scripts/game/temp.ws`, but inspection showed this is a broad stock/debug-style script file rather than the core Manticore balance payload.
- W3EE already provides `mods/modW3EE/content/scripts/game/temp.ws`, so `modmanticor` was intentionally placed below W3EE to avoid overriding W3EE's script version.
- The useful payload appears to be in the bundled/XML content: `modmanticor/content/blob0.bundle` and `DLC/dlcmant/content/blob0.bundle`.

Validation:
- Launched through `tools/direct-launchers/Witcher3DirectDX12.exe`.
- Startup/script compile passed; `witcher3` remained running and responding after the launch window.

Rollback:
- Backup created under `backups/11651-full-manticore-20260622-171621/`.

Reusable lesson:
- When a mod ships a large generic `temp.ws`, inspect whether it is truly needed before letting it win priority. If the functional payload is bundled XML/assets and W3EE already owns the script path, prefer leaving W3EE's script active and loading the new mod at a lower priority.
