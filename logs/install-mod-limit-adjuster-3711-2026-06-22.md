# Mod Limit Adjuster 3711

Installed: 2026-06-22

Source:
- Nexus: https://www.nexusmods.com/witcher3/mods/3711
- ASI loader: https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases

Installed files:
- `bin/x64/dinput8.dll`
- `bin/x64/ModLimitAdjuster.asi`
- `bin/x64/ModLimitAdjuster.cfg`
- `bin/x64_dx12/dinput8.dll`
- `bin/x64_dx12/ModLimitAdjuster.asi`
- `bin/x64_dx12/ModLimitAdjuster.cfg`

Config:
- `ModLimit = 700`

Notes:
- This is not a WitcherScript mod, so Script Merger is not required.
- The Nexus page explicitly requires an ASI loader. The x64 Ultimate ASI Loader `dinput8.dll` was used.
- Installed into both executable folders so the limit patch is active for either DX11 or DX12 launch.
- Avoid `dsound.dll` for this stack unless a later tool requires it; the Nexus instructions warn to use `dinput8.dll`.
