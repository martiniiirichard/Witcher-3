# Restored Content - Shrines of Verna 7307 - 2026-06-24

Source: https://www.nexusmods.com/witcher3/mods/7307

Installed archive:

- `C:\Users\marti\Downloads\Shrine of Verna-7307-2-0-1717720686.zip`

Installed payload:

- `DLC\dlcshrinesofverna`
- `mods\modshrinesofverna`

Settings added to both active `mods.settings` files:

```ini
[modshrinesofverna]
Enabled=1
Priority=231
```

Compatibility decisions:

- `modshrinesofverna\content\scripts\local\vitalityRaise.ws` was disabled as `vitalityRaise.ws.disabled-by-codex-everlasting-wins`.
  - Reason: `modVernaShrine_Everlasting` owns the better `W3Effect_VitalityRaise` implementation with timer refresh behavior.
- `modshrinesofverna\content\scripts\local\vernaShrine.ws` was disabled as `vernaShrine.ws.disabled-by-codex-tosa-owns`.
  - Reason: `modexpansionzero` from Time of the Sword and Axe already includes an identical `W3VernaShrine` class at `local\interactive\vernaShrine.ws`.
- Added `EET_VitalityRaise` effect manager mappings to the active higher-priority effect managers:
  - `modNobsReflex`
  - `modW3EE`
  - `modIcyOcean`

Effective ownership:

- Shrine interaction class: `modexpansionzero`
- Vitality raise effect class: `modVernaShrine_Everlasting`
- World/DLC assets and localization: `dlcshrinesofverna` / `modshrinesofverna`

Verification:

- Initial launch failed with duplicate `W3VernaShrine`; fixed by disabling 7307's duplicate local script.
- DX12 smoke test passed after the fix; process remained running after 45 seconds.

Follow-up:

- In-game validation should interact with a Verna shrine in Velen and confirm the vitality buff appears and persists with the Everlasting behavior.

## Posts Reviewed

Posts page checked after install: https://www.nexusmods.com/witcher3/mods/7307?tab=posts

Useful notes:

- A sticky/user report says the mod works with W3EE Redux 4.04 but should be merged. This matches the current install approach: keep the DLC/world assets, avoid duplicate local classes, and port only the missing active effect-manager mappings.
- A reported `local\vitalityraise.ws(5): Unable to parse value` error aligns with the known failure mode where `EET_VitalityRaise` is not visible/registered in the active effect stack. We addressed this by adding `EET_VitalityRaise` mappings to the active `gameEffectManager.ws` owners.
- The author notes older versions should be removed before installing newer ones. Current install uses only the v2.0 archive plus the Everlasting addon, with duplicate base scripts disabled.
