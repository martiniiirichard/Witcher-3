# Stack Health Audit After RER and WPI

Date: 2026-06-22

Scope:
- Post Random Encounters Reworked
- Post RER Icons addon
- Post Wearable Pocket Items Redux

Repository:
- Branch audited: `main`
- Working tree was clean before audit.

Merged script layer:
- `mod0000_MergedFiles` currently contains 12 active `.ws` files:
  - `game/components/inventoryComponent.ws`
  - `game/gameplay/interactive/monsterNestEntity.ws`
  - `game/gameplay/items/itemEntity.ws`
  - `game/gameplay/items/throwables/petards/petard.ws`
  - `game/gameplay/poster.ws`
  - `game/gui/menus/menuBase.ws`
  - `game/npc/npc.ws`
  - `game/player/playerAiming.ws`
  - `game/player/playerWitcher.ws`
  - `game/player/r4Player.ws`
  - `game/quests/quest_function.ws`
  - `game/vehicles/vehicleComponent.ws`

WPI Redux:
- Only active script inside `mod_WPI_Redux` is `local/WPI.ws`.
- 9 broad WPI game-script overrides are disabled as `.disabled-by-codex`.
- WPI hooks are grafted into the merged script layer.

Menu filelists:
- `dx11filelist.txt` contains `modRandomEncountersReworked.xml;` exactly once.
- `dx12filelist.txt` contains `modRandomEncountersReworked.xml;` exactly once.
- `dx11filelist.txt` contains `WPI.xml;` exactly once.
- `dx12filelist.txt` contains `WPI.xml;` exactly once.

Mods settings:
- Sections: 117
- Priority entries: 117
- Max priority: 117
- Duplicate sections: 0
- Duplicate priorities: 0

Validation status:
- User confirmed launch passed after RER.
- User confirmed launch passed after RER Icons.
- User confirmed launch passed after WPI Redux.

Operating rule:
- The stack still has many bundled non-text conflicts from cosmetic asset overlaps. These are acceptable when the intended winner is selected by priority and there are no script compile errors.
- Treat script conflicts and launch compile errors as blockers; treat bundled non-text conflicts as priority decisions unless a visual bug appears in-game.
