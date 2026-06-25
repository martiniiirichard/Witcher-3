# The Witcher Card Game Music Replacement 4693 - 2026-06-24

Source: https://www.nexusmods.com/witcher3/mods/4693

Installed archive:

- `C:\Users\marti\Downloads\TWCG random theme-4693-1-0-1588593744.zip`

Installed payload:

- `mods\modTWCG_RandomOST`

Archive contents:

- `content\soundspc.cache`

Settings added to both active `mods.settings` files:

```ini
[modTWCG_RandomOST]
Enabled=1
Priority=232
```

Compatibility decision:

- The mod page says not to install multiple TWCG music variants because they replace the same Gwent music files.
- No other TWCG variant was found installed.
- No WitcherScript files are included, so no script merge is expected.
- `modLessmusic` exists in the stack, but no direct same-file `.wem` ownership was found by static scan. If Gwent music behaves unexpectedly, inspect bundled non-text/audio conflicts in Script Merger.

Verification:

- DX12 smoke test passed; process remained running after 45 seconds.

Follow-up:

- In-game validation requires starting a Gwent match outside Toussaint and confirming the random Witcher Card Game music plays.
