---
id: 12-review-log
title: Self Cognitive Walkthrough — Parent-Child Structure Manual v1
date: 2026-04-25
phase: 5 — Validation (Step 16)
sources:
  - docs/manual/02-howto-create-variant.md (SC-1)
  - docs/manual/05-howto-remove-variant.md (SC-5)
  - docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md §5 Phase 5 Step 16
method: Self cognitive walkthrough — read each how-to as a first-time reader, note moments of friction, ambiguity, or stalls, then apply fixes.
---

# Self Cognitive Walkthrough — Review Log

## Method

I re-read two of the most important how-to pages with the mindset of a tester who has never used Parent-Child Structure before but is comfortable with Gen1POS basics — i.e., the v1 audience. At each step I asked: *Could I do this without stopping to ask?* When the answer was "not quite", I noted what got in the way (column **Friction**) and what I changed (column **Fix**).

Two scenarios were chosen for depth over breadth, per spec §5 Phase 5:

- **SC-1 (Create a new variant)** — the baseline create flow. If this is unclear, everything else is unclear.
- **SC-5 (Remove a variant)** — the destructive case. If the warning fails to land, a tester may unknowingly delete a menu item.

The other three how-tos (03 attach, 04 reorder, 05 verification) were skim-read after the deep-read on the two above and yielded only two minor observations, captured at the bottom.

## Walkthrough A — SC-1 (Create a new variant)

File: `docs/manual/02-howto-create-variant.md`.

| Step | Reader's reaction | Friction | Fix |
|:-:|---|---|---|
| Title + opening sentence | "Got it — this is the create-new flow, not the attach flow." | None. | None. |
| Disambiguation paragraph | "Good — it tells me where to go if I want the other flow." | None — useful early branch. | None. |
| Before you start | Three preconditions listed: admin access, parent exists, basic-item familiarity. The third bullet links out to the parent Gen1POS manual. | TODO comment in the source about the parent-manual URL — but the user-facing render is clean text; the TODO is HTML-commented. | None — the TODO is invisible to readers, kept for a future pass when Maya shares the parent-manual link. |
| Step 1 — Navigate | "I know how to navigate." | None. | None. |
| Step 2 — Locate Variants section | Screenshot anchors me. | None. | None. |
| Step 3 — Click Add Variant | Screenshot shows the button at the bottom of the Variants section. After this step, I expect a modal or a new page to open, but the how-to jumps directly to "Step 4 — Fill in the variant's fields." | Mild — I'm not sure whether I'm now in a modal or on a separate page. The screencast shows it goes to a fresh detail page but the how-to does not name that. | **Decided: no edit.** The screenshots in the next step (`shot_11.png`) show the variant detail page with the Short Name field. The transition is implicit but recoverable. Adding "(a new variant detail page opens)" would be redundant given that the next image shows where you are. The friction is "mild" — not "stuck". |
| Step 4 — Fill in the fields | The how-to says "using the same procedure as for a basic menu item" and links to the parent manual. Tells me Product Class is inherited and not needed. | None — the inheritance handoff prevents a "wait, what about Product Class?" stall. | None. |
| Step 5 — Short Name | Clear; screenshot of the field. | None. | None. |
| Step 6 — Save changes | Clear. | None. | None. |
| Expected result | Two checks: confirmation toast + variant in Variants section. Screenshot shows both. | None. | None. |
| Notes | Warns me the variant is "variant-born" and links to the remove how-to for the destructive branch. | None — and the cross-link is the right level: I don't need to read the remove how-to to complete the create flow, but I'm warned that *if* I later detach this item, it disappears. | None. |
| What's next | Three logical next actions. | None. | None. |

**Walkthrough A verdict**: PASS. One mild friction noted (between Step 3 and Step 4); explicitly accepted as no-edit.

## Walkthrough B — SC-5 (Remove a variant)

File: `docs/manual/05-howto-remove-variant.md`.

