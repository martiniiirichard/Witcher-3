# Enable Debug Console - Testing Workflow

Date: 2026-06-23

## Reason

The current saves/characters cannot easily reach all regions or trigger all weather/time conditions needed to visually QA the weather, lighting, rain, Toussaint, Skellige, and Live Bestiary stack.

## Change

Enabled the built-in Witcher 3 debug console by editing:

`C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\bin\config\base\general.ini`

Added:

```ini
[General]
DBGConsoleOn=true
```

Created a timestamped backup:

`general.ini.codex-backup-debug-console-<timestamp>`

## Verification

Runtime smoke:

- Launched `Witcher3DirectDX12.exe`.
- `witcher3.exe` was alive and responding after 45 seconds.
- Closed the game after the smoke test.

## Console Access

Try opening the console in-game with:

- `~`
- or `F2`

Keyboard/layout can affect the key.

## Useful Test Commands

Use a disposable/manual test save before running commands.

Region movement:

```text
gotoNovigrad
gotoSkellige
gotoKaerMohren
gotoProlog
gotoPrologWinter
```

Fast travel and map reveal:

```text
AllowFT(1)
ShowAllFT(1)
ShowPins(1)
```

Weather:

```text
changeweather(WT_Clear)
changeweather(WT_Light_Rain)
changeweather(WT_Rain_Storm)
changeweather(WT_Heavy_Clouds_Dark)
changeweather(WT_q501_Storm)
makeitrain
stoprain
```

Time of day:

```text
settime(1,6,0,0)
settime(1,12,0,0)
settime(1,18,0,0)
settime(1,23,0,0)
```

Live Bestiary:

```text
activateAllGlossaryBeastiary
```

Player setup:

```text
addmoney(5000)
setlevel(30)
levelup
```

## Notes

The newly downloaded mods did not include an obvious dedicated visual testing toolkit. The practical testing toolkit is:

- Built-in debug console.
- Existing `Fast Travel Pack`.
- Existing `Spawn Companions`/Bootstrap utilities if needed later.
- Standalone `Witcher 3 Interactive Map`, which can be staged separately as an external reference tool.

Console command references checked:

- https://witcher-games.fandom.com/wiki/The_Witcher_3_console_mode
- https://commands.gg/witcher3
