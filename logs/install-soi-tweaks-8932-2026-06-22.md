# Shades of Iron Tweaks Install Checkpoint

Date: 2026-06-22

## Mod

- Nexus: `https://www.nexusmods.com/witcher3/mods/8932`
- Archive: `modShadesOfIron_Tweaks-8932-1-00-1710109609.rar`
- Staged at: `staging/soi-tweaks-8932`

## Install Decision

Installed as a separate reversible mod folder instead of overwriting the existing Shades of Iron files.

Reason: the Nexus page says the tweak was only tested on old-gen 1.32, while this stack is Next-Gen 4.04 with Shades of Iron v2, W3EE Redux, AMM, and the SoI W3EE Redux patch. Keeping it separate makes rollback simple.

## Runtime Changes

Created:

- `mods/modShadesOfIronTweaks/content/blob0.bundle`
- `mods/modShadesOfIronTweaks/content/metadata.store`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modShadesOfIronTweaks]
Enabled=1
Priority=16
```

## Inspection Notes

- The archive contains no `.ws` script files.
- No Script Merger work is expected.
- The bundle unpacks to 59 files, mostly `dlc/dlcsoi_chests/levels/.../interactive_entities.w2l`.
- 58 of those unpacked paths match files inside the installed `dlcShadesChests` bundle.
- One extra unpacked file is `characters/player_entities/geralt/geralt_inventory_release.w2ent`.

## Backup

Runtime backup created before install:

- `backups/soi-tweaks-8932-20260622-094835`

## Verification

- Confirmed `modShadesOfIronTweaks` contains only `blob0.bundle` and `metadata.store`.
- Confirmed `mods.settings` contains the new enabled priority entry.
- Confirmed no `.ws` scripts were added by this tweak.
- User confirmed the game launched and ran fine after install.

Next step: commit this working checkpoint before installing additional mods.
