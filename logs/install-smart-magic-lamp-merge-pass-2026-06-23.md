# Smart Magic Lamp Merge Pass

Date: 2026-06-23

Source:
- Nexus mod 2943
- Downloaded archive: `C:\Users\marti\Downloads\Smart Magic Lamp (Shared)-2943-3-31-1.zip`
- Staging folder: `C:\Users\marti\OneDrive\Documents\New project\Witcher-3\staging\inspect-smart-magic-lamp-20260623\modSmartMagicLamp`

Install decision:
- Installed `modSmartMagicLamp` into the game `Mods` folder.
- Did not leave the mod's shipped `game\gameplay\items\itemEntity.ws` active.
- Manually merged the required Smart Lamp changes into the existing active merged file instead:
  `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\mod0000_MergedFiles\content\scripts\game\gameplay\items\itemEntity.ws`

Reason:
- `mod0000_MergedFiles` is priority 1 and already owns the active `itemEntity.ws`.
- `modW3EE` also modifies `itemEntity.ws`.
- Letting Smart Magic Lamp add another active copy would create an avoidable script conflict and risk overriding existing W3EE/merged behavior.

Merge actions:
- Inserted the Smart Magic Lamp / Natural Torchlight utility block before `class W3LightSource`.
- Changed `class W3MagicOilLamp extends W3QuestUsableItem` to inherit from `W3SmartLamp`.
- Kept `W3SmartLamp` active through `modSmartMagicLamp\content\scripts\local\smartLamp.ws`.
- Disabled the shipped duplicate script by renaming it under the installed mod folder.
- Added `[modSmartMagicLamp]` to `C:\Games\The Witcher 3\mods.settings` at priority `169`.

Backups:
- Merged script backup:
  `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\mod0000_MergedFiles\content\scripts\game\gameplay\items\itemEntity.ws.codex-backup-smart-magic-lamp-20260623-154839`
- Mods settings backup:
  `C:\Games\The Witcher 3\mods.settings.codex-backup-smart-magic-lamp-20260623-154839`

Static verification:
- Active merged `itemEntity.ws` contains:
  - `CNaturalLightManager`
  - `NaturalTorchlight`
  - `class W3MagicOilLamp extends W3SmartLamp`
- Installed `modSmartMagicLamp` has only one active `.ws` file:
  `content\scripts\local\smartLamp.ws`
- The shipped `itemEntity.ws` from Smart Magic Lamp is disabled in the installed mod folder.

Runtime verification:
- Launch compile test passed after the manual merge.

Pending verification:
- In-game lamp smoke test in a scene where the magic lamp is usable.
