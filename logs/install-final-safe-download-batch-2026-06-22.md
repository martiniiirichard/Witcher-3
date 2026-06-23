# Final Safe Download Batch

Date: 2026-06-22

Installed:
- `dlcAlchemyRecipesRewards`
  - Source: `Alchemy Recipes Reward-9955-2-0-1767814703.zip`
  - DLC-only bundle.
- `modW3EETrophies`
  - Source: `W3EE Trophies-9628-1-0-1725539831.zip`
  - Added to `mods.settings` at priority `121`.
- `modDilatedPupils`
  - Source: `modDilatedPupils-5576-1-0-0-1615449927.7z`
  - Added to `mods.settings` at priority `122`.
- `modScabbards` and `DLCScabbards`
  - Source: `All NPC Scabbards v1.22-1569-1-22.rar`
  - Added `modScabbards` to `mods.settings` at priority `123`.
- `modnewlightningfx` and `dlcnewlightningfx`
  - Source: `New Lightning Effect - Next Gen Version-2985-3-0-1780800527.7z`
  - Added `NewLightningFX.xml;` to both DX11 and DX12 menu filelists.
  - Added to `mods.settings` at priority `124`.
  - Did not apply the optional alternative `weathers_list.ws`, because no dependent weather overhaul is currently being installed.
- `modLessIndignantNPCs`
  - Source: `Less Indignant NPCs v1.1-4987-1-1-1595248968.zip`
  - Added to `mods.settings` at priority `125`.
- `modSwordscampfire` and `dlcSwordsAndMeditation`
  - Source: `Swords and Meditation-4064-2-1-ng-1671611660.rar`
  - Added `modASwordscampfire.xml;` to both DX11 and DX12 menu filelists.
  - Added to `mods.settings` at priority `126`.
- `modactivemedallion` and `dlcactivemedallion`
  - Source: `Active Medallion - Next Gen 4.04-6251-2-23b-1740359718.7z`
  - Added `activemedallionconfig.xml;` to both DX11 and DX12 menu filelists.
  - Added to `mods.settings` at priority `127`.
  - Skipped the bundled `mod_sharedutils_oneliners` folder to avoid duplicate `SUOL_*` class definitions. The existing sharedutils oneliner install is reused.

Smoke Tests:
- Launched the DX12 direct launcher after the content-only/New Lightning batch; `witcher3` stayed alive after 45 seconds, then was stopped.
- Launched again after `modLessIndignantNPCs`; `witcher3` stayed alive after 45 seconds, then was stopped.
- Launched again after `modSwordscampfire`; `witcher3` stayed alive after 45 seconds, then was stopped.
- Launched again after `modactivemedallion`; `witcher3` stayed alive after 45 seconds, then was stopped.

Backups:
- `backups/before-safe-content-batch-20260622-231013`
- `backups/before-new-lightning-fx-20260622-231211`
- `backups/before-less-indignant-npcs-20260622-231401`
- `backups/before-swords-meditation-20260622-231533`
- `backups/before-active-medallion-20260622-231737`

Deferred:
- `W3EE Redux - Vigor Regen Tweak`
  - Replaces `modW3EE`'s `adrenaline.ws` directly and removes existing W3EE Redux mutation/White Honey logic. Not safe to apply unattended.
- `Community Patch - Besserwisser and Nitpicker`
  - Replaces base content and core scripts (`actor.ws`, `playerWitcher.ws`, `r4Player.ws`). Too broad for unattended install on this stack.
- `Shields`
  - Large gameplay/script mod touching `PlayerAbilityManager.ws`, `playerWitcher.ws`, `r4Player.ws`, projectiles, and local classes. Needs a dedicated merge pass.
- `CCS`, `Icy Ocean`, `Enable Mimics`
  - Override core player/effect/actor scripts already heavily merged by W3EE and other mods.
- `Immersive Sound`
  - Overrides `r4Player.ws`, focus, boat, and interactive scripts.
- `Less Is More`
  - Overrides `engine/sound.ws`, already owned by W3EE.
- `LiveBestiary`
  - Overrides `glossaryBestiaryMenu.ws`, already touched by W3EE, Better Icons, and E3 HUD.
- `Natural Torchlight` and `Smart Magic Lamp`
  - Both override `itemEntity.ws`, already present in W3EE and merged files.
- Incomplete zero-byte or `.part` downloads:
  - HD Reworked Project, HD Tree LOD Billboards, Music Overhaul Project Redux, and Dilated Pupils Black Irises.
