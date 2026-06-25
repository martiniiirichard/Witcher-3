# Immersive Wine Cellar of Corvo Bianco 8548 - 2026-06-24

Source: https://www.nexusmods.com/witcher3/mods/8548

Installed archives:

- `C:\Users\marti\Downloads\dlcvineyard-8548-2-2-1768338301.zip`
- `C:\Users\marti\Downloads\dlcvineyard(dlc menu strings)-8548-1-2-1696160018.zip`

Installed payload:

- `DLC\dlcvineyard`

Archive contents:

- Main DLC: `content\blob0.bundle`, `content\metadata.store`, and localized `.w3strings`
- Menu strings overlay: English/Russian `.w3strings` and `.csv` localization files

Compatibility decision:

- The mod page describes this as a pure DLC mod with no technical compatibility issues.
- No `mods.settings` entry was added because there is no `mods\...` folder or WitcherScript payload.
- The optional DLC menu strings archive was applied over the main `dlcvineyard` folder.

Verification:

- DX12 smoke test passed; process remained running after 45 seconds.

Follow-up:

- In-game validation requires Corvo Bianco after `Capture the Castle` and vineyard renovation. Check the wine cellar tool box, hammer/taps, barrel interactions, and wine restock behavior.
