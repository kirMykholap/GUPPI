---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether a Case that changes a reader and the text it reads, where the reader loses what it refuses before the text lands, keeps the old form in its then until the writer is measured live, and whether a Case that changes a test over a live file, or the code of a check it runs, while the same session changes that file, makes the test pass on the old text and the new until the text lands
method: "by hand, after the first Case case-guppi builds under the Render of rule-case-build that names a test over a live file, which changes a reader in code and the text or the writer it reads, or a test of .guppi/tests/ or the code of a check it runs, and a live file the test reads: the then and tasks of that Case read against the Criterion, recorded in the estimate line"
checked: 2026-10-13
origin: raw/2026-09-28/0000/ledger.md#case-473.2
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes a reader in code and the text or the writer that reader reads, or a test of `.guppi/tests/` or the code of a check that test runs, and a live file of `vault/` or `.claude/` that the test reads, where the code and the test run from the working tree at once and the text lands at the librarian's run or the render.

Then:
Where the reader refuses in between and what it refuses is lost, such as a hook that refuses a ledger line, the `then` of the Case says that the reader accepts the old form beside the new one until a reading of the writer passes live.
**＋** Where the test would fail on the text of the file before the change or after it, whether the Case changes the test, the code of a check the test runs or the file, a task of the Case makes the test pass on the text before the change and on the text after it, until the text lands.
**＋** The removal of the old form from the reader, after that reading, and of the old text from the test, after the text lands, is left to a Case of a later session.
**－** A reader that only goes red, such as `uv run --project .guppi guppi check`, keeps no old form: its red is a note for the handoff by `rule-retro`.
**－** A test of `.guppi/tests/` is no such reader: by `rule-retro` a red test is never an expected red, so no task leaves the test red until the librarian's run.

## Result

2026-10-13, /hi of session 2118, the then of Case 804.4 in vault/raw/2026-10-13/1753/cases/case-804.md read against the Criterion: 804.4 changes the reader check_origin of guppi/lint.py and 804.5 writes the field core it reads, which lands at the librarian's run; the reader is lint, which only goes red and loses nothing it refuses, so by the － line it keeps no old form, and the then keeps none — it keeps every earlier origin form and adds origin guppi on a page with core: true; make lint printed 0 lines at the close of the librarian's run (brief)

## History

- 2026-09-28 created · [[decision-case-473.2]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/1318/ledger.md#L38
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-13 updated: the Criterion replaced whole — the line that put the insight actioned is dropped, since the insight was reopened; the method names its event (case 797.2) · [[decision-case-797.2]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L2
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-10-17 updated: the Criterion replaced whole — a test over a live file that the same session changes passes on the old text and the new until the text lands · [[decision-case-868]]
