# Quarantine: E3 Quen visual mods

Date: 2026-06-25

## Decision

The user does not want/need E3 visual design for Quen. These mods are cosmetic VFX overrides, while W3EE already owns Quen gameplay/mechanics.

Quarantined:

- `modE3QuenEER`
- `mod0E3Quen_NextGen`
- `modE3Quen`

Moved to:

- `DISABLED_modE3QuenEER.disabled-by-codex-not-needed-e3-visual-design-20260625`
- `DISABLED_mod0E3Quen_NextGen.disabled-by-codex-not-needed-e3-visual-design-20260625`
- `DISABLED_modE3Quen.disabled-by-codex-not-needed-e3-visual-design-20260625`

Updated both `mods.settings` files to `Enabled=0` for all three.

## Loader impact

Active physical mod folders reduced from `206` to `203`.

This matters because the stack is near a loader/package pressure cliff where even a few active folders can decide whether content bundles launch.

## Verification

DX12 launch smoke test passed after removal:

- visible window at about `15s`
- title: `The Witcher 3`
- private memory reached about `5712 MB`

