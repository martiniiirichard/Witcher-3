# Marlene The Cook 8041 - 2026-06-24

Source: https://www.nexusmods.com/witcher3/mods/8041

Installed archive:

- `C:\Users\marti\Downloads\mod00MarlenaTheCook-8041-2-2a-1774723815.zip`

Installed payload:

- `mods\mod00MarlenaTheCook`

Archive contents:

- `content\blob0.bundle`
- `content\metadata.store`
- `content\scripts\local\marlenathecook.ws`

Settings added to both active `mods.settings` files:

```ini
[mod00MarlenaTheCook]
Enabled=1
Priority=5
```

Compatibility decision:

- The mod page says it is compatible with Brothers in Arms but should have priority over BiA.
- Priority 5 puts it above BiA and most general content mods, while still leaving the highest-risk core stack ahead of it (`mod0000_MergedFiles`, Gwent Redux patch, Gwent Redux, etc.).
- No duplicate `MarlenaTheCook` script/function was found in the active mod stack.

Verification:

- DX12 smoke test passed; process remained running after 45 seconds.

Follow-up:

- In-game validation requires Corvo Bianco access after Blood and Wine progression. Check Marlene's food box, shorter restock cadence, and progressing food list.
