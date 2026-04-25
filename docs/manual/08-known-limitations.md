<!--
Document type: Diátaxis Reference (information-oriented).
Target length: 80–120 lines.
Sources: docs/ba-artifacts/04-observation-log.md (UK1–UK12), 06-source-matrix.md, 10-rtm.md Part 2.
Style: First-class document (per ISO/IEC/IEEE 26514 safe-scope publication principle), not appendix.
Per user direction (2026-04-25): no Round 2 answers will be sought; UK1–UK5 stay listed here rather than transitioning into Rules.
-->

# Known limitations

This page lists what v1 of the Parent-Child Structure manual **does not cover**. Each entry says what is missing, why we did not document it, and where to look (or whom to ask) for an answer.

We list missing items explicitly rather than leaving them out silently - so that a reader who is testing or supporting the feature knows the boundary between confirmed behaviour and territory we did not verify.

## How to read this page

Each row in the tables below has four columns:

- **Topic** - what the limitation concerns.
- **What is not documented** - the specific gap.
- **Why** - the reason we did not document it (sources are silent, narration self-contradictory, or out of scope for v1).
- **How to find out** - the recommended route to a reliable answer.

---

## Behavioural gaps the source materials do not cover

These items concern behaviours that the screencast and product-owner narration do not demonstrate or describe in enough detail to publish.

| ID | Topic | What is not documented | Why | How to find out |
|---|---|---|---|---|
| UK1 | **Parent-item deletion** - what happens to variants when the parent is deleted | The screencast covers detaching a variant from a parent, not deleting the parent itself. We do not state whether parent deletion cascades to its variants, blocks until the parent is empty, or another rule applies. | Source materials are silent. | Ask the Gen1POS product owner before relying on any specific behaviour. Verify in a test environment before performing the action in production. |
| UK2 | **Multi-level nesting** - whether a variant can itself be the parent of sub-variants | The screencast demonstrates exactly one parent level. We do not document a maximum nesting depth or a rule that disallows nesting. | Source materials are silent. | Same as UK1. |
| UK3 | **Migration of legacy items** - what happens when Parent-Child is enabled for a restaurant that already has items in production | The feature is shown in steady-state on a system that already has Parent-Child active. The before/after migration path is not in the screencast. | Out of scope of the source materials. | Ask the Gen1POS product owner for the migration runbook or release notes. |
| UK4 | **Discounts** - how a discount applies when targeted at a parent vs. at a variant, and which precedence rule wins | Not shown, not narrated. | Source materials are silent. | Ask the Gen1POS product owner. |
| UK5 | **Permissions** - role-based rules for creating, attaching, detaching, or deleting variants | Not shown, not narrated. The screencast assumes an admin role. | Source materials are silent. | Consult the Gen1POS permissions documentation or ask the product owner. |

---

## Constraints not stated in the source

These items concern constraints (limits, formats, edges of fields) that we know the system has - every system has them - but the source materials never quantify.

| ID | Topic | What is not documented | Why | How to find out |
|---|---|---|---|---|
| UK6 | **Maximum number of variants per parent** | Not shown, not narrated. The screencast shows up to three variants on one parent. | Source materials are silent. | Test in a sandbox environment if a high-variant scenario is realistic; otherwise ask the product owner. |
| UK7 | **Exact kitchen ticket layout** | The kitchen ticket is described as receiving the item's full identifying name. The actual ticket - the layout, the wording, line breaks - is not shown anywhere in the source materials. | The kitchen-side image was not part of the screencast. | Inspect a printed kitchen ticket in a test environment that has Parent-Child enabled. The ProductMix report (R6.4) is the closest documented surface and uses a `Parent Name – Short Name Parent Name` composite, but it is not the same surface as the kitchen ticket. |
| UK8 | **`Short Name` length and character constraints** | The screencast enters `5'` (single character + symbol). Maximum length, allowed characters, special handling of Unicode or quotation marks is not specified. | Source materials are silent. | Test in a sandbox environment. |
| UK9 | **Multiple `Pre Chosen` variants on one parent** | The screencast toggles `Pre Chosen` on a single variant. Whether the toggle is mutually exclusive across variants of one parent (forcing exactly one) or independent (allowing more than one) is not stated. | Only one variant was toggled in the source. | Test by toggling `Pre Chosen` on a second variant and observing whether the first toggle remains on. |

---

## Edges where the narration is self-contradictory

Two fields are described in the screencast in language that does not unambiguously translate to a publishable rule.

| ID | Topic | What is not documented | Why | How to find out |
|---|---|---|---|---|
| UK10 | **`Modifiers` and `Color Code` behaviour inside Parent-Child** | The screencast says these fields take effect "outside the parent context". The meaning of "outside" is not defined and the in-context behaviour is not demonstrated. The structural fact that each variant has its own `Modifiers` and `Color Code` field is documented (see [Rules R7, R8](06-reference-rules.md)). The behavioural rule is not. | Narration self-contradictory; in-context behaviour not shown. | Test the variant-level field by changing it on a variant and observing whether the change reaches POS, the order preview, the kitchen ticket, and the ProductMix report. Compare against changing the same field on a standalone item. |

---

## Out of scope for v1 of this manual

These items are deliberately excluded from this v1 manual.

| ID | Topic | Why excluded |
|---|---|---|
| UK11 | **Import / export, API, bulk operations** on Parent-Child | The source materials are an admin-panel screencast. Programmatic interfaces and bulk-operation flows are a different surface and a different audience. They will not be added unless explicitly scoped into a future revision. |
| UK12 | **Localization of `Short Name`** across multi-language menus | Localization is a cross-cutting feature that is out of scope of this Parent-Child-specific manual. Refer to the Gen1POS localization documentation when it covers menu items. |

---

## How to fill these gaps

For any gap above, the resolution path is one of:

1. **Inspect the live system in a test environment** - appropriate for `UK6`, `UK7`, `UK8`, `UK9`, and `UK10` because they are observable behaviours.
2. **Ask the Gen1POS product owner** - appropriate for `UK1`, `UK2`, `UK3`, `UK4`, and `UK5` because they involve product decisions, not just observable behaviour.
3. **Read the relevant out-of-scope documentation** - appropriate for `UK11` (API documentation) and `UK12` (localization documentation).

When a gap is closed, the corresponding row should move out of this file: into [Rules reference](06-reference-rules.md) if it is a rule, into one of the how-to pages if it is a procedure, or into [Glossary](07-reference-glossary.md) if it is a definition.
