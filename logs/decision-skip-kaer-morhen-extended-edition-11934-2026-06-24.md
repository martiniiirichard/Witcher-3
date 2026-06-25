# Kaer Morhen Extended Edition - 11934

Date: 2026-06-24

Source:
- https://www.nexusmods.com/witcher3/mods/11934

Archive inspected:
- `C:\Users\marti\Downloads\Kaer Morhen Extended Edition-11934-1-2-1772604141.7z`

Package contents:
- `modkaer_morhen_extended\content\blob0.bundle`
- `modkaer_morhen_extended\content\buffers0.bundle`
- `modkaer_morhen_extended\content\collision.cache`
- `modkaer_morhen_extended\content\texture.cache`
- `modkaer_morhen_extended\content\metadata.store`
- `modkaer_morhen_extended\content\info.json`
- `modkaer_morhen_extended\content\en.w3strings`

Decision:
- Do not keep installed in the active stack right now.

Reason:
- Content-only REDkit/world package. No scripts and no Script Merger work available.
- Installed as `mods\modkaer_morhen_extended` with `Enabled=1`, `Priority=258`.
- DX12 launch produced hard crash:
  - `ExitCode=-1073741819`
  - Runtime about 20 seconds.
- Disabled the mod and set `[modkaer_morhen_extended]` to `Enabled=0`.
- Baseline DX12 smoke passed after rollback.

Notes:
- This is similar to the Interface Animations DLC/content failure pattern: not a compile issue, but a package/content load crash.
- Future investigation should focus on content/package constraints, possible mod/package-count pressure, or world-edit collisions, not script merging.

Verification:
- After rollback, DX12 launch smoke passed: game remained running after 60 seconds.

Deep isolation follow-up:
- Re-enabled the folder temporarily and tested payload pieces independently.
- Metadata-only state (`info.json`, `metadata.store`, `en.w3strings`) launched normally for 72 seconds, but this provides no useful world expansion.
- `blob0.bundle` active with metadata reproduced the no-window startup hang:
  - `MainWindowHandle=0`
  - `visible=False`
  - memory plateau around 4126 MB
- `blob0.bundle` plus `buffers0.bundle` reproduced the same hang.
- Support payload without `blob0.bundle` also reproduced the same hang.
- Single-file checks reproduced the same hang with:
  - `buffers0.bundle` only
  - `collision.cache` only
  - `texture.cache` only

Final 2026-06-24 decision:
- Keep 11934 disabled.
- The problem is broader than one conflicting Kaer Morhen world layer. Every substantial cooked payload file causes the same DX12 no-window startup hang in the current stack.
- A partial active install is not useful: metadata-only launches but adds no content; any meaningful payload hangs startup.
- Restored disabled folder:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\DISABLED_modkaer_morhen_extended.disabled-by-codex-crashes-11934-20260624153247`
- Final baseline after disabling passed for 72 seconds:
  - visible window
  - title `The Witcher 3`
  - rect `0,0,1920,1080`
  - memory around 5914 MB
