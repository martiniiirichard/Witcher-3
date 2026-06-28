param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path,
    [string]$GameRoot = 'C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY'
)

$ErrorActionPreference = 'Stop'

$smDir = Join-Path $RepoRoot 'tools\sm-fae-0.9.7'
$exe = Join-Path $smDir 'WitcherScriptMerger.exe'
$config = Join-Path $smDir 'WitcherScriptMerger.dll.config'
$inventory = Join-Path $smDir 'MergeInventory.xml'

if (-not (Test-Path -LiteralPath $exe)) {
    throw "SM-FAE executable not found: $exe"
}

if (-not (Test-Path -LiteralPath $config)) {
    throw "SM-FAE config not found: $config"
}

$xml = [xml](Get-Content -LiteralPath $config -Raw)
$settings = $xml.configuration.appSettings.add

function Set-AppSetting {
    param(
        [string]$Key,
        [string]$Value
    )

    $node = $settings | Where-Object { $_.key -eq $Key } | Select-Object -First 1
    if ($null -eq $node) {
        $node = $xml.CreateElement('add')
        $node.SetAttribute('key', $Key)
        [void]$xml.configuration.appSettings.AppendChild($node)
    }
    $node.SetAttribute('value', $Value)
}

Set-AppSetting -Key 'GameDirectory' -Value $GameRoot
Set-AppSetting -Key 'VanillaScriptsDirectory' -Value (Join-Path $GameRoot 'content\content0\scripts')
Set-AppSetting -Key 'ModsDirectory' -Value (Join-Path $GameRoot 'mods')
Set-AppSetting -Key 'AutoDeleteOldMerges' -Value 'false'
Set-AppSetting -Key 'AutoOverwriteOldMerges' -Value 'false'
Set-AppSetting -Key 'MergedModName' -Value 'mod0000_MergedFiles'
Set-AppSetting -Key 'KDiff3Path' -Value (Join-Path $smDir 'Tools\KDiff3\KDiff3.exe')
Set-AppSetting -Key 'QuickBmsPath' -Value (Join-Path $smDir 'Tools\QuickBMS\quickbms.exe')
Set-AppSetting -Key 'QuickBmsPluginPath' -Value (Join-Path $smDir 'Tools\QuickBMS\witcher3.bms')
Set-AppSetting -Key 'WccLitePath' -Value (Join-Path $smDir 'Tools\wcc_lite\bin\x64\wcc_lite.exe')
$xml.Save($config)

if (-not (Test-Path -LiteralPath $inventory)) {
    @'
<?xml version="1.0" encoding="utf-8"?>
<MergeInventory xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" />
'@ | Set-Content -LiteralPath $inventory -Encoding UTF8
}

$shortcutPaths = @(
    "$env:APPDATA\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Witcher 3 Script Merger.lnk",
    "$env:USERPROFILE\OneDrive\Desktop\Witcher 3 Script Merger.lnk"
)

$shell = New-Object -ComObject WScript.Shell
foreach ($path in $shortcutPaths) {
    $parent = Split-Path -Parent $path
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }

    $shortcut = $shell.CreateShortcut($path)
    $shortcut.TargetPath = $exe
    $shortcut.WorkingDirectory = $smDir
    $shortcut.Arguments = ''
    $shortcut.IconLocation = "$exe,0"
    $shortcut.Save()
}

[pscustomobject]@{
    Exe = $exe
    WorkingDirectory = $smDir
    MergeInventoryExists = Test-Path -LiteralPath $inventory
    AutoDeleteOldMerges = ($settings | Where-Object { $_.key -eq 'AutoDeleteOldMerges' } | Select-Object -First 1).value
    AutoOverwriteOldMerges = ($settings | Where-Object { $_.key -eq 'AutoOverwriteOldMerges' } | Select-Object -First 1).value
}
