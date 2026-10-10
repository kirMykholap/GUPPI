---
type: decision
case: "87"
status: archived
update: ["[[rule-materialize]]"]
supersedes: ["[[decision-case-82]]"]
origin: raw/2026-09-12/ledger.md#case-87
sprint: migration
created: 2026-09-12
tags: [harness, workflow, ledger]
---

## Context

`materialize.parse_line` reads the braces of a lesson line into options and returns
`tags` only. `lesson_entry` then marks every `knowledge` lesson `incomplete: [source]`
and `generate` writes the page without the field, though the line carried one. Case 82
deferred it here.

## Problem

The lesson entry's contract (`rule-materialize`, `estimate-materialize-assembles`) names
`kind`, `root_cause`, Trigger and Root cause, and not `source`; carrying the field is a
change of that contract. The pages already written without it need a decision of their
own: a backfill, or debt.

## Given

The lesson branch of `parse_line` returns `record`, `kind`, `slug`, `trigger`,
`root_cause` and `tags`; the decision branch of the same function already reads
`options.get("source")` (line 116), so the grammar is there and only the lesson does not
read it.
**＋** `lesson_entry` builds `fields: {type, kind, root_cause}` with the sections Trigger
and Root cause, and calls `incomplete.append("source")` for every `knowledge` lesson
unconditionally.
**＋** `lessons/schema.md` requires `source` for `knowledge` — "url or reference" — and
defines `knowledge` as external material studied once so the source never has to be
supplied again.
**＋** Twelve `knowledge` lessons are live and eleven carry no `source`. Five of the
eleven have a ledger line that carries one:
`lesson-bash-tool-heredoc-escapes-interpreted`,
`lesson-frame-read-clauses-omit-candidate-check-and-brief`,
`lesson-librarian-reads-beyond-the-four-inputs`,
`lesson-readings-after-librarian-invisible-to-next-hi`,
`lesson-subagents-parallel-on-one-tree-red-mid-flight`. The other six have no source in
the line either.
**＋** `guppi lint` prints exactly eleven findings of class `source`; these are they.
**＋** `rule-materialize` is a Leaf; its first Estimate is `estimate-materialize-assembles`
(33 tests, `passed` in session J).
**－** The librarian set `fields.source` on one entry by hand in the last run because the
handoff told it to — the conflict of F48. After this change no hand is needed.

## Criterion

- [[estimate-materialize-assembles]] § case 87

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-87
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
