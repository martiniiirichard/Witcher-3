# Assessment - Smart Magic Lamp - 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/2943`
- User linked the posts tab, indicating compatibility/install discussion matters.

## Download

Downloaded:

- `C:\Users\marti\Downloads\Smart Magic Lamp (Shared)-2943-3-31-1.zip`

Archive contents:

- `modSmartMagicLamp`
- `game\gameplay\items\itemEntity.ws`
- `local\smartLamp.ws`
- `blob0.bundle`
- `metadata.store`

It contains:

- `2` `.ws` script files
- `0` `.xml` menu files

## Current Stack

`itemEntity.ws` is already owned by:

- `modW3EE`
- `mod0000_MergedFiles`

Shared Imports is already installed and enabled:

- `modSharedImports`

## Decision

Deferred.

Do not install raw. This requires a deliberate Script Merger pass because it modifies `itemEntity.ws`, which is already part of the current W3EE/merged script stack.

## Notes

Potential safe path later:

1. Install `modSmartMagicLamp`.
2. Run Script Merger.
3. Merge `itemEntity.ws` against the existing merged/W3EE script state.
4. Launch compile test.
5. Smoke test:
   - magic lamp use
   - lamp near ghost/anomaly behavior
   - ordinary item equip/visibility behavior
   - any light/torch interactions

No optional menu files were installed during this assessment.
