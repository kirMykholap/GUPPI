---
type: lesson
kind: error
root_cause: materialize.parse_line reads the braces of a lesson line into options and returns tags only, never source; lesson_entry then marks every knowledge lesson incomplete and generate writes no source field; the one line that carries the source is dropped between the ledger and the yaml, and lint reports the page, not the parser; a fix is a change of what the lesson entry carries, taken to the next Plan Mode as a defer at Retro, and the librarian sets the field on the two entries by hand meanwhile
status: clustered
insight: insight-materialize-lift-loses-a-schema-field
origin: raw/2026-09-12/ledger.md#L160
sprint: migration
created: 2026-09-12
tags: [harness, ledger]
---

## Trigger

the yaml preview of 2026-09-12 (materialize --show) marks lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event incomplete: [source] though its ledger line carries {source:...}; the page of lesson-subagents-parallel-on-one-tree-red-mid-flight (session I, a knowledge lesson with a source in its line) has no source field, and the brief counted it among the lessons that lack one

## Root cause

materialize.parse_line reads the braces of a lesson line into options and returns tags only, never source; lesson_entry then marks every knowledge lesson incomplete and generate writes no source field; the one line that carries the source is dropped between the ledger and the yaml, and lint reports the page, not the parser; a fix is a change of what the lesson entry carries, taken to the next Plan Mode as a defer at Retro, and the librarian sets the field on the two entries by hand meanwhile

## Insight

- [[insight-materialize-lift-loses-a-schema-field]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L160
- 2026-09-12 updated: clustered by librarian: the lift from a line to a page loses a field, with lesson-materialize-standalone-estimate-keeps-criterion-as-a-field · raw/2026-09-12/ledger.md#L160
- 2026-09-14 insight section derived
