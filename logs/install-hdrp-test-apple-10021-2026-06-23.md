# HDRP Test Apple 10021

Source: https://www.nexusmods.com/witcher3/mods/10021

## Files

- Download: `C:\Users\marti\Downloads\HDRP Test Apple-10021-1-2-1741795768.zip`
- Installed mod: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modHDRPTestApple`
- Backup: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\hdrp-test-apple-10021-20260623-184421`

## Decision

Installed as a testing utility.

This mod spawns a vegetable/apple stand that can be used to visually confirm whether HD Reworked Project assets are active.

## Load Order

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modHDRPTestApple]
Enabled=1
Priority=177
```

## Input Handling

Did not apply the included `input.settings.txt` F10 binding:

```ini
[Exploration]
IK_F10=(Action=HDRPtest)
```

Reason: the script also exposes a console command, and avoiding another input binding keeps the heavily modded input stack cleaner.

Use this console command instead:

```text
HDRPtest()
```

It spawns:

```text
environment\decorations\decoration_sets\traders\decoration_set_trader_vegetable_a_ref.w2ent
```

## Verification

- DX12 compile smoke passed.
- The game process stayed running after 45 seconds and was then stopped manually by Codex.

## Testing Use

When HD Reworked Project is active/complete, load into a test save, run `HDRPtest()`, screenshot the spawned stand, and compare against HDRP reference visuals.

Note: this utility is useful even before HDRP is fully installed because it gives us a repeatable visual target for later comparison.
