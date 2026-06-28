# Fix SM-FAE Old Merges Prompt - 2026-06-28

Problem:

SM-FAE Script Merger showed:

> Old merges, not made by Script Merger: Fresh & Automated Edition, were found in the "merged mods" directory

Clicking **No** closed the program. Clicking **Yes** would be unsafe because `mod0000_MergedFiles` contains intentional manual grafts for the current W3EE/BiA stack.

Root cause:

Decompiled SM-FAE 0.9.7 and found this clean-install gate:

```csharp
if (!File.Exists("MergeInventory.xml") && Directory.Exists(Paths.RetrieveMergedModDir()))
{
    if (ConfirmRemoveOldMergesOnCleanInstall())
        return RemoveOldMerges();
    return false;
}
```

The shortcut working directory was already correct, but `tools\sm-fae-0.9.7\MergeInventory.xml` was missing. SM-FAE therefore treated the existing manual `mod0000_MergedFiles` folder as old foreign merge output.

Fix applied:

- Created an empty SM-FAE merge inventory marker:
  `tools\sm-fae-0.9.7\MergeInventory.xml`
- Kept the destructive automation disabled in:
  `tools\sm-fae-0.9.7\WitcherScriptMerger.dll.config`

Required config values:

```xml
<add key="AutoDeleteOldMerges" value="false" />
<add key="AutoOverwriteOldMerges" value="false" />
```

- Repointed the taskbar and desktop shortcuts back to:
  `tools\sm-fae-0.9.7\WitcherScriptMerger.exe`
- Confirmed SM-FAE opens and responds without deleting `mod0000_MergedFiles`.

Shortcut backups:

- `settings-backups\script-merger-shortcuts-20260628-012723`
- `settings-backups\script-merger-shortcuts-sm-fae-restored-20260628-013419`

Important:

Do not delete `MergeInventory.xml` unless we intentionally want SM-FAE to treat the current merged folder as unmanaged. Do not click **Yes** on the old-merge deletion prompt without a full backup and a deliberate plan to regenerate `mod0000_MergedFiles`.
