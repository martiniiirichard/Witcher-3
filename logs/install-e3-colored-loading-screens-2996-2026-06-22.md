# E3 Colored Regional Loadingscreen 2996 install

Date: 2026-06-22

Branch: `codex/e3-colored-loading-screens-2996`

## Source archive

- `C:\Users\marti\Downloads\E3 Colored Regional Loadingscreen-2996-1-2.rar`

## Installed files

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modE3HUDColorLoad\content\blob0.bundle`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\mods\modE3HUDColorLoad\content\metadata.store`

## Configuration

`modE3HUDColorLoad` was added to `C:\Games\The Witcher 3\mods.settings` directly after the W3EER E3 HUD compatibility layer and before the base E3 HUD mod:

```ini
[mod0_E3HUD_W3EER_NG]
Priority=4

[modE3HUDColorLoad]
Priority=5

[modE3HUD]
Priority=6
```

This follows the mod page guidance to give the colored loading screen addon higher priority than the main E3 HUD file.

## Merge notes

- No `.ws` scripts.
- No `.xml` menu files.
- No `.redswf` files.
- No Script Merger work required.

## Verification

- DX12 direct launcher startup check passed.
- `witcher3.exe` stayed alive and responding after launch.

## Backup

- `C:\Users\marti\OneDrive\Documents\New project\Witcher-3\backups\e3-colored-loading-screens-2996-20260622-153212`

## User validation needed

Check a few regional loading screens in-game. This addon is visual-only, so the main validation is whether the colored E3 regional loading screens appear as expected.
