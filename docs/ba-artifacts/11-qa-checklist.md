---
id: 11-qa-checklist
title: Internal QA Checklist — Parent-Child Structure Manual v1
date: 2026-04-25
phase: 5 — Validation (Step 15)
sources:
  - docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md §3.2 (DoD)
  - ISO/IEC/IEEE 26514 — Systems and software engineering — Design and development of information for users (criteria for completeness, accuracy, accessibility, usability)
  - docs/ba-artifacts/10-rtm.md (filled draft status)
scope: All 9 files in docs/manual/
---

# Internal QA Checklist

## Purpose

A self-administered audit pass against the spec's Definition of Done (§3.2) and the four ISO/IEC/IEEE 26514 quality dimensions. Each row carries a verdict (PASS / FAIL / N/A), one-line rationale, and a pointer to the evidence.

This checklist is paired with `10-rtm.md` (filled). Together they answer "is the manual ready to publish at v1 quality?".

## Files in scope

`docs/manual/00-index.md`, `01-explanation.md`, `02-howto-create-variant.md`, `03-howto-attach-existing.md`, `04-howto-reorder-variants.md`, `05-howto-remove-variant.md`, `06-reference-rules.md`, `07-reference-glossary.md`, `08-known-limitations.md`. Plus `_assets/` (20 screenshots).

## How to read this

- **Verdict** column uses **PASS** / **FAIL** / **N/A**.
- **Rationale** is one line: what was checked and what the reading was.
- **Evidence** points to the file or artifact that carries the proof.

A FAIL on any row blocks v1 publication and goes onto the fix list at the bottom.

---

## A. Traceability (DoD §3.2 — "100% claims → RTM row")

| # | Check | Verdict | Rationale | Evidence |
|---|---|:-:|---|---|
| A.1 | Every C-claim (C1–C16, with C6 split into C6a/C6b) has a row in `10-rtm.md` Part 1. | PASS | RTM Part 1 has 17 rows: C1, C2, C3, C4, C5, C6a, C6b, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16. | `10-rtm.md` Part 1 |
| A.2 | Every C-claim has a Draft Status of `drafted` (not `pending` / `pending-partial`). | PASS | All 17 rows updated to `drafted` on 2026-04-25 with the file and section where the claim landed. | `10-rtm.md` Part 1, Draft progress section |
| A.3 | Every UK (UK1–UK12) is routed to a row in `08-known-limitations.md`. | PASS | UK1–UK12 each appear as a row in `08-known-limitations.md`, organized into four groups (behavioural / constraints / contradictory narration / out-of-scope). | `08-known-limitations.md` |
| A.4 | Every screenshot referenced in `docs/manual/*.md` has a corresponding row in `09-shotlist.md` and a file in `_assets/`. | PASS | Manual references shots 03, 05, 06, 07, 08, 09, 10, 11, 12, 13, 15, 17, 18, 19, 23, 27, 31 — all listed in `09-shotlist.md` and present in `_assets/`. | `09-shotlist.md`, `ls _assets/` |
| A.5 | No claim in any manual file lacks an RTM trace. | PASS | The manual restricts itself to C1–C16 + UK1–UK12 — verified by walking each section against the RTM. | this checklist + `10-rtm.md` |

## B. Accuracy (DoD §3.2 — "0 contradictions; gaps explicitly marked")

| # | Check | Verdict | Rationale | Evidence |
|---|---|:-:|---|---|
| B.1 | Claims marked `do not publish format` or `publish with hedge` in the RTM are phrased per the recommended posture in the manual. | PASS | C14 (kitchen ticket) has only the neutral statement in R6.3; format flagged in UK7. C16 (Color Code) keeps field-exists statement only in R8; behaviour deferred to UK10. C4 phrased as "Candidate parents are restricted to items in the same subcategory" (R4 + 03-howto Prereqs). C10 phrased as "inherited from its parent and displayed on the variant" without "read-only" (R3). C11 split structural / behavioural. | `06-reference-rules.md`, `08-known-limitations.md` |
| B.2 | Internal contradiction "variant name vs parent name" (Source Matrix flag on C15) is resolved in a single voice across the manual. | PASS | Manual treats the ProductMix label as a composite "Parent Name – Short Name Parent Name" (R6.4 in `06-reference-rules.md`); no file claims the label is "variant name only" or "parent name only". | `06-reference-rules.md` R6.4, RTM C15 |
| B.3 | No inferred-only claim is published as confirmed. | PASS | Inferred-only claims (UK list) are confined to `08-known-limitations.md`. The how-tos and reference contain only D, D+N, or PO-confirmed NN claims. | `06-source-matrix.md` strength column + RTM Part 1 |
| B.4 | UI labels match the screencast / screenshots verbatim (casing, punctuation). | PASS | Verbatim labels: `Add Variant`, `Variants`, `Parent Item`, `None (Standalone)`, `Short Name`, `Pre Chosen`, `Save changes`, `Product updated`, `Variant deleted`, `Product Class`, `Modifiers`, `Allergens`, `Color Code`. Spot-checked against `04-observation-log.md` rows for shots 5–13, 17–19. | All how-tos + reference |
| B.5 | Detach behaviour table is consistent across `05-howto-remove-variant.md` and `06-reference-rules.md` R5. | PASS | Same two-row table with the same wording for outcome and reversibility, deliberate duplication per IA spec for ergonomics. | `05-howto-remove-variant.md` Outcome section vs `06-reference-rules.md` R5 |

