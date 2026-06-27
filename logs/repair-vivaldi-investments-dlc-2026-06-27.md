# Repair - Vivaldi Investments DLC Payload

Date: 2026-06-27

## Why This Was Checked

During backlog/deferred-mod triage, `modvivaldi_investments` was found active:

```ini
[modvivaldi_investments]
Enabled=1
Priority=240
```

The mod folder was present and matched the downloaded archive, but the installed DLC payload had zero-byte files:

- `DLC\dlcvivaldiinvestments\content\blob0.bundle`
- `DLC\dlcvivaldiinvestments\content\metadata.store`

The downloaded archive contains nonzero versions:

- `blob0.bundle`: `22510` bytes
- `metadata.store`: `990` bytes
- `texture.cache`: `0` bytes

The zero-byte `texture.cache` is valid because the archive also ships it as zero bytes.

## Repair Applied

Source archive:

- `C:\Users\marti\Downloads\ModVivaldiInvestments-12215-1-08-1780028997.zip`

Repaired live files:

- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\DLC\dlcvivaldiinvestments\content\blob0.bundle`
- `C:\Program Files (x86)\GOG Galaxy\Games\The Witcher 3 Wild Hunt GOTY\DLC\dlcvivaldiinvestments\content\metadata.store`

Backup:

- `backups\vivaldi-dlc-zero-byte-repair-20260627-140134\content.before`

No script files were changed.

## Verification

DX12 direct-launch smoke after repair:

- `witcher3.exe` running after 65 seconds
- visible window: `True`
- responding: `True`
- working set: about `1940.5 MB`

## Notes

Vivaldi Investments is economy-adjacent but not a broad economy owner like FOCES. Keep the conservative settings documented in `docs/mod-settings-decisions.md` so passive investment flavor does not bypass contracts, looting, dismantling, and merchant routing.
