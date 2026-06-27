# Witcher 3 Compile Error Analysis

- Game root: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY`
- mods.settings: `C:\Users\marti\OneDrive\Documents\The Witcher 3\mods.settings`
- Enabled mods in settings: `194`
- Parsed issues: `5`

## Summary

- `IGMActionType_MrckIMM`: 1 issue(s), kind `unknown_identifier`, active hits `6`, inactive/disabled hits `0`
- `UnforceTargetsAxiiGuardMe`: 1 issue(s), kind `global_function_already_defined`, active hits `1`, inactive/disabled hits `0`
- `AddHitReactionForCriticalEffects`: 1 issue(s), kind `missing_function`, active hits `2`, inactive/disabled hits `0`
- `ShowBookPopup`: 1 issue(s), kind `wrap_missing`, active hits `0`, inactive/disabled hits `0`
- `UnequipSkill`: 1 issue(s), kind `signature_mismatch`, active hits `39`, inactive/disabled hits `0`

## `IGMActionType_MrckIMM`

- Kind: `unknown_identifier`
- Likely cause: No provider found in active scripts. The mod may target another game version, require a missing dependency, or need a custom compatibility shim.

Occurrences:

- `Error [modmenuorganizerng_imm_mrck]mrckimm\imm_ng.ws(109)`: I dont know any 'IGMActionType_MrckIMM'

Symbol hits:

- `active` `modMenuOrganizerNG_IMM_MrCK` `direct_reference` `Mods\modMenuOrganizerNG_IMM_MrCK\content\scripts\mrckIMM\IMM.ws:1195`: l_DataFlashObject = CreateMenuItem(isOptions, "mrckimm_quicksave", "panel_mainmenu_quicksave", NameToFlashUInt('MrckIMM_QuickSave'), IGMActionType_MrckIMM, true);
- `active` `modMenuOrganizerNG_IMM_MrCK` `direct_reference` `Mods\modMenuOrganizerNG_IMM_MrCK\content\scripts\mrckIMM\IMM.ws:1200`: l_DataFlashObject = CreateMenuItem(isOptions, "mrckimm_quickload", "TmrckIMM_mainmenu_quickload", NameToFlashUInt('MrckIMM_QuickLoad'), IGMActionType_MrckIMM, true);
- `active` `modMenuOrganizerNG_IMM_MrCK` `direct_reference` `Mods\modMenuOrganizerNG_IMM_MrCK\content\scripts\mrckIMM\IMM.ws:1393`: l_DataFlashObject = CreateMenuItem(isOptions, "mainmenu_pages", label, typeInt, IGMActionType_MrckIMM, true);
- `active` `modMenuOrganizerNG_IMM_MrCK` `direct_reference` `Mods\modMenuOrganizerNG_IMM_MrCK\content\scripts\mrckIMM\IMM.ws:2618`: currentObject.SetMemberFlashUInt( "type", IGMActionType_MrckIMM );
- `active` `modMenuOrganizerNG_IMM_MrCK` `direct_reference` `Mods\modMenuOrganizerNG_IMM_MrCK\content\scripts\mrckIMM\IMM.ws:2624`: currentObject.SetMemberFlashUInt( "type", IGMActionType_MrckIMM );
- `active` `modMenuOrganizerNG_IMM_MrCK` `direct_reference` `Mods\modMenuOrganizerNG_IMM_MrCK\content\scripts\mrckIMM\IMM_NG.ws:109`: case IGMActionType_MrckIMM :

Suggested next action:

- Find which dependency should add the symbol; if no active provider exists, either install/enable dependency or remove/replace the referring code.

## `UnforceTargetsAxiiGuardMe`

- Kind: `global_function_already_defined`
- Likely cause: Compiler reports a duplicate, but the scan found limited definitions. Check merged files and generated Script Merger output.

Occurrences:

- `Error [modnpctargetingpriorityandaxiifixes]local\modnpctargetingpriorityandaxiifixes.ws(1)`: Global function 'UnforceTargetsAxiiGuardMe' is already defined.

Symbol hits:

- `active` `modW3EE` `function_definition` `Mods\modW3EE\content\scripts\local\codex_w3ee_graft_helpers.ws:25`: function UnforceTargetsAxiiGuardMe(target : CActor)

Suggested next action:

- Compare active definition providers. Usually disable the redundant compatibility mod or remove the duplicate annotation/full-file override.

## `AddHitReactionForCriticalEffects`

- Kind: `missing_function`
- Likely cause: Symbol exists somewhere active, so this is likely a load-order, class-scope, generation mismatch, or private/access issue.

Occurrences:

- `Error [modw3ee]game\gameplay\effects\effectmanager.ws(1516)`: Could not find function 'AddHitReactionForCriticalEffects'

Symbol hits:

- `active` `modW3EE` `function_definition` `Mods\modW3EE\content\scripts\local\codex_w3ee_graft_helpers.ws:1`: function AddHitReactionForCriticalEffects(action : W3DamageAction)
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\gameplay\effects\effectManager.ws:1516`: if((ret == EI_Pass || ret == EI_Cumulate) && !signEntity && IsCriticalEffectType(effectInfos[i].effectType) && !IsKnockdownEffectType(effectInfos[i].effectType) && effectInfos[i].effectType != EET_KnockdownTypeApplicator

Suggested next action:

- Find which dependency should add the symbol; if no active provider exists, either install/enable dependency or remove/replace the referring code.

## `ShowBookPopup`

- Kind: `wrap_missing`
- Likely cause: No provider found in active scripts. The mod may target another game version, require a missing dependency, or need a custom compatibility shim.

Occurrences:

- `Error [modinterfaceanim]local\interfaceanim\interfaceanim_override.ws(228)`: Wrap function 'ShowBookPopup' must wrap an existing function.

No symbol hits found in scanned scripts.

Suggested next action:

- Verify target game/W3EE method exists. If W3EE removed or renamed it, disable that patch or rewrite it against the current method.

## `UnequipSkill`

- Kind: `signature_mismatch`
- Likely cause: Function exists but signature differs. Compare base/W3EE/current signature and update call or override parameters.

Occurrences:

- `Error [modprimer]custom\alchemyskills.ws(178)`: Function 'UnequipSkill' takes 1 parameter(s) which is inconsistent with base function (2).

Symbol hits:

- `active` `mod0000_MergedFiles` `direct_reference` `Mods\mod0000_MergedFiles\content\scripts\game\player\playerWitcher.ws:1027`: UnequipSkill(S_Alchemy_s19);
- `active` `mod0000_MergedFiles` `direct_reference` `Mods\mod0000_MergedFiles\content\scripts\game\player\playerWitcher.ws:1160`: UnequipSkill( slot );
- `active` `mod0000_MergedFiles` `direct_reference` `Mods\mod0000_MergedFiles\content\scripts\game\player\playerWitcher.ws:11202`: UnequipSkill(GetSkillSlotID(skills[i]));
- `active` `mod0000_MergedFiles` `function_definition` `Mods\mod0000_MergedFiles\content\scripts\game\player\r4Player.ws:12961`: public function UnequipSkill(slotID : int) : bool
- `active` `mod0000_MergedFiles` `direct_reference` `Mods\mod0000_MergedFiles\content\scripts\game\player\r4Player.ws:12972`: ret = pam.UnequipSkill(slotID);
- `active` `mod00AMMW3EEReduxNG139b` `direct_reference` `Mods\mod00AMMW3EEReduxNG139b\content\scripts\game\player\playerWitcher.ws:1016`: UnequipSkill(S_Alchemy_s19);
- `active` `mod00AMMW3EEReduxNG139b` `direct_reference` `Mods\mod00AMMW3EEReduxNG139b\content\scripts\game\player\playerWitcher.ws:1149`: UnequipSkill( slot );
- `active` `mod00AMMW3EEReduxNG139b` `direct_reference` `Mods\mod00AMMW3EEReduxNG139b\content\scripts\game\player\playerWitcher.ws:11188`: UnequipSkill(GetSkillSlotID(skills[i]));
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:745`: thePlayer.UnequipSkill( BSS_SkillSlot1 );
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:746`: thePlayer.UnequipSkill( BSS_SkillSlot2 );
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:747`: thePlayer.UnequipSkill( BSS_SkillSlot3 );
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:748`: thePlayer.UnequipSkill( BSS_SkillSlot4 );
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:1303`: tryUnequipSkill(skill);
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:1388`: tryUnequipSkill(skill);
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:1415`: event  OnUnequipSkill(slotID : int)
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:1440`: LogChannel('CHR', "OnUnequipSkill " + slotID);
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:1441`: thePlayer.UnequipSkill(slotID);
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:1615`: protected function tryUnequipSkill(skill : ESkill):void
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:1629`: LogChannel('CHR', "tryUnequipSkill, currentSkillSlotIdx " + currentSkillSlotIdx);
- `active` `modNobsToolTipHandaler` `direct_reference` `Mods\modNobsToolTipHandaler\content\scripts\game\gui\menus\characterMenu.ws:1632`: res = thePlayer.UnequipSkill(currentSkillSlotIdx + 1);
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\player\playerWitcher.ws:1106`: UnequipSkill(S_Alchemy_s19);
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\player\playerWitcher.ws:1252`: UnequipSkill( slot );
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\player\playerWitcher.ws:11823`: UnequipSkill(GetSkillSlotID(skills[i]));
- `active` `modW3EE` `function_definition` `Mods\modW3EE\content\scripts\game\player\r4Player.ws:12842`: public function UnequipSkill(slotID : int) : bool
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\player\r4Player.ws:12853`: ret = pam.UnequipSkill(slotID);
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\gameplay\ability\PlayerAbilityManager.ws:140`: UnequipSkill(skillSlots[i].id);
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\gameplay\ability\PlayerAbilityManager.ws:151`: UnequipSkill(GetSkillSlotID(skills[i].skillType), true);
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\gameplay\ability\PlayerAbilityManager.ws:1708`: UnequipSkill(GetSkillSlotID(skill), true);
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\gameplay\ability\PlayerAbilityManager.ws:1770`: UnequipSkill(ind, true);
- `active` `modW3EE` `direct_reference` `Mods\modW3EE\content\scripts\game\gameplay\ability\PlayerAbilityManager.ws:2451`: UnequipSkill(i);
- ... 9 more hit(s) omitted

Suggested next action:

- Open the current winning base function and update parameter list/calls to match it.
