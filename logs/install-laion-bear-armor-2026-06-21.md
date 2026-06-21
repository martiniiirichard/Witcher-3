# Laion and Bear Armor Concept HD Install Log - 2026-06-21

## Goal

Install the Laion and Bear Armor color concept HD texture mod on top of the current stable W3EE Redux + AMM + Swords on Roach stack.

## Branch

- `codex/laion-bear-armor`

## Nexus Page

- `https://www.nexusmods.com/witcher3/mods/742`

## Archive Used

- `Laion and Bear Armor (Color) Concept HD-742-v3-0.rar`

## Risk Classification

Low risk.

Archive contents are texture/cache payload only:

- `modHDUrsineConcept_Lexars\content\metadata.store`
- `modHDUrsineConcept_Lexars\content\texture.cache`

No scripts, XML files, DLC folders, or input settings were included.

## Installed Files

Copied to game mods folder:

- `mods\modHDUrsineConcept_Lexars`

Installed files:

- `content\metadata.store`
- `content\texture.cache`

## Config Changes

Added to `C:\Games\The Witcher 3\mods.settings`:

```ini
[modHDUrsineConcept_Lexars]
Enabled=1
Priority=12
```

## Verification

- Confirmed installed mod folder exists.
- Confirmed only `metadata.store` and `texture.cache` are present.
- Confirmed no `.ws`, `.xml`, or `.txt` files were added by this mod.
- Script Merger should not show new script conflicts from this install.

## Next Validation

Launch the game and verify:

- No script compilation errors.
- Bear/Ursine armor texture appears as expected.
- Existing AMM and Swords on Roach behavior still works.

Do not commit this install log until launch test succeeds.
