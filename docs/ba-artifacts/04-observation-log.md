---
id: 04-observation-log
title: Observation Log — Parent-Child Structure (frame-by-frame)
date: 2026-04-24
sources:
  - docs/video.mp4 (screencast, 7:31)
  - docs/Meeting Recording Transcription.md
  - docs/transcription.srt
  - docs/narrative_film_storyboard-2026-04-24.md (32-shot breakdown)
  - docs/screens_cropped/shot_01.png ... shot_32.png
phase: 2 — Evidence extraction
---

# Observation Log

## Purpose

For every observable action in the video, classify what we actually know vs. what we infer vs. what the source is silent on. This becomes the ground truth for every claim in the final manual (via RTM, Step 10).

## How to read the Confidence column

| Code | Meaning | Example |
|---|---|---|
| **DO** | Direct observation — visible on screen AND reproducible from video alone | "Add Variant button exists on parent's detail page" |
| **NN** | Narrated, not directly verifiable from UI alone | "Product Class is inherited" (said, but not shown being toggled) |
| **IN** | Inference — derived logically from DO/NN but not stated | "Short Name is mandatory on variants (because it always appears)" |
| **UK** | Unknown / silent — relevant for the feature but not in source | "Max nesting depth" |

## Log

| Shot | Timecode | UI action / visible state | Narration (key fragment) | Claim extracted | Confidence | Notes / links |
|:-:|---|---|---|---|:-:|---|
| 3 | 0:03–0:10 | Admin panel, breadcrumb "Menu Categories / Parent_Category / Tarts", item "Almondine Tarte" visible in list | "Это называется parent-child структура" | Feature name is "Parent-Child Structure" and it is configured via admin panel menu | DO+NN | F1 |
| 4 | 0:10–0:24 | Left sidebar "Menu" expanded, revealing categories; main area shows "Tarts" category items | "Заходим на категорию, субкатегорию и сами айтемы" | Navigation path: Menu → Category → Subcategory → Item | DO | F1 |
| 5 | 0:24–0:38 | "Almondine Tarte" detail page, section "Variants" with rows "3″", "8″", "5″ Almondine Tarte" and prices | "Внутри каждого айтема можно настроить варианты, которые являются его children" | A parent item has a "Variants" section listing its children | DO | F1 |
| 6 | 0:38–0:50 | "Add Variant" button visible on detail page | "Можно создавать внутри как add variant новые, либо добавлять существующие" | Two ways to add a variant: create new via Add Variant, or attach existing | DO+NN | F2 |
| 7 | 0:50–1:05 | 'X' clicked next to "5″ Almondine Tarte"; toast "Variant deleted" | "Открепляю какие-то из этих элементов…" | Variant can be removed from parent via 'X' control; system shows a "Variant deleted" toast | DO | F3 |
| 8 | 1:05–1:15 | Back to "Tarts" category list; "5″ Almondine Tarte" now appears as standalone item with $11 | "Появился в списке всех айтемов, как обычный айтем" | When a previously-standalone variant is detached, it returns to the category's item list as a standalone | DO | F3 (happy-path branch A) |
| 9 | 1:15–1:29 | "5″ Almondine Tarte" detail page; `Parent Item` dropdown shows "None (Standalone)" | "Могу обратно добавить через Parent Item" | Standalone item has a `Parent Item` dropdown currently set to `None (Standalone)` | DO | F2 |
| 10 | 1:29–1:40 | `Parent Item` dropdown opens, shows "Almondine Tarte" as option; user selects it | "Здесь можно выбрать любой айтем из данной субкатегории" | `Parent Item` dropdown lists items from the SAME subcategory | DO+NN | F13 — scope constraint |
| 11 | 1:40–1:56 | After selecting parent: `Short Name` field appears, user types `5'`; clicks "Save changes" | "Появляется дополнительное поле — это Short Name" | When an item is attached as a variant, a `Short Name` field becomes visible on its detail page | DO+NN | F4 |
| 12 | 1:56–2:06 | Back on parent "Almondine Tarte" detail; variant list now shows "5″" with Short Name `5'`; toast "Product updated" | "Теперь он отображается как отдельный айтем внутри Almondine Tarte" | Attached variant appears in the parent's Variants section with its Short Name | DO | F4 |
| 13 | 2:06–2:25 | User drags variants to reorder to 5″, 3″, 8″; toggles "Pre Chosen" on 5″; clicks "Save changes" | "Варианты можно двигать, это влияет на то, как они будут отображаться на POS стороне" + "можно выбрать, какие будут Pre Chosen" | Variants are reorderable by drag; one (at least) can be marked Pre Chosen | DO+NN | F5, F6 |
| 14 | 2:25–2:30 | Toast "Product updated" | — | Save acknowledgement | DO | — |
| 15 | 2:30–2:40 | POS interface; "Almondine Tarte" opened; buttons `3'`, `5'`, `8'` appear; `5'` highlighted | "Пятый как сейчас Pre Chosen" | On POS, variants appear as selectable buttons under parent; pre-chosen one is visually highlighted | DO+NN | F6, F10 (partial: POS-level) |
| 16 | 2:40–2:43 | Switch to admin panel tab | — | UI-only transition | DO | — |
| 17 | 2:43–2:55 | "Edit Variant" modal for `3″ Almondine Tarte`; fields `Name`, `Short Name` (3″), `Product class` (Food), Display Configuration (Food) | "Можно менять цену, как у обычного айтема. Product class берётся от родительского айтема" | Variant has its own Price and inherits Product Class from parent | NN (price) + NN (inheritance); Product Class displayed = visible (DO) but inheritance rule itself = NN | F7, F8 |
| 18 | 2:55–3:15 | Scroll to "Customization"; `Modifiers`, `Allergens` dropdowns visible | "Можно независимо добавлять modifiers. Modifier types and allergens" | Variant can have its own Modifiers and Allergens lists | DO (fields exist) + NN (independence from parent) | F9 ambiguous |
| 19 | 3:15–3:33 | Scroll to "Display Options" → `Color code` selector; modal closes | "Color code — влияет на айтем, когда он находится вне родительской категории" | Color code is a display option; narration claims it only affects items outside parent-child context | DO (field exists) + NN (behaviour scope) | Ambiguous: "outside parent category" not rigorously defined |
| 20 | 3:33–3:47 | Back on "Almondine Tarte" detail page | "Parent-Child — новая фича, влияет на все части проекта, на POS сторону…" | Feature is new; affects POS, kitchen, reports | NN | Meta-claim |
| 21 | 3:47–3:54 | POS interface; "Almondine Tarte" variants visible | "Если у айтема parent-child, они появляются как варианты" | On POS, items with Parent-Child appear with their variants as selectable options | DO | F10 |
| 22 | 3:54–4:18 | Navigate to "Cafe Sua Da" on POS; opens parent; variants `Small`, `Large`, `M`; user taps `Small`, then `Coconut Milk`, then `Cold` | "У каждого разные эмоции (sic: modifiers), которые можно настроить индивидуально" | Another example of parent with variants (Small/Large/M); each variant can have its own modifier choices at purchase time | DO+NN | Corroborates F6, adds M-variant (=Medium?) |
| 23 | 4:18–4:34 | Order preview shows "Cafe Sua Da Small" with "Coconut Milk Cold" underneath; clicks "Add to Order" | "Отображается parent-имя и рядом внизу Short Name" | Order line displays parent name + variant short name (two-line format) | DO+NN | F10 |
| 24 | 4:34–4:49 | Payment screen; selects `Cash`, inputs `20.00`, clicks `Pay`; "Payment successful" dialog | "На заказе на кухню появится полностью название айтема" | Kitchen receives the item with "full name"; semantics of "full name" NOT verifiable from this shot (no kitchen ticket image) | NN only | G7 — kitchen ticket format not shown |
| 25 | 4:49–4:56 | Admin panel; clicks "Reporting" | "Название айтема влияет на то, как оно отображается в репортах" | Reports reflect item naming; specifically linked to Parent-Child concept | NN | — |
| 26 | 4:56–5:12 | ProductMix report; pie charts; date range opened; "Today" selected and Applied | "Здесь можно посмотреть, какие айтемы проданы. Когда продаётся какой-то из вариантов внутри парента…" | ProductMix is the report used; it filters by date range | DO | — |
| 27 | 5:12–5:20 | Report updated; chart shows "Cafe Sua Da – Small Cafe Sua Da" | "Его вариативное имя, а не имя его parent'а" | Report displays the variant's name, not the parent's | DO+NN | F12 — but label format "Cafe Sua Da – Small Cafe Sua Da" suggests parent+short composite, not short alone. Internal contradiction with "not parent name". |
| 28 | 5:20–5:34 | Hovering pie chart segment shows "Cafe Sua Da – Small Cafe Sua Da" | "При наведении будет его вариативное имя" | Hover tooltip shows the same composite label | DO | Reinforces composite format observation |
| 29 | 5:34–6:26 | Custom date range set to narrow window; report now shows only `Cafe Sua Da – Small Cafe Sua Da` | "Отображается Cafe Sua Da и его короткое имя. Вижу полностью его имя, как оно есть" | Filtering to specific window isolates the variant; Maya calls the composite label both "variant name" and "full name with short name" | DO+NN | Strong evidence that "variant name" in ProductMix = `Parent Name – Short Name Parent Name` (repeated). Needs glossary consolidation. |
| 30 | 6:26–6:37 | Back to admin; "Tarts" → "Almondine Tarte" detail | — | Navigation only | DO | — |
| 31 | 6:37–7:16 | Points at 'X' next to variants, re-explains delete logic | "Если айтем ранее существовал как отдельный — вернётся в своё состояние. Если создан именно как вариант — исчезает и не появляется в списке" | Delete/detach logic restated: origin-dependent — standalone-origin → reverts to standalone; variant-born → disappears | NN only (not re-demonstrated for the variant-born case) | F3 happy-path branch B — Maya confirmed Round 1 this is part of functionality |
| 32 | 7:16–7:31 | Outro branding screen | "На этом всё" | End | DO | — |

