---
type: estimate
kind: QA
status: passed
target: "[[rule-plan-mode]]"
method: make test-plan-mode, the pipeline over tests/test_spec.py and tests/test_prespec.py; the flagging one live reading by hand, written into the estimate line
checked: 2026-09-20
origin: raw/2026-09-09/ledger.md#case-19
sprint: migration
created: 2026-09-09
tags: [session, workflow]
---

## Criterion

Given:
The children of `rule-plan-mode` check one mechanism each; this one checks that the two verification points hold across Plan Mode.
**＋** The vault's answer before a `create` without a `ref` enters the `context` of the Case (case 188).

When:
A Case proposes a `create`, and later the person approves the plan.

Then:
A `create` for a page whose `purpose` an index line already carries is named in the `context` of the Case before ratification.
**＋** The pre-spec hook fires before the plan is written — and the plan is still written.

## Result

2026-09-20, `make test-plan-mode` 74 green (tests/test_spec.py, tests/test_prespec.py); live, the plan of this session: ExitPlanMode was let through after the prespec mark of 12:23:17 in the window of the hi 09:58:48 and the plan was written to raw/2026-09-20/0958/spec.md by guppi spec; the one `create` of the session (264.2) carries a `ref`, so no vault query was due and no index line carried its purpose — the flag part of the Criterion was not exercised

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-19
- 2026-09-10 updated: criterion names the Case's given, not now · raw/2026-09-10/ledger.md#case-40
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L38
- 2026-09-20 updated: the recut to the shape of case 193: the paragraph as Given/When/Then, the flag in context by 188, the pre-spec hook, tests/test_prespec.py in method as a field; pending for the reading (case 265.3) · [[decision-case-265.3]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L28
