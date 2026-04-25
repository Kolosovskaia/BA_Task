---
id: 05-capability-map
title: Feature Capability Map — Parent-Child Structure
date: 2026-04-24
derived_from: 04-observation-log.md
phase: 2 — Evidence extraction
---

# Feature Capability Map

## Purpose

Atomic capabilities the feature offers, each with trigger, steps, result, preconditions. Becomes the source for how-to scenarios (Step 7) and the reference rules section (Step 13).

## Capabilities

### CAP-1 — Create a new variant on a parent

- **Trigger**: Admin opens a parent item's detail page and clicks `Add Variant`.
- **Precondition**: Item exists; user has edit permissions (assumed, UK5).
- **Steps**: Click `Add Variant` → enter variant details → set `Short Name` → Save.
- **Result**: New variant appears in parent's Variants section; the variant is **variant-born** (see CAP-5 for delete behaviour).
- **Evidence**: C2, C3, C5 (shots 5, 6, 11, 12).

### CAP-2 — Attach an existing standalone item as a variant

- **Trigger**: Admin opens a standalone item's detail page and selects a parent in the `Parent Item` dropdown.
- **Precondition**: The candidate parent is an item in the **same subcategory** (C4). Item currently standalone.
- **Steps**: Open item → open `Parent Item` dropdown → select parent → fill `Short Name` → Save.
- **Result**: Item becomes a variant under selected parent; a `Short Name` field appears on the item's page (was absent when standalone).
- **Evidence**: C3, C4, C5 (shots 9, 10, 11).

### CAP-3 — Set Short Name on a variant

- **Trigger**: Admin edits a variant (via Edit Variant modal or its detail page).
- **Precondition**: Item is a variant.
- **Steps**: Enter value in `Short Name` → Save.
- **Result**: `Short Name` is used everywhere the variant surfaces (POS, order preview, ProductMix composite label).
- **Evidence**: C5, C12, C13, C15 (shots 11, 15, 17, 23, 27–29).
- **Unknowns**: UK8 (length/charset constraints).

### CAP-4 — Reorder variants; mark one as Pre Chosen

- **Trigger**: Admin drags variants to reorder and/or toggles `Pre Chosen` on one.
- **Precondition**: Parent has ≥ 2 variants for reorder to be meaningful.
- **Steps**: Drag to desired order → toggle `Pre Chosen` on the intended default → Save.
- **Result**: POS displays variants in the saved order; the Pre Chosen one is visually pre-selected.
- **Evidence**: C7, C8, C12 (shots 13, 15).
- **Unknowns**: UK9 (can more than one be Pre Chosen simultaneously?).

### CAP-5 — Detach a variant (origin-dependent outcome)

- **Trigger**: Admin clicks 'X' next to a variant in the parent's Variants section.
- **Precondition**: Variant exists under a parent.
- **Steps**: Click 'X' on the variant row → confirm if prompted (not shown explicitly).
- **Result** — depends on origin:
  - If the variant was **originally standalone** and later attached (CAP-2): the item returns to its subcategory's item list as a standalone. **Observed directly** (shots 7–8).
  - If the variant was **variant-born** (CAP-1): the item disappears and does not appear in the item list. **Narrated only** (shot 31), not re-demonstrated after creation.
- **Evidence**: C6 (shots 7, 8, 31).

### CAP-6 — Configure variant-level fields independently (Price, Modifiers, Allergens, Color Code)

- **Trigger**: Admin opens Edit Variant modal.
- **Precondition**: Item is a variant.
- **Steps**: Edit fields (Price, Modifiers, Allergens, Display Options → Color Code) → Save.
- **Result**: Fields take effect on this variant.
- **Scope caveat**: `Product Class` is displayed but inherited from parent (CAP-7). `Color Code` narrated as only effective "outside parent-child context" (C16). Modifiers narration self-contradictory (UK10).
- **Evidence**: C9, C10, C11, C16 (shots 17, 18, 19).
- **Unknowns**: UK10 (effective modifier behaviour when item is a variant).

### CAP-7 — Product Class inheritance (system rule, not user action)

- **Trigger**: Automatic — whenever an item is a variant.
- **Precondition**: Item is a variant of a parent.
- **Effect**: Variant's `Product Class` is the parent's value and is not editable at the variant level.
- **Evidence**: C10 (shot 17).
- **Classification**: NN-only — the inheritance rule itself is narrated; we observe only the displayed Product Class being "Food" on a variant whose parent is also "Food".

### CAP-8 — POS display: variants as tappable buttons under parent

- **Trigger**: Customer/operator taps a parent on POS.
- **Precondition**: Item has at least one variant.
- **Effect**: POS renders variant buttons labelled with `Short Name`; order follows admin-saved order; the Pre Chosen variant is visually pre-selected.
- **Evidence**: C7, C8, C12 (shots 15, 21, 22).

### CAP-9 — Order preview / receipt composition

- **Trigger**: Operator adds a variant to the order on POS.
- **Effect**: Order line displays the `parent name` together with the `short name` and selected modifiers.
- **Evidence**: C13 (shot 23).

### CAP-10 — Kitchen ticket format (claim-only; not verifiable in source)

- **Trigger**: Payment completes; order routes to kitchen.
- **Effect**: Kitchen ticket shows the item's "full name".
- **Evidence**: C14 (shot 24) — **narrated, not shown**.
- **Classification**: NN only. Flag UK7 — exact kitchen ticket format.

### CAP-11 — ProductMix reporting label for variants

- **Trigger**: ProductMix report loaded for a period during which variant sales occurred.
- **Effect**: Sold variants appear under the composite label `Parent Name – Short Name Parent Name` (observed format in shots 27–29). Narration calls this "variant name".
- **Evidence**: C15 (shots 27–29).
- **Note**: Resolves the internal contradiction from `plan.md` (F10 vs F12) — "variant name" in ProductMix context = a composite label that contains the parent name.

### CAP-12 — Subcategory scope constraint on parent selection

- **Trigger**: Admin opens `Parent Item` dropdown on a standalone item.
- **Effect**: Only items from the SAME subcategory appear as candidates.
- **Evidence**: C4 (shot 10), narrated.

## Summary

| Capability | Confidence | In scope v1 | Source shots |
|---|:-:|:-:|---|
| CAP-1 Create variant | DO+NN | ✅ | 5, 6, 11, 12 |
| CAP-2 Attach existing | DO+NN | ✅ | 9, 10, 11 |
| CAP-3 Set Short Name | DO+NN | ✅ | 11, 15, 17, 23, 27–29 |
| CAP-4 Reorder + Pre Chosen | DO+NN | ✅ | 13, 15 |
| CAP-5 Detach | DO+NN | ✅ | 7, 8, 31 |
| CAP-6 Variant-level fields | DO+NN | ✅ (caveats) | 17, 18, 19 |
| CAP-7 Product Class inheritance | NN | ✅ | 17 |
| CAP-8 POS display | DO | ✅ | 15, 21, 22 |
| CAP-9 Order preview | DO+NN | ✅ | 23 |
| CAP-10 Kitchen ticket | NN only | 🟡 (partial — say what we know, flag format) | 24 |
| CAP-11 ProductMix label | DO+NN | ✅ | 27–29 |
| CAP-12 Subcategory scope | NN | ✅ | 10 |

**Total**: 12 capabilities (≥ 8 DoD threshold met).

**Pending Round 2 decisions for scope**: parent-deletion cascade (UK1), max nesting (UK2), migration (UK3), discounts (UK4), permissions (UK5).
