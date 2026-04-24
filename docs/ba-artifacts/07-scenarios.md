---
id: 07-scenarios
title: Scenario Catalogue — Parent-Child Structure
date: 2026-04-24
derived_from:
  - 03-audience.md
  - 05-capability-map.md
phase: 3 — Scope lock & IA (partial — independent of Round 2)
---

# Scenario Catalogue

## Purpose

Translate capabilities (CAP-1…CAP-12) into **user scenarios** that feed directly into how-to drafts (Step 12) and align with the audience's jobs-to-be-done (`03-audience.md`).

## Scope

- **Included**: 5 happy-path scenarios covering CAP-1, CAP-2, CAP-4, CAP-5 (+ Short Name as step within create/attach).
- **Excluded from scenarios** (but documented in Reference, Step 13): CAP-3 stand-alone (Short Name as a field), CAP-6 (variant-level field configuration — already covered by parent-manual item config), CAP-7 (Product Class inheritance — system behaviour, not user action), CAP-8–11 (display / reporting — reader-observed behaviour, not a flow), CAP-12 (subcategory scope — a constraint surfaced in SC-2).

## Scenario format

Each scenario uses the pattern from *Google Developer Docs Style Guide* and *Microsoft Writing Style Guide* procedure writing:

- **ID** — stable identifier for cross-linking.
- **Name** — imperative, in the reader's voice.
- **Actor** — the role performing the action in production.
- **User goal (JTBD)** — what the user wants to accomplish.
- **Trigger** — what starts the flow.
- **Preconditions** — state that must be true before.
- **Main flow** — numbered steps in imperative mood.
- **Expected result** — success criteria, observable.
- **Alternative / branches** — edge branches within happy path.
- **Evidence** — source shot(s) and capability mapping.
- **Target doc** — where this scenario lives in `docs/manual/`.

---

## SC-1. Create a new variant under a parent item

- **Actor**: Admin (configures menu).
- **User goal**: Add a new size/option (e.g., `5"`) of an existing menu item as a variant under its parent (e.g., `Almondine Tarte`).
- **Trigger**: Admin decides to offer a new option of an item that is not already in the menu.
- **Preconditions**:
  - A candidate parent item exists in a subcategory.
  - Admin has access to the item's detail page.
- **Main flow**:
  1. Open the parent item's detail page (Menu → Category → Subcategory → Item).
  2. Locate the **Variants** section.
  3. Click **Add Variant**.
  4. Enter the variant's `Name` and other details.
  5. Enter a `Short Name` (e.g., `5"`).
  6. Save changes.
- **Expected result**:
  - The new variant appears in the parent's **Variants** list with its `Short Name`.
  - A `Product updated` notification is shown.
  - The variant is **variant-born** (see SC-5, branch B).
- **Alternative / branches**: none in happy path.
- **Evidence**: CAP-1; shots 5, 6, 11, 12.
- **Target doc**: `docs/manual/02-howto-create-variant.md`.

---

## SC-2. Attach an existing standalone item as a variant

- **Actor**: Admin.
- **User goal**: Turn an existing standalone item (e.g., a separate `5" Almondine Tarte`) into a variant under an existing parent (e.g., `Almondine Tarte`).
- **Trigger**: Admin wants to consolidate similar items under one parent.
- **Preconditions**:
  - Both items exist **in the same subcategory** (scope constraint — CAP-12).
  - The item to attach is currently **standalone** (its `Parent Item` field = `None (Standalone)`).
- **Main flow**:
  1. Open the standalone item's detail page.
  2. Open the **Parent Item** dropdown.
  3. Select the target parent from the list.
  4. When the `Short Name` field appears, enter a value (e.g., `5"`).
  5. Save changes.
- **Expected result**:
  - The item becomes a variant of the selected parent.
  - On the parent's detail page, it now appears in the **Variants** list with its `Short Name`.
  - The item is **standalone-origin** (see SC-5, branch A).
- **Alternative / branches**:
  - If no candidate parent exists in the subcategory, the dropdown will be effectively empty (verify in Observation Log / UI test — flagged).
- **Evidence**: CAP-2, CAP-12; shots 9, 10, 11.
- **Target doc**: `docs/manual/03-howto-attach-existing.md`.

---

## SC-3. Reorder variants and set a pre-chosen default

- **Actor**: Admin.
- **User goal**: Control how variants are presented to the cashier on POS — both the order and which one is selected by default.
- **Trigger**: Admin wants to surface variants in a meaningful order (e.g., by size) and nominate a default choice.
- **Preconditions**:
  - Parent has at least two variants (for reorder to be meaningful); at least one variant (for pre-chosen).
