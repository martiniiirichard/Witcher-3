# Removing Oil Descriptions When Charges Are Exhausted - 12196

Date: 2026-06-25

Source:
- https://www.nexusmods.com/witcher3/mods/12196

Archive:
- `C:\Users\marti\Downloads\Removing oil descriptions when charges exhausted-12196-1-0-1778486967.7z`

Purpose:
- Removes expired oil buffs instead of leaving the red exhausted-oil description.
- Also prevents bugs when more than one oil is applied to a sword.

Install decision:
- Do not install the archive as a standalone mod folder.
- The archive ships a full `game\player\r4Player.ws`, which would conflict badly with W3EE and our active merged player script.
- The actual Next-Gen change is a one-line behavior graft in `ReduceAllOilsAmmo`.

Graft applied:
- Added the expired-oil removal after W3EE reduces oil ammo:

```witcherscript
oils[ i ].ReduceAmmo(isHeavyAttack);
if(oils[i].GetAmmoCurrentCount() == 0) thePlayer.RemoveEffect( oils[ i ] ); // modRemovingOilDescriptionsWhenChargesAreExhausted
```

Files edited:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modW3EE\content\scripts\game\player\r4Player.ws`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\mod0000_MergedFiles\content\scripts\game\player\r4Player.ws`

Backups:
- `r4Player.ws.codex-backup-oil-description-12196-20260625`

Verification:
- DX12 compile/startup passed.
- Visible full-screen `The Witcher 3` window appeared.
- No script compilation error dialog.

Notes:
- No `mods.settings` entry was added because the archive itself was not installed as an active mod.
- This is the preferred pattern for small single-line mods that ship full vanilla/NG script overrides: identify the minimal delta and graft it into W3EE/merged sources.
