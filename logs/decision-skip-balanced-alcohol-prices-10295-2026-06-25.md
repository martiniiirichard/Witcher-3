# Balanced Alcohol Prices - 10295

Date: 2026-06-25

Source:
- https://www.nexusmods.com/witcher3/mods/10295

Archive:
- `C:\Users\marti\Downloads\Balanced Alcohol Prices-10295-1-0-1-1761992119.zip`

Purpose:
- Adjusts/balances alcohol item prices.

Package:
- Content-only mod:
  - `mods\modBalancedAlcoholPrices\content\blob0.bundle`
  - `mods\modBalancedAlcoholPrices\content\metadata.store`
  - `mods\modBalancedAlcoholPrices\content\info.json`
- No scripts.
- No Script Merger work available.

Compatibility context:
- Current stack already has economy/alcohol-related mods:
  - `mod00FlorenEconomySystem_W3EE_REDUX`
  - `modAlcoholFactory`
- Installed conservatively at late priority `260` so the existing economy stack would remain dominant if records overlapped.

Result:
- Active install caused the known no-window startup hang:
  - `MainWindowHandle=0`
  - `visible=False`
  - memory plateau around 4127 MB
  - no script compilation dialog

Action:
- Disabled the mod folder:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\DISABLED_modBalancedAlcoholPrices.disabled-by-codex-startup-hang-10295-20260625102159`
- Left the settings entry disabled in both active `mods.settings` files:

```ini
[modBalancedAlcoholPrices]
Enabled=0
Priority=260
```

Verification:
- Baseline DX12 launch passed after disabling:
  - visible full-screen `The Witcher 3`
  - rect `0,0,1920,1080`
  - memory around 5922 MB

Decision:
- Skip for now.
- This is not a script issue. It behaves like a content/package startup incompatibility and is also likely redundant with the existing economy stack.
