# Compile Error Analyzer

Tool:

`tools/analyze-witcher-compile-errors.py`

Purpose: speed up WitcherScript compile-error triage by parsing raw error output, searching active scripts, and identifying likely dependency, duplicate-symbol, signature, or annotation problems.

## Basic Use

Save compiler output to a text file:

```powershell
python .\tools\analyze-witcher-compile-errors.py --errors .\tmp\compile-errors.txt
```

Or pipe clipboard text:

```powershell
Get-Clipboard | python .\tools\analyze-witcher-compile-errors.py
```

Write a report:

```powershell
python .\tools\analyze-witcher-compile-errors.py --errors .\tmp\compile-errors.txt --out .\logs\compile-analysis-latest.md
```

## What It Detects

- `Could not find function`
- `I dont know any`
- `Unknown type`
- `Unknown base class`
- duplicate classes/functions/properties
- missing `Wrap` or `Overwrite` targets
- function parameter/signature mismatches
- private function access errors
- syntax errors with `near 'symbol'`

## What It Searches

- vanilla `content/content0/scripts`
- enabled mod `content/scripts` folders from `mods.settings`
- DLC script folders

By default it skips disabled and backup files such as:

- `.disabled`
- `disabled-by-codex`
- `.codex-backup`
- `.bak`

Use `--include-disabled` when you suspect a dependency was intentionally disabled or archived:

```powershell
python .\tools\analyze-witcher-compile-errors.py --errors .\tmp\compile-errors.txt --include-disabled
```

## How To Read The Report

For each symbol, the report gives:

- parsed issue kind;
- likely cause;
- compiler occurrences;
- active and inactive script hits;
- suggested next action.

The best use is not automatic fixing. It narrows the search space before manual patching.

## Typical Decisions

- Duplicate active definitions: disable one compatibility provider or remove one duplicate annotation/full-file override.
- Missing function/member with inactive hits: restore or re-enable the dependency that adds the symbol.
- Missing function/member with no hits: likely wrong game generation, missing dependency, or mod needs a compatibility shim.
- Signature mismatch: compare the current W3EE/base method signature and update the call/override.
- Private function call: wrap inside the owning class or expose a safe helper.
