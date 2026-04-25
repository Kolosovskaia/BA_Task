# Skill: Manual Screenshot Processing And Annotation

## Purpose

Turn raw UI screenshots into publish-ready manual images with precise callouts that help the reader find the right control immediately.

Use this skill when a documentation set includes screenshots and the caption alone is not enough to locate the target action, field, or state.

## Related skill

- For frame extraction and crop from video, use [skill_video_to_manual_screens.md](skill_video_to_manual_screens.md).

## Required inputs

- Source screenshots in a stable cropped archive such as `docs/screens_cropped/`.
- Target markdown files that will reference the images.
- A shot map that says:
  - which doc uses each shot;
  - what the reader must notice;
  - whether the current source frame is semantically correct.
- Output directory for publish assets, for example `docs/manual/_assets/`.

## Default output

- Publish-ready `PNG` screenshots with lightweight annotations.
- Stable publish filenames in the manual, ideally `shot_XX.png`.
- One machine-editable annotation spec such as `callouts.yaml`.
- One renderer script such as `render_callouts.py`.

## Workflow

### 1. Validate the source frame before annotating

- Do not start from drawing boxes.
- First confirm that the frame actually proves the caption.
- If the frame shows an intermediate state, wrong report filter, hidden modal, or unreadable label, replace the frame first.
- Prefer adding a new shot number over silently reinterpreting an old bad frame.

### 2. Build a table-driven shot map

For each shot, record:

- shot id;
- manual usage;
- what the reader must notice;
- planned annotation;
- frame quality note.

This table is the decision layer. It prevents random visual edits and helps reviewers discuss the screenshot semantically, not pixel-by-pixel.

### 3. Prefer bounded callouts over heavy overlays

Recommended style:

- thin red rounded rectangle around the exact actionable area;
- numbered badge placed in whitespace, not on top of the UI text;
- short bottom legend matching the badge number.

Avoid:

- giant panel-wide boxes;
- OCR-first pipelines on dense admin screens;
- arrows or labels that cover the UI text the reader must read.

### 4. Keep source and publish assets separate

- Keep the cropped source archive untouched.
- Render annotated images into a separate publish path.
- Once approved, copy the approved annotated PNG into the stable publish filename used by markdown.

This keeps markdown simple while allowing multiple review iterations.

### 5. Update markdown only after the image itself is correct

- If a source frame was replaced, update shot numbers across:
  - manual docs;
  - shot list;
  - observation log;
  - RTM;
  - any other BA artifacts that still name the old shot.
- If the filename stays stable, markdown may not need further edits.

### 6. Validate links and cleanup

Before finishing:

- check that every markdown image link resolves to an existing file;
- check that internal markdown links still resolve after edits;
- remove review-only images, candidate sheets, grids, and other temporary visuals;
- keep only the source archive, publish assets, and the reusable annotation spec / renderer.

## Decision rules

- Replace the frame before drawing a box if the screenshot does not prove the claim.
- Use one precise box per user-visible point whenever possible.
- Expand the box only enough to include the label or field name; do not cover it.
- If a caption mentions the parent name plus chips or modifiers, the box must include all of them.
- If the badge starts causing clutter, move the badge, not the box.
- If a screenshot remains hard to annotate cleanly after several adjustments, reconsider the source frame.

## Publish checklist

- Source frame is semantically correct.
- Annotation points to the exact target.
- Caption matches what is visibly highlighted.
- Manual references the current shot number.
- Publish PNG exists in `_assets/`.
- Review-only images are deleted when no longer needed.

## Common failures

### Caption says one thing, screenshot shows another

Cause:

- wrong frame chosen.

Fix:

- replace the frame; do not compensate with a more complicated annotation.

### The box covers the label it is supposed to explain

Cause:

- top border too low or box too large.

Fix:

- raise the top border or tighten the box before changing anything else.

### The badge is correct but the box still feels wrong

Cause:

- the box is centered on whitespace, not on the actual control or text.

Fix:

- re-anchor the box to the UI hotspot first, then reposition the badge.

### Publish assets drift away from review assets

Cause:

- review PNG approved, but `_assets/shot_XX.png` not updated.

Fix:

- copy approved annotated PNG into the stable publish path before closing the task.

## Recommended repo artifacts

- `docs/manual/_assets/callouts.yaml`
- `docs/manual/_assets/render_callouts.py`
- `docs/skill_video_to_manual_screens.md`
- this file: `docs/skill_manual_image_annotation.md`
