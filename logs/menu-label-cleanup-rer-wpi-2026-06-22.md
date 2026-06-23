# Mod Menu Label Cleanup

Date: 2026-06-22

Reason:
- Long mod names in the in-game Mods menu wrapped and visually overlapped adjacent entries.

Changes:
- `WPI.xml`
  - Changed the top-level group label from localized `Mods.wpi_name` to `Pocket Items`.
- `modRandomEncountersReworked.xml`
  - Changed the top-level `RERmain` group label from localized `Mods.rer_name.rer_main_settings` to `Encounters`.

Notes:
- These are menu display-label changes only.
- No gameplay scripts or mod settings were changed.
