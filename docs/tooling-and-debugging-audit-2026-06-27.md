# Tooling And Debugging Audit

Date: 2026-06-27

Purpose: capture useful practices from the old Google Drive TW3 modding guide, Sinitar's modern TW3 guide, SM-FAE, and the local REDkit install.

## Sources Reviewed

- Google Drive guide: `TW3 Modding Guide.pdf`, downloaded to `tools/tmp/TW3-Modding-Guide-drive-1oq4B8RA.pdf`.
- Local guide: `C:\Users\marti\Downloads\The Tome of Witcher 3 Modding.pdf`.
- Local large cut-content reference: `C:\Users\marti\Downloads\What.Lies.Unseen.Volume.1.-.A.Time.of.Sword.and.Axe.pdf`.
- Nexus mod 8405: SM-FAE 0.9.7, already downloaded and extracted to `tools/sm-fae-0.9.7`.
- Modern guide: `https://www.sinitargaming.com/tw3.html`.
- Official REDkit script override documentation.
- Local REDkit install: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 REDkit`.

## Current State

- Pinned taskbar shortcut `Witcher 3 Script Merger.lnk` now targets:
  - `tools/sm-fae-0.9.7/WitcherScriptMerger.exe`
- Previous shortcut target was:
  - `tools/script-merger-0.6.5/WitcherScriptMerger.exe`
- Shortcut backup:
  - `settings-backups/shortcuts-20260627-1235/Witcher 3 Script Merger.before.lnk`
- Mod Limit Adjuster is installed in both launch paths:
  - `bin/x64/ModLimitAdjuster.asi`
  - `bin/x64_dx12/ModLimitAdjuster.asi`
- `ModLimitAdjuster.cfg` is set to:
  - `ModLimit = 700`

## Guide Takeaways To Keep

1. Lower numeric priority wins in `mods.settings`.
2. Script conflicts are not all equal:
   - `.ws` conflicts are script merges.
   - bundled text conflicts such as XML can sometimes be merged or repacked.
   - bundled non-text conflicts are usually load-order decisions.
3. Do not treat Script Merger's non-text count as automatically bad. It is a decision queue.
4. For bundled text conflicts, priority-only can silently drop lower-priority gameplay changes. This is exactly what happened with Lighter Bombs vs Food Rebalance.
5. `mods.settings`, `input.settings`, user settings, and mod menu XML are part of the install, not optional afterthoughts.
6. Launch after each meaningful batch. Script compilation errors are the fastest signal that an annotation, function signature, or dependency assumption is wrong.

## Modern REDkit/Script Lesson

The official REDkit script override docs matter for newer mods. Modern scripts can use annotations:

- `@wrapMethod`
- `@addMethod`
- `@replaceMethod`
- `@addField`

This changes the debugging pattern. Errors like:

- member not found
- class already defined
- wrap function must wrap an existing function
- replace/overwrite target does not exist
- cannot call private function

often mean one of these is true:

- the annotation file is missing, disabled, or losing priority;
- a dependency that adds a field/method is disabled;
- the mod targets a different game generation or patch level;
- another compatibility patch already adds the same symbol;
- an old full-file override is fighting a newer annotation-style patch.

Preferred fix order:

1. Verify the expected dependency is installed and enabled.
2. Check whether the failing symbol is supposed to be added by an annotation file.
3. Search all active scripts for the symbol.
4. Prefer `@wrapMethod`/`@addField` style compatibility where practical.
5. Only edit full vanilla/W3EE files when no annotation-style patch is viable.

## REDkit Local Tools

Useful local REDkit executables:

- `bin/x64_RedKit/editor.exe`: full editor. Useful for inspection, not routine mod installation.
- `bin/x64_RedKit/scriptStudio.exe`: useful for script browsing and source inspection.
- `bin/x64_RedKit/wcc_lite.exe`: official command-line tool. Useful for validating, packing, and inspecting assets.
- `bin/x64_RedKit/bundlebuilder.exe`: bundle build tooling.
- `bin/tools/cooker/*.bat`: official cooking/build pipeline scripts.
- `bin/tools/GFx4/gfxexport_mult4fix.exe`: SWF/GFx related tooling.
- `bin/tools/MinimapConverter/MiniMap.exe`: minimap tooling.

Practical rule: keep using SM-FAE and repo scripts for day-to-day modding. Use REDkit when we need official asset inspection, script browsing, cooking, or non-trivial bundle work.

## Recommended Debugging Additions

### 1. Standard Conflict Triage Matrix

For every conflict:

- `.ws`: Script Merger or manual script compatibility.
- `.xml`: compare winners, then merge/repack if both changes matter.
- `.csv`: avoid blind merge; compare rows and choose/port deliberately.
- `.redswf`: usually one UI owner wins.
- `.xbm`, `.mesh`, `.w2ent`, `.w2scene`, `.env`: load-order decision unless there is a specific visual/content reason to unpack and rebuild.

### 2. Symbol Search Before Script Edits

Before patching compile errors, search active scripts:

- exact missing function/member;
- class definition;
- annotation adding the field/method;
- duplicate definitions.

This prevents over-patching and helps decide whether a dependency is missing or a mod should lose priority.

### 3. Bundle Winner Audit Before Removing Mods

For redundancy work:

- build/refresh the bundle conflict index;
- identify actual winner by `mods.settings`;
- check whether loser has scripts, menu XML, DLC, or strings;
- only archive when the mod has no active non-shadowed role.

### 4. Keep A Custom Compatibility Layer

Our new `custom-mods/` pattern is good. It lets us preserve intentional edits without mutating original downloaded mods.

Example already applied:

- `mod000000_W3EER_FoodRebalance_LighterBombsCompat`

### 5. Add WIDE As Optional Script IDE

Potentially useful external addon/tool:

- WIDE / WitcherScript IDE for VS Code.

Value: syntax diagnostics and symbol analysis for WitcherScript. It will not replace launch testing, but it can catch duplicate symbols, missing types, and annotation issues earlier.

## Notable Non-Debug Source

`What Lies Unseen Volume 1` is mainly a cut-content/lore/reference document, not a Script Merger guide. It may help evaluate restoration mods, but it is not a core debugging source.

## Strong Next Moves

1. Add a repeatable conflict-index refresh script if we do not already have one.
2. Add a symbol-audit script for compile errors: parse error text, search active scripts, and report likely owner/dependency. Implemented as `tools/analyze-witcher-compile-errors.py`; see `docs/compile-error-analyzer.md`.
3. Continue redundancy audits using the matrix above.
4. Use REDkit `scriptStudio.exe` only when normal text search is not enough.
5. Consider installing WIDE in VS Code if we start doing more annotation-style custom patches.
