# RT Config Tweaks 8865 + 8890

Date: 2026-06-27

Sources:

- https://www.nexusmods.com/witcher3/mods/8865
- https://www.nexusmods.com/witcher3/mods/8890

Downloads:

- `C:\Users\marti\Downloads\Ray Bleach-8890-1-0-1709182310.zip`
- `C:\Users\marti\Downloads\Improved RT Reflections and Shadows-8865-1-03-1755030985.rar`
- `C:\Users\marti\Downloads\Improved RT Reflections and Shadows Sharp Shadows-8865-1-02-1755022034.rar`

Installed files:

- `bin\config\platform\pc\BlueFix_RTXMirrors.ini`
- `bin\config\platform\pc\RT_ImprovedReflectionsAndShadows.ini`

Decision:

- Installed the standard `Improved RT Reflections and Shadows` variant.
- Skipped the `Sharp Shadows` variant for now because it sets `SunAngularDiameter=0`, which can create harsher, less natural lighting and is less aligned with the current immersive/weather stack.
- Installed `Ray Bleach` because it is a tiny additive RTX mirror tweak and does not replace scripts, bundles, or HDRP files.

Notes:

- These are config-only changes. No Script Merger pass is required.
- Existing RT tweak files remain in place:
  - `0_TW3_FasterRTifNoRTShadows.ini`
  - `0_TW3_Modified_RTX_Tweaks.ini`
- Backup created under:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\rt-config-tweaks-8865-8890-20260627-144332`
