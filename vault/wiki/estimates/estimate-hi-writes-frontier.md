---
type: estimate
kind: QA
status: pending
target: rule-skill-hi
origin: raw/2026-09-12/ledger.md#case-59.2
sprint: migration
created: 2026-09-12
tags: [session, harness, workflow]
ref: rule-skill-hi
---

## Context

The Frontier lived in the agent's memory; a plan was closed on one item of it
(lesson-plan-mode-exited-per-frontier-item). The file makes the rule checkable.

## Criterion

After `/hi`, `raw/<date>/frontier.md` exists with one line per item the agent presented,
each `- [ ] F<n> — <title> · <source>`. At `/pre-task` of the same session every line is
`[x] … · case N`, `[x] … · work` or `[-] … · defer case N`, and `guppi pretask --check`
prints no frontier finding; unit: a missing file, an open line, a `case N` without its
heading, a `defer case N` without its item are each one finding, exit 1.

## Method

pytest in `tests/test_pretask.py` against a temp plan and frontier; the live reading at
this session's `/hi` (the file written by hand from the presented list) and `/pre-task`.

## History

- 2026-09-12 created · [[decision-case-59.2]]
