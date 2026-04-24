---
id: 06-source-matrix
title: Source Reliability Matrix — Parent-Child Structure
date: 2026-04-24
derived_from:
  - 04-observation-log.md
  - 05-capability-map.md
phase: 2 — Evidence extraction
---

# Source Reliability Matrix

## Purpose

For every claim that may appear in the final manual, record where it comes from and how strong that provenance is. Feeds directly into RTM (Step 10) and into the "Known Limitations" drafting (Step 14).

## Legend

- **D** — Direct: visibly demonstrated in video (reproducible from the screencast alone).
- **N** — Narrated: spoken by Maya in the video/transcript; not visibly demonstrated.
- **I** — Inferred: derived logically from D/N but not directly stated.
- **G** — Gap / Unknown: relevant but no source data available.

A claim can be D+N (both shown and narrated — the strongest state).

## Matrix — claims vs. sources

| Claim | Transcript | Video (shot #) | Storyboard | `plan.md` F | Strength | Publishable without PO confirm? |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| C1 Feature name + admin location | ✓ | 3, 4 | ✓ | F1 | D+N | ✅ |
| C2 Parent has Variants section | ✓ | 5, 12 | ✓ | — | D | ✅ |
| C3 Two ways to add variant | ✓ | 6, 9, 10 | ✓ | F2 | D+N | ✅ |
| C4 Subcategory-scope constraint | ✓ | 10 | ✓ | F13 | N | ⚠️ — publishable with UI wording ("within the same subcategory") but worth phrasing cautiously |
| C5 Short Name appears on variants only | ✓ | 11, 12 | ✓ | F4 | D | ✅ |
| C6a Detach standalone-origin → returns to list | ✓ | 7, 8 | ✓ | F3 | D+N | ✅ |
| C6b Detach variant-born → disappears | ✓ | 31 (re-narrated) | — | F3 | N only | ⚠️ — PO re-confirmed as part of functionality in Round 1 → **treat as reliable**, document clearly |
| C7 Reorder via drag | ✓ | 13, 15 | ✓ | F5 | D+N | ✅ |
| C8 Pre Chosen toggle | ✓ | 13, 15 | ✓ | F6 | D+N | ✅ |
| C9 Variant has own Price | ✓ | 17 | ✓ | F7 | N (price field visible, edit not demonstrated) | ✅ (safe, low-risk claim) |
| C10 Product Class inherited | ✓ | 17 | ✓ | F8 | N | ⚠️ — say "inherited from parent (displayed read-only at variant level per narration)"; flag if edit state not visually confirmed |
| C11 Variant has own Modifiers & Allergens | ✓ | 18 | ✓ | F9 partial | D (fields exist) + N (independence), N contradictory on behaviour | ⚠️ — publish the structural claim (fields exist); defer behavioural claim (modifiers apply when? — UK10) |
| C12 POS shows variants as tappable buttons | ✓ | 15, 21, 22 | ✓ | F10 partial | D | ✅ |
| C13 Order preview = parent + short name | ✓ | 23 | ✓ | F10 | D+N | ✅ |
| C14 Kitchen ticket = "full name" | ✓ | 24 | (no kitchen shot) | F11 | N only | 🔴 — do NOT publish exact format; say "includes item's full identifying name (exact layout not documented in v1)"; see UK7 |
| C15 ProductMix composite label | ✓ | 27, 28, 29 | ✓ | F12 | D+N | ✅ — but **reframe**: the visible label is `Parent Name – Short Name Parent Name`, document as such instead of quoting Maya's "variant name, not parent name" (which is contradicted by what's on screen) |
| C16 Color code "outside parent-child" | ✓ | 19 | ✓ | — | N | 🔴 — narration self-contradictory; do not publish behavioural claim; optional mention of "behaviour of Color code under Parent-Child not documented in v1" (UK10 adjacent) |

## Gaps mapped to open questions

| UK | Description | Current route | PO dependency |
|---|---|---|:-:|
| UK1 | Parent-item deletion cascade | Round 2, Q re-ask | ✓ |
| UK2 | Multi-level nesting | Round 2 | ✓ |
| UK3 | Migration on first enablement | Round 2 | ✓ |
| UK4 | Discounts parent vs variant | Round 2 | ✓ |
| UK5 | Permissions | Round 2 | ✓ |
| UK6 | Max number of variants per parent | `08-known-limitations.md` | (optional) |
| UK7 | Exact kitchen ticket layout | `08-known-limitations.md` | (optional, could append to Round 2) |
| UK8 | Short Name length/charset limits | `08-known-limitations.md` | — |
| UK9 | Multiple Pre Chosen variants allowed? | `08-known-limitations.md` | — |
| UK10 | Modifier/Color Code behaviour under Parent-Child | `08-known-limitations.md` (narration contradictory) | — |
| UK11 | Import/export/API | `08-known-limitations.md` (explicit out-of-scope) | — |
| UK12 | Localization of Short Name | `08-known-limitations.md` (explicit out-of-scope) | — |

## Provenance statistics

- **Claims with D strength (direct)**: C1, C2, C5, C6a, C12 → 5 / 16 = 31%
- **Claims with D+N strength**: C1, C3, C7, C8, C9 (partial), C13, C15 → 7 / 16 = 44%
- **Combined reliable (D or D+N)**: **12 / 16 = 75%** ≥ 70% target ✅
- **Narrated only**: C4, C6b, C10, C14, C16 → 5 / 16 = 31% (overlaps)
- **Must not publish as stated**: C14 (kitchen format), C16 (color code behaviour)
- **Publish with careful phrasing**: C4 (subcategory constraint), C10 (inheritance), C11 (modifier behaviour structural-only)

## Cross-check against `plan.md` F-list

| F (plan.md) | Matching claim(s) | Status in Source Matrix |
|---|---|---|
| F1 hierarchy | C1, C2 | ✅ |
| F2 two ways to add variant | C3 | ✅ |
| F3 detach origin-dependent | C6a, C6b | ✅ (C6b narrated-only, PO-confirmed) |
| F4 Short Name field | C5 | ✅ |
| F5 reorder | C7 | ✅ |
| F6 pre-chosen | C8 | ✅ |
| F7 price | C9 | ✅ |
| F8 Product Class inherited | C10 | ⚠️ N only |
| F9 modifiers ambiguous | C11, UK10 | 🔴 narration self-contradictory |
| F10 POS display | C12, C13 | ✅ |
| F11 kitchen | C14 | 🔴 N only — do not publish format |
| F12 reports | C15 | ✅ (reframed as composite label) |
| F13 subcategory scope | C4 | ⚠️ N |

## Next deliverable

`07-scope.md` — Scope & Confidence Register (Step 6 of plan). Will place each capability and each unknown into one of three buckets: **in-scope v1 / conditional on Round 2 / out-of-scope v1**. Awaits Maya's Round 2 answers before final lock.
