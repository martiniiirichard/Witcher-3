# Install - Useful Place of Power Map Pin 11300

Date: 2026-06-27

Source:

- Nexus: https://www.nexusmods.com/witcher3/mods/11300
- Archive: `C:\Users\marti\Downloads\Useful Place of Power Map Pin - Next-Gen-11300-1-1-1764868477.7z`

## Decision

Installed.

Reason: tiny script-only helper that improves Place of Power map pin descriptions by appending the sign type/color. It does not ship full vanilla menu scripts.

## Installed Folder

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modUsefulPOPMapPin`

## Load Order

Added to active `mods.settings` files:

```ini
[modUsefulPOPMapPin]
Enabled=1
Priority=266
```

## Payload

- `witcherscript.toml`
- `content\scripts\local\UsefulPOPMapPin.ws`

The script:

- adds `SPlaceOfPowerMapPinSign`
- adds `popMapPinSigns` to `CR4MapMenu`
- wraps `CR4MapMenu.OnConfigUI`
- wraps `CR4MapMenu.AddPinTypeData`
- appends colored Aard/Yrden/Igni/Axii/Quen text to Place of Power descriptions

## Compatibility Check

Active `mapMenu.ws` owners:

- `mod0_E3HUD_W3EER_NG`
- `modW3EE`

Both expose:

```witcherscript
private function AddPinTypeData(out dataObject : CScriptedFlashObject, targetPin: SCommonMapPinInstance) : void
```

The candidate uses the matching wrapper signature. No full `mapMenu.ws` override is shipped.

## Backup

- `backups\useful-pop-map-pin-11300-install-20260627-141348\mods.settings.before`

## Verification

DX12 direct-launch smoke after install:

- `witcher3.exe` running after 65 seconds
- visible window: `True`
- responding: `True`
- working set: about `1949.8 MB`

No Script Merger GUI action was needed because this is a local annotation/wrapper script.
