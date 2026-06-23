# W3EE Redux Vigor Regen Tweak Manual Merge

Date: 2026-06-23

Source:
- Nexus mod 9416
- File: `W3EE Redux - Vigor Regen Tweak`
- Downloaded archive: `C:\Users\marti\Downloads\W3EE Redux - Vigor Regen Tweak-9416-1-1-1722604945.rar`

Install decision:
- Did not directly copy the archive over `modW3EE`.
- The archive ships a replacement:
  `mods\modW3EE\content\scripts\game\gameplay\effects\effects\auto\adrenaline.ws`
- Direct copy would have reverted newer W3EE Redux logic already present in our installed script.

Manual merge target:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modW3EE\content\scripts\game\gameplay\effects\effects\auto\adrenaline.ws`

Merged behavior:
- Added `regenDelay`.
- Added a regen delay gate at the start of `OnUpdate`.
- Added movement-aware vigor regeneration behavior:
  - running/moving fast stops focus gain and applies a short delay
  - guarded stance reduces focus gain
  - standing still increases focus gain

Preserved current W3EE Redux behavior:
- `Kolaris - Mutation Rework`
- `Kolaris - Mutation 2, Kolaris - White Honey`
- Existing W3EE Redux focus gain modifiers and toxicity penalty logic.

Backup:
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\Mods\modW3EE\content\scripts\game\gameplay\effects\effects\auto\adrenaline.ws.codex-backup-vigor-regen-tweak-20260623-161056`

Static verification:
- Active `adrenaline.ws` contains:
  - `regenDelay`
  - `playerVelocity`
  - `Vigor Regen Tweak` markers
  - `Kolaris - Mutation Rework`
  - `Kolaris - Mutation 2, Kolaris - White Honey`
- Only one active `adrenaline.ws` was found in the current `Mods` tree.

Risk notes:
- Compile risk is moderate because this modifies an active W3EE script directly.
- Balance risk is intentional: vigor regeneration now depends more strongly on movement/guard/standing state.
- Future W3EE Redux updates may overwrite this manual merge.

Pending verification:
- Launch compile test.
- Optional in-game stamina/vigor behavior smoke test.
