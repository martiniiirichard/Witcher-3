# Icy Ocean 8997 Install

Source: https://www.nexusmods.com/witcher3/mods/8997

## Files

- Next Gen script download: `C:\Users\marti\Downloads\Icy Ocean - Killer Whale-8997-1-0-1712950349(1).zip`
- Original dependency source: `C:\Users\marti\Downloads\Icy Ocean (2 percent version)-3895-1-0-9-1626160902.rar`
- Installed mod: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modIcyOcean`
- Installed DLC dependency: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\DLC\dlc__icy_ocean`
- Backup: `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\!codex-backups\icy-ocean-8997-20260623-180950`

## Decision

Installed the 8997 Next Gen Killer Whale variant and used the older 3895 archive only for the required `dlc__icy_ocean` DLC payload.

The Nexus page notes that the Next Gen file is script-side and still needs the original DLC folder. The local 3895 archive contained that DLC folder.

## Manual Merge

The first compile failed:

```text
Error [modicyocean]game\gameplay\effects\effects\damageovertime\icyoceaneffect.ws(11): Unable to parse value
```

Root cause: `modIcyOcean` defines `EET_IcyOcean`, but the active W3EE/NobsReflex effect type and effect manager scripts did not know about that enum value.

Patched both W3EE and NobsReflex copies to keep future merge passes stable:

- `Mods\modW3EE\content\scripts\game\gameplay\effects\effectTypes.ws`
- `Mods\modNobsReflex\content\scripts\game\gameplay\effects\effectTypes.ws`
- `Mods\modW3EE\content\scripts\game\gameplay\effects\gameEffectManager.ws`
- `Mods\modNobsReflex\content\scripts\game\gameplay\effects\gameEffectManager.ws`

Added:

- `EET_IcyOcean`
- `case EET_IcyOcean : effects[effect] = new W3Effect_IcyOcean in this; break;`
- `case "IcyOceanEffect" : type = EET_IcyOcean; break;`
- `case EET_IcyOcean : effectName = 'IcyOceanEffect'; break;`

## Verification

- DX12 compile smoke passed after the manual merge.
- The game process stayed running after 45 seconds and was then stopped manually by Codex.

## Remaining Functional Test

Functional behavior still needs an in-world check:

- Swim in a cold region/ocean.
- Confirm the Icy Ocean effect applies.
- Drink/use Killer Whale and confirm it suppresses/removes the Icy Ocean effect.

This was not tested during install because the smoke test only verifies script compilation.
