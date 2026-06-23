# All-in-One RT Tweaks 7979

Source: https://www.nexusmods.com/witcher3/mods/7979

## Files

- Download: `C:\Users\marti\Downloads\AiO RT Tweaks v.3.2 - Ultra Plus Performance-7979-3-2-1739741820.zip`
- Installed to: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\platform\pc`
- Backup root: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\aio-rt-tweaks-7979-20260623-183501`

## Decision

Installed the `Ultra Plus Performance` preset as additive platform config `.ini` files.

This was applied after installing RTXGI Setting Unlocker 7426, which the mod page says is required for RTXGI setting overrides to work reliably on current Next Gen builds.

## Installed INIs

- `0_TW3_BetterMultiCoreUsage_NoLimit.ini`
- `0_TW3_FasterRTifNoRTShadows.ini`
- `0_TW3_Modified_FasterRTUltraPerformanceGlobalIllumination.ini`
- `0_TW3_Modified_General_Perf_Tweaks.ini`
- `0_TW3_Modified_Optimized RT.ini`
- `0_TW3_Modified_RTX_Tweaks.ini`

No existing RT tweak `.ini` files were present in `bin\config\platform\pc`, so this was a clean add.

## Notes

These files do not replace `dx12user.settings`. They are platform config overrides loaded from the game folder.

The current user profile still has RT disabled:

```ini
[Rendering/RT]
EnableRT=false
EnableRtRadiance=false
RTAOEnabled=false
```

So the RT-specific parts are mainly relevant if RT/RTXGI is enabled later. Some general rendering/resource-loading tweaks can still apply.

## Verification

- DX12 smoke test passed.
- The game process stayed running after 45 seconds and was then stopped manually by Codex.

## Rollback

Remove the six `0_TW3_*.ini` files listed above from:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\platform\pc`
