# Skip Decision - Waterwheel2 and Shadow Flickers Fix - 2026-06-24

## Decision

Skip the remaining two startup blockers for now:

- `modwaterwheel2`
- `mod_ShadowFlickersFix`

## Reason

Both reproduced the known headless startup hang:

- `witcher3.exe` stays alive
- no visible top-level game window
- memory parks around 4.1 GB

They are lower-value than the larger quest/lore mods and not worth a deeper cooked-asset salvage pass right now.

## Current State

Both mods are held out of the active `mods` folder:

- `modwaterwheel2` is under `_codex_isolation_hold\slice_20260624_1000_1400`
- `mod_ShadowFlickersFix` is under `_codex_isolation_hold\recent_non_menu_longtest`

Both are set to `Enabled=0` in:

- `C:\Games\The Witcher 3\mods.settings`
- `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`

## Related Reduced Installs

The higher-value startup blockers were partially salvaged instead of skipped:

- `modWitcherLoreCollection`: active with `blob0.bundle` disabled
- `modW3QE`: active with `blob0.bundle` disabled

Do not restore `modwaterwheel2` or `mod_ShadowFlickersFix` without a strict visible-window launch test.
