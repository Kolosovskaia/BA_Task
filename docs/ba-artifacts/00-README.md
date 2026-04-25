---
id: 00-README
title: BA Artifacts — Reader's Guide
date: 2026-04-24
purpose: Navigation and legend for everything in this folder
---

# BA Artifacts — How to Read This Folder

## What this folder is (and is not)

This folder holds **internal working artifacts** a BA produces while figuring out **what** to put into the final user manual. None of these files are the manual itself.

- **Final user manual** lives in `docs/manual/`.
- **These files** are the "how we got there" evidence trail.
- **Design spec with the overall plan** is in `docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md`.

Each file is numbered by **production order**, not by reading priority. If you need a fast overview: read this README + `01-task-contract.md` + `08-ia.md`.

## The artifacts in order

| # | File | What question does it answer? | Produced in plan step |
|:-:|---|---|:-:|
| 00 | `00-README.md` (you are here) | What does each file mean, and what do all these codes refer to? | — |
| 01 | `01-task-contract.md` | What did we agree to deliver? (audience, format, language, scope, deadline, non-goals) | Step 1 |
| 02 | `02-glossary.md` | What do Russian transcript terms map to in the English manual? | Step 2 |
| 03 | `03-audience.md` | Who reads this, and what do they already know? | Step 2 |
| 04 | `04-observation-log.md` | Shot by shot (34 cropped frames: 32 original + 2 replacements), what does the video **show** vs **say** vs **leave out**? | Step 3 |
| 05 | `05-capability-map.md` | What can this feature actually do, atomically? | Step 4 |
| 06 | `06-source-matrix.md` | For every statement we might write in the manual, how solid is the source? | Step 5 |
| 07 | `07-scenarios.md` | What user flows become the how-to pages in the manual? | Step 7 |
| 08 | `08-ia.md` | How does the final `docs/manual/` folder map onto these scenarios and rules? | Step 8 |
| 09 | `09-shotlist.md` | Which of the 34 screenshots go where in the final manual, with captions? | Step 9 |
| 10 | `10-rtm.md` | For every claim we might publish, what's the evidence and where does it land? | Step 10 |
| 11 | `11-qa-checklist.md` | Did the manual pass the Definition of Done — traceability, accuracy, accessibility, safe-scope publication? | Step 15 |
| 12 | `12-review-log.md` | What happened when I read the how-tos as a first-time reader, and what got fixed? | Step 16 |

**Step 6** (Scope Register) was not produced — per user direction on 2026-04-25, Round 2 PO answers are not sought for v1; UK1–UK5 stay as out-of-scope-for-v1 entries in `docs/manual/08-known-limitations.md` instead of triggering scope renegotiation.

## Human-language summary per file

### 01-task-contract.md — "The handshake"

What we committed to with PO, based on her Round 1 voice message:

- **Who reads it**: internal testers + team members (not customers, not admins).
- **Prior knowledge**: they already know Gen1POS basics from parent manual.
- **Format**: Markdown in a GitHub repo; we share the link back.
- **Integration**: our doc must fit into the existing Gen1POS manual's style. PO will send a link to that manual.
- **Scope**: the 5 main scenarios from the video + detach-logic (both branches). 4 edge-case terms pending her Round 2 decision.
- **Deadline**: "as fast as possible, so she can gauge work pace" — soft but visible.
- **Language**: English only.

### 02-glossary.md — "The dictionary"

Every term Maya used in the transcript, mapped to the English term the final manual will use. Includes: core concepts (parent item, variant, standalone), actions (Add Variant, Detach, Reorder), fields (Short Name, Pre Chosen, Product Class), and surfaces (POS, Kitchen ticket, ProductMix). Flags three terms where Maya's narration is ambiguous or self-contradictory.

### 03-audience.md — "Who am I writing for"

Primary reader = **internal tester / QA**. They read the manual as reference while testing, not as a tutorial. They already know how to create a base item in Gen1POS. Five top "jobs to be done" identified (e.g., "I need to check what happens when a variant is detached"). Tone guidance: technical-but-concise, no marketing language.

### 04-observation-log.md — "What the video actually shows"

The heart of the evidence trail. Every one of the 32 video shots was classified: is this thing **directly visible**, **only narrated (said but not shown)**, **inferred** from context, or **unknown** (not in source at all)? The file produces:

- **16 extracted claims (C1–C16)**: specific statements we might put in the manual, each with its confidence code.
- **12 unknowns (UK1–UK12)**: things the video never covers but that matter for the feature.
- **2 internal contradictions flagged**: Maya says one thing but the screen shows another (e.g., "variant name, not parent name" in reports — but the on-screen label actually contains the parent name twice).

### 05-capability-map.md — "What the feature can do"

12 atomic capabilities of Parent-Child Structure, each with trigger, preconditions, steps, expected result. For example:

- **Create a variant** (what happens when admin clicks Add Variant).
- **Attach an existing item** (via Parent Item dropdown).
- **Reorder + mark Pre Chosen**.
- **Detach** (with its two origin-dependent outcomes).
- **Product Class inheritance**.
- **POS display** / **Order preview** / **Kitchen ticket** / **ProductMix reporting label**.
- **Subcategory scope constraint**.

These capabilities feed directly into both the scenarios (how-tos) and the reference rules.

### 06-source-matrix.md — "Can we actually publish this?"

For each of the 16 claims from observation log, what's the source strength and can we safely publish it?

- **12 out of 16 claims are reliable** (directly shown or shown+narrated) — passes the 70% threshold.
- **2 claims must NOT be published as stated**: kitchen ticket format (narrated only, never shown) and Color Code behaviour (narration is self-contradictory).
- **3 claims publishable with careful phrasing**: subcategory scope, product class inheritance, modifier behaviour.