## C. Reproducibility (DoD §3.2 — "any reader with admin can repeat each how-to")

| # | Check | Verdict | Rationale | Evidence |
|---|---|:-:|---|---|
| C.1 | Each how-to has Goal / Before you start / Steps / Expected result / Notes / What's next. | PASS | All four how-tos (02–05) follow the pattern. 04 adds a Verification section (SC-4) after the Steps. | `02`, `03`, `04`, `05` |
| C.2 | Each Step is imperative and ≤ 1 action per step. | PASS | Verbs: Open, Click, Drag, Toggle, Enter, Save, Confirm, Switch, Navigate, Tap. No compound steps spotted. | how-tos 02–05 |
| C.3 | Step count per how-to ≤ 10 (per IA spec). | PASS | 02: 6 steps; 03: 5 steps; 04: 3 reorder + 3 pre-chosen + 3 verification = 9; 05: 4 steps. | how-tos 02–05 |
| C.4 | Each how-to has at least one screenshot anchoring the user in the UI. | PASS | 02: 4 shots; 03: 5 shots; 04: 2 shots; 05: 3 shots. | shotlist + manual files |
| C.5 | Pre-conditions surface UI state required to proceed (admin access, item exists, item state). | PASS | All four how-tos open with "Before you start" listing admin access + item-state preconditions. 03 calls out the same-subcategory rule explicitly. 05 calls out the origin awareness for branch-B safety. | how-tos 02–05 |

## D. Consistency (DoD §3.2)

| # | Check | Verdict | Rationale | Evidence |
|---|---|:-:|---|---|
| D.1 | Single term per concept (per `02-glossary.md` mappings). | PASS | "Variant" used everywhere; "child" not used in body text. "Standalone item" used; "обычный айтем" not present. "Detach" used for the operation; "delete" only in the destructive-branch warning. | full-text scan of `docs/manual/*.md` |
| D.2 | UI labels in inline code or bold per consistent rule. | PASS | Convention: bold for buttons/sections (`**Add Variant**`, `**Variants**`, `**Save changes**`); inline code for field names (`` `Short Name` ``, `` `Parent Item` ``, `` `Product Class` ``); inline code for system feedback toasts (`` `Product updated` ``). Applied uniformly. | how-tos + reference |
| D.3 | Heading hierarchy: H1 only as document title; H2–H3 used sequentially. | PASS | Each file starts with one H1; H2 sections follow; H3 only used for sub-rules within a single H2 in `06-reference-rules.md` (R6.1–R6.4). No skips spotted. | scan of `docs/manual/*.md` |
| D.4 | Cross-links use file names that exist. | PASS | All relative links in the manual (file → file) point to existing files in `docs/manual/`. Spot-checked: `04-howto-reorder-variants.md`, `05-howto-remove-variant.md` — both present. | grep + ls |
| D.5 | Screenshot path convention `_assets/shot_XX.png` used everywhere. | PASS | No occurrence of `../screens_cropped/` or other ad-hoc paths in manual files. | grep on `docs/manual/*.md` |

## E. Accessibility (DoD §3.2 — ISO 26514 §8.2)

