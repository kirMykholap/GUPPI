---
type: lesson
kind: error
root_cause: "assemble builds `known = {e[\"line\"]: e for e in entries}` over every entry of the existing yaml, but the three entries the librarian appended at synthesis in session F (an insight create and two lesson updates, marked `librarian: synthesis`) carry no `line` because no ledger line made them; the first materialize over a yaml the librarian has extended fails; entries without `line` must be skipped when the ledger is matched, as the contract of case 41 already says"
status: archived
insight: "[[insight-harness-yaml-entry-shape-assumed]]"
origin: raw/2026-09-10/ledger.md#L122
sprint: migration
created: 2026-09-10
tags: [harness, ledger, librarian]
---

## Trigger

the librarian's `guppi materialize` of session G stopped with `materialize.yaml not written: 'line'` on 2026-09-10, nothing written, the run ended at step 1 and the brief of session F stayed

## Root cause

assemble builds `known = {e["line"]: e for e in entries}` over every entry of the existing yaml, but the three entries the librarian appended at synthesis in session F (an insight create and two lesson updates, marked `librarian: synthesis`) carry no `line` because no ledger line made them; the first materialize over a yaml the librarian has extended fails; entries without `line` must be skipped when the ledger is matched, as the contract of case 41 already says

## Insight

- [[insight-harness-yaml-entry-shape-assumed]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L122
- 2026-09-10 updated: clustered by librarian: the yaml entry shape a script assumes, with lesson-generate-replace-mapping-crashes · raw/2026-09-10/ledger.md#L122
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-14 insight section derived
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
