# Fix - DX12 Missing Mouse Cursor

Date: 2026-06-23

## Symptom

The mouse cursor was often not visible in menus, making navigation difficult.

## Likely Cause

The runtime config had:

```ini
[Rendering]
HardwareCursor=true
```

With DX12 and a heavily modded UI stack, the hardware cursor can disappear or render behind the game/UI surface while the menu still accepts mouse input.

## Fix

Created a timestamped backup of:

`C:\Games\The Witcher 3\dx12user.settings`

Then changed:

```ini
HardwareCursor=false
```

This forces the game to use its software-rendered cursor path.

## Verification Needed

Restart the game and open several menus:

- Main menu
- Inventory
- Character
- Map
- Mods/options menu

If the cursor still disappears, the next suspects are E3 HUD/CommonMenu cursor request stack behavior or a popup/menu leaving `RequestMouseCursor(false)` active.
