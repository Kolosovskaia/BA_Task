---
id: 10-rtm
title: Requirements Traceability Matrix — Parent-Child Structure Manual
date: 2026-04-24
sources:
  - 04-observation-log.md (claims C1–C16, unknowns UK1–UK12)
  - 06-source-matrix.md (source strength per claim)
  - 08-ia.md (target docs)
  - 09-shotlist.md (screenshot anchors)
phase: 3 — Scope lock & IA (Step 10)
status: skeleton — rows populated from current evidence; "Draft status" column will be filled during Phase 4 (Drafting) and Phase 5 (Validation)
---

# Requirements Traceability Matrix (RTM) Skeleton

## Purpose

A single table that lets anyone trace any statement in the final manual back to its evidence — video timestamp, narration, prior analysis, or PO communication — **and** forward to its location in the published doc. It serves two jobs:

1. **During drafting (Phase 4)** — a checklist: every row must end up in a specific doc.
2. **During validation (Phase 5)** — an audit tool: every claim in the manual must have a matching RTM row with confidence and source.

## How to read this

- **Claim ID** — the stable code for the statement (e.g., `C5`). Full human-language text is in the next column, so you never have to dig for what `C5` means.
- **Claim (plain language)** — the statement itself, as close to final-manual wording as useful.
- **Confidence** — how solid the source is. Legend at the top of `04-observation-log.md`; in short: `DO` = directly shown, `NN` = narrated only, `D+N` = both, `NN-only` = narrated but never demonstrated.
- **Primary source** — the strongest evidence that supports this claim (video shot, transcript passage, PO answer).
- **Secondary / corroborating source** — optional supporting evidence.
- **Target doc** — the file in `docs/manual/` where this statement will live.
- **Target section** — the specific section of that file.
- **Draft status** — `pending` / `drafted` / `reviewed` / `flagged`. Updated during Phase 4–5.
- **Publication posture** — `publish as stated` / `publish with hedge` / `do not publish as stated` / `known-limitation only`.

## Part 1 — Confirmed claims (the spine of the manual)

