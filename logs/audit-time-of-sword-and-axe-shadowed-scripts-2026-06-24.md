# Time of the Sword and Axe Shadow Audit - 2026-06-24

Purpose: identify Time of the Sword and Axe scripts that are installed but currently shadowed by higher-priority mods. Lower numeric priority wins in this stack.

Total shadowed ToSA script paths: 35
Potentially at-risk paths where ToSA has expansion-specific markers but winner has none: 7

## Highest Marker Shadowed Paths

- game\gui\menus\gwintManager.ws -> winner modGwentRedux priority 3; ToSA markers 398, winner markers 344
- game\player\playerWitcher.ws -> winner mod0000_MergedFiles priority 1; ToSA markers 396, winner markers 376
- game\gameplay\effects\gameEffectManager.ws -> winner modNobsReflex priority 18; ToSA markers 302, winner markers 102
- game\gameplay\ability\PlayerAbilityManager.ws -> winner modW3EE priority 21; ToSA markers 160, winner markers 126
- game\gui\menus\characterMenu.ws -> winner modNobsToolTipHandaler priority 17; ToSA markers 147, winner markers 155
- game\components\inventoryComponent.ws -> winner mod0000_MergedFiles priority 1; ToSA markers 145, winner markers 132
- game\player\r4Player.ws -> winner mod0000_MergedFiles priority 1; ToSA markers 143, winner markers 147
- game\gui\_old\components\guiTooltipComponent.ws -> winner modW3EE priority 21; ToSA markers 113, winner markers 111
- game\player\playerTypes.ws -> winner modW3EE priority 21; ToSA markers 86, winner markers 80
- game\gameplay\damage\damageManagerProcessor.ws -> winner modNobsReflex priority 18; ToSA markers 68, winner markers 78
- game\gameplay\effects\effectTypes.ws -> winner modNobsReflex priority 18; ToSA markers 49, winner markers 47
- game\player\playerInput.ws -> winner modNobsReflex priority 18; ToSA markers 45, winner markers 42
- game\gui\menus\inventoryMenu.ws -> winner mod0_E3HUD_W3EER_NG priority 8; ToSA markers 38, winner markers 41
- game\gui\popups\CharacterStatsPopup.ws -> winner modW3EE priority 21; ToSA markers 37, winner markers 67
- game\player\states\unconscious.ws -> winner modW3EE priority 21; ToSA markers 29, winner markers 19
- game\npc\npc.ws -> winner mod0000_MergedFiles priority 1; ToSA markers 27, winner markers 16
- game\gameplay\effects\effectManager.ws -> winner modW3EE priority 21; ToSA markers 24, winner markers 5
- game\player\states\combat.ws -> winner modW3EE priority 21; ToSA markers 15, winner markers 20
- game\player\states\exploration.ws -> winner modW3EE priority 21; ToSA markers 11, winner markers 0
- game\gui\main_menu\ingameMenu.ws -> winner modW3EE priority 21; ToSA markers 10, winner markers 1
- game\gui\main_menu\ingamemenu\igmOptions.ws -> winner modW3EE priority 21; ToSA markers 8, winner markers 4
- game\gui\inventoryContext.ws -> winner modW3EE priority 21; ToSA markers 7, winner markers 4
- game\gameplay\items\throwables\throwable.ws -> winner modAMM priority 15; ToSA markers 6, winner markers 0
- game\gameplay\containers\container.ws -> winner modW3EE priority 21; ToSA markers 5, winner markers 4
- game\gui\_old\components\guiPlayerInventoryComponent.ws -> winner mod0_E3HUD_W3EER_NG priority 8; ToSA markers 5, winner markers 4
- game\gui\main_menu\ingamemenu\igmStructureCreator.ws -> winner modW3EE priority 21; ToSA markers 5, winner markers 2
- game\player\player.ws -> winner modW3EE priority 21; ToSA markers 4, winner markers 2
- game\vehicles\horse\horseManager.ws -> winner modAMM priority 15; ToSA markers 4, winner markers 0
- game\gui\hud\modules\hudModuleRadialMenu.ws -> winner mod0_E3HUD_W3EER_NG priority 8; ToSA markers 3, winner markers 0
- game\gui\menus\craftingMenu.ws -> winner modBetterIcons2025_NextGen_W3EE priority 11; ToSA markers 3, winner markers 10

## At-Risk Paths

- game\player\states\exploration.ws -> winner modW3EE priority 21; owners: modW3EE:21, modexpansionzero:228
- game\gameplay\items\throwables\throwable.ws -> winner modAMM priority 15; owners: modAMM:15, modW3EE:21, modexpansionzero:228
- game\vehicles\horse\horseManager.ws -> winner modAMM priority 15; owners: modAMM:15, modW3EE:21, modexpansionzero:228
- game\gui\hud\modules\hudModuleRadialMenu.ws -> winner mod0_E3HUD_W3EER_NG priority 8; owners: mod0_E3HUD_W3EER_NG:8, modBetterIcons2025_NextGen_W3EE:11, modW3EE:21, modexpansionzero:228
- game\gameplay\effects\effects\other\repairObjectEnhancement.ws -> winner modW3EE priority 21; owners: modW3EE:21, modexpansionzero:228
- game\gameplay\effects\effects\other\wellFed.ws -> winner modW3EE priority 21; owners: modW3EE:21, modexpansionzero:228
- game\gameplay\leveling\levelManager.ws -> winner modW3EE priority 21; owners: modW3EE:21, modexpansionzero:228

CSV: C:\Users\marti\OneDrive\Documents\New project\Witcher-3\logs\tosa-shadow-inventory-2026-06-24.csv

## Decision

Do not perform a blanket Script Merger/manual port pass for Time of the Sword and Axe. The highest-marker files are core W3EE/Brothers in Arms/Gwent Redux/Better Icons ownership zones, and the game currently compiles. Treat the shadowed ToSA paths as feature-validation backlog items.

The only immediate ordering correction was `local\effects\vitalityRaise.ws`: `modVernaShrine_Everlasting` must win over `modexpansionzero` because it keeps the shrine effect timer refreshed. Both active `mods.settings` files were adjusted so `modVernaShrine_Everlasting` is priority 228 and `modexpansionzero` is priority 229.

Smoke test after the priority correction: passed. DX12 process remained running after 45 seconds.
