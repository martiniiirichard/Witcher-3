# Install - Ice Breath Next Gen

Date: 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/7302?tab=files&file_id=62791`
- Download: `C:\Users\marti\Downloads\Ice Breath Next Gen-7302-1-06-1742909024.zip`

## Installed

- `Mods\modIceBreath`
- `DLC\DLCIceBreath`
- `bin\config\r4game\user_config_matrix\pc\IceBreath.xml`

Added `IceBreath.xml;` to both:

- `dx11filelist.txt`
- `dx12filelist.txt`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modIceBreath]
Enabled=1
Priority=171
```

## Bootstrap Registry

The archive includes its own `mods_registry.ws`, but the current loadout uses the shared Bootstrap registry at:

`Mods\modBootstrap-registry\content\scripts\local\mods_registry.ws`

To avoid duplicate `CModRegistry` class definitions, the archive-local file was disabled:

`Mods\modIceBreath\content\scripts\local\mods_registry.ws.disabled-by-codex-20260623-163506`

The shared registry now contains:

```witcherscript
add(modCreate_CIceBreathMod());
```

## Compatibility Decision

Skipped the older `Skellige Ice Breath Compatibility - Next Gen` patch from the Skellige Winter Weather page.

Reason: the downloaded Ice Breath Next Gen 1.06 script already includes weather names for:

- Skellige Winter Weather
- Realistic Weather
- Immersive Lighting
- More Variable Weather

The older compatibility patch would replace the current script with an older, smaller 1.02-style file and risk losing newer options such as dialogue/cutscene handling.

## Backups

Created backups under:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\icebreath-20260623-163425`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\icebreath-finish-20260623-163448`

## Verification

- Static checks passed:
  - `DLCIceBreath\content\metadata.store` exists.
  - `IceBreath.xml` exists and is registered in both DX11 and DX12 filelists.
  - `modIceBreath` is enabled in `mods.settings`.
  - Shared Bootstrap registry has `modCreate_CIceBreathMod()`.
  - Duplicate local registry script is disabled.
- Runtime smoke passed:
  - Launched `bin\x64_dx12\witcher3.exe`.
  - `witcher3.exe` stayed alive after 55 seconds.
  - Test process was closed after verification.

## Notes

This is a script-bearing Bootstrap mod. If future compile errors mention duplicate `CModRegistry`, check that no active `mods_registry.ws` exists inside individual Bootstrap mods.
