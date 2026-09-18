---
type: lesson
kind: error
root_cause: "the Body table of a schema.md is one row per section — the required column belongs to a section, not to a list — and prose_names reads the first code span of a row, as it does for a field; the row was the error, not the reader, and the findings were right in fact: the .md described no requirement for the two sections; a reader that gathers every span of a cell would license a row without its own required value"
status: new
origin: raw/2026-09-18/1252/ledger.md#L16
sprint: migration
created: 2026-09-18
tags: [harness, workflow]
---

## Trigger

case 229.1 wrote the three sections of the sprint page into one row of the Body table of entities/schema.md — `## Milestones`, `## Backlog`, `## Closed` in one cell — and guppi lint printed two schema-prose findings, schema.yaml names section ## Backlog / ## Closed, schema.md does not; the row was split into three in Work Mode of session 1119 and the findings went

## Root cause

the Body table of a schema.md is one row per section — the required column belongs to a section, not to a list — and prose_names reads the first code span of a row, as it does for a field; the row was the error, not the reader, and the findings were right in fact: the .md described no requirement for the two sections; a reader that gathers every span of a cell would license a row without its own required value

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#L16
