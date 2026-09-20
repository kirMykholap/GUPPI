---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
purpose: The written shape of a ledger line, as the documents state it
method: one reading by hand of `case-schema.md` and `index.md` §4 after the render, at a session start
checked: 2026-09-20
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
---

## Criterion

Given:
The table of the lines and the paragraph of the ledger mechanics are in `case-schema.md` (273.1); §4 of `index.md` is the second copy of the line's form.

When:
`/hi` loads the schema; someone reads `case-schema.md` or `index.md` §4; the main agent writes a `- lesson[knowledge][...]` line.

Then:
The table of `case-schema.md` and §4 of the map show `- decision[case 12][update][rule-x]{ref:rule-x}` and `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` and say: the id is `case N` with the word and a space, in `{supersedes:case N}` too.
**＋** The ledger paragraph of the schema carries the sentence on `{source:...}` on a `knowledge` lesson line, `incomplete: [source]` without it, an `error` lesson never carrying one.
**－** The estimate and lesson rows of the table do not change; `rule-ledger-write` does not change — the hook writes verbatim and checks nothing.

## Result

2026-09-20, case-schema.md and index.md §4 read by hand at session 1749: the table shows the two example lines and says the id is case N, the word and a space, in {supersedes:case N} too; the ledger paragraph carries the {source:...} sentence, incomplete: [source] without it, an error lesson never; §4 shows the general form with {source} and {tags}, the {supersedes:case 4} form and the case N sentence — the create example stands in the schema only

## History

- 2026-09-16 created · [[decision-case-188]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L38
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-20 updated: the Criterion replaced whole — the table and the ledger paragraph are one document since 273.1, two documents read, not three (case 277.6) · [[decision-case-277.6]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L3
