---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether a Case that changes a reader and the text it reads, where the reader loses what it refuses before the text lands, keeps the old form in its then until the writer is measured live
method: one reading by hand at the first Case case-guppi builds after the render that changes a reader and the text or writer it reads, recorded in the estimate line
checked: 2026-09-28
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
**－** `insight-workflow-code-live-before-the-page-it-reads` stands `actioned` with `addressed_by: decision-case-473.2` and leaves the backlog.

## Result

2026-09-28, by hand, Case 476.3 of session 1318, the first Case after the render that changes a reader (the pre-spec finding) and what it reads (guppi.toml, landing at the librarian's render): the reader only goes red, and the context of 476 says it keeps no old form; the refusing branch of the Criterion was not met in this session; insight-workflow-code-live-before-the-page-it-reads stands actioned with addressed_by decision-case-473.2 and is not in backlog.md

## History

- 2026-09-28 created · [[decision-case-473.2]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/1318/ledger.md#L38
