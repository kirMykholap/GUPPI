---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: A line of a Criterion replaced whole that the new Criterion does not carry goes back to case-guppi once as a note, and pre-spec prints it, with no Case held back
method: uv run pytest tests/test_casecheck.py tests/test_prespec.py -k note, then by hand the first note the hook sends back to case-guppi
origin: raw/2026-09-28/0000/ledger.md#case-472.1
sprint: migration
created: 2026-09-28
tags: [hooks, harness, workflow]
---

## Criterion

When:
`uv run guppi casecheck --subagent` checks an answer of `case-guppi` on `SubagentStop`, or `uv run guppi prespec --check <plan>` checks the plan, and a Case of it holds an `update` of an Estimate that names no part of the page by `names_a_part` of `guppi/materialize.py`, and so replaces its `## Criterion` whole.

Then:
The old Criterion is the `## Criterion` of the Estimate page as it stands. The new one is the Criterion the item writes under `sections`, or else the `when` and `then` of the Case that holds the item.
**＋** Each line of the old Criterion that no line of the new one equals is a note that names the Case, the Estimate and the line. The operand at the head of a line, the labels `When:`, `Then:` and `Given:`, and whitespace are set aside.
**＋** The notes of a Case are judged by functions of `guppi/prespec.py`, and `guppi/casecheck.py` imports them, not copies.
**＋** `uv run guppi prespec --check <plan>` prints each note as a line opening with `note:`, which sets no exit code.
**＋** `uv run guppi casecheck --subagent` exits 2 with the notes on stderr, beside any findings, and `case-guppi` answers again: it restores the line, or it keeps the change and says why in `context`.
**＋** It stores the notes it sent for each Case id in `<plan>.checked.json`, apart from the findings, and a later answer for the same id keeps them.
**－** A note that the store already holds for the same Case id is not sent again, and an answer whose only notes are held exits 0.
**－** A note is not a finding. The file of the Case is written as for an answer with no finding, and the `Stop` check of `guppi casecheck` does not refuse a showing for a note.
**－** An Estimate that a Case creates has no old Criterion and gets no note.

## History

- 2026-09-28 created · [[decision-case-472.1]]
