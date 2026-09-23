---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: The written shape of a ledger line and of its marks, as the agent writes them
method: "by hand: the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together"
checked: 2026-09-23
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
---

## Criterion

When:
The agent writes the ledger lines of a session: the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists.

Then:
A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
**＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
**＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
**－** A lesson whose fix is ratified in another session gets no mark.

## Result

2026-09-23, case-schema.md as loaded at the /hi of session 0034, read by hand: the ledger paragraph says a decision line whose Case closes the root cause of a lesson of this session carries {addresses:<lesson slug>}, written when the lesson line already stands in the ledger, one mark per lesson, and a lesson fixed in another session gets no mark; the lesson and estimate rows of the table carry no addressed_by; the writing leg had no instance — no Case of this session closed the cause of its one lesson

## History

- 2026-09-16 created · [[decision-case-188]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L38
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-20 updated: the Criterion replaced whole — the table and the ledger paragraph are one document since 273.1, two documents read, not three (case 277.6) · [[decision-case-277.6]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L3
- 2026-09-21 updated: the Criterion replaced whole — the mark {addresses:<lesson slug>} beside {source} and {supersedes} (case 284.2) · [[decision-case-284.2]]
- 2026-09-21 status: pending → passed · raw/2026-09-21/0019/ledger.md#L1
- 2026-09-22 updated: the Criterion reads case-schema.md alone; the second copy in index.md is gone (case 318) · [[decision-case-318]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/0034/ledger.md#L61
- 2026-09-23 updated: the Criterion replaced whole — the shape of a decision line and the two marks, by the order of the lines (case 379) · [[decision-case-379]]
