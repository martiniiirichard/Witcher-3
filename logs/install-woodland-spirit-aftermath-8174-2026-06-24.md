# Restored Content - Woodland Spirit Aftermath 8174 - 2026-06-24

Source: https://www.nexusmods.com/witcher3/mods/8174

Installed archive:

- `C:\Users\marti\Downloads\Woodland Spirit Aftermath-8174-1-1-1694833212.zip`

Installed payload:

- `mods\modWoodlandSpirit`

Archive contents:

- `content\blob0.bundle`
- `content\metadata.store`

No WitcherScript files are included.

Settings added to both active `mods.settings` files:

```ini
[modWoodlandSpirit]
Enabled=1
Priority=0
```

Compatibility decision:

- The author says this mod should be given priority over other mods.
- Since the archive contains only bundled non-script content, it was installed at priority 0 so its quest/cutscene edits can win if there is an overlap.
- No Script Merger script work is expected. If Script Merger reports bundled non-text conflicts later, choose `modWoodlandSpirit` for the quest/cutscene aftermath files.

Verification:

- DX12 smoke test passed; process remained running after 45 seconds.

Follow-up:

- In-game validation requires completing `In the Heart of the Woods` and confirming the correct retrospective video plays for the selected outcome.
