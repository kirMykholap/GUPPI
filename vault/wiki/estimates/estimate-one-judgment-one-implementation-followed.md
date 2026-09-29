---
type: estimate
kind: QA
status: passed
target: "[[rule-one-judgment-one-implementation]]"
purpose: CLAUDE.md holds the rule between its markers, and the code of a session keeps one judgment in one implementation
method: render --check exit 0, then by hand the section in CLAUDE.md and the diff of the next Work Mode session — a judgment made in two places imported from one module, or a test over both sides
checked: 2026-09-29
origin: raw/2026-09-23/0034/ledger.md#case-360
sprint: migration
created: 2026-09-23
tags: [harness, workflow, tests]
---

## Criterion

When:
The agent writes code in `guppi/` that judges a text another part of the pipeline already judges, such as a check beside a writer, a ticker or another check.

Then:
The pattern or the predicate lives in one module, and both sides import it.
**＋** Where the two sides cannot share the code, one test runs both over the same input and asserts they answer alike.
**＋** `CLAUDE.md`, which every session and every subagent loads, holds this text between the markers of `rule-one-judgment-one-implementation`; `render --check` keeps it equal to the page, and the hook of `rule-governed-files-hook` refuses a hand edit.
**－** No script refuses a second copy: the guard is the text in the file every context reads, and the reading of the session's diff.

## Result

2026-09-29, uv run guppi render --check exit 0; CLAUDE.md holds the section in its markers; by hand, the diff of the Work Mode of session 1134 (commit 35bb520): code removed from guppi/lint.py and guppi/generate.py, no judgment written in two places

## History

- 2026-09-23 created · [[decision-case-360]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1228/ledger.md#L43
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the functions lifted by case 351 out (case 492.3) · [[decision-case-492.3]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L72
