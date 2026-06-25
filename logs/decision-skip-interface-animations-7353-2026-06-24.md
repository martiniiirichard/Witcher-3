# Interface Animations (NGE) - 7353

Date: 2026-06-24

Source:
- https://www.nexusmods.com/witcher3/mods/7353

Archives inspected:
- `C:\Users\marti\Downloads\InterfaceAnim-7353-5-1-5-1756967904.rar`
- `C:\Users\marti\Downloads\IA_CPatch ( W3EE Redux )-7353-1-42g-1746364673.rar`
- `C:\Users\marti\Downloads\IA_CPatch ( IM )-7353-1-0-1701109057.rar`

Decision:
- Do not keep installed in the active stack right now.

Reason:
- Full install with DLC/menu XML caused a hard crash on DX12 launch:
  - `ExitCode=-1073741819`
- Removing `modInterfaceAnim.xml` from `dx12filelist.txt` did not stop the crash while the IA DLC was active.
- Disabling IA DLC restored stable launch.

Script issues found and fixed during isolation:
- `CPlayerInput::OnFastMenu` duplicate overwrite:
  - E3 HUD already owns this replacement.
  - IA's duplicate `@replaceMethod` block was removed during test.
- `CR4InventoryMenu::ShowBookPopup` and `ShowPainting` missing wrap targets:
  - W3EE replaces `CR4InventoryMenu` with a thin subclass over `WmkCR4InventoryMenu`.
  - IA wrappers were retargeted to `WmkCR4InventoryMenu` during test.
- `CR4HudModuleRadialMenu::OnOpenMeditation` missing wrap target:
  - Removed IA's radial meditation wrapper during test.
- With these script edits and IA DLC disabled, DX12 launch smoke passed.
- With IA DLC re-enabled, hard crash returned.

Rollback state:
- `mods\mod_InterfaceAnim` disabled/renamed with `disabled-by-codex-crashes-7353-*`.
- `DLC\dlc_InterfaceAnim` disabled/renamed with `disabled-by-codex-crashes-7353-*`.
- Removed `modInterfaceAnim.xml;` from DX11/DX12 file lists.
- `[mod_InterfaceAnim]` remains in both `mods.settings` files as `Enabled=0`, `Priority=257`.

Verification:
- After rollback, DX12 launch smoke passed: game remained running after 60 seconds.

Future investigation:
- This likely needs a dedicated DLC/content crash pass, not more script merging.
- Possible causes to check later:
  - DLC/content load limit or package count pressure.
  - Asset/bundle collision with UI/HUD/E3/W3EE stack.
  - Missing/incorrect REDkit asset dependency.
