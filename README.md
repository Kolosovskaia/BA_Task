# Gen1POS Parent-Child Structure Documentation Pack

<table>
  <tr>
    <td valign="top" width="50%">
      <strong>What this repository is</strong><br>
      A complete documentation pack for the Gen1POS <strong>Parent-Child Structure</strong> feature: final user manual, BA evidence trail, source materials, and the workflow notes used to build annotated screenshots.
    </td>
    <td valign="top" width="50%">
      <strong>What has been done</strong><br>
      The repository preserves the full chain from source video to publishable manual: planning, evidence extraction, scope decisions, traceability, QA, review, and screenshot-processing instructions.
    </td>
  </tr>
</table>

## Start Here

| If you want to... | Open this file |
|---|---|
| Read the final manual from the top | [docs/manual/00-index.md](docs/manual/00-index.md) |
| Review the whole BA evidence trail | [docs/ba-artifacts/00-README.md](docs/ba-artifacts/00-README.md) |
| See the governing implementation plan | [docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md](docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md) |
| Inspect the main source transcript | [docs/Meeting Recording Transcription.md](docs/Meeting%20Recording%20Transcription.md) |
| Understand how screenshots were extracted and annotated | [docs/skill_video_to_manual_screens.md](docs/skill_video_to_manual_screens.md) and [docs/skill_manual_image_annotation.md](docs/skill_manual_image_annotation.md) |

## Repository Glossary

| Term | Meaning | Full reference |
|---|---|---|
| **Parent-Child Structure** | A feature that lets one menu item act as a parent and hold variants under it. | [docs/manual/07-reference-glossary.md](docs/manual/07-reference-glossary.md) |
| **Parent item** | An item whose detail page contains a `Variants` section. | [docs/manual/07-reference-glossary.md](docs/manual/07-reference-glossary.md) |
| **Variant** | A child item that belongs to a parent. | [docs/manual/07-reference-glossary.md](docs/manual/07-reference-glossary.md) |
| **Standalone item** | An item with no parent; its `Parent Item` value is `None (Standalone)`. | [docs/manual/07-reference-glossary.md](docs/manual/07-reference-glossary.md) |
| **Short Name** | Variant-only label used on POS and in reporting surfaces. | [docs/manual/07-reference-glossary.md](docs/manual/07-reference-glossary.md) |
| **Pre Chosen** | Variant toggle that makes one POS option appear pre-selected. | [docs/manual/07-reference-glossary.md](docs/manual/07-reference-glossary.md) |
| **Standalone-origin variant** | A variant created by attaching an existing standalone item to a parent. | [docs/manual/07-reference-glossary.md](docs/manual/07-reference-glossary.md) |
| **Variant-born variant** | A variant created directly inside a parent via `Add Variant`. | [docs/manual/07-reference-glossary.md](docs/manual/07-reference-glossary.md) |

## Suggested Reading Paths

### Fast product view

1. [docs/manual/00-index.md](docs/manual/00-index.md)
2. [docs/manual/01-explanation.md](docs/manual/01-explanation.md)
3. One or more how-to pages in [docs/manual/02-howto-create-variant.md](docs/manual/02-howto-create-variant.md), [docs/manual/03-howto-attach-existing.md](docs/manual/03-howto-attach-existing.md), [docs/manual/04-howto-reorder-variants.md](docs/manual/04-howto-reorder-variants.md), [docs/manual/05-howto-remove-variant.md](docs/manual/05-howto-remove-variant.md)
4. [docs/manual/06-reference-rules.md](docs/manual/06-reference-rules.md)
5. [docs/manual/08-known-limitations.md](docs/manual/08-known-limitations.md)

### Full BA traceability view

1. [docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md](docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md)
2. [docs/ba-artifacts/00-README.md](docs/ba-artifacts/00-README.md)
3. [docs/ba-artifacts/04-observation-log.md](docs/ba-artifacts/04-observation-log.md)
4. [docs/ba-artifacts/06-source-matrix.md](docs/ba-artifacts/06-source-matrix.md)
5. [docs/ba-artifacts/09-shotlist.md](docs/ba-artifacts/09-shotlist.md)
6. [docs/ba-artifacts/10-rtm.md](docs/ba-artifacts/10-rtm.md)
7. [docs/ba-artifacts/11-qa-checklist.md](docs/ba-artifacts/11-qa-checklist.md)
8. [docs/ba-artifacts/12-review-log.md](docs/ba-artifacts/12-review-log.md)

## Repository Map

<details open>
  <summary><strong>Final Manual</strong></summary>

