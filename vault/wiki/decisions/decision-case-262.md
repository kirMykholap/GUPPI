---
type: decision
case: "262"
status: current
update: ["[[estimate-generate-renames]]"]
origin: raw/2026-09-20/0740/ledger.md#case-262
sprint: migration
created: 2026-09-20
tags: [harness, workflow, tests]
---

## Context

`estimate-generate-renames` is a QA Estimate under `rule-page-generation`, created by 258.1, `pending`: pytest is green, the live part is the librarian's run on the first real rename — Case 261 of this session. Its Criterion's `then` quotes the History line `generate` writes twice, with the placeholder `[[decision-case-N]]` as a bare wikilink. `guppi lint` reads every `[[…]]` in a page body as a link and finds `ref: body names decision-case-N, which no live or archived page carries`; a wikilink inside a code span it skips — `links_of` strips code spans before the search. The Decision pages 100.x and 101.x carry the same placeholder in a code span, with no finding. The Case touches no other Estimate of the rule.

## Problem

The ratified text of the Criterion holds the placeholder in a form lint reads as a broken link; the finding stands until the text changes, a reading does not clear it. The choice: repair the Criterion, or leave it as debt.

## History

- 2026-09-20 created · raw/2026-09-20/0740/ledger.md#case-262
