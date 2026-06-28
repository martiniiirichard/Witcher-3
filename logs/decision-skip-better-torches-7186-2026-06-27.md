# Decision: Skip Better Torches Next-Gen (7186)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/7186
Archive: `C:\Users\marti\Downloads\Better Torches Next-Gen-7186-4-4-0-1689801474.7z`

## Decision

Skip.

## Why

This is not just a torch visual asset package. The archive includes full script replacements for:

- `game/explorations/exploration_movement_system/exploration_substates/explorationStateInteraction.ws`
- `game/gameplay/items/itemEntity.ws`
- `game/player/playerInput.ws`
- `game/player/r4Player.ws`
- `game/player/states/vehicles/mountHorse.ws`
- `game/player/states/vehicles/useVehicle.ws`

Those are broad hot zones in the current W3EE/BiA/Immersive Cam/Natural Torchlight stack.

The current fire/torch lane is intentional:

- True Fires owns many fire/torch visuals.
- Natural Torchlight behavior is manually grafted into merged files.
- Natural Torchlight menu/settings are already documented for tuning.

Better Torches would add high script risk for overlapping functionality.

## Status

No live game files changed.
