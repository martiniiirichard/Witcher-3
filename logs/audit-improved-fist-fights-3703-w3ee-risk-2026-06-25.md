# Audit - Improved Fist Fights 3703

Date: 2026-06-25

## Source

- Nexus: `https://www.nexusmods.com/witcher3/mods/3703`
- Archive: `C:\Users\marti\Downloads\modImprovedFistFightNGE-3703-4-04-00-1689864508.zip`

## Nexus Notes

The mod balances fist-fight events/minigames by changing Geralt's fist damage and minigame health scaling.

The page states it modifies:

- `scripts\game\player\r4Player.ws`
- `gameplay\items\def_items_weapons.xml`
- `gameplay\items_plus\def_items_weapons.xml`

The page explicitly says scripts and bundled text must be merged.

## Local Package Shape

Extracted to:

- `C:\Users\marti\AppData\Local\Temp\codex_improved_fistfight_3703_inspect`

Package contains:

- full `content\scripts\game\player\r4Player.ws`
- `blob0.bundle`
- `metadata.store`

Bundle strings show:

- `gameplay\items\def_item_weapons.xml`
- `gameplay\items_plus\def_item_weapons.xml`

## Compatibility Findings

This is a high-risk install for the current W3EE stack.

The current setup already has several `r4Player.ws` participants:

- `mods\modW3EE\content\scripts\game\player\r4Player.ws`
- `mods\mod0000_MergedFiles\content\scripts\game\player\r4Player.ws`
- other installed mods with player-script hooks/overrides

The downloaded mod ships a full `r4Player.ws`, not a small wrapper or annotation file.

W3EE already changes the fist-fight minigame section. In `modW3EE`:

```witcherscript
// W3EE - Begin
//FistFightHealthChange( true );
SetHealthPerc(100);
// W3EE - End
```

And on ending the minigame:

```witcherscript
// W3EE - Begin
//FistFightHealthChange( false );
SetHealthPerc(100);
...
// W3EE - End
```

Improved Fist Fights wants to re-enable `FistFightHealthChange()` and replace fixed health scaling with difficulty-based max-health scaling:

```witcherscript
diffMode = theGame.GetDifficultyMode();
if (diffMode == EDM_Medium) ...
else if (diffMode == EDM_Hard) ...
else if (diffMode == EDM_Hardcore) ...
else ...
```

This means the mod is not merely absent from W3EE; W3EE intentionally chose a different fist-fight health behavior.

## Decision

Do not install as packaged.

Reasons:

- full `r4Player.ws` replacement is too risky in this heavily merged W3EE stack
- W3EE has explicit fist-fight logic that conflicts with the mod's health-scaling model
- installing only the bundle/XML portion would not deliver the full mod behavior
- active mod count/load pressure is already near the known threshold

## Possible Future Manual Graft

If we decide fist fights need this balance change anyway, do a manual W3EE-aware graft instead of installing the mod:

1. Back up both `modW3EE` and `mod0000_MergedFiles` versions of `r4Player.ws`.
2. Add a local difficulty variable or use a function-local `diffMode`.
3. Reconcile W3EE's `SetHealthPerc(100)` behavior with the mod's `FistFightHealthChange()` behavior.
4. Decide whether W3EE's intentional health model should stay authoritative.
5. Only then consider integrating the weapon XML bundle.

For now, skipping is the safer line.
