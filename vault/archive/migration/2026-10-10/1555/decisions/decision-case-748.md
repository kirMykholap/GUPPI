---
type: decision
case: "748"
status: archived
children: ["[[decision-case-748.1]]", "[[decision-case-748.2]]"]
origin: raw/2026-10-09/0200/ledger.md#case-748
sprint: migration
created: 2026-10-09
tags: [harness, workflow, ledger, schema]
---

## Problem

A `create` item can reach the ratified Spec without a field that `materialize` requires, since nothing before the Spec judges those fields. Among them, `type` is one that the page writer derives anyway, so its absence raises a false mark that a Retro read as a page not built.

## Recommend

- **What the fix does about the type field**
  - Recommended: (a) fill the type, check the rest: `materialize` fills `type` from the folder for every new page, and `/pre-spec` and the check of each case file report a new page whose item lacks any other required field, by one list the tool uses; two parts with a check each.
  - Answer: agreed, (a).
- **Whether a missing field stops the Case or only warns**
  - Recommended: (a) a finding, which sends the case file back and keeps `/pre-spec` from passing, as for an unmet schema condition.
  - Answer: agreed, (a).
- **How the filled-in type is checked**
  - Recommended: (a) a new check of its own on `rule-materialize`, read by a test in this session; `estimate-materialize-assembles` stays as it is.
  - Answer: agreed, (a).
- **How the new missing-field check is checked**
  - Recommended: (a) a new check of its own on `rule-prespec-hook`, read by a test in this session; `estimate-prespec-hook-reports-a-schema-condition-not-met` stays as it is.
  - Answer: agreed, (a).
- **Whether a put-off item is checked too**
  - Recommended: (a) new pages only; a put-off item with no `purpose` is still marked only after ratification.
  - Answer: agreed, (a).

## History

- 2026-10-09 created · raw/2026-10-09/0200/ledger.md#case-748
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
