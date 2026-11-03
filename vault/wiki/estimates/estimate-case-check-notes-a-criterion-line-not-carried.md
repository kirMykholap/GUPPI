---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A line of a Criterion replaced whole that the new Criterion does not carry goes back to case-guppi once as a note, and pre-spec prints it, with no Case held back
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py .guppi/tests/test_prespec.py -k note, then by hand the first note the hook sends back to case-guppi
checked: 2026-10-05
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi casecheck --subagent` checks on `SubagentStop` the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that `case-guppi` wrote, or `uv run --project .guppi guppi prespec --check <plan>` checks the plan, and a Case of it holds an `update` of an Estimate that names no part of the page by `names_a_part` of `.guppi/guppi/materialize.py`, and so replaces its `## Criterion` whole.

Then:
The old Criterion is the `## Criterion` of the Estimate page as it stands. The new one is the Criterion the item writes under `sections`, or else the `when` and `then` of the Case that holds the item.
**＋** Each line of the old Criterion that no line of the new one equals is a note that names the Case, the Estimate and the line. The operand at the head of a line, the labels `When:`, `Then:` and `Given:`, and whitespace are set aside.
**＋** The notes of a Case are judged by functions of `.guppi/guppi/prespec.py`, and `.guppi/guppi/casecheck.py` imports them, not copies.
**＋** `uv run --project .guppi guppi prespec --check <plan>` prints each note as a line opening with `note:`, which sets no exit code.
**＋** `uv run --project .guppi guppi casecheck --subagent` exits 2 with the notes on stderr, beside any findings, and `case-guppi` changes the file: it restores the line, or it keeps the change and says why in `context`.
**＋** It stores the notes it sent for each Case id in `<plan>.checked.json`, apart from the findings, and a later check of the same id keeps them.
**－** A note that the store already holds for the same Case id is not sent again, and a check whose only notes are held exits 0.
**－** A note is not a finding: the Case is stored with no finding for it, and the `Stop` check of `guppi casecheck` does not refuse a showing for a note.
**－** An Estimate that a Case creates has no old Criterion and gets no note.

## Result

2026-10-05, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
