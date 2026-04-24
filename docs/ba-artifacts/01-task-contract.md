---
id: 01-task-contract
title: Task Contract — Parent-Child Structure Manual
date: 2026-04-24
status: locked (Round 1 PO answers applied); pending Round 2 clarifications
phase: 1 — Framing & Elicitation
---

# Task Contract

## 1. Task

Describe how the Parent-Child Structure feature works in Gen1POS, in the form of a section of a user manual.

**Origin**: test assignment from Maya Pivovarova (AXIOM.tech) to Kseniia.

## 2. Stakeholders

| Role | Person | Contact |
|---|---|---|
| PO / SME | Maya Pivovarova | Telegram @mayya_pi |
| BA / Author | Kseniia | — |

## 3. Contract fields

| Field | Value | Source |
|---|---|---|
| **Audience (primary)** | Internal testers / QA | PO Round 1, Q-1 |
| **Audience (secondary)** | Team members who need to understand how the feature works («кому необходимо») | PO Round 1, Q-1 |
| **Reader's prior knowledge** | Already knows: basic item creation, modifier configuration, full item field-by-field setup — all covered by existing Gen1POS manual | PO Round 1, Q-1 |
| **Deliverable form** | Markdown pack in a GitHub repo; I share link back to PO | PO Round 1, Q-2 |
| **Integration constraint** | Must fit into existing Gen1POS manual structure and tone; PO will share link to parent manual for reference | PO Round 1, Q-2 |
| **Scope v1 — in** | Happy path (create / attach / reorder / pre-chosen / remove) + detach-logic (Maya confirmed this is part of functionality, not edge-case) | PO Round 1, Q-3 |
| **Scope v1 — pending Round 2** | multi-level nesting, migration, discounts parent-vs-variant, permissions, real cascade-delete-of-parent | PO Round 1, Q-3 (reclarified) |
| **Deadline** | "As fast as possible" — no hard date; PO explicitly said she wants to gauge work pace | PO Round 1 follow-up |
| **Language** | English only. No Russian version. | PO Round 1, Q-4 |

## 4. Non-goals (explicit)

- Not a full Gen1POS manual — scoped to Parent-Child Structure feature only.
- Not a replacement for existing manual content (basic item, modifiers, fields).
- No Russian / bilingual version.
- No onboarding tutorial for Gen1POS in general.
- No developer / API documentation — end-user (tester-facing) perspective.

## 5. Open dependencies

| # | Dependency | Blocks | Status |
|---|---|:-:|---|
| D1 | PO link to existing Gen1POS manual (tone/template reference) | Phase 4 finalization | awaiting Maya |
| D2 | PO Round 2 answers (4 unclear terms + cascade-delete-of-parent re-ask) | Phase 3 Scope Register (Step 6) | sent; awaiting |

**Not blocking now**: Phase 2 (Observation Log, Capability Map, Source Matrix) proceeds in parallel.

## 6. Assumptions (used if PO silent on a point)

- **Accessibility baseline**: ISO/IEC/IEEE 26514 §8.2 (alt-text on images, H1–H3 without skipping, plain language).
- **Versioning**: single v1 published; later changes as amendments with changelog entry.
- **Repo license**: inherits parent repo license; no separate notice.
- **Screenshot source**: reuse `docs/screens_cropped/*.png` (32 shots already extracted from video).
- **Terminology reference**: Maya's transcript and video UI labels are authoritative for EN naming in final (already in English in UI).

## 7. Signals and pacing note

PO said: "чем быстрее тем лучше, чтобы понимать примерно темп твоей работы". Interpretation: visible, frequent deliverables matter; quality-over-speed trade-off should lean slightly towards speed without becoming sloppy. Preference: merge-in-stages, not big-bang-final.