- **Main flow**:
  1. Open the parent item's detail page.
  2. In the **Variants** section, drag variants to the desired order.
  3. Toggle **Pre Chosen** on the variant that should be pre-selected on POS.
  4. Save changes.
- **Expected result**:
  - On POS, under this parent, variants appear in the saved order.
  - The variant with **Pre Chosen** toggled is visually pre-selected when the operator opens the parent (CAP-8).
- **Alternative / branches**: none in happy path; **UK9** flags the question of whether multiple pre-chosen is allowed.
- **Evidence**: CAP-4, CAP-8; shots 13, 15.
- **Target doc**: `docs/manual/04-howto-reorder-variants.md`.

---

## SC-4. Verify a Pre Chosen variant on POS

- **Actor**: Admin (verifying post-setup) or tester.
- **User goal**: Confirm that the admin-side configuration is correctly reflected on the customer-facing side.
- **Trigger**: After saving variants and pre-chosen, validate the POS outcome.
- **Preconditions**: SC-3 completed for a parent.
- **Main flow**:
  1. Switch to the POS interface.
  2. Navigate to the category that contains the parent.
  3. Tap the parent item.
  4. Observe the variant buttons.
- **Expected result**:
  - Variant buttons appear labelled with `Short Name`, in the saved order.
  - The **Pre Chosen** variant is visually pre-selected.
- **Alternative / branches**: none.
- **Evidence**: CAP-8; shots 15, 21, 22.
- **Target doc**: `docs/manual/04-howto-reorder-variants.md` (as **Verification** section).
- **Note**: This is a verification micro-scenario used within SC-3's how-to, not a standalone file.

---

## SC-5. Remove a variant from a parent

- **Actor**: Admin.
- **User goal**: Detach a variant from its parent (e.g., a size is being discontinued from the variant list, but may need to remain as a standalone item).
- **Trigger**: Admin wants to remove a variant from the Variants list.
- **Preconditions**: Parent has at least one variant.
- **Main flow**:
  1. Open the parent item's detail page.
  2. In the **Variants** section, click the **X** next to the variant to remove.
  3. Confirm if prompted (confirmation modal not observed in source — verify when writing how-to).
- **Expected result — branch-dependent**:
  - **Branch A — standalone-origin variant** (attached via SC-2): The item returns to the subcategory's item list as a standalone. Its `Parent Item` field resets to `None (Standalone)`.
  - **Branch B — variant-born variant** (created via SC-1): The item disappears entirely. It does NOT appear in the subcategory's item list. This is irreversible.
- **System feedback**: A `Variant deleted` notification is shown.
- **Evidence**: CAP-5; shots 7, 8, 31; PO Round 1 re-confirmation (docs/po-answers-2026-04-24.md, Q-3).
- **Target doc**: `docs/manual/05-howto-remove-variant.md` + summary table duplicated in `06-reference-rules.md` (detach behaviour).
- **Risk note**: Branch B is destructive. The how-to must prominently warn readers: *"If the variant was created directly via Add Variant, removing it permanently deletes the item."*

---

## Scenario-to-capability coverage

| Scenario | Capabilities used |
|---|---|
| SC-1 | CAP-1, CAP-3 (Short Name) |
| SC-2 | CAP-2, CAP-3, CAP-12 |
| SC-3 | CAP-4 |
| SC-4 | CAP-8 |
| SC-5 | CAP-5 |

**Not covered by scenarios** (deliberately, go to Reference):

- CAP-6 (variant-level field configuration) — same pattern as parent item; link to parent manual.
- CAP-7 (Product Class inheritance) — system rule; stated in Reference.
- CAP-9 (Order preview) — observable behaviour; documented in Reference (Display matrix).
- CAP-10 (Kitchen ticket) — narrated-only, see Source Matrix C14 warning.
- CAP-11 (ProductMix label) — reporting behaviour; Reference.
- CAP-12 (Subcategory scope) — constraint surfaced in SC-2; also a row in Reference (Rules).

## Pending Round 2 scenarios

If any Round 2 answer promotes an edge-case into v1 scope, the following new scenarios may emerge:

- **SC-R2a (conditional)**: Delete a parent item → outcome for its variants (if Maya elects to document parent-deletion cascade). Target: new how-to or a section in `05-howto-remove-variant.md`.
- **SC-R2b (conditional)**: Migrate legacy standalone items into Parent-Child (if migration in scope). Target: its own how-to.
- **SC-R2c (conditional)**: Configure a discount that applies across parent and variants (if discount semantics in scope). Target: Reference rule + possibly a short how-to snippet.

Permissions (UK5) and multi-level nesting (UK2) most likely become **Reference rules** (not scenarios) even if in-scope.
