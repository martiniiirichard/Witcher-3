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
- `modRandomEncountersReworked/content/en.w3strings`
  - Patched string id `2115018010` / key `panel_rer_name` from `Random Encounters Reworked` to `RER` using `tools/w3strings_patch_rer_title.py`.
  - Re-enabled `modRandomEncountersReworked.xml;` in both DX11 and DX12 menu filelists after shortening the compiled title.

Notes:
- These are menu display/order/localization changes only.
- No gameplay scripts or mod settings were changed.
- The temporary hidden-menu workaround was replaced by the compiled string patch, so the RER config page is visible again.
