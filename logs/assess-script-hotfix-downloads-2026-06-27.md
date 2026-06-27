# Script Hotfix Download Assessment

Date: 2026-06-27

## Fix sounds of sword hits when adding effects - 11267

Archive:
- `C:\Users\marti\Downloads\Fix sounds of sword hits when adding effects-11267-1-2-5-1-1770319556.7z`

Decision:
- Do not install raw.

Reason:
- Active W3EE `actor.ws` already contains the intended Codex 11267 sound behavior:
  - kill actions carry `playHitSound`
  - damage sound handling includes `codex 11267: always allow strike sound when damage qualifies`
- Installing an external full script over W3EE would risk undoing later W3EE/BiA/current-stack edits.

## Life Steal Fix - 5104

Archive:
- `C:\Users\marti\Downloads\Life Steal Fix-5104-1-0-1749102829.rar`

Decision:
- Do not install raw.

Reason:
- Ships a full `game\player\r4Player.ws`.
- This is a core W3EE/player-state hot file and not worth replacing for a narrow fix without a manual graft target.

## Superior Black Blood redesign - 10416

Archive:
- `C:\Users\marti\Downloads\Superior Black Blood redesign-10416-1-1-1749839573.7z`

Decision:
- Do not install raw.

Reason:
- Ships full replacements for:
  - `game\gameplay\damage\damageManagerProcessor.ws`
  - `game\gameplay\effects\effects\potion\BlackBlood.ws`
- Those overlap W3EE, Nobs Reflex, toxicity, damage, and potion behavior.

## Skellige Ice Breath Compatibility - 4138

Archive:
- `C:\Users\marti\Downloads\Skellige Ice Breath Compatibility - Next Gen-4138-2-0-1672174955.rar`

Decision:
- Do not install.

Reason:
- Current `modIceBreath` is the newer Ice Breath Next Gen script.
- The compatibility archive is an older 1.02-style script.
- Current script already includes Skellige Winter Weather support plus newer dialogue/cutscene handling.

## Memory of Iris - 10939

Archive:
- `C:\Users\marti\Downloads\Memory of Iris-10939-0-1-1749825659.zip`

Decision:
- Do not reinstall.

Reason:
- Previously installed, then intentionally quarantined during low-value content cleanup as `modolgierd_rose`.
