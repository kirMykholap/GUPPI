---
type: estimate
kind: QA
status: passed
target: "[[rule-session-start]]"
purpose: A ledger line reaches the session's ledger only in a session opened with /hi, and a refusal tells the person why
method: make test-session-start
checked: 2026-10-05
origin: raw/2026-09-09/ledger.md#case-12
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks]
---

## Criterion

When:
The main agent ends a reply that carries a `- decision[...]` line inside a `LEDGER` block, and the `Stop` hook `.guppi/guppi/ledger.py` looks in `vault/raw/<date>/event_log.md` for a `hi` line of the session.

Then:
In a session opened without `/hi`, the line reaches no ledger of the session, and the reply the person sees names the cause.
**＋** In a session opened with `/hi`, the line reaches `vault/raw/<hi date>/<hi HHMM>/ledger.md` once, with the time of writing before it.

## Result

2026-10-05, at the /hi of session 0109: make test-session-start 123 passed

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-12
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-09 updated: criterion follows the LEDGER block · raw/2026-09-09/ledger.md#case-16.1
- 2026-09-09 updated: Method names the make pipeline over the children · raw/2026-09-09/ledger.md#case-26.2
- 2026-09-28 updated: the Criterion replaced whole — one When and Then, the session folder of the ledger; purpose and method set, Context and Method out (case 485.1) · [[decision-case-485.1]]
- 2026-10-05 updated: the method is the make target alone; the live session without /hi is no longer waited for (case 637.4) · [[decision-case-637.4]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/0109/ledger.md#L7
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