## Derived claims (extracted and de-duplicated)

| ID | Claim | Confidence | Source shots |
|---|---|:-:|---|
| C1 | Feature is called "Parent-Child Structure"; configured in admin panel under Menu → Category → Subcategory → Item | DO+NN | 3, 4 |
| C2 | A parent item has a "Variants" section listing its children | DO | 5, 12 |
| C3 | Two ways to add a variant to a parent: (a) Add Variant button (create new), (b) via `Parent Item` dropdown on an existing item | DO+NN | 6, 9, 10 |
| C4 | `Parent Item` dropdown lists items from the SAME subcategory only | NN | 10 |
| C5 | When an item is attached as a variant, a `Short Name` field becomes visible on its detail page | DO | 11, 12 |
| C6 | Detach behaviour is origin-dependent: standalone-origin → returns to item list; variant-born → disappears | DO (branch A) + NN (branch B) | 7, 8, 31 |
| C7 | Variants are reorderable by drag; order affects POS display | DO+NN | 13, 15 |
| C8 | A variant can be marked Pre Chosen; on POS it is visually pre-selected | DO+NN | 13, 15 |
| C9 | Variant has its own Price | NN | 17 |
| C10 | Variant inherits Product Class from parent (not editable at variant level) | NN | 17 |
| C11 | Variant has independent Modifiers and Allergens | DO (fields present) + NN (independence rule) | 18 |
| C12 | POS shows variants as tappable buttons labeled with Short Name under the parent | DO | 15, 21, 22 |
| C13 | Order preview shows `parent name` + `short name` in two-line format | DO+NN | 23 |
| C14 | Kitchen ticket shows the "full name" of the item — exact format NOT visible in video | NN only | 24 |
| C15 | ProductMix report displays a composite label `Parent Name – Short Name Parent Name` for sold variants | DO+NN | 27, 28, 29 |
| C16 | Variant's Color code display option "only affects item outside parent-child context" | NN | 19 |

