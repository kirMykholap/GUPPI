---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: The written shape of a ledger line, as the documents state it
method: one reading by hand of case-schema.md after the render, at a session start
checked: 2026-09-21
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
---

## Criterion

Given:
A decision line is markup: `- decision[case N][kind][slug]{ref:...}{tags:...}`, `{supersedes:case N}` when it applies (case 75.1); the Case schema is the Render of `rule-case-protocol`, the one place the line's form is written.
**＋** A lesson line is written the moment the lesson exists — before the ratification of its fix.

When:
`/hi` loads the schema; someone reads `case-schema.md`; the agent writes the `decision[...]` lines in the reply that acknowledges a ratification.

Then:
The ledger paragraph of the schema says: a decision line whose Case closes the root cause of a lesson of this session carries `{addresses:<lesson slug>}`, written when the lesson line already stands in the session's ledger, one mark per lesson — two lessons, two marks.
**＋** The agent writes the line so, and the mark stands in the preview of the ledger lines the person ratifies.
**－** The lesson line does not change: no `{addressed_by}` on it; the estimate row and the lesson row of the table do not change.
**－** A lesson whose fix is ratified in another session gets no mark — the Insight is open by then, and a Case is due, as today.

## Result

2026-09-21, case-schema.md and index.md §4 read by hand at session 0019: the ledger paragraph of the schema and the field list of §4 both say a decision line whose Case closes the root cause of a lesson of this session carries {addresses:<lesson slug>}, written when the lesson line already stands in the ledger, one mark per lesson; the schema alone says a lesson fixed in another session gets no mark, §4 says it through "of this session"; the lesson line and the estimate line of the schema table and of §4 carry no addressed_by; the general form of §4 shows {source}{tags} and not {addresses} — the mark stands in the field list, not the example

## History

- 2026-09-16 created · [[decision-case-188]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L38
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-20 updated: the Criterion replaced whole — the table and the ledger paragraph are one document since 273.1, two documents read, not three (case 277.6) · [[decision-case-277.6]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L3
- 2026-09-21 updated: the Criterion replaced whole — the mark {addresses:<lesson slug>} beside {source} and {supersedes} (case 284.2) · [[decision-case-284.2]]
- 2026-09-21 status: pending → passed · raw/2026-09-21/0019/ledger.md#L1
- 2026-09-22 updated: the Criterion reads case-schema.md alone; the second copy in index.md is gone (case 318) · [[decision-case-318]]
