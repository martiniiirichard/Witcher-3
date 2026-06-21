# Swords on Roach Install Log - 2026-06-21

## Goal

Install Swords on Roach with the AMM Next-Gen compatibility patch on top of the confirmed W3EE Redux + AMM stack.

## Branch

- `codex/swords-on-roach`

## Nexus Pages

- Base: `https://www.nexusmods.com/witcher3/mods/3952`
- AMM compatibility patch: `https://www.nexusmods.com/witcher3/mods/10830`

## Archives Used

- `Swords on Roach-3952-1-4-ng-1671371791.rar`
- `Next-Gen Compatibility Patch-10830-1-0-1747366393.zip`

## Installed Files

Base Swords on Roach:

- `mods\modSwordsonroach`
- `dlc\dlcSwordsOnRoach`
- `bin\config\r4game\user_config_matrix\pc\modASwordsonroach.xml`

AMM compatibility patch overlay:

- Replaced `mods\modSwordsonroach\content\scripts\local\swordsonroach.ws`

The installed `swordsonroach.ws` contains AMM calls such as:

- `GetWitcherPlayer().getAMM().AMMisDisabled`
- `GetWitcherPlayer().getAMM().ApplyStscab()`
- `GetWitcherPlayer().getAMM().ApplySvscab()`
- `GetWitcherPlayer().getAMM().SwordsChange(...)`

## Config Changes

Added to both Next-Gen filelists:

```text
modASwordsonroach.xml;
```

Files updated:

- `bin\config\r4game\user_config_matrix\pc\dx11filelist.txt`
- `bin\config\r4game\user_config_matrix\pc\dx12filelist.txt`

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modSwordsonroach]
Enabled=1
Priority=11
```

## Current Load Order

```ini
[mod00AMMW3EEReduxNG139b]
Enabled=1
Priority=1

[mod_SNC_W3EERedux]
Enabled=1
Priority=2

[modAMM]
Enabled=1
Priority=3

[modSharedImports]
Enabled=1
Priority=4

[modReduxW3EE]
Enabled=1
Priority=5

[modW3EE]
Enabled=1
Priority=6

[modW3EELocalization1]
Enabled=1
Priority=7

[modW3EELocalization2]
Enabled=1
Priority=8

[modW3EELocalization3]
Enabled=1
Priority=9

[modW3EELocalization4]
Enabled=1
Priority=10

[modSwordsonroach]
Enabled=1
Priority=11
```

## Verification

- Confirmed `mods\modSwordsonroach` exists.
- Confirmed `dlc\dlcSwordsOnRoach` exists.
- Confirmed `modASwordsonroach.xml` exists.
- Confirmed patched `swordsonroach.ws` is installed.
- Confirmed `dx11filelist.txt` and `dx12filelist.txt` include `modASwordsonroach.xml;`.
- Confirmed these XML files parse successfully:
  - `modASwordsonroach.xml`
  - `AMM.xml`
  - `AMMRoach.xml`
  - `hidden.xml`
  - `input.xml`

## Rollback

If launch fails because of this mod:

1. Remove `mods\modSwordsonroach`.
2. Remove `dlc\dlcSwordsOnRoach`.
3. Remove `bin\config\r4game\user_config_matrix\pc\modASwordsonroach.xml`.
4. Remove `modASwordsonroach.xml;` from both `dx11filelist.txt` and `dx12filelist.txt`.
5. Remove the `[modSwordsonroach]` section from `C:\Games\The Witcher 3\mods.settings`.

## Next Validation

Launch the game and verify:

- No script compilation errors.
- Swords on Roach menu appears.
- AMM menu still appears.
- Standing near Roach, pressing sword keys can place/retrieve swords.
- Mounted sword draw/retrieve behavior does not break AMM appearances.

Do not commit this install log until launch test succeeds.
