# Direct Launcher Checkpoint

Date: 2026-06-22

## Purpose

Created a small launcher to bypass GOG Galaxy and REDprelauncher for faster mod testing.

## Source

- `launchers/Witcher3DirectLauncher.cs`

## Local Build Outputs

Compiled executables are local-only and ignored by Git:

- `tools/direct-launchers/Witcher3DirectDX12.exe`
- `tools/direct-launchers/Witcher3DirectDX11.exe`

Start Menu shortcuts were created under:

- `%APPDATA%/Microsoft/Windows/Start Menu/Programs/Witcher 3 Modded`

## Behavior

- DX12 launcher starts `bin/x64_dx12/witcher3.exe`.
- DX11 launcher starts `bin/x64/witcher3.exe`.
- No GOG Galaxy, REDprelauncher, launcher update check, or internet connection is required for normal single-player launch.

## Verification

- User confirmed the direct launcher worked.
- User confirmed it was much faster than the existing launcher.
