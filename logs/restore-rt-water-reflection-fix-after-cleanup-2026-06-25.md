# Restore: RT Water Reflection Fix full bundle

Date: 2026-06-25

## Context

`modRTWaterReflectionColorFix` previously launched only in script-only state. Its `content\blob0.bundle` produced the no-window startup hang while the stack was at the loader/package pressure cliff.

After cleanup, active physical mod folders were reduced from `206` to `196`.

## Change

Restored:

`mods\modRTWaterReflectionColorFix\content\blob0.bundle`

from:

`mods\modRTWaterReflectionColorFix\content\blob0.bundle.disabled-by-codex-startup-hang-test`

The mod remains enabled in `mods.settings`.

## Verification

DX12 launch smoke test passed with the full RT Water bundle active:

- active physical folders: `196`
- visible window at about `15s`
- title: `The Witcher 3`
- first visible-window memory observation: about `5678 MB`

Conclusion: the earlier failure was consistent with loader/package pressure, not an inherently broken RT Water bundle.