| Step | Reader's reaction | Friction | Fix |
|:-:|---|---|---|
| Title + opening sentence | "Got it — this is the variant-removal flow." | None. | None. |
| Warning callout above "Before you start" | The very first thing I see after the title is a big visible block telling me the action can be destructive. | None — actively addresses the worst failure mode. | None. |
| Before you start (third bullet) | Asks me to know the variant's origin. If I don't, treat as destructive. | **Caught a phrasing issue**: the bullet links to "How to attach an existing item" with the parenthetical "(via How to attach an existing item)". A first-time reader could read this as "the only way to attach is via this linked how-to" rather than "if you used that flow, the variant is standalone-origin". | **Edited**: minor wording adjustment to clarify the bullet refers to *origin*, not *flow*. Verified after fix. *(See Fixes Applied below.)* |
| Step 1 — Navigate | Clear. | None. | None. |
| Step 2 — Locate Variants section | Clear. | None. | None. |
| Step 3 — Click X | Screenshot shows the X control. I notice the alt text is descriptive. | None. | None. |
| Step 4 — Confirm if prompted | The "if prompted" hedge is a giveaway: the source did not observe a confirmation dialog. | None — the hedge is honest and reads as a defensive instruction, not a contradiction. | None. |
| Outcome | Two-row table; the **No.** verdict in the reversibility column for the variant-born branch is bold. | None — the boldness lands. | None. |
| Outcome screenshots | Two: `shot_08.png` confirms the "returns to list" branch, `shot_31.png` anchors the destructive branch. The caption on `shot_31.png` explicitly tells me there is no separate "deleted-item view" image. | None — the caption pre-empts the question "where's the proof". | None. |
| Destructive-action section | Three bullets list what is lost; a closing paragraph offers a workaround (move-to-another-parent first). | **Caught a missing detail**: the workaround says "first attach a different parent in the Parent Item dropdown, then save". A reader could ask: "But the X is in the Variants section — am I now in a different file/page?" The implicit answer is yes (you'd open the variant's detail page), but it is not stated. | **Decided: light edit** — added a half-sentence that names the page change. *(See Fixes Applied below.)* |
| Notes | Two notes — about parent-when-last-variant-removed and about the variant-born branch being PO-confirmed but not re-demonstrated. | None — both notes preserve the reader's trust by being honest about the source. | None. |
| What's next | Three logical next actions. | None. | None. |

**Walkthrough B verdict**: PASS after two fixes (one wording, one half-sentence clarification). Verified after applying.

## Skim-read of the other how-tos

Read once at normal pace; only friction recorded.

| File | Friction | Fix |
|---|---|---|
| `01-explanation.md` | The mermaid diagram renders parent and standalone at the same level under subcategory; the relationship "any item can become a parent" is stated in text. **No friction**. | None. |
| `03-howto-attach-existing.md` | The "no candidates" note in the Notes section is a graceful answer to a real edge. **No friction**. | None. |
| `04-howto-reorder-variants.md` | Three numbered sequences (Part 1, Part 2, Verification) restart at 1 each. Briefly checked — the section headings make the scope of each numbered list unambiguous. **No friction**. | None. |
| `06-reference-rules.md` | R-section codes used as cross-references from how-tos (e.g., "Rules R5"). **No friction.** | None. |
| `07-reference-glossary.md` | Origin-related entries duplicate part of R5. Decided this is intentional — a glossary lookup should not require chasing to the rules page for the one-line definition. | None. |
| `08-known-limitations.md` | Four-section structure (behavioural / constraints / contradictory / out-of-scope) reads cleanly. The final "How to fill these gaps" section adds the resolution path. **No friction.** | None. |

## Fixes applied

### Fix 1 — `05-howto-remove-variant.md` Before-you-start third bullet

**Before**:

> You know whether the variant was **created inside the parent** (via [How to create a new variant](02-howto-create-variant.md)) or **attached from the item list** (via [How to attach an existing item](03-howto-attach-existing.md)). If you do not know, treat the operation as destructive — see the warning below.

**After**:

> You know the variant's **origin** — whether it was created inside the parent (with **Add Variant** — see [How to create a new variant](02-howto-create-variant.md)) or attached from the item list (via the **Parent Item** dropdown — see [How to attach an existing item](03-howto-attach-existing.md)). If you do not know, treat the operation as destructive — see the warning below.

Why: the original phrasing tied origin to a how-to file rather than to a UI action. Renamed-on-the-fly to reference the UI action (`Add Variant` / `Parent Item` dropdown) and demoted the file links to "see also" parentheticals. Reader still gets the link, but the rule is anchored to UI behaviour.

### Fix 2 — `05-howto-remove-variant.md` Destructive-action section, workaround paragraph

**Before**:

> If you want to take the variant off this parent but keep the item available — for example, to move it to a different parent later — first attach a different parent in the **Parent Item** dropdown, then save. Detaching it via the X control is the wrong tool when the item must survive.

**After**:

> If you want to take the variant off this parent but keep the item available — for example, to move it to a different parent later — open the variant's detail page first, change the **Parent Item** dropdown to a different parent (or to `None (Standalone)`), then save. Detaching via the X control is the wrong tool when the item must survive.

Why: named the page change explicitly so the reader doesn't have to infer that the workaround starts on a different page than where the X control lives. Added `None (Standalone)` as a valid target so the workaround also covers "I want to keep the item but unparent it entirely".

## Verification after fixes

Re-read both edited paragraphs in context; both now read smoothly. No collateral consistency breaks introduced (UI labels still match the screencast; cross-links unchanged).

`docs/manual/05-howto-remove-variant.md` re-read end-to-end after the edits — no further friction.

## Phase 5 Step 16 verdict

**PASS**. Two minor edits applied; both verified. The manual is ready to advance to Step 17 (Publish & Handover).

## Note on next phase

Per user direction on 2026-04-25, no Round 2 PO interaction is performed for v1; per the spec the publication phase (Step 17) is the final step. The handover deliverable in v1 is the GitHub repo at its current commit; no PDF export, no separate cover letter, beyond the repository contents themselves.
