---
id: 09-shotlist
title: Screenshot Shot-list — Parent-Child Structure Manual
date: 2026-04-24
sources:
  - docs/screens_cropped/shot_01.png … shot_32.png (32 frames extracted from video.mp4)
  - 08-ia.md (target document structure)
  - 04-observation-log.md (what each shot depicts)
phase: 3 — Scope lock & IA (Step 9)
---

# Screenshot Shot-list

## Purpose

Assign each of the 32 screenshots to a specific location in the final manual `docs/manual/`, with a caption. Ensures:

- **No orphaned shots** — every shot either has a home or is explicitly marked as excluded.
- **No visual redundancy** — we don't show the same thing twice across adjacent docs.
- **Captions drafted now** — so Drafting (Phase 4) is not slowed down by ad-hoc captioning.

## How to read this

Each row in the tables below:

- **Shot** — the source file in `docs/screens_cropped/shot_XX.png`. All are 1664×887 px, cropped from the 1920×1080 screencast.
- **Target doc** — where the shot goes in `docs/manual/`.
- **Section** — the subsection within the target doc.
- **Caption (EN)** — the caption that will appear in the manual under the image, following MS Style Guide (plain, descriptive, complete sentence, period).
- **Why this shot** — one line on why this particular frame earns its place.

All captions are English (per PO Round 1 Q-4 — EN-only final).

## Path convention

- **Source of truth**: `docs/screens_cropped/shot_XX.png` — full 32-shot archive. Referenced by BA artifacts.
- **Published to manual**: `docs/manual/_assets/shot_XX.png` — a curated copy of the 20 shots used in the final manual. Referenced by `docs/manual/*.md` with the relative path `_assets/shot_XX.png`.
- **Reason for the split**: short relative paths (`_assets/shot_XX.png`) render reliably in VSCode markdown preview, GitHub, and other renderers — unlike parent-traversal paths (`../screens_cropped/...`) which can fail in VSCode preview.

## Summary of decisions

- **Used**: 19 shots across 5 how-to + 1 reference file.
- **Optional** (used only if length allows): 3 shots.
- **Excluded**: 10 shots (branding, transitions, generic navigation).
- **Orphaned**: 0.

## 01-explanation.md — Concept page

| Shot | Section | Caption (EN) | Why this shot |
|:-:|---|---|---|
| `shot_03.png` | Opening illustration | The admin panel shows the path Menu → Categories → Tarts, with Almondine Tarte listed as a parent item. | Establishes where the feature lives and what a parent item looks like in the menu tree. |
| `shot_05.png` | "What it looks like" | The Variants section of the Almondine Tarte detail page lists three variants — 3″, 5″, and 8″. | Shows the core visual result of using Parent-Child Structure — a parent holding multiple variants. |

## 02-howto-create-variant.md — How to create a new variant

| Shot | Section | Caption (EN) | Why this shot |
|:-:|---|---|---|
| `shot_05.png` | Step 2 context | The parent item's detail page has a Variants section where child items are listed. | Anchors the reader to the Variants section before they click anything. |
| `shot_06.png` | Step 3 Add Variant | The Add Variant button sits at the bottom of the Variants section. | Points to the specific UI control for the step. |
| `shot_11.png` | Step 5 Short Name | When an item is configured as a variant, a Short Name field becomes editable on its detail page. | Shows the field that appears only in the variant context. |
| `shot_12.png` | Expected result | After saving, the new variant appears in the parent's Variants list with its Short Name and a Product updated confirmation. | Closes the loop — reader sees what success looks like. |

## 03-howto-attach-existing.md — How to attach an existing item

| Shot | Section | Caption (EN) | Why this shot |
|:-:|---|---|---|
| `shot_08.png` | Prerequisite context | A standalone item appears in the subcategory's item list alongside other items. | Grounds the reader in the starting state. |
| `shot_09.png` | Step 1 opening the item | The standalone item's Parent Item field is set to None (Standalone). | Shows the pre-attachment state of the critical field. |
| `shot_10.png` | Step 2 selecting parent | The Parent Item dropdown lists candidate parents from the same subcategory. | Illustrates the subcategory-scope constraint visually. |
| `shot_11.png` | Step 3 Short Name | After selecting a parent, the Short Name field appears and must be filled before saving. | Same control as in the create flow — reinforces consistency. |
| `shot_12.png` | Expected result | The formerly-standalone item now appears inside the parent's Variants section. | Confirms the attachment succeeded. |

## 04-howto-reorder-variants.md — How to reorder and set a default (Pre Chosen)

| Shot | Section | Caption (EN) | Why this shot |
|:-:|---|---|---|
| `shot_13.png` | Steps 2–3 drag and toggle | Variants are reordered by drag; the Pre Chosen toggle selects the default variant. | Core admin interaction for this how-to. |
| `shot_15.png` | Verification on POS | On POS, variants under the parent appear in the saved order with the Pre Chosen variant visually pre-selected. | Proves the admin configuration reached the customer-facing side. |
| `shot_21.png` *(optional)* | Alternative POS view | A second example of variants appearing under a parent on POS. | Only include if we have room; adds variety. |
| `shot_22.png` *(optional)* | Alternative: Cafe Sua Da | Another item's variants (Small, Large, M) displayed on POS with per-variant customization available. | Reinforces that Parent-Child is a general pattern, not tied to one item. Use only if reinforcement helps. |

## 05-howto-remove-variant.md — How to remove a variant

