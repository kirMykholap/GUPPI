---
type: lesson
kind: error
root_cause: case-guppi does not search the code for an existing implementation of a judgment its tasks add, so a check of rule-one-judgment-one-implementation stands only at pre-spec
status: clustered
insight: "[[insight-workflow-case-written-without-reading-the-pages-it-changes]]"
origin: raw/2026-10-09/0200/ledger.md#L23
sprint: migration
created: 2026-10-09
tags: [harness, workflow]
---

## Trigger

case-guppi built Case 748.1 with a task that had materialize fill the type by a map of its own, while SINGULAR of guppi/generate.py already held it and guppi/prespec.py imported it; the pre-spec run of ask-guppi found the second copy and the Case was built again

## Root cause

case-guppi does not search the code for an existing implementation of a judgment its tasks add, so a check of rule-one-judgment-one-implementation stands only at pre-spec

## History

- 2026-10-09 created · raw/2026-10-09/0200/ledger.md#L23
- 2026-10-09 updated: clustered under insight-workflow-case-written-without-reading-the-pages-it-changes (synthesis) · raw/2026-10-09/0200/ledger.md#L23