| Claim ID | Claim (plain language) | Confidence | Primary source | Corroborating | Target doc | Target section | Draft status | Publication posture |
|---|---|:-:|---|---|---|---|:-:|---|
| **C1** | The feature is called Parent-Child Structure and is configured in the admin panel under Menu → Category → Subcategory → Item. | D+N | `shot_03.png` (breadcrumb visible) + transcript 0:03–0:24 | `plan.md` F1 | `01-explanation.md` | Section: What it is / The mental model | **drafted** (2026-04-24) | publish as stated |
| **C2** | A parent item has a Variants section listing its child items. | D | `shot_05.png` | `shot_12.png` | `01-explanation.md`, `02-howto-create-variant.md` | Explanation: illustration; How-to: Step 2 context | pending | publish as stated |
| **C3** | There are two ways to add a variant: Add Variant (create new) or the Parent Item dropdown (attach existing). | D+N | `shot_06.png`, `shot_10.png` + transcript 0:38–1:29 | — | `01-explanation.md` (summary); `02-howto-create-variant.md`, `03-howto-attach-existing.md` (detailed) | How-tos, each one flow | pending | publish as stated |
| **C4** | The Parent Item dropdown lists only items from the same subcategory. | NN | transcript 1:29–1:40 | `shot_10.png` (dropdown visible with one option) | `03-howto-attach-existing.md`; `06-reference-rules.md` R4 | How-to: Prerequisites; Reference: R4 | pending | **publish with hedge** — phrasing must reflect that only a single-option case was shown; recommended wording: "Candidate parents are restricted to items in the same subcategory." |
| **C5** | The Short Name field appears on a variant's detail page but not on a standalone item's. | D | `shot_11.png` + `shot_09.png` (absent in standalone state) | transcript 1:40–1:56 | `02-howto-create-variant.md`, `03-howto-attach-existing.md`, `06-reference-rules.md` R2 | How-to: Step; Reference: R2 | pending | publish as stated |
| **C6a** | When a variant that was originally standalone is detached, it returns to the item list as a standalone. | D+N | `shot_07.png` → `shot_08.png` sequence + transcript 1:05–1:15 | `plan.md` F3 | `05-howto-remove-variant.md`; `06-reference-rules.md` R5 | How-to: Branch A; Reference: R5 table | pending | publish as stated |
| **C6b** | When a variant that was created inside a parent is detached, it is permanently deleted. | NN | transcript 6:37–7:16 (restated) | PO Round 1 confirmation (`docs/po-answers-2026-04-24.md` Q-3) | `05-howto-remove-variant.md`; `06-reference-rules.md` R5 | How-to: Branch B + **warning callout**; Reference: R5 table | pending | publish as stated (PO-confirmed; treat as reliable) |
| **C7** | Variants can be reordered by drag; the admin-saved order determines the order shown on POS. | D+N | `shot_13.png` + transcript 2:06–2:25 | `shot_15.png` (POS result) | `04-howto-reorder-variants.md`; `06-reference-rules.md` R6 | How-to: Part 1; Reference: R6 POS row | pending | publish as stated |
| **C8** | A variant can be marked Pre Chosen; on POS it appears visually pre-selected. | D+N | `shot_13.png` (toggle) + `shot_15.png` (POS) | transcript 2:06–2:25 | `04-howto-reorder-variants.md`; `06-reference-rules.md` R6 | How-to: Part 2 + Verification; Reference: R6 | pending | publish as stated |
| **C9** | A variant has its own Price, configurable independently. | NN | transcript 2:43–2:55 | `shot_17.png` (Price field visible in Edit Variant) | `06-reference-rules.md` R6 | Reference: Variant-level fields | pending | publish as stated (low-risk structural claim) |
| **C10** | A variant's Product Class is inherited from its parent and is not editable at the variant level. | NN | transcript 2:43–2:55 | `shot_17.png` (Product class = Food on a variant) | `06-reference-rules.md` R3 | Reference: R3 | pending | **publish with hedge** — say "inherited from the parent" and "displayed at variant level"; do not assert "read-only" visually-unverified |
| **C11** | A variant has its own Modifiers and Allergens lists. The effect of Modifiers when the item is inside a Parent-Child context is not documented. | D (fields) + NN (independence) + contradictory (behaviour) | `shot_18.png` + transcript 2:55–3:15 | — | `06-reference-rules.md` R7; `08-known-limitations.md` UK10 | Reference: structural only; Limitations: behavioural note | pending | **publish with hedge** — structural yes, behavioural deferred to limitations |
| **C12** | On POS, under a parent item, variants appear as tappable buttons labelled with Short Name. | D | `shot_15.png`, `shot_21.png`, `shot_22.png` | transcript 3:47–3:54 | `04-howto-reorder-variants.md` (Verification); `06-reference-rules.md` R6 | How-to: Verification; Reference: R6 POS | pending | publish as stated |
| **C13** | On the order preview, a selected variant shows the parent name as the main line with the Short Name and modifier choices beneath. | D+N | `shot_23.png` + transcript 3:54–4:34 | — | `06-reference-rules.md` R6 | Reference: R6 Order preview | pending | publish as stated |
| **C14** | The kitchen ticket includes the item's full identifying name. The exact layout of that name is not shown in the source materials. | NN-only | transcript 4:34–4:49 | `plan.md` F11 | `06-reference-rules.md` R6 (short neutral note); `08-known-limitations.md` UK7 | Reference: short note; Limitations: detailed | pending | **do not publish format** — only state that the kitchen ticket receives the item; layout is flagged under known limitations |
| **C15** | In the ProductMix report, a sold variant appears under a composite label that includes both the parent name and the Short Name — not the parent name alone, and not the Short Name alone. | D+N | `shot_27.png`, `shot_28.png`, `shot_29.png` (observed label "Cafe Sua Da – Small Cafe Sua Da") + transcript 5:12–6:26 | `plan.md` F12 (narration — but on-screen resolves the apparent contradiction with F10) | `06-reference-rules.md` R6 | Reference: R6 ProductMix | pending | publish as stated (**reframed** from Maya's "not parent name" narration to reflect what is actually on screen) |
| **C16** | The Color Code display option is described in the video as affecting items "outside the parent category" — its behaviour within Parent-Child context is not documented. | NN (self-contradictory narration) | transcript 3:15–3:33 | `shot_19.png` (field visible) | `06-reference-rules.md` R8 (field exists only); `08-known-limitations.md` UK10 | Reference: structural only; Limitations: behaviour | pending | **do not publish behavioural claim** — field-exists statement only |

**Summary**: 17 rows (C6 split into a/b). 11 rows `publish as stated`. 5 rows `publish with hedge` or partial. 1 row `do not publish format` (C14). Alignment with Source Matrix thresholds verified.

### Draft progress as of 2026-04-24

- **Drafted (fully in primary target doc)**: C1 → `01-explanation.md`.
- **Drafted at summary level in `01-explanation.md` (full coverage pending in how-to / reference)**: C2, C3, C4, C5, C8, C12, C14, C15. Their primary targets are `02`–`06` — status remains `pending` until those files are written.
- **Not drafted yet**: all other claims.

## Part 2 — Unknowns tracker (drives `08-known-limitations.md`)

Each row here becomes a row in the Known Limitations table of the final manual.

| Unknown ID | Topic | Why it's unknown | Current route | PO Round 2 dependency |
|---|---|---|---|:-:|
| **UK1** | What happens to variants when the PARENT item is deleted. | The scenario is not shown in the video and Maya's Round 1 answer addressed variant-detach instead. Re-asked in Round 2. | `08-known-limitations.md` unless PO elects to include in v1. | ✅ |
| **UK2** | Whether a variant can itself be a parent of sub-variants (multi-level nesting). | Not shown; the video demonstrates exactly one level. | `08-known-limitations.md` unless PO confirms a limit (e.g., "one level only"), in which case it becomes a rule in `06-reference-rules.md`. | ✅ |
| **UK3** | Migration behaviour when a restaurant enables Parent-Child with pre-existing legacy items. | The feature is already in production; the before/after state is not in the video. | `08-known-limitations.md` unless PO provides migration description. | ✅ |
| **UK4** | How discounts interact with Parent-Child (parent-level vs variant-level; precedence rules). | Not shown, not narrated. | `08-known-limitations.md` unless PO provides semantics. | ✅ |
| **UK5** | Role-based permissions for creating, detaching, or deleting under Parent-Child. | Not shown, not narrated. | `08-known-limitations.md` unless PO provides a permission model. | ✅ |
| **UK6** | Maximum number of variants per parent. | Not shown, not narrated. | `08-known-limitations.md`. | — |
| **UK7** | Exact layout of the item name on the kitchen ticket. | Kitchen ticket is never shown in the video. | `08-known-limitations.md`. | Optional — could fold into Round 2 if PO has the ticket template handy. |
| **UK8** | Short Name length and character constraints. | Not shown; only `5'` entered as a sample value. | `08-known-limitations.md`. | — |
| **UK9** | Whether more than one variant can be Pre Chosen simultaneously. | Only one toggled in the video. | `08-known-limitations.md`. | — |
| **UK10** | Actual Modifier and Color Code behaviour when an item is inside Parent-Child context. | Narration self-contradictory. | `08-known-limitations.md` (linked from R7, R8 in `06-reference-rules.md`). | — |
| **UK11** | Import / export, API, bulk operations on Parent-Child. | Out of screencast scope. | `08-known-limitations.md` (explicit out-of-scope). | — |
| **UK12** | Localization of Short Name across language menus. | Not shown, not narrated. | `08-known-limitations.md` (explicit out-of-scope). | — |

**Round 2 gate**: UK1–UK5 statuses change depending on Maya's answers. Possible transitions:

- `08-known-limitations.md` (default) → `06-reference-rules.md` (if Maya provides the rule).
- `08-known-limitations.md` (default) → new how-to scenario (if Maya elects a user flow to document, e.g., a migration walkthrough).

## Part 3 — Claims pending (conditional on Round 2)

Reserved IDs for claims that may become required once Round 2 comes back. Kept empty for now; when Round 2 lands, the relevant UK row moves into Part 1 with a new C-code.

| Reserved ID | Conditional on | Target doc (if confirmed) |
|---|---|---|
| `C17` | Round 2 answer on parent-delete cascade (UK1). | `06-reference-rules.md` R5 expansion; `05-howto-remove-variant.md` new branch. |
| `C18` | Round 2 answer on nesting depth (UK2). | `06-reference-rules.md` new rule (R-new) or `08-known-limitations.md`. |
| `C19` | Round 2 answer on migration (UK3). | Possibly new how-to + rule. |
| `C20` | Round 2 answer on discounts (UK4). | `06-reference-rules.md` new rule. |
| `C21` | Round 2 answer on permissions (UK5). | `06-reference-rules.md` new rule. |

## Coverage check

Every claim C1–C16 is assigned to at least one target doc.
Every shot used in `09-shotlist.md` supports at least one claim.
All 12 unknowns UK1–UK12 have a routing decision.

Next deliverable update: after Maya's Round 2 answers arrive, re-run this RTM to move UK → C transitions and lock in `07-scope.md` (Step 6). After that, Phase 4 (Drafting) begins.
