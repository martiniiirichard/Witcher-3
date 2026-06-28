# Decision: Skip Easier to Read Font Mod for TW3 (11657)

Date: 2026-06-27
Source: https://www.nexusmods.com/witcher3/mods/11657
Archives:

- `C:\Users\marti\Downloads\Easier to Read for TW3 - UI Fix.rar`
- `C:\Users\marti\Downloads\Easier to Read for TW3 - Belgrano-11657-1-0-1767247130.rar`

## Decision

Skip for now.

## Why

The Nexus page describes this as a font replacer that removes the default condensed font and changes Latin glyphs. The archives are bundle-only and contain no scripts:

- `modtw3EasierToRead-UI-Fix/content/blob0.bundle`
- `modTW3FontBelgrano/content/blob0.bundle`

This is technically low compile risk, but it is not low UI-layout risk. We already had to tune E3 HUD/menu text spacing. A wider, less-condensed font can make the exact menu clipping issues worse.

Keep the current E3 HUD text baseline unless we intentionally run a font screenshot comparison pass.

## Status

No live game files changed.
