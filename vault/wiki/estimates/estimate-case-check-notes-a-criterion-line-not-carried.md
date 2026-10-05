---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A line of a Criterion replaced whole that the new Criterion does not carry goes back to case-guppi once as a note, and pre-spec prints it, with no Case held back
method: uv run pytest tests/test_casecheck.py tests/test_prespec.py -k note, then by hand the first note the hook sends back to case-guppi
checked: 2026-10-05
origin: raw/2026-09-28/0000/ledger.md#case-472.1
sprint: migration
created: 2026-09-28
tags: [hooks, harness, workflow]
---

## Criterion

When:
`uv run guppi casecheck --subagent` checks on `SubagentStop` the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that `case-guppi` wrote, or `uv run guppi prespec --check <plan>` checks the plan, and a Case of it holds an `update` of an Estimate that names no part of the page by `names_a_part` of `guppi/materialize.py`, and so replaces its `## Criterion` whole.

Then:
The old Criterion is the `## Criterion` of the Estimate page as it stands. The new one is the Criterion the item writes under `sections`, or else the `when` and `then` of the Case that holds the item.
**＋** Each line of the old Criterion that no line of the new one equals is a note that names the Case, the Estimate and the line. The operand at the head of a line, the labels `When:`, `Then:` and `Given:`, and whitespace are set aside.
**＋** The notes of a Case are judged by functions of `guppi/prespec.py`, and `guppi/casecheck.py` imports them, not copies.
**＋** `uv run guppi prespec --check <plan>` prints each note as a line opening with `note:`, which sets no exit code.
**＋** `uv run guppi casecheck --subagent` exits 2 with the notes on stderr, beside any findings, and `case-guppi` changes the file: it restores the line, or it keeps the change and says why in `context`.
**＋** It stores the notes it sent for each Case id in `<plan>.checked.json`, apart from the findings, and a later check of the same id keeps them.
**－** A note that the store already holds for the same Case id is not sent again, and a check whose only notes are held exits 0.
**－** A note is not a finding: the Case is stored with no finding for it, and the `Stop` check of `guppi casecheck` does not refuse a showing for a note.
**－** An Estimate that a Case creates has no old Criterion and gets no note.

## Result

2026-10-05, by hand at the Work readings of session 1343: uv run pytest -q tests/test_casecheck.py tests/test_prespec.py -k note 16 passed; the first note of the session came from `uv run guppi casecheck --subagent` on case-guppi of Case 650 (agent a8b021dff7985c631) after its first Write of cases/case-650.md: three notes and no finding, the first naming case 650.2, `estimate-spec-reconcile-refuses-an-edit-of-the-plan` and the line not carried; the agent kept its change and added a context paragraph saying why; its next stop got no feedback, the notes not sent again; the store holds the three notes under `650.2` in `notes`, apart from `findings: []`; the showing passed the Stop check; `uv run guppi prespec --check` printed the same note among 19 `note:` lines, exit 0

## History

- 2026-09-28 created · [[decision-case-472.1]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/2000/ledger.md#L22
- 2026-10-05 updated: the Criterion replaced whole — the note goes back on the file case-guppi wrote, and a note writes no file since the hook writes none (case 645.8) · [[decision-case-645.8]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L37
