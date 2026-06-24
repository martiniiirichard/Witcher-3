# Slimmer Griffin Armor 5631

Date: 2026-06-23

## Source

- https://www.nexusmods.com/witcher3/mods/5631

## Installed Download

- `C:\Users\marti\Downloads\Slimmer Griffin Armor-5631-1-4-1625179914.zip`

## Installed Game Folder

- `mods\modSlenderGriffinArmor`

The archive has a wrapper folder named `SlimmerGriffinArmor`; only the inner real mod folder was copied into the game `mods` directory.

## Load Order

Added to both active `mods.settings` copies:

- `modSlenderGriffinArmor`: priority `201`

## Script Merger

No Script Merger pass needed. The archive contains bundled content only and no `.ws` scripts.

## Verification

- Confirmed `content\metadata.store` exists under the installed mod folder.
- DX12 smoke test passed when launching `bin\x64_dx12\witcher3.exe` with its own working directory; process stayed alive for 45 seconds and was killed manually.

## Notes

- Main residual risk is visual overlap with other Griffin armor model/texture replacers.
- The install avoided placing the wrapper folder directly in `mods`, which would not have been the loadable mod folder.
