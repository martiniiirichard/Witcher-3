# Assess - Advanced Icons for Witcher Gear 11339

Date: 2026-06-27

Source archive:

- `C:\Users\marti\Downloads\Advanced Icons for Witcher Gear (version E)-11339-2-3-1763466572.zip`

Nexus:

- https://www.nexusmods.com/witcher3/mods/11339

## Payload

Extracted for inspection only:

- `modAIWGe\content\blob0.bundle`
- `modAIWGe\content\texture.cache`
- `modAIWGe\content\metadata.store`

QuickBMS unpacked four bundled XML files:

- `dlc\bob\data\gameplay\items\def_item_crafting_weapons.xml`
- `dlc\bob\data\gameplay\items\def_item_weapons.xml`
- `dlc\bob\data\gameplay\items_plus\def_item_crafting_weapons.xml`
- `dlc\bob\data\gameplay\items_plus\def_item_weapons.xml`

## Conflict Read

This is not just a harmless icon texture cache. It replaces Blood and Wine item definition XML.

Existing active owners from the bundle conflict index:

- `dlc\bob\data\gameplay\items\def_item_crafting_weapons.xml`
  - `modW3EE`
  - `modmanticor`
- `dlc\bob\data\gameplay\items\def_item_weapons.xml`
  - `mod000_Patch_BIA-W3EER`
  - `modBrothersInArms`
  - `modScabbards`
  - `modW3EE`
- `dlc\bob\data\gameplay\items_plus\def_item_weapons.xml`
  - `modBrothersInArms`
  - `modScabbards`

Lower numeric priority wins in this stack, so installing this as a normal late visual mod would either do nothing or, if prioritized high, could override W3EE/BiA/scabbard item definitions.

## Decision

Do not install now.

Reason: the value is cosmetic, but the payload is gameplay/item XML. Any safe integration would be a manual XML graft into the current W3EE/BiA item-definition winners, not a normal mod install.

## Revisit Only If

- We specifically want these Blood and Wine gear icons.
- We are willing to manually port only the icon fields into the current winning XML files.
- We verify the patch does not overwrite W3EE item balance, scabbard behavior, or BiA restoration values.
