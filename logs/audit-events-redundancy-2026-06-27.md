# Audit: Events Redundancy

Date: 2026-06-27

Question:

- Is `modEvents` redundant because its bundled assets are shadowed in the old bundle index?

Result:

- Keep it while the Events feature is desired.

Active settings:

| Mod | Enabled | Priority |
| --- | --- | --- |
| `modEvents` | `1` | `225` |

Live payload:

- `Mods\modEvents`
- `DLC\dlcEvents`
- `bin\config\r4game\user_config_matrix\pc\Events.xml`
- `Events.xml;` registered in both `dx11filelist.txt` and `dx12filelist.txt`

Script state:

- Active:
  - `content\scripts\local\events_journal.ws`
  - `content\scripts\local\events_modMenu.ws`
- Disabled:
  - `content\scripts\local\events_modDescriptions.ws.disabled-by-codex`

Reason for disabled descriptor:

- Brothers in Arms already defines/registers `EVENTS_MenuDescriptor`.
- Leaving the standalone Events descriptor active caused duplicate class compilation:
  - `Class 'EVENTS_MenuDescriptor' already defined.`

Conclusion:

The bundled rows may be shadowed, but the mod still supplies active Events menu/fact/journal behavior plus the valid DLC package. Keep unless the Events feature itself is unwanted.
