<!--
Document type: Diátaxis Reference (information-oriented).
Target length: 100–150 lines.
Source: docs/ba-artifacts/02-glossary.md (working RU↔EN glossary). This file is the EN-only consolidated version for end readers.
Style: Reference-first. Terms grouped by concept / action / field / surface, alphabetical inside each group.
-->

# Glossary

Terms used in the Parent-Child Structure manual. Where a term appears in the Gen1POS UI, the spelling matches the UI label exactly.

Terms covered by the parent Gen1POS admin manual (`Menu`, `Category`, `Item`, `Price`, `Tax`, `SKU`, `Cost`, `Modifiers` in their general sense, etc.) are not repeated here.

## Concepts

| Term | Definition |
|---|---|
| **Parent-Child Structure** | The mechanism that lets a single menu item act as a parent holding one or more child items called variants underneath it. The feature shapes what the cashier sees on POS, what prints to the kitchen, and how sales appear in reports. |
| **Parent item** | A menu item that has at least one variant. Its detail page contains a **Variants** section listing the children. |
| **Variant** | A menu item that belongs to a parent. In this manual, child items are always called **variants** - never "child" - because that is the wording used in the Gen1POS UI and in product-owner communication. |
| **Standalone item** | A menu item with no parent. A standalone item's **Parent Item** field reads `None (Standalone)`. This is the default state of any newly created item before it is attached as a variant. |
| **Subcategory** | A grouping one level below a top-level category, containing items. The same-subcategory rule (R4) restricts which items can act as a parent for a given variant. |

A menu item is in exactly one of three states at any time: **standalone**, **parent**, or **variant**.

## Origin (relevant to detach behaviour)

| Term | Definition |
|---|---|
| **Standalone-origin variant** | A variant that existed in the subcategory as a standalone item before being attached to a parent via the **Parent Item** dropdown. Detaching it returns the item to the subcategory's item list. See [How to attach an existing item](03-howto-attach-existing.md) and [Rules R5](06-reference-rules.md#r5-detach-behaviour-origin-dependent). |
| **Variant-born variant** | A variant that was created with **Add Variant** under a parent and never existed as a standalone item. Detaching it permanently deletes the underlying item. See [How to create a new variant](02-howto-create-variant.md) and [Rules R5](06-reference-rules.md#r5-detach-behaviour-origin-dependent). |

## Actions

| Term | Definition |
|---|---|
| **Add Variant** | The button on a parent item's detail page that creates a new variant under that parent. The created item is variant-born. |
| **Attach (a variant)** | Configure an existing standalone item as a variant of a parent by selecting the parent in the **Parent Item** dropdown on the item's detail page. The result is a standalone-origin variant. |
| **Detach (a variant)** | Remove a variant from a parent. The outcome on the underlying item depends on origin (see Rules R5). The action is initiated by the **X** control next to a variant in the parent's **Variants** section. |
| **Reorder (variants)** | Drag variants in the parent's **Variants** section to change the order in which they appear on POS. |

The term *delete* is avoided for the detach operation because it is ambiguous: detaching a standalone-origin variant does not delete anything, whereas detaching a variant-born variant does.

## Fields

| Term | Definition |
|---|---|
| **Parent Item** (field) | A dropdown on a child item's detail page. In the observed flow, its values are `None (Standalone)` or an item from the same subcategory. Selecting a parent here turns the item into a variant. |
| **Pre Chosen** | A toggle on a variant. When active, that variant is visually pre-selected on POS when the operator opens the parent. Whether more than one variant can be `Pre Chosen` simultaneously is not documented - see [Known limitations](08-known-limitations.md). |
| **Product Class** | A classification field (for example, `Food`). On a variant it is inherited from the parent and displayed at the variant level. |
| **Short Name** | A field that exists only on a variant. Used as the variant-button label on POS, as the second line in the order preview, and as part of the composite label in the ProductMix report. Length and character constraints are not documented - see [Known limitations](08-known-limitations.md). |
| **Modifiers** | A list of optional modifications attached to an item. A variant has its own `Modifiers` list structurally; the interaction between variant-level modifiers and the Parent-Child context is not documented in v1. |
| **Allergens** | Optional allergen tags on an item. Per variant, alongside `Modifiers`. |
| **Color Code** | A display-option field on a variant. The field exists per variant; the effect inside Parent-Child context is not documented in v1. |

## Surfaces (where data appears)

| Term | Definition |
|---|---|
| **Admin panel** | The Gen1POS administration interface where parents and variants are configured. The path to a variant: **Menu** → category → subcategory → parent item → **Variants** section → variant. |
| **POS** (cashier-side) | The interface used by cashiers. A parent on POS opens a row of variant buttons labelled with `Short Name`; the `Pre Chosen` variant is pre-selected. |
| **Order preview** | The order summary of a selected variant in the order in progress: parent name together with the `Short Name` and modifier choices. |
| **Kitchen ticket** | The ticket printed to the kitchen after payment. Receives the item's full identifying name; the exact layout is not documented in v1. |
| **ProductMix** | The reporting view that lists items sold over a time range. Variants appear under a composite label combining the parent name and the `Short Name`. |

## Notifications

| Term | Definition |
|---|---|
| `Product updated` | Confirmation toast shown after saving changes on an item's detail page. |
| `Variant deleted` | Confirmation toast shown when the **X** control on a variant row is used to detach a variant. The notification is the same for both detach branches (standalone-origin and variant-born). |

## See also

- [Rules reference](06-reference-rules.md) - how these terms behave together.
- [Known limitations](08-known-limitations.md) - terms whose behaviour is partially documented are flagged there with the reason.
