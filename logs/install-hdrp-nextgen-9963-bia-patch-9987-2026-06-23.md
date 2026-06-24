# HDRP NextGen 9963 + BiA HDRP Patch 9987

Date: 2026-06-23

## Sources

- HDRP: https://www.nexusmods.com/witcher3/mods/9963
- BiA HDRP compatibility patch: https://www.nexusmods.com/witcher3/mods/9987

## Installed Downloads

- `C:\Users\marti\Downloads\The Witcher 3 HD Reworked Project NextGen Edition-9963-20-0-fixed-1736185630.7z`
- `C:\Users\marti\Downloads\BiA - HDRP Compatible Patch-9987-1-1-1764609344.zip`

Skipped the old-gen HDRP archive because it is not the active NextGen package and the local old-gen file is incomplete/zero-byte.

## Installed Game Folders

HDRP main package:

- `mods\mod00000HDReworkedProject`
- `mods\modHDReworkedProject`
- `mods\modHDReworkedProject2`
- `mods\modHDReworkedProject3`
- `mods\modHDReworkedProject4`

BiA compatibility patch:

- `mods\mod000000aHDRP_BiA`

## Config Files Overwritten By HDRP

HDRP replaced these game config files:

- `bin\config\base\rendering.ini`
- `bin\config\platform\pc\rendering.ini`
- `bin\config\r4game\user_config_matrix\pc\graphics.xml`
- `bin\config\r4game\user_config_matrix\pc\graphicsdx11.xml`

Backup path:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\HDRP_9963_20260623_195039`

Risk note: these config files overlap with prior graphics/menu/RT tweak work, especially the graphics menu XML from `modTweaks`. For HDRP, I let the HDRP package win because its install instructions require those replacements. If graphics menu options look wrong later, compare against the backup above before changing mod content.

## Load Order

Added to both active `mods.settings` copies:

- `mod00000HDReworkedProject`: priority `189`
- `modHDReworkedProject`: priority `190`
- `modHDReworkedProject2`: priority `191`
- `modHDReworkedProject3`: priority `192`
- `modHDReworkedProject4`: priority `193`
- `mod000000aHDRP_BiA`: priority `194`

The BiA patch is intentionally after the HDRP folders so its overlapping bundled content can win.

## Script Merger

No Script Merger pass needed. HDRP and the BiA HDRP patch are bundled texture/cache/config content only and do not add WitcherScript files.

## Verification

- Confirmed the five HDRP mod folders and the BiA HDRP patch folder exist under `mods`.
- Confirmed HDRP changed all four expected graphics/rendering config hashes.
- DX12 smoke test passed when launching `bin\x64_dx12\witcher3.exe` with its own working directory; process stayed alive for 45 seconds and was killed manually.

## Follow-Up

- Do a visual pass in a loaded save when convenient: inspect Geralt/NPC skin, armor, roads/stone/wood, vegetation, and Novigrad/White Orchard/Toussaint surfaces.
- If there is a rendering option/menu issue, compare the backed-up `graphics.xml` and `graphicsdx11.xml` against HDRP's installed versions before editing.
