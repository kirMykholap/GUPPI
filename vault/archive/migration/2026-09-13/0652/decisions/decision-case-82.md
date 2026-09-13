---
type: decision
case: "82"
status: archived
defer: [rule-materialize]
superseded_by: [decision-case-87]
origin: raw/2026-09-12/ledger.md#case-82
sprint: migration
created: 2026-09-12
tags: [harness, workflow, ledger]
---

## Context

`materialize.parse_line` reads the braces of a lesson line and returns `tags` only;
`lesson_entry` then marks every `knowledge` lesson `incomplete: [source]` and
`generate` writes no `source` field, though the line carries one
(`lesson-materialize-lesson-line-source-dropped`, session J). Two knowledge lessons of
sessions I and J are affected; the librarian sets the field on their entries by hand.

## Problem

The lesson entry's contract (`rule-materialize`, `estimate-materialize-assembles`)
names `kind`, `root_cause`, Trigger and Root cause and not `source`; carrying it is a
change of that contract. One `update` of `rule-materialize`; the next Plan Mode.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-82
- 2026-09-12 superseded by decision-case-87 · [[decision-case-87]]
- 2026-09-13 archived · superseded
- 2026-09-13 archived · cleanup
