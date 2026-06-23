# Install - Enable Mimics Blinking 1902

Date: 2026-06-23

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/1902?tab=files&file_id=30513`
- Local downloads:
  - `C:\Users\marti\Downloads\modEnableMimics_blinking-1902-0-5-3b-1590864461.rar`
  - `C:\Users\marti\Downloads\modEnableMimics_blinking-1902-0-5-3b-1590864461(1).rar`

## Initial Risk

The Nexus page marks this file as Next-Gen incompatible, and the archive is a script-bearing core override:

- `mods\modEnableMimics_blinking\content\scripts\game\actor.ws`
- `mods\modEnableMimics_blinking\content\scripts\game\npc\npc.ws`
- `mods\modEnableMimics_blinking\content\scripts\game\player\player.ws`
- `mods\modEnableMimics_blinking\content\scripts\local\activateMimicsAndHiResShadows.ws`
- `dlc\DLCEnableMimics`

Those files are high-conflict surfaces in the current W3EE Redux build, so this was treated as a controlled experiment with backups and compile testing.

## Installed

- `Mods\modEnableMimics_blinking`
- `DLC\DLCEnableMimics`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modEnableMimics_blinking]
Enabled=1
Priority=172
```

## Fix Applied

First compile attempt failed with:

```text
Error [modenablemimics_blinking]local\activatemimicsandhiresshadows.ws(21):
Property 'useHiResShadows' exists but was not imported from C++ code.
```

The mod's own `actor.ws` had:

```witcherscript
import var useHiResShadows : bool; default useHiResShadows = true;
```

For the current Next-Gen build, the working pattern was to declare the imported native property without the scripted default:

```witcherscript
import var useHiResShadows : bool;
```

Applied this import surface to all active `actor.ws` overlays so any load-order path exposes the property:

- `Mods\modEnableMimics_blinking\content\scripts\game\actor.ws`
- `Mods\modW3EE\content\scripts\game\actor.ws`
- `Mods\modShadesOfIron\content\scripts\game\actor.ws`

## Verification

User confirmed the game passed after the import fix.

Static checks:

- `DLCEnableMimics\content\metadata.store` exists.
- `modEnableMimics_blinking` is enabled at priority `172`.
- `useHiResShadows` import exists in all three active `actor.ws` overlays.

## Generalizable Technique

For old mods that fail with:

```text
Property '<native property>' exists but was not imported from C++ code.
```

Do not assume the local script using the property is wrong. Check the winning class declaration/overlay chain and add the native property import to every active override of that class. For Next-Gen, avoid copying oldgen/default-value syntax on imported native properties unless the compiler accepts it.

## Outcome

Installed and passing.