## Unknowns (UK) — will map to `08-known-limitations.md`

| UK | Topic | Why we don't know |
|---|---|---|
| UK1 | What happens to variants when the PARENT item is deleted | Not shown, not narrated — real "cascade delete" question |
| UK2 | Whether a variant can itself become a parent (max nesting depth) | Not shown, not narrated |
| UK3 | Migration behaviour on first enablement for a restaurant with legacy items | Not relevant in video (feature already in prod) |
| UK4 | How discounts apply at parent vs. variant level | Not shown, not narrated |
| UK5 | Role-based permissions for create/detach/delete | Not shown, not narrated |
| UK6 | Maximum number of variants a parent can hold | Not shown |
| UK7 | Exact kitchen ticket format (C14) | Not shown (only narrated as "full name") |
| UK8 | Whether `Short Name` has length/charset constraints | Not shown, not narrated |
| UK9 | Whether more than one variant can be Pre Chosen simultaneously | Only one shown being toggled |
| UK10 | Modifier behaviour INSIDE parent-child context (narration F9 ambiguously says they "affect item when outside") | Narration self-contradictory |
| UK11 | Import/export, API, bulk-operations | Not covered by screencast |
| UK12 | Localization of `Short Name` across language menus | Not covered |

## Internal contradictions spotted

1. **"Variant name" vs "Parent Name + Short Name"** (shots 27–29 vs shot 23). Maya says in reports it's the variant name, "not the parent", but the visible label is `Cafe Sua Da – Small Cafe Sua Da`, which contains parent twice. Resolution: **treat "variant name" as a composite label rather than a standalone field**. Document as such, flag in glossary.

2. **Color code and Modifiers "outside parent-child"** — narration repeats this phrase, but the meaning of "outside" is never defined. Resolution: document observable (field exists; inheritance rule not asserted) and flag UK10 for limitations.

## Provenance statistics

- Total distinct claims: 16 (C1–C16) + 12 unknowns (UK1–UK12)
- Direct observation (DO or DO+NN): 12 / 16 ≈ **75%** — meets Phase 2 DoD (≥70% direct in confirmed scope).
- Narrated only (NN): 4 / 16 (C4, C9, C10, C14, C16) — flagged accordingly in Source Matrix.
