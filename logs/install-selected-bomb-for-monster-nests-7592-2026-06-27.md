# Selected Bomb for Monster Nests - 7592

Date: 2026-06-27

Source:
- https://www.nexusmods.com/witcher3/mods/7592

Archive:
- `C:\Users\marti\Downloads\Selected Bomb for Monster Nests-7592-2-0-0-1762881147.zip`

Installed:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modSelectedBombForMonsterNests`

Settings:

```ini
[modSelectedBombForMonsterNests]
Enabled=1
Priority=267
```

Files:
- `content\info.json`
- `content\scripts\local\SelectedBombForMonsterNests_anno.ws`

Compatibility Notes:
- Lightweight annotation-only mod.
- Wraps existing `CMonsterNestEntity.PlayerHasBombActivator()`.
- Does not replace `monsterNestEntity.ws`, so it preserves active W3EE/merged nest behavior.

Verification:
- DX12 launch smoke passed.
- The game opened a responsive `The Witcher 3` window.
- No script compilation dialog appeared.

Backup:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\backups\selected-bomb-nests-7592-install-20260627-142416`
