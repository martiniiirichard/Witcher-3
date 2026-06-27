# Audit: Menu Organizer Redundancy

Date: 2026-06-27

Question:

- Can `modMenuOrganizerNG_IMM_MrCK` be removed as redundant menu infrastructure?

Result:

- Keep it.

Active settings:

| Mod | Enabled | Priority |
| --- | --- | --- |
| `modMenuOrganizerNG_IMM_MrCK` | `1` | `22` |

Live payload:

- Menu organizer scripts:
  - `content\scripts\game\gui\main_menu\ingameMenu.ws`
  - `content\scripts\game\gui\main_menu\ingamemenu\igmOptions.ws`
  - `content\scripts\game\gui\main_menu\ingamemenu\igmStructureCreator.ws`
  - multiple `content\scripts\mrckIMM\*.ws` files
- Localization/string files.
- `IMM_NG_info.txt` and `input.settings.txt`.

Registered config:

- `bin\config\r4game\user_config_matrix\pc\modMenuOrganizer_IMM_MrCK.xml`
- Included in:
  - `dx11filelist.txt`
  - `dx12filelist.txt`

Relevant history:

- We previously saw the in-game error: `The XML file for the Menu Organizer options menu is not installed correctly.`
- That was fixed by adding `modMenuOrganizer_IMM_MrCK.xml;` to both DX11 and DX12 filelists.
- Current menu option inventory and settings recommendations include the Menu Organizer options as active infrastructure.

Conclusion:

Do not remove Menu Organizer as redundancy cleanup. It is structural UI infrastructure for the crowded current mod menu. Removing it should be treated as a deliberate UI-stack redesign with launch and menu testing afterward.
