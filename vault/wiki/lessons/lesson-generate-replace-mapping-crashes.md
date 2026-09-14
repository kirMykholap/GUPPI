---
type: lesson
kind: error
root_cause: case-schema.md describes `replace` as `old` → `new` without pinning a shape, the Spec wrote it as a mapping, materialize lifted it as written, and generate.py iterates `replace` as a list of items; a shape the script does not expect must fail that entry alone, not the run
status: clustered
insight: insight-harness-yaml-entry-shape-assumed
origin: raw/2026-09-10/ledger.md#L96
sprint: migration
created: 2026-09-10
tags: [harness, ledger]
---

## Trigger

the librarian's first `guppi generate` of 2026-09-10 stopped with `'str' object has no attribute 'get'` on entries 83 and 85 of materialize.yaml, the Case 43 updates of rule-page-generation and rule-documentation

## Root cause

case-schema.md describes `replace` as `old` → `new` without pinning a shape, the Spec wrote it as a mapping, materialize lifted it as written, and generate.py iterates `replace` as a list of items; a shape the script does not expect must fail that entry alone, not the run

## Insight

- [[insight-harness-yaml-entry-shape-assumed]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L96
- 2026-09-10 updated: clustered by librarian: the yaml entry shape a script assumes, with lesson-materialize-assumes-every-entry-has-a-line · raw/2026-09-10/ledger.md#L122
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-14 insight section derived
