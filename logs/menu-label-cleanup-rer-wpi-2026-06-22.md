# Mod Menu Label Cleanup

Date: 2026-06-22

Reason:
- Long mod names in the in-game Mods menu wrapped and visually overlapped adjacent entries.

Changes:
- `WPI.xml`
  - Changed the top-level group label from localized `Mods.wpi_name` to `Pocket Items`.
- `modRandomEncountersReworked.xml`
  - Restored the original localized `RERmain` group label after the direct XML title change did not affect the visible left-nav menu label.
- `dx11filelist.txt` and `dx12filelist.txt`
  - Moved `modRandomEncountersReworked.xml;` after `FastTravelPack.xml;` so the long RER label wraps at the bottom of the visible cluster instead of overlapping the following menu entry.

Notes:
- These are menu display/order changes only.
- No gameplay scripts or mod settings were changed.
