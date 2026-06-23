# Fix - Live Bestiary DLC Root Cleanup

Date: 2026-06-23

## Symptom

After the first Live Bestiary install pass, opening a later save showed a missing DLC dialog listing official DLC such as:

- Blood and Wine
- Hearts of Stone
- Beard and Hairstyle Set
- New Game+
- Multiple free quest DLCs

The official DLC folders were still present and had metadata.

## Cause

The first Live Bestiary pass created two loose helper folders directly under the game `dlc` root:

- `dlc\globals`
- `dlc\dlclb`

These were not real DLC packages and had no `content\metadata.store`. The game appears to scan direct children of `dlc` as DLC packages, so malformed direct children can confuse DLC detection.

## Fix

Moved the malformed folders out of the game DLC root to:

`backups\live-bestiary-invalid-dlc-roots-20260623-071600`

Then copied `lbTable.csv` into the valid Live Bestiary DLC content tree instead:

`dlc\DLCLiveBestiary\content\dlc\globals\lbTable.csv`

This preserves the virtual path expected by the active E3 HUD script:

`LoadCSV( "dlc\globals\lbTable.csv" )`

without creating fake DLC packages under the game `dlc` root.

## Verification

Checked direct children of the game `dlc` folder for malformed packages. After cleanup, the only remaining folder without `content\metadata.store` is:

- `DLCScabbards`

That folder predated this Live Bestiary change and had already been working in the current stack.

Runtime smoke:

- Launched `Witcher3DirectDX12.exe`.
- `witcher3.exe` was alive and responding after 45 seconds.
- Closed the game after the smoke test.

## Follow-Up

The user should retry the later save. If the official DLC missing dialog persists, the next suspect is DLC-count/load-order pressure rather than missing official DLC files.
