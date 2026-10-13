---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether a Case that changes a reader and the text it reads, where the reader loses what it refuses before the text lands, keeps the old form in its then until the writer is measured live
method: "by hand, after the first Case case-guppi builds that changes a reader in code and the text or the writer it reads: the then of that Case read against the Criterion, recorded in the estimate line"
checked: 2026-10-13
origin: raw/2026-09-28/0000/ledger.md#case-473.2
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi` builds a Case that changes a reader in code and the text or the writer that reader reads, where the reader runs from the working tree at once and the text lands at the librarian's run or the render.

Then:
Where the reader refuses in between and what it refuses is lost, such as a hook that refuses a ledger line, the `then` of the Case says that the reader accepts the old form beside the new one until a reading of the writer passes live.
**＋** The removal of the old form is left to a Case of a later session, after that reading.
**－** A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`.

## Result

2026-10-13, /hi of session 2118, the then of Case 804.4 in vault/raw/2026-10-13/1753/cases/case-804.md read against the Criterion: 804.4 changes the reader check_origin of guppi/lint.py and 804.5 writes the field core it reads, which lands at the librarian's run; the reader is lint, which only goes red and loses nothing it refuses, so by the － line it keeps no old form, and the then keeps none — it keeps every earlier origin form and adds origin guppi on a page with core: true; make lint printed 0 lines at the close of the librarian's run (brief)

## History

- 2026-09-28 created · [[decision-case-473.2]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/1318/ledger.md#L38
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-13 updated: the Criterion replaced whole — the line that put the insight actioned is dropped, since the insight was reopened; the method names its event (case 797.2) · [[decision-case-797.2]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L2
