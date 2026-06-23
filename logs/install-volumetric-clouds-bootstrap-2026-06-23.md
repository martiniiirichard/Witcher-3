# Volumetric Clouds Over Skellige Bootstrap Install

Date: 2026-06-23

Source:
- Nexus mod 1302
- Downloaded archive: `C:\Users\marti\Downloads\modVolumetricCloudsBootstrap_131-1302-.zip`
- Installed package: Bootstrap variant `modVolumetricCloudsBootstrap1_31`

Install decision:
- Installed the Bootstrap version rather than any direct `playerWitcher.ws` edit path.
- This avoids a direct vanilla/player script conflict with W3EE, AMM, and the existing merged scripts.

Installed files:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modVolumetricCloudsBootstrap1_31`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\DLC\DLCVolumetricCloudsBootstrap`

Configuration changes:
- Added `add(modCreate_VolumetricCloudsMod());` to:
  `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modBootstrap-registry\content\scripts\local\mods_registry.ws`
- Added `[modVolumetricCloudsBootstrap1_31]` to:
  `C:\Games\The Witcher 3\mods.settings`
- Assigned priority `170`.

Backups:
- Bootstrap registry backup:
  `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modBootstrap-registry\content\scripts\local\mods_registry.ws.codex-backup-volumetric-clouds-20260623-160044`
- Mods settings backup:
  `C:\Games\The Witcher 3\mods.settings.codex-backup-volumetric-clouds-20260623-160044`

Static verification:
- Registry contains `add(modCreate_VolumetricCloudsMod());`.
- Mod script defines:
  - `class CVolumetricCloudsMod extends CEntityMod`
  - `class CVolumetricClouds extends CEntity`
  - `function modCreate_VolumetricCloudsMod() : CMod`
- Installed mod has one active script:
  `content\scripts\local\game\VolumetricClouds.ws`
- No direct `playerWitcher.ws` or `r4Player.ws` override was installed.

Risk notes:
- Compile risk should be low because this is Bootstrap-based.
- Visual/performance risk exists because the stack already has Skellige Winter Weather, New Clouds 3.0, and New Toussaint Clouds.
- In-game verification should focus on Skellige mountain/coast visibility, cloud density, FPS, and whether fog/cloud effects look excessive with winter weather enabled.

Runtime verification:
- Launch compile test passed after install.

Pending verification:
- Skellige visual smoke test.
