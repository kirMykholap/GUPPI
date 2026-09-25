---
type: estimate
kind: QA
status: passed
target: "[[rule-one-judgment-one-implementation]]"
purpose: CLAUDE.md holds the rule between its markers, and the code of a session keeps one judgment in one implementation
method: render --check exit 0, then by hand the section in CLAUDE.md and the diff of the next Work Mode session — a judgment made in two places imported from one module, or a test over both sides
checked: 2026-09-25
origin: raw/2026-09-23/0034/ledger.md#case-360
sprint: migration
created: 2026-09-23
tags: [harness, workflow, tests]
---

## Criterion

Given:
`CLAUDE.md` is loaded in every context, a subagent's too; `rule-claude-md` renders it whole, each child between its markers (case 272).
**＋** `render --check` keeps the file equal to the page, and the hook refuses a hand edit.
**＋** Case 351 lifted `generate.READ_LINE`, `lint.names_a_form` and `generate.replace_once` so that both sides import them.

When:
The agent writes code that judges a text another part of the pipeline already judges — a check beside a writer, a ticker or another check.

Then:
The pattern or the predicate lives in one module, and both sides import it.
**＋** Where the two sides cannot share the code, one test runs both over the same input and asserts they answer alike.
**＋** `CLAUDE.md` holds this text between the markers of `rule-one-judgment-one-implementation`.
**－** No script refuses a second copy: the guard is the text in the file every context reads, and the reading of the session's diff.

## Result

2026-09-25, uv run guppi render --check exit 0; by hand, the diff of the Work Mode of session 1228: the History heading is one constant of guppi/pages.py that generate and lint import; history_line shares the walk of split_sections; one function, ratified.case_section, builds the Spec section of a Case for the write and for casecheck; casecheck imports prespec.judge

## History

- 2026-09-23 created · [[decision-case-360]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1228/ledger.md#L43
