# Random Encounters Reworked 5018

Date: 2026-06-22

Source:
- Nexus mod: https://www.nexusmods.com/witcher3/mods/5018
- Current upstream: https://github.com/Aelto/tw3-random-encounters-reworked
- Installed GitHub release asset: `tw3-random-encounters-reworked.zip` from the latest release endpoint.

Installed folders:
- `mods/modRandomEncountersReworked`
- `mods/mod_sharedutils_damagemodifiers`
- `mods/mod_sharedutils_dialogChoices`
- `mods/mod_sharedutils_glossary`
- `mods/mod_sharedutils_helpers`
- `mods/mod_sharedutils_mappins`
- `mods/mod_sharedutils_noticeboards`
- `mods/mod_sharedutils_npcInteraction`
- Existing shared dependencies present/updated: `mods/modSharedImports`, `mods/mod_sharedutils_oneliners`
- `dlc/dlcmodRandomEncountersReworked`
- `dlc/dlcsharedutils`
- `bin/config/r4game/user_config_matrix/pc/modRandomEncountersReworked.xml`

Configuration:
- Added `modRandomEncountersReworked.xml;` to both `dx11filelist.txt` and `dx12filelist.txt`.
- Added explicit `mods.settings` entries for the new RER/sharedutils folders at priorities `109` through `116`.
- Preserved existing priorities for `modSharedImports`, `mod_sharedutils_oneliners`, and `mod_sharedutils_menudescriptors`.

Notes:
- The downloaded Nexus package was only an install script. It downloads the latest GitHub release and copies `bin`, `dlc`, and `mods`.
- The script's W3EE compatibility patch logic is commented out, so no separate W3EE-specific RER patch was installed from that script.
- Official RER guide says latest Next-Gen should not require a merge for RER itself, but this stack is heavily modded, so Script Merger was launched for validation.

Pending:
- Confirm Script Merger conflict state.
- Launch test the game and confirm the RER preset selector/mod menu appears.

Post-install fix:
- Launch error reported duplicate `SUOL_*` / `SU_Oneliner*` classes from `mod_sharedutils_oneliners`.
- Root cause: the package contained both `content/scripts/local/oneliners` and `content/scripts/local/sharedutils/oneliners`, with duplicate class definitions.
- Kept the newer namespaced `local/sharedutils/oneliners` copy and disabled the older `local/oneliners` `.ws` files by renaming them to `.ws.disabled-by-codex`.
