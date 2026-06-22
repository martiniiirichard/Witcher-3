# Hoods Install Log - 2026-06-22

## Goal

Install Hoods on top of the current stable W3EE Redux + AMM + Swords on Roach stack.

## Branch

- `codex/hoods`

## Nexus Page

- `https://www.nexusmods.com/witcher3/mods/4242`

## Archive Used

- `Hoods-4242-3-3-1762297143.zip`

## Page Notes

Nexus page reports:

- Version `3.3`
- Last updated `04 November 2025`
- Next-Gen compatible
- Adds hoods, capes, hats, scarves, masks, dyeing, and hood-up/down switching
- Version `3.2` changelog says the mod is merge-free thanks to annotations

## Risk Classification

Medium.

Reason:

- Adds DLC assets.
- Adds local annotation scripts.
- Wraps inventory/player UI behavior.
- Adds optional input bindings.

Lower than direct `playerWitcher.ws` or combat-script mods because the scripts are unique local files and use annotation/wrap methods.

## Installed Files

Copied:

- `Mods\mod__hoods` -> `mods\mod__hoods`
- `dlc\dlc__hoods` -> `dlc\dlc__hoods`

Hoods script files:

- `content\scripts\local\customDyeing.ws`
- `content\scripts\local\mod__hoods_Annotations.ws`
- `content\scripts\local\mod__hoods_Keybind.ws`
- `content\scripts\local\mod__hoods_Main.ws`

## Input Settings

Merged `Hoods.input.settings` into:

```text
C:\Games\The Witcher 3\input.settings
```

Added `ToggleArdHood` bindings to:

- `Boat`
- `BoatPassenger`
- `Combat`
- `Diving`
- `Exploration`
- `Horse`
- `Swimming`
- `Scene`

Bindings added:

```ini
IK_9=(Action=ToggleArdHood)
IK_Pad_RightThumb=(Action=ToggleArdHood,State=Duration,IdleTime=0.4)
```

Note: `IK_Pad_RightThumb` already has vanilla/Next-Gen actions in several contexts. If controller behavior feels wrong, remove only the Hoods `IK_Pad_RightThumb=(Action=ToggleArdHood,State=Duration,IdleTime=0.4)` lines and keep the keyboard `IK_9` binding.

## Config Changes

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[mod__hoods]
Enabled=1
Priority=13
```

## Backup

Created:

```text
backups\pre-hoods-20260622
```

Backed up existing:

- `C:\Games\The Witcher 3\input.settings`
- `C:\Games\The Witcher 3\mods.settings`

## Verification

- Confirmed `mods\mod__hoods` exists.
- Confirmed `dlc\dlc__hoods` exists.
- Confirmed Hoods keybinds were inserted into `input.settings`.
- Confirmed `mods.settings` includes `[mod__hoods]` at priority `13`.
- Static check found no direct duplicate script paths for Hoods' local script files.

## Script Merger Delta

After installing Hoods, Script Merger still shows the known baseline script conflicts:

- `game\gameplay\items\swords\witcherSword.ws`
- `game\gameplay\items\throwables\throwable.ws`
- `game\player\playerWitcher.ws`
- `game\player\states\combatSword.ws`
- `game\vehicles\horse\horseManager.ws`
- `local\W3EE_Uniques.ws`

New conflict introduced by Hoods:

```text
Bundled Non-text - Not Mergeable
gameplay\gui_new\swf\inventory\panel_inventory.redswf
- mod__hoods
- modW3EE
```

This is not mergeable in Script Merger and is resolved by priority. Current `mods.settings` has:

- `modW3EE` priority `6`
- `mod__hoods` priority `13`

Therefore W3EE wins this bundled UI conflict. Expected tradeoff: W3EE inventory UI is preserved, but Hoods' inventory-panel dyeing UI enhancement may not appear. Hoods' items and keybind/scripts may still work.

## Compatibility Fixes

First launch produced:

```text
Error [mod__hoods]local\customdyeing.ws(16): Wrap function 'OnUseDye' must wrap an existing function.
```

Cause:

- Hoods targets vanilla `CR4InventoryMenu`.
- W3EE's installed inventory menu class is `WmkCR4InventoryMenu`.
- `OnUseDye(...)` and `ShowSelectionMode(...)` exist on `WmkCR4InventoryMenu` in the W3EE stack.

Applied a narrow compatibility patch to:

```text
mods\mod__hoods\content\scripts\local\customDyeing.ws
```

Changed:

```witcherscript
@wrapMethod(CR4InventoryMenu) function OnUseDye(...)
@wrapMethod(CR4InventoryMenu) function ShowSelectionMode(...)
```

to:

```witcherscript
@wrapMethod(WmkCR4InventoryMenu) function OnUseDye(...)
@wrapMethod(WmkCR4InventoryMenu) function ShowSelectionMode(...)
```

Backup:

```text
backups\hoods-customDyeing-w3ee-menu-class-20260622\customDyeing.ws.pre-w3ee-menu-class-fix
```

Second launch progressed farther and produced:

```text
Error [mod__hoods]local\mod__hoods_annotations.ws(2): Cannot call private function 'PlayPaperdollAnimation' in class 'WmkCR4InventoryMenu' here.
```

Cause:

- Hoods' `HoodsAnim()` helper calls `PlayPaperdollAnimation('armor')`.
- W3EE's inventory menu keeps `PlayPaperdollAnimation(...)` private.
- This animation is cosmetic after toggling a hood; the actual hood swap and inventory refresh happen elsewhere.

Applied a narrow compatibility patch to:

```text
mods\mod__hoods\content\scripts\local\mod__hoods_Annotations.ws
```

Changed `HoodsAnim()` to a no-op:

```witcherscript
@addMethod(CR4InventoryMenu) function HoodsAnim(){
    // W3EE compatibility: PlayPaperdollAnimation is private on WmkCR4InventoryMenu.
}
```

Backup:

```text
backups\hoods-private-paperdoll-animation-20260622\mod__hoods_Annotations.ws.pre-private-animation-fix
```

## Next Validation

Before commit:

1. Refresh Script Merger.
2. Confirm no new unexpected conflicts beyond the documented baseline plus the Hoods `panel_inventory.redswf` priority conflict.
3. Launch the game.
4. Confirm no script compilation errors.
5. Confirm Hoods items/menu behavior works.
6. Test `9` for hood toggle.
7. If using controller, test right-thumb hold does not break other actions.

Do not commit this install log until launch test succeeds.
