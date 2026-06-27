# Audit: Hoods Redundancy

Date: 2026-06-27

Question:

- Is `mod__hoods` redundant because its inventory SWF loses to E3/W3EE HUD?

Result:

- Keep it while Hoods items/capes/hood toggles are desired.

Active settings:

| Mod | Enabled | Priority |
| --- | --- | --- |
| `mod__hoods` | `1` | `34` |

Live payload:

- `Mods\mod__hoods`
- `DLC\dlc__hoods`
- `Mods\mod__hoods\Hoods.input.settings`

Active scripts:

- `content\scripts\local\customDyeing.ws`
- `content\scripts\local\mod__hoods_Annotations.ws`
- `content\scripts\local\mod__hoods_Keybind.ws`
- `content\scripts\local\mod__hoods_Main.ws`

Compatibility history:

- `customDyeing.ws` was patched for the W3EE inventory menu class.
- `mod__hoods_Annotations.ws` was patched to no-op `HoodsAnim()` because W3EE keeps `PlayPaperdollAnimation(...)` private.
- The inventory panel SWF conflict is accepted: E3/W3EE inventory UI wins, while Hoods keeps items, DLC content, keybinds, and local behavior.

Conclusion:

The losing `panel_inventory.redswf` does not make Hoods redundant. It is a deliberate UI tradeoff in a still-active item/DLC/script mod.
