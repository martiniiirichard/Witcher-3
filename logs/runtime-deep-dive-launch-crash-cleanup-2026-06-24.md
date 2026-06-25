# Runtime Deep Dive - Launch Crash / Merge Footprint Cleanup

Date: 2026-06-24

Reason:
- User suspected the recent content-mod failures were not purely individual mod problems.
- Baseline launch began exiting immediately with code `1`.

Findings:
- A stray `witcher3.exe` process was still running with no window title:
  - Started around `2026-06-24 15:26`.
  - Later launches exited quickly until it was killed.
- Windows Event Viewer showed repeated Witcher 3 access violations:
  - Exception code: `0xc0000005`
  - Fault offset: `0x0000000001cf1980`
  - This matched the `-1073741819` launch failures seen with some large content packages.
- Several disabled folders still began with loader-looking names such as `mod...disabled...` or `DLC...disabled...`.
  - These were renamed with a `DISABLED_` prefix so the game loader should not treat them as active packages.
- `modPrimer` and `modAlchemyBIDEPatch` were supposed to be deferred/disabled per prior Alchemy Primer notes, but their folders still began with `mod` and no longer had active settings sections.
  - Both were quarantined with `DISABLED_` prefixes.
- `mod0BASENGEAll` was intentionally present but had no `mods.settings` section.
  - Added explicit settings for it.

Actions:
- Killed orphaned `witcher3.exe`.
- Renamed disabled loader-looking folders:
  - `modEnableMimics_blinking.disabled-*` -> `DISABLED_modEnableMimics_blinking.disabled-*`
  - `modFixNGESwordsBugfix.disabled-*` -> `DISABLED_modFixNGESwordsBugfix.disabled-*`
  - `modFloren.disabled-*` -> `DISABLED_modFloren.disabled-*`
  - `modkaer_morhen_extended.disabled-*` -> `DISABLED_modkaer_morhen_extended.disabled-*`
  - `mod_InterfaceAnim.disabled-*` -> `DISABLED_mod_InterfaceAnim.disabled-*`
  - `DLCEnableMimics.disabled-*` -> `DISABLED_DLCEnableMimics.disabled-*`
  - `dlc_InterfaceAnim.disabled-*` -> `DISABLED_dlc_InterfaceAnim.disabled-*`
- Quarantined deferred Alchemy Primer remnants:
  - `modPrimer` -> `DISABLED_modPrimer.disabled-by-codex-deferred-*`
  - `modAlchemyBIDEPatch` -> `DISABLED_modAlchemyBIDEPatch.disabled-by-codex-deferred-*`
- Added/updated settings in both active `mods.settings` files:
  - `[modPrimer] Enabled=0 Priority=259`
  - `[modAlchemyBIDEPatch] Enabled=0 Priority=260`
  - `[mod0BASENGEAll] Enabled=1 Priority=261`

Post-cleanup audit:
- No active-looking `mod*` folders are missing from `mods.settings`.
- No disabled folders still begin with `mod`, `dlc`, or `DLC`.
- Active package footprint after cleanup:
  - `209` active `mod*` folders.
  - `83` active `dlc*`/`DLC*` folders.

Verification:
- Baseline DX12 launch after cleanup passed:
  - Game remained running after 120 seconds.
- Retested `11934` Kaer Morhen Extended Edition after clean process state:
  - Still crashed with `ExitCode=-1073741819`.
  - Disabled again afterward.
- Baseline DX12 launch after disabling `11934` passed again:
  - Game remained running after 120 seconds.

Interpretation:
- There was a real structural/runtime issue: orphaned process plus unsafe disabled-folder naming and uncontrolled deferred folders.
- `11934` still appears incompatible with the current active stack after cleanup.
- Duplicate script paths remain numerous, but the baseline compiles/launches; they are not necessarily unresolved Script Merger conflicts.
- Large REDkit/content packages may still be hitting a content/package-load collision or limit in this stack.
