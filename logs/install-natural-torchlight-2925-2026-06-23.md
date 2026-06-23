# Install - Natural Torchlight 2925

Date: 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/2925?tab=files&file_id=20920`
- Downloads:
  - `C:\Users\marti\Downloads\Natural Torchlight (GUI)-2925-4-31-1.zip`
  - `C:\Users\marti\Downloads\Natural Torchlight (Shared)-2925-4-31-1.zip`

## Installed

- `Mods\modNaturalTorchlight`
- `bin\config\r4game\user_config_matrix\pc\naturaltorchlight.xml`

Added `naturaltorchlight.xml;` to:

- `dx11filelist.txt`
- `dx12filelist.txt`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modNaturalTorchlight]
Enabled=1
Priority=174
```

## Script Strategy

The archive ships an `itemEntity.ws`, but the current stack already owns that file through:

`Mods\mod0000_MergedFiles\content\scripts\game\gameplay\items\itemEntity.ws`

That merged file already contained the Natural Torchlight utility block from the earlier Smart Magic Lamp work:

- `CNaturalLightManager`
- `NaturalTorchlight` GUI group usage

The missing piece was the actual torch inheritance change. Applied this manually to the active merged file:

```witcherscript
class W3LightSource extends W3NaturalTorchlight
```

The mod's local `W3NaturalTorchlight` class was then inlined into the active merged `itemEntity.ws` before `W3LightSource`. This avoids compile-order/base-class resolution issues from relying on a separate local script.

Disabled duplicate shipped scripts under `modNaturalTorchlight`:

- `content\scripts\game\gameplay\items\itemEntity.ws.disabled-by-codex-20260623-174106`
- `content\scripts\local\naturalTorchlight.ws.disabled-by-codex-20260623-174321`

No active `.ws` files remain under `modNaturalTorchlight`; the active script merge lives in `mod0000_MergedFiles`.

## Backup

Created:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_backups\natural-torchlight-20260623-174106`

Additional backup before inlining the local class:

`itemEntity.ws.codex-backup-natural-torchlight-class-inline-20260623-174321`

## Verification

Static checks:

- `naturaltorchlight.xml` exists and is registered in both DX11 and DX12 filelists.
- `modNaturalTorchlight` is enabled at priority `174`.
- Active merged `itemEntity.ws` contains:
  - `class W3NaturalTorchlight extends W3UsableItem`
  - `class W3LightSource extends W3NaturalTorchlight`

Runtime:

- User confirmed the game passes after the inline-class fix.

## Generalizable Technique

When an old mod changes a class inheritance in a heavily merged core file, define the required base/helper class in the same active merged file before the derived class. This avoids relying on separate local script compile order and reduces duplicate-script conflict risk.
