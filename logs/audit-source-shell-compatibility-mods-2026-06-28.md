# Audit: Source-Shell Compatibility Mods

Date: 2026-06-28

## Goal

Identify enabled folders whose loose scripts all lose to higher-priority merged files, then separate true redundancy from source/reference shells where the behavior has been manually grafted elsewhere.

## Mechanical Scan

Enabled folders with scripts but zero winning scripts:

| Folder | Runtime payload read |
| --- | --- |
| `mod00AMMW3EEReduxNG139b` | Source shell. Its only `playerWitcher.ws` loses to `mod0000_MergedFiles`, but AMM/W3EE compatibility blocks are present in the active merged `playerWitcher.ws`. |
| `modBasicCookingRecipes` | Future cleanup candidate. It has only two losing alchemy scripts; the useful payload appears to be `dlcBasicCookingRecipes`. Needs in-game recipe check before archiving the script shell. |
| `modNPCTargetingPriorityAndAxiiFixes` | Source shell. Broad scripts lose by design; helper behavior and call sites are present in active W3EE/Nobs/MergedFiles winners. |
| `modAllGearEnchantingBasedOnSockets` | Source/string shell after graft. Main behavior is in active Better Icons/W3EE enchanting path; strings remain installed. User validation passed. |
| `modReduxW3EE` | Core Redux content/config/string/cache layer. Its loose script loss is not a cleanup signal. |
| `modshrinesofverna` | Split compatibility install. Bundle/cache/DLC/localization assets remain; duplicate local scripts are disabled or superseded by Everlasting Shrine behavior. |
| `modmanticor` | Bundle/DLC/string content layer. Loose `temp.ws` intentionally loses to W3EE. |
| `mod00ReputationSystem_W3EE_REDUX` | Economy/reputation data layer. Scripts lose to Floren Economy by design; not a cleanup candidate. |

## AMM W3EE Redux Patch

Folder: `mod00AMMW3EEReduxNG139b`

Current shape:

- One file:
  - `content\scripts\game\player\playerWitcher.ws`
- No bundles, strings, XML, or cache.

Evidence in active merged owner:

- AMM field and initialization are present in active `mod0000_MergedFiles\...\playerWitcher.ws`:
  - `var vAMM : CAMM;`
  - `vAMM = new CAMM in this;`
  - `AddTimer('InitAMM', 2.0, false);`
  - `timer function InitAMM(...)`
  - `function getAMM() : CAMM`
- W3EE Redux compatibility blocks from the patch are also present.

Decision:

- Keep for now as a source/reference shell because it documents the AMM/W3EE merge source.
- Possible future cleanup: archive only after verifying AMM menu and appearance toggles still work with the folder removed from the active scan path.

## NPC Targeting Priority And Axii Fixes

Folder: `modNPCTargetingPriorityAndAxiiFixes`

Current shape:

- Five broad game scripts lose to active W3EE/Nobs/MergedFiles owners.
- One duplicate helper file is disabled:
  - `modNPCTargetingPriorityAndAxiiFixes.ws.disabled-by-codex-duplicate-w3ee-graft`

Evidence in active winners:

- `mod0000_MergedFiles\content\scripts\game\npc\npc.ws` has mod-specific `UnforceTarget` call sites.
- Active W3EE/Nobs files already contain the needed Axii/confusion targeting behavior from earlier graft work.

Decision:

- Keep for now as a source/reference shell.
- Do not remove casually; if we archive it later, first snapshot the exact graft locations in active W3EE/Nobs/MergedFiles scripts.

## Rule Learned

An enabled folder with zero winning scripts can mean three different things:

1. dead/redundant folder,
2. source shell after manual graft,
3. content/DLC/string folder whose loose scripts intentionally lose.

Only the first category is a removal candidate. The current stack has many cases in categories 2 and 3.
