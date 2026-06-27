# Audit: RT CHAR DX12 Eyes Fix

Date: 2026-06-27

Question:

- Is `modRRTCHARDX12eyes` redundant with parent `modRTCHARDX12`?

Result:

- Keep it.

Active settings:

| Mod | Enabled | Priority |
| --- | --- | --- |
| `modRRTCHARDX12eyes` | `1` | `182` |
| `modRTCHARDX12` | `1` | `183` |

Evidence:

- Lower numeric priority wins, so the eyes fix wins over the parent for overlapping files.
- The eyes fix contains only the two overlapping eye material files.
- Both files differ from the parent by hash while keeping the same byte size, consistent with a targeted material override.

Comparison:

| Path | Same as parent? | Fix bytes | Parent bytes |
| --- | --- | ---: | ---: |
| `characters/models/common/materials/base_materials/base_eye.w2mi` | No | 1663 | 1663 |
| `characters/models/common/materials/eyes/component__shadow.w2mi` | No | 745 | 745 |

Conclusion:

This is a valid companion patch for the current DX12 character/SSAO visual setup. Revisit only if eye artifacts appear in-game.
