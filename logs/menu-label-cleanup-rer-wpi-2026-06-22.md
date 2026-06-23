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
  - Later removed `modRandomEncountersReworked.xml;` from the menu filelists because the left-nav panel title is controlled by compiled RER localization (`panel_rer_name`) rather than the XML group label, and the wrapped title overlapped `Back`.

Notes:
- These are menu display/order changes only.
- No gameplay scripts or mod settings were changed.
- RER remains installed and active; only its in-game configuration page is hidden until the compiled `.w3strings` title can be shortened safely.