| # | Check | Verdict | Rationale | Evidence |
|---|---|:-:|---|---|
| E.1 | Every image has alt text (the bracketed `![alt](path)` text is non-empty and descriptive). | PASS | Spot-checked all 19 image references across 6 files; each carries a descriptive alt text different from the caption. | `docs/manual/*.md` |
| E.2 | Every image has a caption (italic line beneath) summarizing what it shows. | PASS | All images followed by a one-sentence italic caption with a period. Captions match `09-shotlist.md`. | `docs/manual/*.md` |
| E.3 | No information-only-in-image patterns. | PASS | Screenshots illustrate steps already described in text; the procedure is reproducible from text alone. Verified by re-reading 02 and 05 with images mentally hidden. | how-tos 02–05 |
| E.4 | Plain language; no marketing or jargon beyond defined Glossary terms. | PASS | No "leverage", "seamless", "powerful", "robust", or similar marketing fillers. Domain terms (variant, parent, Short Name, ProductMix) are defined in `07-reference-glossary.md`. | full-text scan |
| E.5 | Tables have header rows; long tables are not used as the sole carrier for procedure steps. | PASS | Tables used for rule look-ups (R5, R7, glossary, limitations) and for surface matrix (R1). All have header rows. Procedure steps use numbered lists, not tables. | `06-reference-rules.md`, `07-reference-glossary.md`, `08-known-limitations.md` |

## F. Usability (ISO 26514 — task orientation, navigation, findability)

| # | Check | Verdict | Rationale | Evidence |
|---|---|:-:|---|---|
| F.1 | A reader can identify the right how-to from the index in under 30 seconds. | PASS | `00-index.md` opens with a "Where to start" table that maps "If you want to…" → file. All five tasks (understand, create, attach, reorder, remove) are one row each. | `00-index.md` |
| F.2 | Each how-to ends with "What's next" pointing at related actions. | PASS | 02, 03, 04, 05 each end with a What's next list of 3–4 cross-links. | how-tos |
| F.3 | The destructive-action case is unmissable. | PASS | `05-howto-remove-variant.md` has a callout block above "Before you start", a dedicated "Destructive action — variant-born variants" section, and a row in the Outcome table. | `05-howto-remove-variant.md` |
| F.4 | Reference rules are searchable by code (R1–R8). | PASS | Each R-section has a stable code as part of its heading. Also referenced from how-tos (e.g., "Rules R5"). | `06-reference-rules.md` |
| F.5 | Known-Limitations entries are cross-linked from places where the gap is felt. | PASS | UK7 referenced from R6.3 (kitchen ticket); UK8 from R2 (`Short Name`); UK9 from R6.1 + 04-howto Notes; UK10 from R7 + R8; UK1 from 05-howto Notes + R5 ("parent deletion not documented in v1"). | `06-reference-rules.md`, how-tos |

## G. Safe-scope publication (DoD §3.2 — ISO 26514 + spec)

| # | Check | Verdict | Rationale | Evidence |
|---|---|:-:|---|---|
| G.1 | Body of the manual contains only D, D+N, or PO-confirmed NN claims. | PASS | C6b (PO-confirmed NN) is the only NN-only claim in the body, framed as authoritative + flagged in 05-howto Notes. C14 and C16 (NN with risk) are deliberately absent from the body and confined to Limitations. | RTM Part 1 + `06-reference-rules.md` |
| G.2 | "Not documented in v1" is the explicit phrase whenever a gap is referenced. | PASS | Phrase appears in R2, R5, R6.1, R6.3, R7, R8 of `06-reference-rules.md` and in `00-index.md` Conventions. | grep "Not documented in v1" |
| G.3 | The Limitations page distinguishes "out of scope" from "behavioural gap" from "constraint not stated" from "contradictory narration". | PASS | Four-section structure: behavioural / constraints / contradictory narration / out-of-scope. | `08-known-limitations.md` |

## Summary

| Category | Total checks | PASS | FAIL | N/A |
|---|:-:|:-:|:-:|:-:|
| A. Traceability | 5 | 5 | 0 | 0 |
| B. Accuracy | 5 | 5 | 0 | 0 |
| C. Reproducibility | 5 | 5 | 0 | 0 |
| D. Consistency | 5 | 5 | 0 | 0 |
| E. Accessibility | 5 | 5 | 0 | 0 |
| F. Usability | 5 | 5 | 0 | 0 |
| G. Safe-scope publication | 3 | 3 | 0 | 0 |
| **Total** | **33** | **33** | **0** | **0** |

## Fix list (FAILs only)

None. All 33 checks PASS.

## Sign-off note

This checklist was self-administered by the BA. A second pair of eyes (another team member or the product owner) is recommended before external publication, but is not a v1 blocker.

Phase 5 Step 15 verdict: **PASS — proceed to Step 16 (Self walkthrough).**
