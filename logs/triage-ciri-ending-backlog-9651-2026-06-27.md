# Ciri Witcher Ending Restoration Backlog Triage - 9651

Date: 2026-06-27

## Result

No new install action is recommended.

The selected installed variant remains:

- `mod_ciri_witcherending_restored`
- Source archive: `Ciri Witcher Ending Restoration-9651-1-1a-1732131588.rar`

## Keep

`1.1a` is still the best fit for the current stack because it is the newer normal restoration archive and avoids the extra script surface of the `SPECIAL` variant.

## Skip

| Download | Decision |
| --- | --- |
| `Ciri Witcher Ending Restoration-9651-1-1-1726416351.rar` | Older normal archive. Superseded by installed `1.1a`. |
| `Ciri Witcher Ending Restoration - SPECIAL-9651-1-2-1734434769.rar` | Skip. Includes avoidable Gwent script risk with the active Gwent Redux stack. |
| `Ciri Witcher Ending Restoration - 10th Anniversary-9651-1-3-1764165432.rar` | Skip for now. Triss-special route flavor does not match the current Yennefer-oriented setup. |

## Conflict Rule

BiA wins direct conflicts by default. Do not globally move `mod_ciri_witcherending_restored` above BiA, because that could override other curated BiA/Corvo/guest choices. If a specific ending scene is missing later, handle it as a selective compatibility decision instead of a global priority flip.
