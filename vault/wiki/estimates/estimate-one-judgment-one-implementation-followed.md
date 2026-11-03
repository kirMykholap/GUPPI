---
type: estimate
kind: QA
status: passed
target: "[[rule-one-judgment-one-implementation]]"
purpose: CLAUDE.md holds the rule between its markers, and the code of a session keeps one judgment in one implementation
method: render --check exit 0, then by hand the section in CLAUDE.md and the diff of the Work Mode of a session — a judgment made in two places imported from one module, or a test over both sides
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, tests]
core: true
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

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
