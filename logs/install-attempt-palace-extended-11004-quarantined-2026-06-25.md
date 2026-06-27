# Install Attempt - Full Access To An Expanded Beauclair Palace 11004

Date: 2026-06-25

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/11004`
- Archive: `C:\Users\marti\Downloads\Full Access To An Expanded Beauclair Palace-11004-1-2-1752159480.7z`

## Page / Install Notes

The mod is a Beauclair Palace expansion and ships as a paired mod/DLC install:

- `modpalace_extended`
- `dlc_palace_extended`

The page warns that the mod should have priority on:

- `dlc/bob/data/levels/bob/bob.w2w`

No `.ws` scripts were present, so Script Merger is not relevant.

## Archive Inspection

Extracted to:

- `C:\Users\marti\AppData\Local\Temp\codex_palace_extended_11004_inspect`

Top-level folders:

- `modpalace_extended`
- `dlc_palace_extended`

Internal `info.json` metadata is sloppy:

```json
{
  "name": "palace_extended",
  "modName": "rwerwer",
  "version": "werwergbwer",
  "succesfullyCooked": true,
  "dependencies": []
}
```

This is a caution flag, but not by itself proof of failure.

## Install Attempt

Installed:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modpalace_extended`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\dlc\dlc_palace_extended`

Updated `mods.settings`:

```ini
[modpalace_extended]
Enabled=1
Priority=262
```

Active physical mod folder count became 200.

## Result

DX12 launch smoke test failed:

- launched through `tools/direct-launchers/Witcher3DirectDX12.exe`
- after 45 seconds there was no `witcher3.exe` process

Because the mod has no scripts, this is likely content/package loader failure, DLC/package issue, or hidden loader pressure. It is not a script compilation problem.

## Rollback / Quarantine

Disabled in `mods.settings`:

```ini
[modpalace_extended]
Enabled=0
Priority=262
```

Renamed installed folders:

- `mods/DISABLED_modpalace_extended.disabled-by-codex-launch-fail-20260625`
- `dlc/DISABLED_dlc_palace_extended.disabled-by-codex-launch-fail-20260625`

After quarantine, active physical mod folder count returned to 199.

Baseline DX12 launch recovered:

- process appeared after first 45 seconds
- visible titled window `The Witcher 3` appeared after a second 45-second wait
- process responding, working set ~1.70 GB

## Recommendation

Leave Palace Extended quarantined for now.

If revisiting later, first free loader budget by disabling at least one active content mod, then retest Palace Extended. If it still fails with extra budget, treat it as incompatible with the current content stack or requiring a deeper `bob.w2w`/DLC package priority investigation.
