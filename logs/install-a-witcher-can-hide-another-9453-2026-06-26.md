# Install - A Witcher Can Hide Another

Date: 2026-06-26

## Source

- Nexus ID: `9453`
- Archive: `C:\Users\marti\Downloads\A Witcher Can Hide Another-9453-1-1-1-1761481305.7z`

## Assessment

This is a standalone voiced quest DLC with:

- DLC payload: `dlcAWitcherCanHideAnother`
- Mod payload: `modAWitcherCanHideAnother`
- Input payload: `NGCL_add_to_input.settings`

Despite the readme calling it standalone and merge-free, it is not content-only. It includes `20` script files:

- base exploration movement system scripts
- skating substates
- local `ngcl` quest/helper scripts

Pre-install checks:

- No existing `modAWitcherCanHideAnother` or `dlcAWitcherCanHideAnother` install was found.
- No exact installed mod script-path collisions were found for the candidate `.ws` files.
- No installed mod class-name collisions were found for the major exploration/skating classes.
- Active `input.settings` did not already contain a `[Skating]` section.

## Installed

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modAWitcherCanHideAnother`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\DLC\dlcAWitcherCanHideAnother`

Load order:

```ini
[modAWitcherCanHideAnother]
Enabled=1
Priority=265
```

Input settings:

- Appended `NGCL_add_to_input.settings` to `C:\Users\marti\OneDrive\Documents\The Witcher 3\input.settings`.
- This added the `[Skating]` input context used by the quest's playable-character/skating mechanics.

Backup:

- `backups\a-witcher-can-hide-another-20260626-142011\mods.settings.before`
- `backups\a-witcher-can-hide-another-20260626-142011\input.settings.before`

## Verification

- Script Merger was not required before launch: no exact installed mod script-path conflict was detected.
- DX12 launch smoke passed. `witcher3.exe` stayed alive after 65 seconds.

## Residual Risk

This validates script compilation and basic launch only. The meaningful test is in-game:

- quest start availability
- new world transition
- voiced dialogue playback
- playable-character controls
- skating input/action behavior
- save/load after entering and exiting the new quest area
