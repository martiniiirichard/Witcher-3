# Audit: E3 HUD Colored Loading Screens

Date: 2026-06-27

Question:

- Is `modE3HUDColorLoad` redundant with the E3 HUD stack?

Result:

- Keep unless the colored loading screen look is unwanted.

Active settings:

| Mod | Enabled | Priority |
| --- | --- | --- |
| `mod0_E3HUD_W3EER_NG` | `1` | `10` |
| `modE3HUDColorLoad` | `1` | `11` |
| `modE3HUD` | `1` | `12` |

Payload:

The addon contains exactly ten loading-screen SWFs:

- `gameplay/gui_new/swf/loading/panel_loading_bob.redswf`
- `gameplay/gui_new/swf/loading/panel_loading_islandofmyst.redswf`
- `gameplay/gui_new/swf/loading/panel_loading_kaermorhen.redswf`
- `gameplay/gui_new/swf/loading/panel_loading_novigrad.redswf`
- `gameplay/gui_new/swf/loading/panel_loading_prologuevillage.redswf`
- `gameplay/gui_new/swf/loading/panel_loading_prologuevillagewinter.redswf`
- `gameplay/gui_new/swf/loading/panel_loading_skellige.redswf`
- `gameplay/gui_new/swf/loading/panel_loading_spiral.redswf`
- `gameplay/gui_new/swf/loading/panel_loading_velen.redswf`
- `gameplay/gui_new/swf/loading/panel_loading_wyzima.redswf`

Conclusion:

This is not a broken or shadowed install. It is a tiny visual override that wins its intended loading-screen files over base E3 HUD. Keep it for now because it is low-risk and aligned with the current E3 HUD preference; archive only if the colored loading screens are unwanted or if active mod count pressure becomes severe.
