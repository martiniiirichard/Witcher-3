# Naked Geralt 2183

Date: 2026-06-23

## Source

- https://www.nexusmods.com/witcher3/mods/2183

The Nexus description was behind the adult-content gate in the browser, so the local FOMOD installer metadata was used as the install source of truth.

## Installed Download

- `C:\Users\marti\Downloads\Naked Geralt - All in One Installer v0.6.7 - for 1.31-2183-0-6-7.zip`

## Install Approach

This archive is a FOMOD-style all-in-one installer with many mutually exclusive variants. I did not copy the whole archive into `mods`. Instead, I installed only the FOMOD default path.

Installed default variant folders:

- `mods\modNG_modNudeUndies_M_MFla_B`
- `mods\modNG_modNudeWet_M_MFla_B`
- `mods\modNG_modNudeBody_M_MEre_B`
- `mods\modNG_modTowel_NoTowel`
- `mods\modNG_modUndiesVanillaFix`
- `mods\modNG_tex_MH_Scars_LightPubicHair`
- `mods\modNG_texAs_ScarsOriginal`

Default choices represented:

- Middle/default model position.
- Default underwear/body/wet-body model choices from the installer.
- No towel variant.
- Vanilla underwear mesh fix.
- Original scars with the default light body-hair texture.
- No Heart of Stone texture override.

## Load Order

Added to both active `mods.settings` copies:

- `modNG_modNudeUndies_M_MFla_B`: priority `205`
- `modNG_modNudeWet_M_MFla_B`: priority `206`
- `modNG_modNudeBody_M_MEre_B`: priority `207`
- `modNG_modTowel_NoTowel`: priority `208`
- `modNG_modUndiesVanillaFix`: priority `209`
- `modNG_tex_MH_Scars_LightPubicHair`: priority `210`
- `modNG_texAs_ScarsOriginal`: priority `211`

## Script Merger

No Script Merger pass needed. Installed folders are bundled model/texture content only and contain no `.ws` scripts.

## Verification

- Confirmed all seven selected folders exist under `mods`.
- DX12 smoke test passed when launching `bin\x64_dx12\witcher3.exe` with its own working directory; process stayed alive for 45 seconds and was killed manually.

## Residual Risk

- The package is old and labeled for game `1.31`; because it is content-only, it can still load, but visual QA matters.
- Main visual risk is conflict with other Geralt body, underwear, towel, bath, or scene model replacers.
- Visual QA target: Geralt underwear/no-armor state, bath/wet scenes, towel scenes, and scenes using the vanilla underwear fix.
