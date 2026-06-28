# Install - Kaer Morhen Armory Rubble Removed

Date: 2026-06-28

Source archive:

- `C:\Users\marti\Downloads\Kaer Morhen Armory Rubble Removed-5813-1-2-1708274171.rar`

Installed from archived inspected copy:

- From: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_CodexArchivedMods\modKMArmoryRubbleRemoved.disabled-settings-20260627`
- To: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modKMArmoryRubbleRemoved`

Files:

- `content\blob0.bundle`
- `content\buffers0.bundle`
- `content\metadata.store`

Decision:

- Re-enabled as a small content-only Kaer Morhen cleanup candidate.
- No script merge needed; the mod contains no `.ws` scripts.
- The broad Kaer Morhen overhauls remain disabled/deferred.

Load order:

```ini
[modKMArmoryRubbleRemoved]
Enabled=1
Priority=199
```

Validation:

- Enabled mod count: `200`
- Enabled priority range: `0..199`
- Duplicate enabled priorities: `0`
- Invalid enabled priorities: `0`
- DX12 launch smoke: passed. `witcher3.exe` was running and responsive after 45 seconds, then closed cleanly.

Residual risk:

- Compile risk is effectively none.
- Visual/world-layer behavior should be checked in Kaer Morhen later, especially near the armory/rubble area.
