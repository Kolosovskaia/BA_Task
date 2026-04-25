# Annotation Plan

Table-driven plan for manual screenshot annotation. The goal is to define **what each image should communicate** before generating any overlay.

## Rules

- Prefer **numbered callouts + bottom legend** over large boxes painted across the interface.
- Use a box only to indicate the exact actionable area.
- Place badges in nearby whitespace, not on top of text or controls.
- If a source frame does not clearly show the claimed result, flag it and replace the shot instead of forcing an annotation.

## Shot Map

| Shot | Manual usage | What the reader must notice | Planned annotation | Frame quality note |
|---|---|---|---|---|
| `shot_03` | `01-explanation` opening illustration | Where Parent-Child lives in admin and which row is the parent item | `1` breadcrumb path, `2` parent row `Almondine Tarte` | Usable |
| `shot_05` | `01-explanation`, `02-howto-create` step context | The `Variants` section on the parent page | `1` variants card on the right | Usable |
| `shot_06` | `02-howto-create` step 3 | The `Add Variant` button | `1` button only | Sample-ready |
| `shot_07` | `05-howto-remove` step 3 | The `X` control on the variant row | `1` X icon on the target row | Usable |
| `shot_08` | `03-howto-attach` start state, `05-howto-remove` outcome | The standalone item in the list | `1` item row `5" Almondine Tarte` | Usable |
| `shot_09` | `03-howto-attach` step 2 | `Parent Item = None (Standalone)` | `1` Parent Item field | Usable |
| `shot_10` | `03-howto-attach` step 3 | Opened `Parent Item` dropdown with the parent option | `1` dropdown field, `2` option `Almondine Tarte` | Usable |
| `shot_11` | `02-howto-create` step 5, `03-howto-attach` step 4 | The `Short Name` field that appears for a variant | `1` Short Name label + input | Sample-ready |
| `shot_12` | previously used as expected result in `02` and `03` | Source frame actually shows `Edit Variant` modal, not the final row in the list | Retire from publish set; replaced by `shot_33` | Retired |
| `shot_13` | `04-howto-reorder` | Reorder area, `Pre Chosen` toggle, and final `Save changes` action | `1` variants list for drag ordering, `2` Pre Chosen toggle, `3` Save changes button | Sample-ready |
| `shot_15` | `04-howto-reorder` verification, `06-reference-rules` POS | POS variant buttons and selected default variant | `1` variant button group, `2` highlighted pre-selected option | Usable |
| `shot_17` | `06-reference-rules` R3 | Inherited `Product class` field in the modal | `1` Product class field | Usable |
| `shot_18` | `06-reference-rules` R7 | Variant-level `Modifiers` dropdown is clearly visible | `1` Modifiers field + open dropdown | Usable, but weaker for Allergens |
| `shot_19` | `06-reference-rules` R8 | `Color code` selector in Display Options | `1` Color code selector | Usable |
| `shot_23` | `06-reference-rules` R6.2 | The selected variant summary on POS before adding to order | `1` summary chips at the top | Usable, but wording should be checked when manual is updated |
| `shot_27` | previously used as `06-reference-rules` R6.4 | Source frame does not clearly expose the composite variant label from the report | Retire from publish set; replaced by `shot_34` | Retired |
| `shot_31` | `05-howto-remove` branch B | The same `X` control for variant-born removal | `1` X icon on the variant row | Usable |
| `shot_33` | replacement for `shot_12` expected result | Final parent page after save, with the `Variants` list visible | `1` visible rows in the `Variants` section | Replacement-ready |
| `shot_34` | replacement for `shot_27` ProductMix evidence | Filtered ProductMix report with readable composite label | `1` date filter, `2` composite label in chart legend | Replacement-ready |

## Immediate follow-up

1. Validate the new visual style on `shot_06`, `shot_11`, and `shot_13`.
2. Keep `shot_18` under review if we want a frame that proves both `Modifiers` and `Allergens` in one image.
3. After approval, update manual references and generate publish assets in one pass.

## Problem Frames Explained

### `shot_12` - why the current frame does not match the text

Where the mismatch is now:

- [09-shotlist.md](../../ba-artifacts/09-shotlist.md) says this shot should show the **expected result** after saving.
- [02-howto-create-variant.md](../02-howto-create-variant.md) says the new variant appears in the parent's `Variants` list and the user sees `Product updated`.
- [03-howto-attach-existing.md](../03-howto-attach-existing.md) says the attached item now appears inside the parent's `Variants` section.

What the actual frame shows:

- the `Edit Variant` modal is still open;
- the `Variants` list is partially hidden behind the modal;
- the frame does **not** cleanly show the final post-save state that the caption promises.

Why this matters:

- the reader is told "this is what success looks like";
- the image instead shows an intermediate state inside editing, not the final result on the parent page.

Recommended replacement:

- use a **new extracted frame** from the source video around `00:02:05` (final replacement: `shot_33.png`);
- this replacement clearly shows the parent page with the full `Variants` list visible;
- it matches the statement "the item appears in the Variants list" much better than the current `shot_12`.

Important nuance:

- if we want to prove the toast `Product updated`, use a separate nearby frame where the toast is visible and the modal is already closed;
- therefore the better documentation choice is:
  - either use `shot_33.png` and keep the toast only in text,
  - or extract one more frame a fraction later where both the parent page and the toast are still visible.

### `shot_27` - why the current frame does not match the ProductMix claim

Where the mismatch is now:

- [09-shotlist.md](../../ba-artifacts/09-shotlist.md) says this shot is visual evidence for the ProductMix composite variant label.
- [06-reference-rules.md](../06-reference-rules.md) says the image shows a sold variant under a composite label with parent name + `Short Name`.

What the actual frame shows:

- generic ProductMix charts with many unrelated items;
- no readable `Cafe Sua Da - Small Cafe Sua Da` label;
- no isolated proof of the Parent-Child naming rule.

Why this matters:

- the caption claims the image resolves the naming ambiguity;
- the frame itself does not resolve anything, because the needed label is simply not visible there.

Recommended replacement:

- use a **new extracted frame** from the source video around `00:06:20` (final replacement: `shot_34.png`);
- this replacement shows the narrowed report window after filtering;
- the legend clearly reads `Cafe Sua Da - Small Cafe Sua Da`;
- that is exactly the rule the manual is trying to prove.

Why not reuse the current `shot_28` or `shot_29` as-is:

- current `shot_28.png` shows a tooltip for `Tea Set, Butterfly Duplicated`, which is unrelated to the Parent-Child example;
- current `shot_29.png` still shows generic charts and does not isolate the target composite label;
- therefore both are weaker evidence than the newly extracted `00:06:20` frame.

## Recommended replacement strategy

To keep traceability clean, do **not** silently overwrite the meaning of the old source frames.

Preferred approach:

1. Add new source screenshots extracted from the video for the corrected frames.
2. Update `09-shotlist.md` and manual links to those new files.
3. Annotate only after the source frame itself is semantically correct.

Suggested new files:

- `shot_33.png` - parent page with visible final `Variants` list after save, for the current `shot_12` role.
- `shot_34.png` - ProductMix filtered frame with visible `Cafe Sua Da - Small Cafe Sua Da`, for the current `shot_27` role.