- [docs/manual/00-index.md](docs/manual/00-index.md) - entry page for the manual.
- [docs/manual/01-explanation.md](docs/manual/01-explanation.md) - feature concept and mental model.
- [docs/manual/02-howto-create-variant.md](docs/manual/02-howto-create-variant.md) - create a new variant.
- [docs/manual/03-howto-attach-existing.md](docs/manual/03-howto-attach-existing.md) - attach an existing item as a variant.
- [docs/manual/04-howto-reorder-variants.md](docs/manual/04-howto-reorder-variants.md) - reorder variants and set a default.
- [docs/manual/05-howto-remove-variant.md](docs/manual/05-howto-remove-variant.md) - remove a variant, including the destructive case.
- [docs/manual/06-reference-rules.md](docs/manual/06-reference-rules.md) - rules reference.
- [docs/manual/07-reference-glossary.md](docs/manual/07-reference-glossary.md) - end-reader glossary.
- [docs/manual/08-known-limitations.md](docs/manual/08-known-limitations.md) - documented gaps and out-of-scope items.

</details>

<details>
  <summary><strong>BA Artifacts and Traceability Pack</strong></summary>

- [docs/ba-artifacts/00-README.md](docs/ba-artifacts/00-README.md) - reader's guide for the BA folder.
- [docs/ba-artifacts/01-task-contract.md](docs/ba-artifacts/01-task-contract.md) - scope, audience, language, and delivery agreement.
- [docs/ba-artifacts/02-glossary.md](docs/ba-artifacts/02-glossary.md) - RU to EN glossary normalization.
- [docs/ba-artifacts/03-audience.md](docs/ba-artifacts/03-audience.md) - audience and jobs-to-be-done.
- [docs/ba-artifacts/04-observation-log.md](docs/ba-artifacts/04-observation-log.md) - shot-by-shot evidence extraction.
- [docs/ba-artifacts/05-capability-map.md](docs/ba-artifacts/05-capability-map.md) - feature capabilities.
- [docs/ba-artifacts/06-source-matrix.md](docs/ba-artifacts/06-source-matrix.md) - source-strength and publication posture matrix.
- [docs/ba-artifacts/07-scenarios.md](docs/ba-artifacts/07-scenarios.md) - task scenarios that became how-to pages.
- [docs/ba-artifacts/08-ia.md](docs/ba-artifacts/08-ia.md) - information architecture for the final manual.
- [docs/ba-artifacts/09-shotlist.md](docs/ba-artifacts/09-shotlist.md) - screenshot routing and captions.
- [docs/ba-artifacts/10-rtm.md](docs/ba-artifacts/10-rtm.md) - requirements traceability matrix.
- [docs/ba-artifacts/11-qa-checklist.md](docs/ba-artifacts/11-qa-checklist.md) - internal QA checklist.
- [docs/ba-artifacts/12-review-log.md](docs/ba-artifacts/12-review-log.md) - self walkthrough and fix log.

</details>

<details>
  <summary><strong>Planning, Source Materials, and Context</strong></summary>

- [docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md](docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md) - end-to-end implementation plan.
- [docs/Meeting Recording Transcription.md](docs/Meeting%20Recording%20Transcription.md) - normalized transcript of the source recording.
- [docs/narrative_film_storyboard-2026-04-24.md](docs/narrative_film_storyboard-2026-04-24.md) - film-style storyboard.
- [docs/product_commercial_storyboard-2026-04-24.md](docs/product_commercial_storyboard-2026-04-24.md) - commercial-style storyboard.
- [docs/po-answers-2026-04-24.md](docs/po-answers-2026-04-24.md) - PO answers used during drafting.
- [docs/po-round2-clarifications-2026-04-24.md](docs/po-round2-clarifications-2026-04-24.md) - preserved clarification file from the wider exploration.
- [docs/plan.md](docs/plan.md) - earlier BA analysis and hypothesis document.
- [docs/conversation_context_parent_child_manual.md](docs/conversation_context_parent_child_manual.md) - working context for the manual track.
- [docs/conversation_context_senior_ba_parent_child.md](docs/conversation_context_senior_ba_parent_child.md) - working context for the senior BA track.

</details>

<details>
  <summary><strong>Image and Workflow Guides</strong></summary>

- [docs/skill_video_to_manual_screens.md](docs/skill_video_to_manual_screens.md) - repeatable workflow for extracting manual screenshots from screencast video.
- [docs/skill_manual_image_annotation.md](docs/skill_manual_image_annotation.md) - repeatable workflow for screenshot annotation and publish assets.
- [docs/how_to_make_manual_images_from_screencast.md](docs/how_to_make_manual_images_from_screencast.md) - image-processing notes and method summary.
- [docs/manual/_assets/annotation-plan.md](docs/manual/_assets/annotation-plan.md) - table-driven annotation planning document for the current screenshot set.

</details>

## How the Repository Fits Together

1. The plan in [docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md](docs/superpowers/specs/2026-04-23-parent-child-manual-plan.md) defines the documentation method and target deliverables.
2. The source transcript, PO answers, and storyboards preserve the raw inputs used for analysis.
3. The BA artifacts turn those inputs into claims, scenarios, screenshot decisions, QA checks, and traceability.
4. The manual in [docs/manual/00-index.md](docs/manual/00-index.md) is the publishable result.
5. The image workflow guides explain how the screenshot set was extracted, reviewed, and annotated for reuse in future projects.

## Link Health

Markdown links across the repository were checked so that `.md` references resolve correctly in GitHub-friendly relative form.
