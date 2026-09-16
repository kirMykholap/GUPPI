---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
ref: rule-case-protocol
purpose: The written shape of a ledger line, as the documents state it
method: one reading by hand of `case-schema.md`, `index.md` §4 and the ledger paragraph of the Render, at a session start
---

## Criterion

When:
A session starts with `CLAUDE.md`; someone reads `case-schema.md` or `index.md` §4;
the main agent writes a `- lesson[knowledge][...]` line.

Then:
The table of `case-schema.md`, §4 of the map and the ledger paragraph of the Render
show `- decision[case 12][update][rule-x]{ref:rule-x}` and
`- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` and say: the id is
`case N` with the word and a space, in `{supersedes:case N}` too.
**＋** The ledger paragraph of the Render carries the sentence: "A `knowledge` lesson
line carries `{source:...}`, the url or reference the lesson studied — a file of the
harness, a probe, a client version; the schema requires it, and a line without it is
`incomplete: [source]` in the yaml and a lint finding on the page. An `error` lesson
never carries one."
**－** The estimate and lesson rows of the table do not change.
**－** `rule-ledger-write` does not change: the hook writes verbatim and checks
nothing.

## History

- 2026-09-16 created · [[decision-case-188]]
