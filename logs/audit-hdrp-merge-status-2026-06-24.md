# HDRP Merge Status Audit

Date: 2026-06-24

## Result

No Script Merger work is needed for the active HDRP stack.

## Active HDRP-Related Mods

- `mod00000HDReworkedProject`
- `modHDReworkedProject`
- `modHDReworkedProject2`
- `modHDReworkedProject3`
- `modHDReworkedProject4`
- `mod000000aHDRP_BiA`
- `modATrueFiresHDReworkedProjectCompatibility`

These folders contain bundle/cache/config-style content only:

- `blob0.bundle`
- `buffers0.bundle`
- `metadata.store`
- `texture.cache`
- `collision.cache`
- `info.json`
- `pl.w3strings`

None of the active HDRP folders above contain WitcherScript files.

## Current Load Order

Current observed priorities in both active `mods.settings` files:

- `modATrueFiresHDReworkedProjectCompatibility`: `167`
- `mod00000HDReworkedProject`: `191`
- `modHDReworkedProject`: `192`
- `modHDReworkedProject2`: `193`
- `modHDReworkedProject3`: `194`
- `modHDReworkedProject4`: `195`
- `mod000000aHDRP_BiA`: `196`

The BiA HDRP patch still loads after the main HDRP folders, which is the important ordering rule.

## Backup

HDRP config overwrite backup remains available at:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\HDRP_9963_20260623_195039`

That backup contains the pre-HDRP graphics/rendering config files:

- `bin\config\base\rendering.ini`
- `bin\config\platform\pc\rendering.ini`
- `bin\config\r4game\user_config_matrix\pc\graphics.xml`
- `bin\config\r4game\user_config_matrix\pc\graphicsdx11.xml`

## Separate Testing Utility

`modHDRPTestApple` is not part of HDRP itself. It is a small test utility with one script:

- `content\scripts\local\HDRPTestApple.ws`

Search found no duplicate `HDRPtest`, `HDRP_test`, or `InitialiseHDRPtest` definitions elsewhere in `mods`, so no merge is currently required for that utility either.
