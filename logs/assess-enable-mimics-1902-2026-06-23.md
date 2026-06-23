# Assessment - Enable Mimics Blinking 1902

Date: 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/1902?tab=files&file_id=30513`
- Local downloads:
  - `C:\Users\marti\Downloads\modEnableMimics_blinking-1902-0-5-3b-1590864461.rar`
  - `C:\Users\marti\Downloads\modEnableMimics_blinking-1902-0-5-3b-1590864461(1).rar`

## Decision

Do not install.

## Reason

The Nexus page marks this file as Next-Gen incompatible, and the archive is a script-bearing core override:

- `mods\modEnableMimics_blinking\content\scripts\game\actor.ws`
- `mods\modEnableMimics_blinking\content\scripts\game\npc\npc.ws`
- `mods\modEnableMimics_blinking\content\scripts\game\player\player.ws`
- `mods\modEnableMimics_blinking\content\scripts\local\activateMimicsAndHiResShadows.ws`
- `dlc\DLCEnableMimics`

Those files are high-conflict surfaces in the current W3EE Redux build. Installing this late would almost certainly create Script Merger conflicts or compile errors, and a manual port would need to identify and re-implement only the mimics/blinking behavior against the current W3EE/merged versions.

## Outcome

No game files were changed.

If we revisit this later, look for a maintained Next-Gen replacement rather than installing this archive directly.
