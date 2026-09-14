---
type: estimate
kind: QA
status: passed
target: "[[rule-session-start]]"
origin: raw/2026-09-09/ledger.md#case-12
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks]
---

## Context

The children check that each mechanism works on its own. This check is the cross-cutting
one: that the distinction between an ordinary session and a working session holds end to
end, from the mark `/hi` leaves to what the person sees when a line is refused.

## Criterion

In a session opened without `/hi`, a `- decision[...]` line inside a LEDGER block does not
reach `raw/<date>/ledger.md` and the reply the person sees names the cause. In a session
opened with `/hi`, the same line does reach it, with its time. Both readings taken end to
end.

## Method

`make test-session-start`, the pipeline over `tests/test_event.py` and
`tests/test_ledger.py`; the two end-to-end readings by hand, recorded in the estimate line.

## Result

Passing, both readings on 2026-09-09. Reading 1, session `51e9ced9` started 16:26:17 with no
`/hi`: the reply carried the bare line `- decision[case 0][defer][probe]`, the hook refused
with `ledger: 1 line(s) not written — no /hi recorded for session …`, the owner saw the
cause and `raw/2026-09-09/ledger.md` was untouched. Reading 2, session `e2ea2380` started
16:28:24, `hi` at 16:29:18: the eight estimate lines of the first reply reached the ledger,
once each. Reading 1 was taken with a bare line under the pre-15.1 contract; the refusal
path is unchanged since, and `tests/test_ledger.py` holds it in the LEDGER-block shape.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-12
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-09 updated: criterion follows the LEDGER block · raw/2026-09-09/ledger.md#case-16.1
- 2026-09-09 updated: Method names the make pipeline over the children · raw/2026-09-09/ledger.md#case-26.2