### 07-scenarios.md — "What the how-to pages will cover"

Five user flows that turn into how-to pages in the final manual:

1. **SC-1 Create a new variant** → `docs/manual/02-howto-create-variant.md`
2. **SC-2 Attach an existing item as a variant** → `docs/manual/03-howto-attach-existing.md`
3. **SC-3 Reorder variants and set Pre Chosen** → `docs/manual/04-howto-reorder-variants.md`
4. **SC-4 Verify the Pre Chosen variant on POS** → part of `docs/manual/04-howto-reorder-variants.md`
5. **SC-5 Remove a variant** → `docs/manual/05-howto-remove-variant.md` (with **big warning** on the destructive branch)

Three extra scenarios remain outside v1 unless the package is explicitly reopened for a later revision (parent-delete cascade, migration, discounts).

### 09-shotlist.md — "Which shot goes where"

For each of the 34 screenshots, the file says: does it go into the final manual (and if so, into which doc, which section, with what caption) or is it excluded (and why).

- **17 published shots used** across 5 how-tos + 1 reference file.
- **4 optional shots** retained only as backup evidence.
- **13 shots excluded** (branding, transitions, retired replacements, or generic navigation that the parent manual already covers).
- **No orphaned shots** — every frame has a routing decision.

### 10-rtm.md — "Trace every claim to its evidence"

The Requirements Traceability Matrix. One row per claim (C1–C16) with: plain-language statement, source (shot / transcript / PO answer), confidence, target doc in `docs/manual/`, target section, draft status, and publication posture (publish as stated / publish with hedge / do not publish format).

Plus a second table for the 12 unknowns (UK1–UK12) — what's known about why it's unknown, and where it will end up in the final manual.

Plus a reserved-IDs block for claims that **may** emerge from Maya's Round 2 answers (C17–C21) — pre-slotted so we don't have to restructure when they land.

### 08-ia.md — "The final manual's structure"

The blueprint for `docs/manual/`: 9 files organized using the **Diátaxis** framework:

- **Explanation** (1 file): the concept, one page only.
- **How-to** (4 files): one per scenario.
- **Reference** (3 files): rules, glossary, known-limitations.
- **Tutorial slot is deliberately empty** (audience doesn't need it — they already know Gen1POS).

Each file has: purpose, length target, structure pattern, source capabilities/scenarios, screenshots assigned. Plus a navigation sitemap and a cross-reference map between files.

## Cheat sheet for all the codes you'll see

| Prefix | Meaning | Defined in | Example |
|---|---|---|---|
| **F#** | Fact extracted in the earlier BA analysis | `docs/plan.md` §1.2 | F3 = "detach is origin-dependent" |
| **G#** | Open gap from earlier analysis | `docs/plan.md` §1.4 | G1 = "what happens when parent is deleted?" |
| **H#** | Hypothesis from earlier analysis | `docs/plan.md` §3.2 | H1 = "audience is restaurant admin" (later revised) |
| **M#** | Missing input blocking our work | spec §4.2 | M1 = "scope contract from PO" |
| **C#** | Claim derived from the video / transcript | `04-observation-log.md` → derived claims | C5 = "Short Name appears only on variants" |
| **UK#** | Unknown — relevant but no data in source | `04-observation-log.md` → Unknowns | UK1 = "parent deletion cascade behaviour" |
| **CAP-#** | Capability — atomic thing the feature does | `05-capability-map.md` | CAP-1 = "Create a new variant" |
| **SC-#** | Scenario — user flow | `07-scenarios.md` | SC-5 = "Remove a variant" |
| **R#** | Reference rule section (planned) | `08-ia.md` §06-reference-rules | R5 = "Detach behaviour table" |
| **J#** | Job-to-be-done of the audience | `03-audience.md` | J1 = "verify what detach does" |
| **Q-#** | Question to PO, Round 1 | spec §6 | Q-1 = "who is the primary reader?" |
| **D1, D2** | Open dependencies on PO | `01-task-contract.md` §5 | D1 = "link to parent manual template" |

### Confidence codes in `04-observation-log.md`

| Code | Meaning |
|---|---|
| **DO** | Directly observable — visibly shown on screen and reproducible from video alone |
| **NN** | Narrated only — said in the video but never demonstrated visually |
| **IN** | Inferred — logically derived from DO/NN but not stated |
| **UK** | Unknown — source is silent on this |

(A claim can be "DO+NN" — both shown and narrated, the strongest state.)

### Source strength codes in `06-source-matrix.md`

Same idea as above, different scope:

| Code | Meaning |
|---|---|
| **D** | Direct (visually demonstrated) |
| **N** | Narrated (spoken only) |
| **I** | Inferred |
| **G** | Gap (no source) |

## Where to look for what

- "What does the feature actually do?" → `05-capability-map.md`.
- "How will the manual be structured?" → `08-ia.md`.
- "What's in scope vs not?" → `01-task-contract.md` + `docs/manual/08-known-limitations.md`.
- "Can we publish claim X?" → `06-source-matrix.md`.
- "What words do we use in English?" → `02-glossary.md`.
- "Who are we writing for?" → `03-audience.md`.
- "What does the video actually show?" → `04-observation-log.md`.

## What's still missing (to be produced)

- `07-scope.md` (Step 6) — not produced for v1 (Round 2 PO answers not sought).
- All other artifacts (Steps 1–16 of the plan) — produced. Phase 6 Step 17 (Publish & Handover) is git-publication of the repository at the current state.

## Note on numbering

Steps 1–18 are **plan steps** (in the design spec). Files in this folder are numbered by **production order within the plan**, so a file `04-observation-log.md` is the output of **Step 3** in the plan (Phase 2). Mismatch is intentional — file numbering is local to this folder, step numbering is global to the plan.
