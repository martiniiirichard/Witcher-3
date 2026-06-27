# Audit: Additional Stash Locations + BiA Compatibility

Date: 2026-06-27

Question:

- Is `mod0BiA_ASL_Compatibility` redundant with `modAdditionalStashLocations`?

Result:

- Keep both.

Active settings:

| Mod | Enabled | Priority |
| --- | --- | --- |
| `mod0BiA_ASL_Compatibility` | `1` | `10` |
| `modAdditionalStashLocations` | `1` | `226` |

Unpacked bundle contents:

`mod0BiA_ASL_Compatibility`:

- `dlc/bob/data/game/hub_pins/bob.w2em`
- `game/hub_pins/novigrad.w2em`

`modAdditionalStashLocations`:

- `dlc/bob/data/game/hub_pins/bob.w2em`
- `game/hub_pins/novigrad.w2em`
- `game/hub_pins/skellige.w2em`
- `levels/novigrad/gameplay/player_stash/player_stash_velen/player_stash_velen.w2l`
- `levels/skellige/gameplay/player_stash/player_stash.w2l`

Overlap comparison:

| Path | Same as base ASL? | Compatibility bytes | Base ASL bytes |
| --- | --- | ---: | ---: |
| `dlc/bob/data/game/hub_pins/bob.w2em` | No | 37159 | 37527 |
| `game/hub_pins/novigrad.w2em` | No | 63364 | 63764 |

Conclusion:

The BiA compatibility patch is intentionally winning only the two overlapping hub files. Base ASL still supplies the non-overlapping Skellige and stash level files, while our manual script merge keeps the local spawner active without enabling ASL's full `playerWitcher.ws` copy. This is a valid paired install, not a redundancy cleanup target.
