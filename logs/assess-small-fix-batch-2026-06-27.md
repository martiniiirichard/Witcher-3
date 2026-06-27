# Small Fix Batch Assessment

Date: 2026-06-27

## Fix sound of rotfiend exploding - 11267

Archive:
- `C:\Users\marti\Downloads\Fix sound of rotfiend exploding-11267-1-2-6-1771986672.7z`

Decision:
- Do not install raw.

Reason:
- Archive ships a full `btTaskExplodeAtDeath.ws`.
- Active owner is W3EE.
- The useful fix is already grafted into W3EE:
  - `l_damageAction.SetSuppressHitSounds( true ); // codex 11267: suppress sword-hit sound from rotfiend explosion`
- Raw install would replace W3EE's adjusted rotfiend death explosion behavior.

## Fix Loot Sound - 8316

Archive:
- `C:\Users\marti\Downloads\Fix Loot Sound 4.03-8316-0-2-1688671368.zip`

Decision:
- Do not install raw.

Reason:
- Archive ships full replacements for:
  - `game\components\inventoryComponent.ws`
  - `game\gameplay\containers\container.ws`
  - `game\gui\popups\LootPopup.ws`
- Those are hot files owned by W3EE, Better Icons, Floren Economy, Reputation, Expansion Zero, BiA, and merged files.
- The useful behavior is already grafted into active W3EE / Better Icons paths:
  - Buckthorn uses herb loot sound.
  - Single-item and take-all loot paths call the correct `PlayItemEquipSound(...)`.

## No Stair Rolling - 7774

Archive:
- `C:\Users\marti\Downloads\No Stair Rolling-7774-1-0-1674652801.zip`

Decision:
- Do not install.

Reason:
- Archive ships a full `explorationStateLand.ws`.
- Active owner is W3EE.
- Text diff showed only small movement-threshold differences and removal of W3EE's falling-damage option gate:
  - Candidate sets `m_AutoSlopeAngleB` to `60.0f`.
  - W3EE sets it to `80.0f`.
  - Candidate removes the `Options().FallingDamage()` guard.
- Not worth overriding W3EE movement behavior.

## Selected Bomb for Monster Nests - 7592

Decision:
- Installed.

Reason:
- Tiny annotation-only wrapper.
- Wraps existing `CMonsterNestEntity.PlayerHasBombActivator()`.
- Preserves active W3EE/merged `monsterNestEntity.ws`.

Verification:
- See `logs/install-selected-bomb-for-monster-nests-7592-2026-06-27.md`.
