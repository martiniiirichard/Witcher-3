# Audit: HDRP Redundancy Status

Date: 2026-06-27

Question:

- Are the multiple HDRP-looking folders duplicates or required install parts?

Result:

- Keep the stack.

Current active HDRP-related settings:

| Mod | Enabled | Priority | Role |
| --- | --- | ---: | --- |
| `mod000000aHDRP_BiA` | `1` | `39` | Brothers in Arms / HDRP compatibility patch |
| `modATrueFiresHDReworkedProjectCompatibility` | `1` | `167` | True Fires / HDRP compatibility patch |
| `mod00000HDReworkedProject` | `1` | `191` | HDRP install part |
| `modHDReworkedProject` | `1` | `192` | HDRP install part |
| `modHDReworkedProject2` | `1` | `193` | HDRP install part |
| `modHDReworkedProject3` | `1` | `194` | HDRP install part |
| `modHDReworkedProject4` | `1` | `195` | HDRP install part |

Live folder size check:

| Mod | File count | Approx MB |
| --- | ---: | ---: |
| `mod00000HDReworkedProject` | 7 | 165.4 |
| `modHDReworkedProject` | 4 | 3117.3 |
| `modHDReworkedProject2` | 4 | 3630.0 |
| `modHDReworkedProject3` | 4 | 2824.7 |
| `modHDReworkedProject4` | 4 | 2736.9 |
| `mod000000aHDRP_BiA` | 4 | 21.1 |
| `modATrueFiresHDReworkedProjectCompatibility` | 3 | 0.7 |

Conclusion:

The similarly named HDRP folders are the official multi-part texture/content payload, not redundant copies. The smaller `mod000000aHDRP_BiA` and `modATrueFiresHDReworkedProjectCompatibility` folders are compatibility layers. No Script Merger work is expected because these are bundled assets/config/cache payloads, not WitcherScript mods.
