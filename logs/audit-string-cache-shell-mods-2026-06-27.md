# Audit: String / Cache / Shell Mods

Date: 2026-06-27

## Goal

Review active mods with no `.ws` scripts and no `.bundle` files. These can look like empty shells in a script/bundle audit, but they often carry localization, texture cache, sound cache, or menu-category payloads.

## Result

No removal candidate found in this pass.

## Keep

| Mod | Payload | Why to keep |
| --- | --- | --- |
| `modHDTreeBillboards` | `content\texture.cache` | Texture cache-only HD tree billboard payload. Previously reviewed as part of the visual/weather stack. |
| `modHDTreeBillboardsBnW` | `content\texture.cache` | Blood and Wine companion texture cache for HD tree billboards. |
| `modTWCG_RandomOST` | `content\soundspc.cache` | Audio cache payload for the Gwent/random OST install. No script work expected. |
| `modHDUrsineConcept_Lexars` | `content\texture.cache`, `metadata.store` | Texture cache payload for Laion/Bear/Ursine concept armor. |
| `modZ_GrammarOfThePath` | `content\en.w3strings` | Active polish string package; low-risk future trim only if the naming stack feels cluttered. |
| `mod_SNC_W3EERedux` | `.w3strings` plus `localization\en.csv` | Main Standardised Naming Convention package for W3EE Redux. Keep; separate SNC Bombs package was skipped as redundant because this broader package is active. |
| `mod_ModsMenuCategory` | `.w3strings` plus `content\en.csv` | Menu-category localization/support package. Keep while the crowded mod menu stack remains active. |
| `modMenuStrings` | `.w3strings`, localization CSV/readme files | NOBs Reflex support strings. Keep while Reflex remains active. |
| `modW3EELocalization1-4` | `.w3strings` | Core W3EE localization volumes. Keep. |

## Rule Learned

Do not classify cache-only or string-only mods as redundant just because they do not appear in Script Merger. For this install, `.cache` and `.w3strings` folders are legitimate active payloads.

The better cleanup signal is:

- enabled folder,
- no scripts,
- no bundles,
- no strings/cache/config payload,
- no paired DLC or documented feature role.

None of the folders in this pass matched that removal pattern.
