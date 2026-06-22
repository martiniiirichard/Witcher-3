# Knight Accessories Install Checkpoint

Date: 2026-06-22

## Mod

- Nexus: `https://www.nexusmods.com/witcher3/mods/2143`
- Downloaded archives:
  - `Hip Armor-2143-1.rar`
  - `Amm Knight Necklace and Belt-2143-2-1.rar`
  - `Remove Witcher Medallion on Knight Armors-2143-2-1.rar`

## Install Decision

Installed two unique mod folders:

- `modKnightHips`
- `modKnightPendant`

The two pendant/medallion archives were byte-for-byte identical and both contained the same `modKnightPendant` folder, so only one copy was installed.

## Runtime Changes

Created:

- `mods/modKnightHips`
- `mods/modKnightPendant`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modKnightHips]
Enabled=1
Priority=17

[modKnightPendant]
Enabled=1
Priority=18
```

## Inspection Notes

- The archive roots contain only packed content files: `blob0.bundle`, `metadata.store`, and `texture.cache`.
- Unpacked bundle contents contain only texture files:
  - `modKnightHips`: one Toussaint knight hip texture.
  - `modKnightPendant`: two Toussaint citizen/knight pendant textures.
- No `.ws` script files were added.
- No Script Merger work is expected.

## Backup

Runtime backup created before install:

- `backups/knight-accessories-2143-20260622-100006`

## Verification

- Confirmed both mod folders exist in the game root.
- Confirmed both mod entries exist in `mods.settings`.
- Confirmed no `.ws` scripts were added.
- User confirmed the game launched and ran fine after install.

Next step: commit this working checkpoint before installing additional mods.
