# Menu Organizer XML Filelist Fix

Date: 2026-06-25

Symptom:
- In-game popup:
  - `Error: The XML file for the Menu Organizer options menu is not installed correctly.`

Cause:
- `modMenuOrganizer_IMM_MrCK.xml` existed in:
  - `bin\config\r4game\user_config_matrix\pc`
- But it was missing from:
  - `dx12filelist.txt`
  - `dx11filelist.txt`
- Result: the game could not load the Menu Organizer options XML even though the XML file was present on disk.

Key distinction:
- For Witcher 3 option menus, copying the XML file is not enough.
- The XML must also be listed in the relevant filelist, usually `dx12filelist.txt` for the current launch path.

Input settings:
- Menu Organizer keybinds were already present in:
  - `C:\Users\marti\OneDrive\Documents\The Witcher 3\input.settings`
- No keybind repair was needed.

Fix:
- Added this entry to both DX filelists:

```text
modMenuOrganizer_IMM_MrCK.xml;
```

Files edited:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\r4game\user_config_matrix\pc\dx12filelist.txt`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\r4game\user_config_matrix\pc\dx11filelist.txt`

Backups:
- `dx12filelist.txt.codex-backup-menu-organizer-xml-20260625`
- `dx11filelist.txt.codex-backup-menu-organizer-xml-20260625`

Verification:
- DX12 startup passed after the fix.
- Visible full-screen `The Witcher 3` window appeared.
- No script compilation dialog.

Follow-up:
- User should revisit the Menu Organizer options menu in-game to confirm the red XML error popup is gone.

Generalizable rule:
- When a mod option menu does not appear or reports a missing XML, inspect both:
  - the XML file under `bin\config\r4game\user_config_matrix\pc`
  - `dx12filelist.txt` / `dx11filelist.txt`
- Missing filelist registration can make installed menu XML behave as if it is absent.
