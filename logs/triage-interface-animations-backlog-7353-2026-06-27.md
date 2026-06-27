# Interface Animations Backlog Triage - 7353

Date: 2026-06-27

## Result

Do not install Interface Animations in the current backlog pass.

This is already a known skipped/deferred mod, not an unresolved simple install.

## Evidence

Prior install attempt hit both script and runtime/content issues:

- duplicate overwrite for `CPlayerInput::OnFastMenu`
- missing wrap targets for `ShowBookPopup`, `ShowPainting`, and `OnOpenMeditation`
- removing `modInterfaceAnim.xml` from filelists did not stop the crash while the IA DLC was active
- IA mod and DLC were disabled/renamed after causing a DX12 no-window startup failure

## Skip

| Download | Decision |
| --- | --- |
| `InterfaceAnim-7353-*` | Skip. Main package caused hard runtime/content failure. |
| `IA_CPatch ( W3EE Redux )-*` | Skip until the main package is proven safe. |
| `IA_CPatch ( FM )-*` | Skip until the main package is proven safe. |
| `IA_CPatch ( IM )-*` | Skip until the main package is proven safe. |

## Guardrail

Do not treat Interface Animations as a normal script merge. If revisited, isolate in a dedicated branch/pass:

1. install only the main mod
2. launch-test the DLC/content before patches
3. add one compatibility patch at a time
4. keep DX11/DX12 filelist changes and disabled folders easy to revert
