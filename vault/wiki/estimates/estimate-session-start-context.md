---
type: estimate
kind: QA
status: pending
target: "[[rule-session-start]]"
purpose: A ledger line reaches the session's ledger only in a session opened with /hi, and a refusal tells the person why
method: "make test-session-start; by hand: one session opened without /hi whose reply carries a LEDGER block, and the ledger of the next working session after its first ratification, written into the estimate line"
origin: raw/2026-09-09/ledger.md#case-12
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks]
---

## Criterion

When:
The main agent ends a reply that carries a `- decision[...]` line inside a `LEDGER` block, and the `Stop` hook `guppi/ledger.py` looks in `vault/raw/<date>/event_log.md` for a `hi` line of the session.

Then:
In a session opened without `/hi`, the line reaches no ledger of the session, and the reply the person sees names the cause.
**＋** In a session opened with `/hi`, the line reaches `vault/raw/<hi date>/<hi HHMM>/ledger.md` once, with the time of writing before it.

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
- 2026-09-28 updated: the Criterion replaced whole — one When and Then, the session folder of the ledger; purpose and method set, Context and Method out (case 485.1) · [[decision-case-485.1]]
