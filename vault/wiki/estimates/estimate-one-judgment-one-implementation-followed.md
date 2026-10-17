---
type: estimate
kind: QA
status: passed
target: "[[rule-one-judgment-one-implementation]]"
purpose: CLAUDE.md holds the rule between its markers, and the code of a session keeps one judgment in one implementation
method: render --check exit 0, then by hand the section in CLAUDE.md and the diff of the next Work Mode session — a judgment made in two places imported from one module, or a test over both sides
checked: 2026-10-17
origin: raw/2026-09-23/0034/ledger.md#case-360
sprint: migration
created: 2026-09-23
tags: [harness, workflow, tests]
---

## Criterion

When:
The agent writes code that judges a text another part of the pipeline already judges, such as a check beside a writer, a ticker or another check.

Then:
The pattern or the predicate lives in one module, and both sides import it.
**＋** Where the two sides cannot share the code, one test runs both over the same input and asserts they answer alike.
**＋** `CLAUDE.md`, which every session and every subagent loads, holds this text between the markers of `rule-one-judgment-one-implementation`; `render --check` keeps it equal to the page, and the hook of `rule-governed-files-hook` refuses a hand edit.
**－** No script refuses a second copy: the guard is the text in the file every context reads, and the reading of the session's diff.

## Result

2026-10-17, Retro of session 1805: uv run --project .guppi guppi render --check exit 0, CLAUDE.md holds the text between the markers of rule-one-judgment-one-implementation; the diff of this Work Mode: defer_only of .guppi/guppi/ratified.py imports is_short_form of .guppi/guppi/casecheck.py, which shows_sections of the same module uses, and writes no second copy

## History

- 2026-09-23 created · [[decision-case-360]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1228/ledger.md#L43
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the functions lifted by case 351 out (case 492.3) · [[decision-case-492.3]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L72
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-17 updated: the Criterion replaced whole — the code that judges a text is any code, not only that of the package of GUPPI · [[decision-case-880.14]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L71
