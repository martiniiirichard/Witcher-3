# Cat Hood Fix 8732 Audit

Source: https://www.nexusmods.com/witcher3/mods/8732

Result: already installed.

Observed files:
- `mods\modCatHoodFix\content\blob0.bundle`
- `mods\modCatHoodFix\content\buffers0.bundle`
- `mods\modCatHoodFix\content\metadata.store`

Settings:
- `modCatHoodFix` is enabled in both active `mods.settings` files.
- Current priority: `146`.

Notes:
- Nexus page version checked: `1.2`, last updated 2025-08-27.
- Purpose: fixes the shadow issue on the hood of the Grandmaster Cat/Lynx Armor.
- Nexus warns that it conflicts with mods editing the Grandmaster Lynx Armor `.w2ent`.
- `modlynx_witch` still appears in `mods.settings`, but no matching installed folder was found in the game `mods` directory during this audit.
- No scripts are included, so Script Merger is not needed.
