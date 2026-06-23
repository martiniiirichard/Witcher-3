# Assessment - W3EE Aefderaedd 5604

Date: 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/5604?tab=description`
- Local downloads:
  - `C:\Users\marti\Downloads\W3EE_Aefderaedd_Presets_1.5.1.zip-5604-1-5-1-1622587425.zip`
  - `C:\Users\marti\Downloads\mods_directory_manifest.txt-5604-1-5-1621633399.zip`

## Decision

Do not install Aefderaedd into the current Next-Gen stack.

Reason: the actual integration package expected by the manifest is not downloaded, and the available preset files are old menu/config replacements. Applying them would overwrite newer W3EE Redux, Random Encounters Reworked, Gwent Redux, and Modular Eyes menu definitions.

## What Was Found

The manifest expects a large script integration mod:

- `mod00008_aefderaedd`

It would touch broad script surfaces including:

- W3EE gameplay scripts
- Gwent Redux scripts
- FHUD scripts
- SharedUtils mappins/NPC interaction/noticeboards/dialog choices
- Bootstrap registry
- Modular Eyes
- Spawn Companions

No active `mod00008_aefderaedd` or Aefderaedd script folder exists in the game install.

## Current Stack Coverage

Many adjacent components are already installed independently:

- `modW3EE`
- `modReduxW3EE`
- `modRandomEncountersReworked`
- `modGwentRedux`
- `modPatchGwentRedux_W3EE_W3EERedux`
- `modmodulareyes`
- `modSpawnCompanions`
- `modBootstrap`
- `modBootstrap-registry`
- `modMenuStrings`
- SharedUtils modules

These are newer or heavily patched versions compared to the Aefderaedd-era preset assumptions.

## Preset Comparison

Downloaded presets contain only:

- `W3EnhancedEdition.xml`
- `modRandomEncountersReworked.xml`
- `modGwentReduxConfig.xml`
- `modulareyesconfig.xml`

Compared with current installed configs:

| File | Preset bytes | Current bytes | Risk |
|---|---:|---:|---|
| `W3EnhancedEdition.xml` | 66,605 | 81,873 | Would remove W3EE Redux/KolRedux preset structure. |
| `modRandomEncountersReworked.xml` | 380,080 | 353,253 | Different RER menu shape; current file includes later menu edits and layout fixes. |
| `modGwentReduxConfig.xml` | 10,219 | 9,936 | Minor but still version-sensitive. |
| `modulareyesconfig.xml` | 5,441 | 9,418 | Would collapse the newer 5-group Modular Eyes config into an older single-group config. |

The Modular Eyes preset has an `Aefderaedd` preset name, but installing it would remove newer Modular Eyes categories such as toxicity thresholds, vein effects, other settings, and other-witcher behavior.

## Related Archive Checked

`C:\Users\marti\Downloads\ModIntegrationAll-6049-1-95-1644927440.rar` was inspected because it sounded adjacent, but it is not the Aefderaedd 5604 integration package. It contains unrelated merged/script integration folders such as `mod0000_CezarMergedF`, Monster Hunt Challenge DLC, and Lazarus Project content. It was not installed.

## Outcome

No game files were changed.

This tab can be closed unless the user wants to intentionally attempt a manual, high-risk port of the old Aefderaedd script integration into the current Next-Gen W3EE Redux build.
