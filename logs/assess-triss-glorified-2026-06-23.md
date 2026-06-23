# Assessment - Triss (G)Lorified - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/3223`
- File ID: `24565`

## Assessment

The linked file maps to the local download name:

- `C:\Users\marti\Downloads\Triss (G)Lorifed-3223-LATEST-1561002981.rar`

Initial download state was incomplete, but the archive later completed and was reassessed:

- `Triss (G)Lorifed-3223-LATEST-1561002981.rar` exists and is complete.

Completed archive contents:

- `modTrissGlorified\content\blob0.bundle`
- `modTrissGlorified\content\buffers0.bundle`
- `modTrissGlorified\content\metadata.store`
- `modTrissGlorified\content\texture.cache`

It contains:

- `0` `.ws` script files
- `0` `.xml` menu files

## Decision

Not installed.

This is a full Triss appearance replacer and overlaps the currently installed Triss appearance stack:

- `modIMTTrissNGE_Main`
- `mod_triss_earrings_fix`
- `modTrissCBTrueDress`

It is not redundant in the sense of being identical, but it is mutually exclusive with the primary Triss appearance replacer. Installing it at the end of the load order would make `modTrissGlorified` win Triss appearance conflicts and effectively replace the current IMT Triss look.

## Notes

Potential overlap areas:

- Triss appearance/model/texture mods.
- Corvo Bianco guest/appearance variants.
- Non-mergeable bundled asset conflicts are more likely than script conflicts.

Safe install path later:

1. Decide whether `modTrissGlorified` should replace `modIMTTrissNGE_Main`.
2. If yes, install `modTrissGlorified` at high priority after the current Triss appearance mods.
3. Keep earrings and Corvo Bianco dress only if visual testing shows they compose cleanly.
4. Smoke test Triss in normal scenes and Corvo Bianco guest contexts.
