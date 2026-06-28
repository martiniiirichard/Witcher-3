# Witcher 3 Modding Debugging Techniques

These are general techniques that have worked well for this W3EE-heavy mod stack.

## Treat Script Merger Output As Evidence

Do not assume a Script Merger prompt means a merged file was actually produced. If the game throws missing member/function errors after a merge, check whether `mod0000_MergedFiles` exists and contains the expected script path.

If Script Merger asks to remove old merges from `mod0000_MergedFiles`, click **No** by default. This stack has manual grafts in the merged folder, and removing old merges can delete working compatibility fixes unless we have made a targeted backup and decided to rebuild the merged folder on purpose.

For this stack, the pinned shortcut should use `tools\sm-fae-0.9.7\WitcherScriptMerger.exe` with its own folder as the working directory. SM-FAE also needs `tools\sm-fae-0.9.7\MergeInventory.xml` to exist; an empty inventory file is enough to avoid the false "old merges" clean-install prompt for the current hand-maintained `mod0000_MergedFiles` folder.

Example failure pattern:

- A helper script compiles from the new mod.
- The helper script calls methods or vars expected on `CR4Player`.
- The active winning `r4Player.ws` does not contain those methods or vars.

This usually means the new mod's core script additions were not merged into the active winner.

## Prefer Grafting Small Marked Blocks Into The Active Winner

For W3EE compatibility, the safest fix is often not to let an older mod's full vanilla script override W3EE. Instead, identify the mod's small marked additions and graft only those into the active W3EE script.

Good candidates:

- Blocks marked by comments like `// modHoodToggle`.
- Small listener registrations in `playerInput.ws`.
- Small player API additions in `r4Player.ws` or `playerWitcher.ws`.
- Timers, vars, and wrapper functions that helper scripts require.

Avoid wholesale replacement of W3EE scripts unless the mod is explicitly built for the exact W3EE version.

## Use Compiler Errors As A Dependency Map

Compile errors often tell us which script won the conflict.

Examples:

- `Could not find function 'SetAnim'`
- `'HoodToggleButton' is not a member of 'handle:CR4Player'`
- `'animHoodCape' is not a member of 'handle:CR4Player'`

These point to missing members in the active `CR4Player` implementation. Find those members in the mod source, then graft them into the script that is actually winning load order.

## Back Up Before Runtime Patches

Before changing game files, create a targeted backup under `backups/` with the mod name and timestamp. Prefer one backup per intervention:

- Install backup for copied folders and settings.
- Compatibility graft backup for patched scripts.
- Recovery backup before disabling or renaming a conflicting script.

This keeps rollback precise.

## Preserve W3EE Load Order

When adding older or vanilla-based mods to this stack, assume W3EE should usually remain the behavioral baseline. Let compatibility patches, bridge mods, or targeted grafts adapt the new mod to W3EE instead of letting the new mod replace W3EE systems.

## Validate Settings Separately From Scripts

Split checks into clear layers:

- `mods.settings`: mod enabled and priority assigned.
- `input.settings`: key bindings added to every required section without duplicates.
- Runtime files: mod folder copied and expected scripts/assets present.
- Script conflicts: active winner contains required mod additions.
- Launch: required when scripts changed.

This prevents chasing script errors caused by a missing input binding or disabled mod.
