# Everlasting Shrines of Verna 12293

Date: 2026-06-24

## Mod

Nexus: `https://www.nexusmods.com/witcher3/mods/12293`

Installed archive:

- `C:\Users\marti\Downloads\Everlasting Shrines Of Verna-12293-2-1780454240.zip`

## Installed

- `mods\modVernaShrine_Everlasting`

Added settings entry:

```ini
[modVernaShrine_Everlasting]
Enabled=1
Priority=228
```

This is intentionally higher priority than `modexpansionzero` in this stack's ordering model, where lower numeric priority wins. It lets the everlasting Verna shrine effect win over Time of the Sword and Axe.

Note: this entry was initially added as priority 229, then corrected to 228 after verifying that `modexpansionzero` was priority 229 and was otherwise winning the `local\effects\vitalityRaise.ws` conflict.

## Files

The archive contains one script:

- `content\scripts\local\effects\vitalityRaise.ws`

## Backup

Backup folder:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\VernaEverlasting_12293_20260624_065800`

## Verification

Smoke compile passed:

`SmokePassed_StillRunningAfter45s`
