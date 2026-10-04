---
type: estimate
kind: QA
status: pending
target: "[[rule-lint]]"
purpose: Whether make lint runs all five steps when an earlier one is red, prints the lines of each, and exits non-zero when any step is red
method: "by hand, the make lint of the Baseline of a /work of a later session whose backlog step is red: the steps that printed, the page findings of guppi lint and the exit code, recorded in the estimate line"
origin: raw/2026-10-02/1202/ledger.md#case-587
sprint: migration
created: 2026-10-02
tags: [harness, workflow]
---

## Criterion

When:
Someone runs `make lint` of the `Makefile`: by hand, in the Baseline of `/work`, or in the librarian's run of `.claude/agents/librarian-guppi.md`.

Then:
`make lint` runs all five steps in the order `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint`, whether an earlier step exited 0 or not.
**＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
**＋** `make lint` exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
**－** No step reads the stdin of its caller, and `make lint` writes nothing to the tree.

## History

- 2026-10-02 created · [[decision-case-587]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 deferred · [[decision-case-631]]
