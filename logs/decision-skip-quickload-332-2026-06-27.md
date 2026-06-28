# Decision: Skip QuickLoad (332)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/332
Archive: `C:\Users\marti\Downloads\QuickLoad-332-v4-0-4-1767435456.7z`

## Decision

Skip.

## Why

The archive includes:

- `modQuickLoad/content/scripts/game/player/playerInput.ws`
- `modQuickLoad/bin/config/r4game/user_config_matrix/pc/modQuickLoadConfig.xml`
- `modQuickLoad/input.settings.part.txt`
- `modQuickLoad/input.xml.part.txt`

`playerInput.ws` is a hot file in the current W3EE/E3 HUD/Menu Organizer/input stack. Menu Organizer already exposes quickload-style infrastructure, so this adds risk for a convenience feature.

## Status

No live game files changed.
