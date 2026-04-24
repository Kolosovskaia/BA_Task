---
id: 02-glossary
title: Glossary v1 — Parent-Child Structure
date: 2026-04-24
sources:
  - docs/Meeting Recording Transcription.md
  - docs/transcription.srt
  - docs/narrative_film_storyboard-2026-04-24.md
  - docs/screens_cropped/*.png (UI labels)
phase: 1 — Framing & Elicitation
note: Final manual is EN-only. RU column is the transcript's source wording; EN is the term that will appear in docs/manual/.
---

# Glossary v1

## How to read this

- **RU (source)** — term as Maya uses it in the transcript / voice.
- **EN (manual)** — canonical term to use in `docs/manual/*.md`. Matches Gen1POS UI where possible.
- **Definition** — neutral definition.
- **Notes** — synonyms, ambiguities, or usage constraints.

## Core concepts

| # | RU (source) | EN (manual) | Definition | Notes |
|:-:|---|---|---|---|
| 1 | Parent-Child структура | Parent-Child Structure | A mechanism that turns a menu item into a parent holding one or more related child items (variants) under it. | Maya's primary label. Feature name. |
| 2 | Родительский айтем / parent-item | Parent Item | A menu item that contains one or more variants. | Gen1POS UI shows it as a dropdown field `Parent Item` on a child item's detail page. |
| 3 | Вариант / child / дочерний элемент / вариативный айтем | Variant | A menu item that belongs to a parent. In docs we prefer "variant" per Maya's guidance: *«в документации, конечно, можно просто писать варианты»*. | Use **variant** throughout. Do not use "child" in user-facing text. |
| 4 | Standalone / обычный айтем / отдельный айтем | Standalone Item | A menu item with no parent. Default state before attachment. | In UI dropdown: `None (Standalone)`. |
| 5 | Subcategory | Subcategory | A category one level below a top-level category, containing items. | Scope constraint: Parent Item can only be selected from items within the same subcategory (F13 / transcript). |

## Actions and operations

| # | RU (source) | EN (manual) | Definition | Notes |
|:-:|---|---|---|---|
| 6 | Add Variant (button) | Add Variant | UI button on a parent item's detail page to create a new child. | Keep verbatim. |
| 7 | Открепить / убрать / detach | Detach (a variant) | Remove a variant from a parent. Destination depends on origin (see F3). | Avoid "delete" for this op — ambiguous with full deletion. |
| 8 | Перетащить / двигать / reorder | Reorder (variants) | Drag variants to change their display order on POS. | Drag interaction (visual in video). |

## Fields

| # | RU (source) | EN (manual) | Definition | Notes |
|:-:|---|---|---|---|
| 9 | Short Name | Short Name | A mandatory field that appears on a variant (not on standalone items). Used in POS display and reports. | Introduced when an item becomes a variant of a parent. |
| 10 | Parent Item (поле) | Parent Item (field) | Dropdown on a child item's detail page, values: `None (Standalone)` or an item from the same subcategory. | The mechanism to attach / detach via configuration. |
| 11 | Pre Chosen | Pre Chosen | Toggle on a variant. When active, that variant is selected by default on POS when the customer opens the parent. | Exactly one variant pre-chosen per parent (to be verified — Observation Log). |
| 12 | Product Class | Product Class | A classification field (e.g., "Food") inherited from the parent onto each variant. | Inherited, not separately editable on variant (F8). |
| 13 | Modifiers | Modifiers | Optional list of modifications attached to an item. | Narrated caveat: *«влияет на айтем, когда он находится вне Parent-Child структуры»* — behaviour under Parent-Child ambiguous (G5). |
| 14 | Allergens | Allergens | Optional allergen tags on an item. | Same level as modifiers. |
| 15 | Color code | Color Code | Display-options field. Affects item display when outside a parent context. | Narrated in video shot 19. |

## Surfaces (where data shows up)

| # | RU (source) | EN (manual) | Definition | Notes |
|:-:|---|---|---|---|
| 16 | POS сторона / клиентская сторона | POS (cashier-side) | Cashier interface where variants appear as tappable buttons under the parent. | Display = `parent name + short name` per F10. |
| 17 | Заказ на кухню / kitchen ticket | Kitchen ticket | Ticket printed to kitchen after payment. | Narrated: *«появится полностью название айтема»* — semantics of "full name" ambiguous (G7). |
| 18 | ProductMix (report) | ProductMix | Reporting view that shows what items were sold over a time range. | Displays variant name, not parent name (F12). |

## Ambiguities flagged for Round 2 or Observation Log

- **"Полное название"** on kitchen ticket — `parent + short` or something else? (G7)
- **"Вариативное имя"** in reports — same as Short Name? Or Parent + Short Name combined? (internal contradiction between narration snippets F10 vs F12)
- **Modifier behaviour** "when variant is outside parent-child" — Observation Log needs to distinguish what actually applies inside parent-child.

## Out of glossary (intentionally)

Terms covered by parent Gen1POS manual and therefore not redefined here:

- Menu, Category, Item (base concept), Price, Tax, Barcode, SKU, Cost, Display Configuration, Status, Allergens (general, not P-C-specific), Dine-in, Takeout.
