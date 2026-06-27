# Investigation: no-window startup hang / loader pressure

Date: 2026-06-25

## Symptom

Recent content mods sometimes compile cleanly but the game never opens a visible window. The process stays alive/responding with `MainWindowHandle=0` and private memory around `4125-4128 MB`.

This is different from a script compile failure. There is no red compiler dialog; the loader appears to stall before the normal window/menu initialization.

## Current stack counts

- Active physical mod folders: `206`
- Enabled `mods.settings` entries: `255`
- Active folders containing scripts: `82`
- Active content-only folders: `124`
- Active payload files: `1149`
- Active `.bundle` files: `182`
- Active `.cache` files: `79`
- Active `metadata.store` files: `145`
- Active `.w3strings` files: `743`
- Total active payload size: about `26.5 GB`
- Enabled settings entries with no active physical folder: `50`

## Mod Limit Adjuster state

Mod Limit Adjuster is installed for both executables:

- `bin\x64\dinput8.dll`
- `bin\x64\ModLimitAdjuster.asi`
- `bin\x64\ModLimitAdjuster.cfg`
- `bin\x64_dx12\dinput8.dll`
- `bin\x64_dx12\ModLimitAdjuster.asi`
- `bin\x64_dx12\ModLimitAdjuster.cfg`

Both configs currently contain:

```ini
[Adjust]
ModLimit = 700
```

So the obvious old `~49` or default `192` style mod cap is not the active configured limit. However, the live stack still shows a loader pressure cliff around the current package count.

Reference: Nexus Mod Limit Adjuster describes itself as an `.asi` that lets the mod limit be set through `.cfg` and requires an ASI loader.

## Controlled tests

### Baseline

With the current safe stack, `witcher3.exe` DX12 launched successfully:

- visible window at about `15s`
- title: `The Witcher 3`
- private memory settled around `5916 MB`

### Balanced Alcohol Prices

`modBalancedAlcoholPrices` was previously suspected because it had triggered the same no-window symptom.

Retests:

- Full stack plus Balanced active: passed.
- 45 content-only folders held out plus Balanced active: passed.

Conclusion: Balanced Alcohol Prices is not inherently broken. Its earlier failure was likely caused by being installed while the loader/config state was already at or past the pressure cliff.

Balanced was restored to disabled state after tests.

### RT Water Reflection Fix full bundle

`modRTWaterReflectionColorFix` script-only state is safe. Its `content\blob0.bundle` had previously been disabled because it caused the no-window hang.

Retests:

- Full current stack + RT Water `blob0.bundle`: failed.
  - `MainWindowHandle=0`
  - visible `False`
  - memory stuck around `4127 MB` through `72s`
- Held out 45 content-only folders, then enabled RT Water bundle: passed.
- Held out 20 content-only folders: passed.
- Held out 10 content-only folders: passed.
- Held out 5 content-only folders: passed.
- Held out 2 content-only folders: passed.

Conclusion: RT Water's bundle is not independently broken. It fails only when the aggregate loader/package pressure is too high.

## Important related finding

The earlier in-game red error:

`The XML file for the Menu Organizer options menu is not installed correctly.`

was a real separate issue. The XML existed under:

`bin\config\r4game\user_config_matrix\pc\modMenuOrganizer_IMM_MrCK.xml`

but was missing from:

- `dx12filelist.txt`
- `dx11filelist.txt`

Adding `modMenuOrganizer_IMM_MrCK.xml;` fixed that menu error. This did not fully solve the no-window hang class, but it removed one misleading configuration problem.

## Working theory

We are not hitting a simple script conflict or a single bad mod. We are near a hidden loader/resource pressure cliff despite Mod Limit Adjuster being configured to `700`.

The practical threshold appears to be shaped by some combination of:

- physical mod folder count,
- active bundle/cache/metadata count,
- large content packages,
- load order / package index pressure,
- possibly dead `mods.settings` entries and redundant folders.

At this stack size, adding or enabling a small content bundle can tip the game into a silent pre-window hang. Removing even 2-5 content-only mod folders can allow the same bundle to pass.

## Rules for future troubleshooting

1. Treat `no window + 4127 MB plateau + responding process` as loader/package pressure until proven otherwise.
2. Do not assume a "simple" mod is safe just because it has no scripts.
3. For content-only mods, test by reducing physical active folder count, not just `mods.settings`.
4. Keep disabled/replaced mods physically outside the active `mods` scan, not merely `Enabled=0`.
5. Keep a safety margin below the observed cliff. A stack that launches at 206 folders can still fail when one content bundle is restored.
6. Prefer consolidating or removing redundant cosmetic/content mods before adding more content bundles.
7. Keep Mod Limit Adjuster installed, but do not assume `ModLimit=700` solves all package-loader ceilings.
8. For XML option menus, verify both actual XML presence and inclusion in the DX11/DX12 filelists.

## Recommended next move

Create a permanent quarantine/cleanup pass:

- Move obsolete disabled/replaced content mods out of `mods` entirely.
- Remove or disable at least 10-20 low-value content-only cosmetic folders from active scan.
- Clean `mods.settings` entries for missing folders or set them disabled.
- Then retest currently desirable content bundles one at a time:
  - RT Water Reflection Fix full bundle
  - Balanced Alcohol Prices
  - any recent "same signature" content mods

Do not keep adding new mods until this margin exists. We are currently operating too close to the loader cliff.
