# Kaer Morhen's Bastion Restored 9723

Date: 2026-06-26

## Source

- Nexus page: https://www.nexusmods.com/witcher3/mods/9723
- Download: `C:\Users\marti\Downloads\Kaer Morhen's Bastion restored-9723-1-3-1729026448.zip`

## Installed

- `Mods\modkaermorhensbastionrestoredtoitsancientsplendor`

## Settings

Added to `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`:

```ini
[modkaermorhensbastionrestoredtoitsancientsplendor]
Enabled=1
Priority=261
```

## Priority Rationale

This mod has no `.ws` scripts, so it does not require Script Merger.

It is bundled Kaer Morhen world/mesh content, so the main risk is worldspace overlap with the active Kaer Morhen stack. Priority `261` puts it behind the currently selected `mod_KaerMorhenEnhanced` layer at `260`, while still ahead of the narrow `modKMArmoryRubbleRemoved` cleanup at `264`.

## Verification

- DX12 direct-launch smoke test passed.
- `witcher3` process was present and responding after 65 seconds.
- Process was closed after the test.

## Residual Risk

No script compiler risk was observed, but Kaer Morhen should still get an in-world visual pass later. This may add or hide some Bastion geometry depending on bundled non-text priority conflicts with the active Kaer Morhen overhaul stack.
