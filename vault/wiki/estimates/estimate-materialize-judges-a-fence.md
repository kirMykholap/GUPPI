---
type: estimate
kind: QA
status: pending
target: "[[rule-materialize]]"
purpose: "Every reader of a fence judges it by the functions of guppi/materialize.py, as CommonMark does: a fence closes only on a run of its own character at least as long"
method: uv run pytest tests/test_materialize.py -k fence
origin: raw/2026-09-26/2300/ledger.md#case-444.1
sprint: migration
created: 2026-09-26
tags: [harness, workflow, tests]
---

## Criterion

When:
A hook or a script reads a text that holds a fence: `then_blocks`, `tagged_blocks`, `quoted_sections` and `criterion_text` of `guppi/materialize.py`, `fenced_value` of `guppi/ratified.py`, `plan_prose` of `guppi/prespec.py`, the check of `ratification` in `guppi/casecheck.py`, or `ledger_lines` of `guppi/ledger.py`.

Then:
A line opens a fence when, after at most three spaces of indent inside the block it stands in (a quote, a sub-point of `tasks`), it starts with a run of three or more backticks or three or more tildes.
**＋** The fence closes only on a line of the same character whose run is at least as long as the opening run, with nothing after the run but spaces.
**＋** A line with a shorter run, a run of the other character, or a word after its run stays inside the fence as content.
**＋** A fenced value under a sub-point of `tasks` that holds a shorter fence of the same character is read whole, together with the inner fence.
**＋** Every one of these readers takes the judgment from the functions of `guppi/materialize.py`, and they all give the same answer for the same text.
**－** No reader keeps a fence pattern of its own: the `FENCE` of `guppi/ledger.py`, the `OPEN_FENCE` of `guppi/ratified.py`, and the tests on three backticks in `guppi/ratified.py` and `guppi/casecheck.py` are removed.

## History

- 2026-09-27 created · [[decision-case-444.1]]
- 2026-09-27 updated: the Criterion replaced whole — quoted_sections of guppi/materialize.py is the one reader of the sections of a Case; case_text and the copy in guppi/ratified.py removed (case 462) · [[decision-case-462]]
