---
type: decision
case: "274.2"
status: archived
update: ["[[rule-prespec]]", index, entities-schema, estimates-schema]
superseded_by: ["[[decision-case-277.4]]"]
origin: raw/2026-09-20/1308/ledger.md#case-274.2
sprint: migration
created: 2026-09-20
tags: [session, workflow, harness]
---

## Context

`rename` of 258.1 renames a page and replaces its slug as a whole word on every live page but History and Result, in one item. A word without a page — the name of a skill, a command — has no such path: 261 renamed `pre-task` to `pre-spec` on the pages it named, and the word stayed in the Purpose of `rule-index-check`, `rule-brief`, `rule-ask`, in the Backlog of `entity-sprint-migration`, in `index.md`, `entities/schema.md`, `estimates/schema.md`; no Estimate holds it in a Criterion — History, Result and the slug of an archived Insight only. To replace a word across the vault today is one `update` per page, or the whole Criterion, which `lesson-estimate-update-must-carry-its-criterion-whole` is about.
State of the pages: `rule-page-generation` `built`, seven Estimates, none on `reword` — a new promise, a `create`; `rule-prespec` `built`, the owner of `/pre-spec`, its Estimates untouched; three Purposes and the Backlog change by the mechanism, the Rule-class files by hand.

## Problem

How to rename a name that has no page in one decision, so that the script neither searches nor guesses, and the person sees and signs every replacement.

## History

- 2026-09-20 created · raw/2026-09-20/1308/ledger.md#case-274.2
- 2026-09-20 superseded by decision-case-277.4 · [[decision-case-277.4]]
- 2026-09-20 archived · superseded
- 2026-09-20 archived · cleanup
