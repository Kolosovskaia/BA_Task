<!--
Document type: Meta / navigation page (no Diátaxis slot).
Target length: ≤ 1 screen (~100 lines).
Sources: docs/ba-artifacts/01-task-contract.md (positioning), 03-audience.md (who-for), 08-ia.md (TOC).
-->

# Parent-Child Structure - User Manual

This section of the Gen1POS documentation covers **Parent-Child Structure**: the feature that lets a single menu item act as a parent holding one or more variant items underneath it. The feature affects the admin panel, POS, the order preview, the kitchen ticket, and the ProductMix report.

The pages here extend - they do not replace - the base item configuration described in the parent Gen1POS admin manual. Where a concept (item, modifier, category) is already defined upstream, this manual links out instead of repeating.

## Who this is for

- **Internal testers** verifying that Parent-Child Structure behaves as specified.
- **Team members** who need a working mental model of the feature before reading the procedures.

The manual assumes you can already create and configure a basic menu item in Gen1POS.

## Where to start

| If you want to… | Read this |
|---|---|
| Understand what Parent-Child Structure is and where it shows up | [01-explanation.md](01-explanation.md) |
| Add a brand-new variant under an existing parent | [02-howto-create-variant.md](02-howto-create-variant.md) |
| Turn a standalone item into a variant | [03-howto-attach-existing.md](03-howto-attach-existing.md) |
| Reorder variants and choose a default for POS | [04-howto-reorder-variants.md](04-howto-reorder-variants.md) |
| Remove a variant - and understand the destructive case | [05-howto-remove-variant.md](05-howto-remove-variant.md) |
| Look up a rule (display, inheritance, scope, detach behaviour) | [06-reference-rules.md](06-reference-rules.md) |
| Look up a term | [07-reference-glossary.md](07-reference-glossary.md) |
| Check whether something is documented or deliberately out of scope | [08-known-limitations.md](08-known-limitations.md) |

## Reading order

The pages stand on their own and can be read in any order, but the recommended path for a first read is:

1. [01-explanation.md](01-explanation.md) - five minutes, builds the mental model.
2. The how-to that matches your task (`02`–`05`).
3. [06-reference-rules.md](06-reference-rules.md) when you need to look up an exact rule during testing or support.
4. [08-known-limitations.md](08-known-limitations.md) when you encounter behaviour the how-to does not cover - this page tells you whether the silence is deliberate.

## Conventions

- **UI labels** are written verbatim, in the casing the UI uses (for example, `Add Variant`, `Parent Item`, `Pre Chosen`).
- **Field names** appear in inline code formatting: `Short Name`, `Product Class`.
- **Variants** is the term used throughout. The terms *child* and *child item* are not used in the body of this manual, even though they appear in some background materials, because the UI and the product owner use *variant*.
- **"Not documented in v1"** is an explicit phrase. Wherever you see it, the gap is intentional and is detailed in [08-known-limitations.md](08-known-limitations.md).

## Version

- Manual version: **v1** (first publication).
- Last updated: **2026-04-25**.
- Source materials: a 7-minute screencast walkthrough by the Gen1POS product owner and accompanying transcript. Each claim in the manual is traceable to a screenshot or to product-owner narration; the trace lives in `docs/ba-artifacts/10-rtm.md`.
