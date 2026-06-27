# Random Encounters Reworked Low-Frequency Horror Tuning

Date: 2026-06-26

Target:
- Make RER behave like a rare wilderness horror/event system, not a background spawn generator.
- Countryside ambush target: roughly 3-4 serious incidents per 20 hours.
- Cities/settlements target: almost quiet, roughly one rare incident per 20 hours and mostly human/social.
- Disable higher-vampire random encounters entirely.
- Minimize monster multiplication and grouped-mob behavior.

Edited live file:
- `C:\Users\marti\OneDrive\Documents\The Witcher 3\dx12user.settings`

Backups:
- Repo backup folder: `backups/rer-low-frequency-profile-20260626`
- Live backup: `C:\Users\marti\OneDrive\Documents\The Witcher 3\dx12user.settings.codex-backup-rer-low-frequency-20260626-205846`

Applied values:
- `customdFrequencyLow=3600`
- `customdFrequencyHigh=6000`
- `customnFrequencyLow=1200`
- `customnFrequencyHigh=2400`
- `RERadditionalDelayPerPlayerLevel=0`
- `RERecosystemFrequencyMultiplier=0`
- `minSpawnDistance=100`
- `spawnDiameter=160`
- `RERstaticEncounterSmallSpawnChance=25`
- `RERstaticEncounterLargeSpawnChance=5`
- `RERfoottracksRatio=25`
- `RERcancelSpawnsWhenNearQuestMarkers=true`
- `allowSpawnInBigCities=false`
- `RERsettlementDelayMultiplier=5`
- `RERenemyCountMultiplier=1`
- `allMonsterAmbushChanceDay=1`
- `allMonsterAmbushChanceNight=4`
- `allMonsterHuntChanceDay=1`
- `allMonsterHuntChanceNight=4`
- `allMonsterHuntingGroundChanceDay=5`
- `allMonsterHuntingGroundChanceNight=10`
- `eventSystemICD=300`
- `eventBloodNecrophages=1`
- `eventBodiesNecrophages=2`
- `eventEntersSwamp=4`
- `eventFightNoise=0`
- `eventFillCreaturesGroup=0`
- `eventFillCreaturesGroupAllowCombat=false`
- `eventMeditationAmbush=3`
- `Higher_Vampires=0` in ambush/hunt/hunting-ground active sections.
- `RERhoursBeforeNewContracts=24`
- `RERcontainerRefillChanceMultiplier=0`
- `RERonlyKnownBestiaryCreatures=true`
- `enableActionCameraScenes=false`
- `hideNextNotifications=true`
- `ecosystemCommunityPowerEffect=0`
- `ecosystemCommunityPowerSpread=0`
- `ecosystemCommunityNaturalDeathSpeed=20`
- RER tutorials disabled.

Notes:
- RER region constraints treat `no_mans_land` and `novigrad` together in some logic, so Novigrad quietness relies on big-city suppression, settlement delay, and low event cadence rather than a clean separate Novigrad frequency slider.
- `Higher_Vampires=0` in region constraints alone would not disable them, because `0` means "no region constraint" there. The important disable is in encounter weight/chance sections.
- No scripts or mod files were changed; this is a settings-only tuning pass.
