# Startup No-Window Hang Isolation - Night to Remember

Date: 2026-06-24

Symptom:
- User reported the game was not running/visible.
- Prior smoke tests were misleading because they only checked whether `witcher3.exe` stayed alive.
- Actual behavior:
  - `witcher3.exe` stayed running.
  - No top-level window was created.
  - CPU kept climbing at roughly one core.
  - Memory stabilized around `4.1 GB`.
  - No script compilation dialog appeared.

Baseline checks:
- Base game with an empty `mods` folder created a real window in about 10 seconds.
- Therefore the issue was in the active mod stack, not the launcher or display settings.

Isolation:
- Temporarily moved the newest post-2PM mod batch out of `mods`.
- Window appeared in about 15 seconds.
- Restored the batch in halves/chunks.
- Clean:
  - `modNoArtificialPlayerLight`
  - `modWitcherLoreCollection`
  - `modNPCTargetingPriorityAndAxiiFixes`
  - `mod_ShadowFlickersFix`
  - `modMenuOrganizerNG_IMM_MrCK`
  - `modGameplayMimicsFix`
  - `modFixStuckQuestItems`
  - `modFixReactionOfSwordHitsWhenAddingEffects`
  - `modFixOceanBottom`
- Culprit:
  - `modNightToRemember`

Action:
- Moved `modNightToRemember` out of active `mods` to:
  - `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\_codex_disabled_mods\modNightToRemember.disabled-by-codex-startup-hang-20260624`
- Set `[modNightToRemember]` to `Enabled=0` in both active `mods.settings` files.

Verification:
- Full stack minus `modNightToRemember` created a real DX12 window in about 15 seconds.
- No Witcher process was left running after the test.

Notes:
- This is not a normal script compile failure.
- It presents as a pre-window startup loader hang/loop.
- Future work on the Night to Remember quest mod should start with package/content isolation, not Script Merger.
