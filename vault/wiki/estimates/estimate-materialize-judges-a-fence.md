---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: "Every reader of a fence judges it by the functions of guppi/materialize.py, as CommonMark does: a fence closes only on a run of its own character at least as long"
method: uv run pytest tests/test_materialize.py -k fence
checked: 2026-09-29
origin: raw/2026-09-26/2300/ledger.md#case-444.1
sprint: migration
created: 2026-09-26
tags: [harness, workflow, tests]
---

## Criterion

When:
A hook or a script reads a text that holds a fence: `then_blocks`, `tagged_blocks`, `quoted_sections` and `criterion_text` of `guppi/materialize.py`, `fenced_value` of `guppi/ratified.py`, `plan_prose` and `check_pairs` of `guppi/prespec.py`, the check of `ratification` in `guppi/casecheck.py`, `ledger_lines` of `guppi/ledger.py`, or the class `fence` of `guppi/lint.py`.

Then:
A line opens a fence when, after at most three spaces of indent inside the block it stands in (a quote, a sub-point of `tasks`), it starts with a run of three or more backticks or three or more tildes.
**＋** The fence closes only on a line of the same character whose run is at least as long as the opening run, with nothing after the run but spaces.
**＋** A line with a shorter run, a run of the other character, or a word after its run stays inside the fence as content.
**＋** `fence_breaks` is built on `fence_opening` and `closes_fence`, so each break it reports is a line these readers keep as content, or an end of section they reach inside a fence.
**＋** A fenced value under a sub-point of `tasks` that holds a shorter fence of the same character is read whole, together with the inner fence.
**＋** Every one of these readers takes the judgment from the functions of `guppi/materialize.py`, and they all give the same answer for the same text.
**－** No reader keeps a fence pattern of its own: the `FENCE` of `guppi/ledger.py`, the `OPEN_FENCE` of `guppi/ratified.py`, and the tests on three backticks in `guppi/ratified.py` and `guppi/casecheck.py` are removed.

## Result

2026-09-29, uv run pytest tests/test_materialize.py -k fence: 14 passed; grep finds no FENCE or OPEN_FENCE pattern and no three-backtick test in guppi/ledger.py, ratified.py, casecheck.py, lint.py

## History

- 2026-09-27 created · [[decision-case-444.1]]
- 2026-09-27 updated: the Criterion replaced whole — quoted_sections of guppi/materialize.py is the one reader of the sections of a Case; case_text and the copy in guppi/ratified.py removed (case 462) · [[decision-case-462]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L23
- 2026-09-29 updated: the Criterion replaced whole — check_pairs of guppi/prespec.py and the class fence of guppi/lint.py join the readers, and fence_breaks, built on the same functions, reports a word after a full run inside a fence, and a fence open at the end of a section, as a break (case 487.4) · [[decision-case-487.4]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L27