| Shot | Section | Caption (EN) | Why this shot |
|:-:|---|---|---|
| `shot_07.png` | Step 1 clicking X | Each variant row has an X control; clicking it triggers the Variant deleted confirmation. | Points to the specific control. |
| `shot_08.png` | Branch A outcome | A previously-standalone variant, once detached, returns to the subcategory's item list as a standalone item. | Visual proof of the "returns to list" branch. |
| `shot_31.png` | Branch B explanation | The same X control is used to remove a variant that was created inside the parent — with a different outcome: the item is deleted entirely. | Supports the warning callout in the how-to. No separate visual exists for the disappearance — this shot shows the UI where the action happens. |

## 06-reference-rules.md — Rules and display matrix

Reference documents use fewer illustrations; included shots are for rule clarifications, not flow.

| Shot | Section | Caption (EN) | Why this shot |
|:-:|---|---|---|
| `shot_15.png` | R6 Display — POS | Variant buttons on POS use the Short Name as label, in the admin-saved order, with the Pre Chosen variant pre-selected. | Single shot covers three R6 sub-rules at once. |
| `shot_17.png` | R3 Product Class + R6 Display — Edit Variant | The Edit Variant modal shows the inherited Product Class field and variant-level fields such as Price, SKU, Taxes. | Primary illustration for the inheritance rule. |
| `shot_18.png` | R7 Modifiers on variants | The Customization section of Edit Variant exposes independent Modifiers and Allergens dropdowns for the variant. | Proof that the fields exist per variant (structural claim). |
| `shot_19.png` | R8 Color Code | The Display Options section contains a Color code selector; its behaviour in the Parent-Child context is not documented in v1. | Anchor for the limitation note. |
| `shot_23.png` | R6 Display — Order preview | An added variant appears in the order summary as two lines: the parent name on top, the Short Name and modifier selections beneath. | Canonical example of the order preview format. |
| `shot_27.png` | R6 Display — ProductMix | In the ProductMix report, variants appear under a composite label that includes both the parent name and the Short Name. | Visual evidence resolving the "variant name vs parent name" ambiguity. |
| `shot_29.png` *(optional)* | R6 Display — ProductMix time-filtered | When the report is filtered to a narrow window, only the specific variant's composite label appears. | Reinforces the previous shot; include only if clarity benefits. |

## 07-reference-glossary.md — Glossary

No screenshots. Text-only document by design.

## 08-known-limitations.md — Known limitations

No screenshots. Text-only document by design.

## Excluded shots (and why)

These 10 shots are deliberately not used:

| Shot | Content | Reason for exclusion |
|:-:|---|---|
| `shot_01.png` | BA Task title slide | Presentation chrome, not product content. |
| `shot_02.png` | Presenter introduction (MP / AXIOM.tech) | Presentation chrome. |
| `shot_04.png` | Left sidebar expanded showing Menu categories | Pure navigation; not feature-specific. Parent manual covers navigation. |
| `shot_14.png` | "Product updated" toast (second occurrence) | Redundant — `shot_12.png` already shows a Product updated toast in the relevant context. |
| `shot_16.png` | Browser tab switch | Transition, not product content. |
| `shot_20.png` | Almondine Tarte detail page (generic) | No new information beyond shots already used. |
| `shot_24.png` | Payment screen | Payment flow is not part of Parent-Child Structure manual; kitchen ticket format is not visible here either. |
| `shot_25.png` | Navigation to Reporting | Generic navigation; parent manual covers. |
| `shot_26.png` | ProductMix before filter | Transitional state before the important `shot_27.png`. |
| `shot_30.png` | Navigation back to the menu | Generic navigation. |
| `shot_32.png` | Outro branding | Presentation chrome. |

_(Note: `shot_28.png` is technically listed but the tooltip content is essentially the same claim as `shot_27.png` + `shot_29.png`; acts as reinforcement if needed — treat as optional.)_

## Cross-check: coverage of claims from `04-observation-log.md`

Every claim (C1–C16) has at least one shot assigned to its Target doc:

| Claim | Shot anchor | Target doc |
|---|---|---|
| C1 — Feature name + admin location | `shot_03.png` | 01-explanation |
| C2 — Variants section on parent | `shot_05.png` | 01-explanation, 02-howto-create |
| C3 — Two ways to add variant | `shot_06.png`, `shot_10.png` | 02-howto-create, 03-howto-attach |
| C4 — Subcategory scope | `shot_10.png` | 03-howto-attach, 06-reference-rules |
| C5 — Short Name appears on variants | `shot_11.png` | 02, 03, 06-reference-rules |
| C6a — Detach standalone-origin | `shot_07.png`, `shot_08.png` | 05-howto-remove |
| C6b — Detach variant-born | `shot_31.png` | 05-howto-remove |
| C7 — Reorder by drag | `shot_13.png` | 04-howto-reorder |
| C8 — Pre Chosen | `shot_13.png`, `shot_15.png` | 04-howto-reorder |
| C9 — Variant Price | `shot_17.png` | 06-reference-rules R6 |
| C10 — Product Class inheritance | `shot_17.png` | 06-reference-rules R3 |
| C11 — Variant Modifiers / Allergens | `shot_18.png` | 06-reference-rules R7 |
| C12 — POS tappable buttons | `shot_15.png` | 04-howto-reorder, 06-reference-rules |
| C13 — Order preview two-line | `shot_23.png` | 06-reference-rules R6 |
| C14 — Kitchen ticket "full name" | *(no visual)* | 06-reference-rules R6 + 08-known-limitations |
| C15 — ProductMix composite label | `shot_27.png` | 06-reference-rules R6 |
| C16 — Color code caveat | `shot_19.png` | 06-reference-rules R8 + 08-known-limitations |

C14 is the only claim with no direct visual — matches the Source Matrix ruling that its format is not shown. Caption in `06-reference-rules.md` phrases it cautiously.
