---
id: 03-audience
title: Audience & Use Context Card
date: 2026-04-24
source: PO Round 1 Q-1 (voice message 2026-04-24)
phase: 1 — Framing & Elicitation
---

# Audience & Use Context Card

## Primary persona — "Internal Tester"

**Role**: QA / tester inside AXIOM.tech (or close-contact internal team member).

**Purpose of reading this manual**:

- Verify feature behaviour matches expectations during testing.
- Look up specific rules and logic quickly when a test case requires it.
- Use as a behaviour reference while writing test cases.

**What they already know (per PO)**:

- How to create a basic menu item in Gen1POS admin.
- How to configure modifiers on an item.
- How to configure the full set of item fields (name, product class, price, display configuration, etc.).

**What they do NOT need re-explained**:

- Navigation into Menu / Categories / Subcategories (covered in parent manual).
- Item creation basics (name, price, status, product class semantics).
- Modifier concept (covered in parent manual).
- POS side general layout.

**Reading context**:

- Open during a testing session — reference lookup, not tutorial reading.
- Part of a larger manual — navigation to related topics matters (link out, don't duplicate).
- Probably English-native or EN-fluent (final mandated EN-only per Q-4).

## Secondary persona — "Team Member Who Needs To Understand"

**Role**: anyone inside the team who touches the feature — support, product, onboarding.

**Purpose**: get a correct mental model fast; find a specific rule.

Same prior-knowledge baseline; same reading context.

## Non-readers (explicit out of audience)

- End customers ordering via POS.
- Restaurant admins / managers outside AXIOM.tech.
- POS operators (cashiers).
- Developers working on the feature implementation.
- Marketing / sales stakeholders.

## Top jobs-to-be-done (derived)

| # | Job | Where in the manual it's served |
|---|---|---|
| J1 | "I need to check what happens when a variant is detached — does it disappear or return to the item list?" | `06-reference-rules.md` (Detach behaviour) + `05-howto-remove-variant.md` |
| J2 | "I need to verify Short Name is displayed correctly in POS / Kitchen / ProductMix — where does each field show up?" | `06-reference-rules.md` (Display matrix) |
| J3 | "I need to understand how Product Class is inherited from parent to variant — is it editable on the variant?" | `06-reference-rules.md` (Inheritance) |
| J4 | "I need to reproduce the end-to-end flow: create parent → add variant → set pre-chosen → verify on POS." | `02-howto-create-variant.md` + `04-howto-reorder-variants.md` |
| J5 | "I need to know what is NOT yet documented so I don't assume behaviour." | `08-known-limitations.md` |

## Tone guidance (derived from audience)

- **Technical but concise** — reader is a colleague, not a layperson.
- **Imperative for how-to, declarative for reference** (per MS Writing Style Guide).
- **No marketing language** — no "delightful", no "powerful feature".
- **UI labels verbatim and capitalized** when referencing fields (Short Name, Product Class, Pre Chosen, Add Variant).
- **Zero assumption** about what the video demonstrated — reader may not have seen it.
