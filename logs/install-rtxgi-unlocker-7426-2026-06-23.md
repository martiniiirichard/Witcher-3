# RTXGI Setting Unlocker 7426

Source: https://www.nexusmods.com/witcher3/mods/7426

## Files

- Unlocker download: `C:\Users\marti\Downloads\RTXGI unlocker and setting auto-updater-7426-4-04c-1739728925(1).zip`
- Preset download, not applied: `C:\Users\marti\Downloads\Complete RT Ultra dx12user.settings-7426-4-04c-1739733271(1).zip`
- Installed DLL: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\x64_dx12\xinput9_1_0.dll`
- Backup root: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\rtxgi-unlocker-7426-20260623-183003`

## Decision

Installed only the RTXGI unlocker DLL.

Did not apply the complete RT Ultra `dx12user.settings` preset. That preset changes a large number of DX12 rendering settings and should be treated as a performance/visual profile choice, not a required mod install step.

## Notes

The unlocker README says the DLL belongs next to `witcher3.exe` in `bin\x64_dx12`.

The DLL can read live overrides from a `custom.ini` file in the game `bin` folder. This can be useful later for controlled RTXGI/RT testing.

Current local `dx12user.settings` already has RT disabled:

```ini
[Rendering/RT]
EnableRT=false
EnableRtRadiance=false
RTAOEnabled=false
```

## Verification

- There was no pre-existing `xinput9_1_0.dll` in `bin\x64_dx12`, so this was a clean add.
- DX12 smoke test passed.
- The game process stayed running after 45 seconds and was then stopped manually by Codex.

## Rollback

Remove:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\x64_dx12\xinput9_1_0.dll`

No `dx12user.settings` changes were made for this install.
