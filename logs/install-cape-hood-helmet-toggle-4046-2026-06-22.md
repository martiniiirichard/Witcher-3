# Cape Hood Helmet Visor Toggle 4046 Install

Date: 2026-06-22

## Source

- Nexus: https://www.nexusmods.com/witcher3/mods/4046
- Archive: `modCapeHoodHelmetToggle-4046-1-0-1572664821.7z`
- Staging folder: `staging/cape-hood-helmet-toggle-4046/Cape Hood Helmet Visor Toggle`

## Runtime Changes

- Installed `modCapeHoodHelmetToggle` into the game `mods` folder.
- Added `[modCapeHoodHelmetToggle]` to `C:\Games\The Witcher 3\mods.settings`.
- Assigned priority `20`, after `modNewHairstylesAndBeards`.
- Added the mod key bindings to these `input.settings` sections:
  - `[Boat]`
  - `[Combat]`
  - `[Diving]`
  - `[Exploration]`
  - `[Horse]`
  - `[Swimming]`
  - `[Scene]`

## Bindings Added

```ini
IK_8=(Action=HoodToggle)
IK_9=(Action=CapeToggle)
IK_Period=(Action=ViserDownToggle)
IK_Comma=(Action=ViserUpToggle)
IK_Slash=(Action=HelmetOffToggle)
```

## Backup

- `backups/cape-hood-helmet-toggle-4046-20260622-102040`

## Script Merger

This mod creates script conflicts with W3EE:

- `game\player\playerInput.ws`: `modCapeHoodHelmetToggle` vs `modW3EE`
- `game\player\r4Player.ws`: `modCapeHoodHelmetToggle` vs `modW3EE`

Script Merger was launched after install. No `mod0000_MergedFiles` output was present after the first launch attempt, so the game compiled with W3EE's `r4Player.ws` and `playerInput.ws` winning over the mod's standalone script files. That caused missing `CR4Player` members such as `ToggleHood`, `SetAnim`, and `animHoodCape`.

Compatibility graft applied directly into active W3EE scripts:

- `mods\modW3EE\content\scripts\game\player\r4Player.ws`
- `mods\modW3EE\content\scripts\game\player\playerInput.ws`

Graft backup:

- `backups/cape-hood-helmet-toggle-w3ee-graft-20260622-102552`

The game launch test is required because this mod touches scripts.

## Verification

- Runtime install: complete
- `mods.settings` entry: verified
- `input.settings` bindings: verified
- W3EE compatibility graft: applied and verified
- Game launch: passed after graft
