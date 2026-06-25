# W3QE Startup Hang Investigation - 2026-06-24

## Mod

- Nexus: `9360`
- Name: `Witcher 3 Quests Extended (W3QE)`
- Installed download observed locally: `W3QE-9360-2-5-1-1723596339.7z`
- Nexus page currently lists page version `2.5.9`, but the main file is still `2.5.1`; the `2.5.9` update appears to be translation strings.

## Install Structure

The mod has two required install parts:

- `dlcW3QE` -> game `DLC` directory
- `modW3QE` -> game `mods` directory

Both parts were present locally.

## Failure

With `modW3QE\content\blob0.bundle` active, the game enters the known headless startup hang:

- `witcher3.exe` alive
- no visible top-level game window
- memory parked around 4.1 GB

## Isolation

`modW3QE` contains only:

- `content\blob0.bundle`
- `content\metadata.store`

Unpacked `modW3QE\content\blob0.bundle` contains exactly one cooked asset:

- `quests\part_2\quest_files\q309_casablanca\scenes\q309_00u_ungrateful_mage_on_steak.w2scene`

No active duplicate override for this exact scene path was found in the current mod stack.

Disabling only this bundle fixed the startup hang.

Current safe reduced state:

- `dlcW3QE` remains installed.
- `modW3QE` remains present/enabled in `mods.settings`.
- `modW3QE\content\blob0.bundle` is renamed to:
  `blob0.bundle.disabled-by-codex-internal-test`

Strict visible-window launch passed in this reduced state.

## Interpretation

This is a content-only cooked scene failure, not a WitcherScript conflict. Script Merger cannot detect or fix it.

The disabled scene is tied to W3QE's `An Ungrateful Mage` / Moritz quest integration. Keeping the DLC half while disabling this scene may preserve much of W3QE's quest content, but that specific Moritz scene hook is likely degraded or unavailable.

## Decision

Keep W3QE in reduced mode unless we later decide to test the quest content in-game or source a compatible updated scene. Do not reactivate `modW3QE\content\blob0.bundle` without a strict visible-window launch test.
