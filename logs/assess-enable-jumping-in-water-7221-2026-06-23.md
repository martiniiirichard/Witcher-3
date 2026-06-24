# Enable Jumping in Shallow Water 7221

Date: 2026-06-23

Source:
- https://www.nexusmods.com/witcher3/mods/7221

Download:
- `C:\Users\marti\Downloads\Enable Jumping in Water-7221-1-3-1705444930.rar`

Decision:
- Not installed.
- Reason: the active W3EE stack already includes the important shallow-water jump compatibility changes.

Archive contents:
- `modEnableJumpInWater\content\scripts\game\player\r4Player.ws`
- `modEnableJumpInWater\content\scripts\game\explorations\exploration_movement_system\exploration_substates\explorationStateJump.ws`
- `ReadMe.txt`

Compatibility assessment:
- The archive ships full script replacements for two core movement/player files.
- Installing those replacements directly would risk overriding W3EE and our merged script stack.
- The active W3EE `r4Player.ws` already comments out the shallow-water `EIAB_Jump` block in `OnEnterShallowWater`.
- The active W3EE `explorationStateJump.ws` already comments out the early `thePlayer.IsInShallowWater()` return in the jump availability path.

Conclusion:
- We already have the useful behavior.
- Keep this mod skipped unless in-game testing proves shallow-water jumping still fails.

If retesting is needed:
- Load near shallow water, not deep swimming water.
- Confirm Geralt can jump while standing/wading in shallow water.
- If it fails, patch the active W3EE files manually instead of installing `modEnableJumpInWater` as a full replacement.
