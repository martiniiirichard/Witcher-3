# Decision: Skip Instant Tooltips (2019)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/2019
Archive: `C:\Users\marti\Downloads\Instant Tooltips-2019-1-311.7z`

## Decision

Skip for now.

## Why

The archive is bundle-only and contains no `.ws` scripts:

- `modInstantTooltips/content/blob0.bundle`
- `modInstantTooltips/content/metadata.store`

However, the Nexus description says the mod works by modifying `componentslib.redswf` to reduce tooltip popup delay.

That shared UI component file is risky in our current stack because E3 HUD, W3EE Redux, Better Icons, Menu Organizer, Live Bestiary behavior, and prior UI fixes are now stable. Installing this below E3 HUD may do nothing; installing it above E3 HUD may replace a shared UI component and destabilize menus/tooltips.

The value is convenience only. Keep the stable UI stack unless tooltip delay becomes a specific complaint.

## Status

No live game files changed.
