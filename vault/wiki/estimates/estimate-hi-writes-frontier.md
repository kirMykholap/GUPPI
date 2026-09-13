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

### case 73.3

When:
The person invokes `/hi`.

Then:
The Frontier goes to `raw/<hi date>/<hi HHMM>/frontier.md`, the folder made at that
moment; the lines and their closing are as in case 59.2.

### case 101.4

When:
The agent assembles the Frontier from the text of `/hi`.

Then:
The skill text: "A `failed` reading or a lesson in the Tail above is an item; a decision line of the tail is not — its page comes with the next librarian."
**＋** `estimate-hi-writes-frontier` gets a `### case 101.4` block, `pending`.

## Method

pytest in `tests/test_pretask.py` against a temp plan and frontier; the live reading at
this session's `/hi` (the file written by hand from the presented list) and `/pre-task`.

## Result

live 2026-09-12 session J: after /hi the agent wrote raw/2026-09-12/frontier.md by hand, F19–F33, one line per item presented, all [ ]; every line closed in Plan Mode as its item ended — work, case N or defer case N; at /pre-task the first guppi pretask --check printed 16 frontier findings, all of session I's lines in the same file (the collision case 73 fixes), none of this session's; after session I's section moved to raw/2026-09-12/0454/frontier.md the check printed nothing, exit 0

## History

- 2026-09-12 created · [[decision-case-59.2]]
- 2026-09-12 criterion: case 73.3 added · [[decision-case-73.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L151
- 2026-09-13 criterion: case 101.4 added · [[decision-case-101.4]]
