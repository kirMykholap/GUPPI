---
type: lesson
kind: error
root_cause: materialize lifts every key of a standalone create into `fields`, while only the `estimate` nested under a Leaf create maps `criterion` and `method` into the sections the estimates schema wants; generate writes the fields as given and does not know the two keys are sections
status: clustered
insight: insight-materialize-lift-loses-a-schema-field
origin: raw/2026-09-10/ledger.md#L131
sprint: migration
created: 2026-09-10
tags: [harness, ledger]
---

## Trigger

the six Estimate pages born of a standalone `create` with a `ref` (the four of Cases 47–48, the two walks-dates of Case 43) carry `criterion`, `method` and `ref` as frontmatter fields and have no Criterion or Method section, so their index lines are empty and lint names missing sections

## Root cause

materialize lifts every key of a standalone create into `fields`, while only the `estimate` nested under a Leaf create maps `criterion` and `method` into the sections the estimates schema wants; generate writes the fields as given and does not know the two keys are sections

## History

- 2026-09-11 created · raw/2026-09-10/ledger.md#L131
- 2026-09-12 updated: clustered by librarian: the lift from a line to a page loses a field, with lesson-materialize-lesson-line-source-dropped · raw/2026-09-12/ledger.md#L160
