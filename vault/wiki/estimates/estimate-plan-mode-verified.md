---
type: estimate
kind: QA
status: passed
target: "[[rule-plan-mode]]"
purpose: Across Plan Mode a create whose purpose the vault already carries is named in the Case before ratification, and the pre-spec hook runs before the plan is written, which is still written
method: make test-plan-mode, the pipeline over tests/test_spec.py and tests/test_prespec.py; the flagging one live reading by hand, written into the estimate line
checked: 2026-10-03
origin: raw/2026-09-09/ledger.md#case-19
sprint: migration
created: 2026-09-09
tags: [session, workflow]
---

## Criterion

When:
`case-guppi` builds a Case that proposes a `create` without a `ref` and runs the vault query first, and later the person approves the plan at `ExitPlanMode`.

Then:
A `create` for a page whose `purpose` an index line already carries is named in the `context` of the Case before ratification.
**＋** At `ExitPlanMode` the hook of `rule-prespec-hook` runs before the plan is written, and once it lets the call through, the hook of `rule-spec-capture` still writes the plan into the session's `spec.md`.

## Result

2026-10-03, at the /hi of session 1416: `make test-plan-mode` 200 passed; by hand, session 1341 (transcript 26e79919 and its case-guppi agent adf74989): Case 614 proposes `create entity-reading-probe` with no ref, the overlap staged on purpose; its case-guppi ran the Grep `^(purpose|deferred_by):` over vault/wiki/entities/ at 13:54:04, before its first answer; the Case shown at 14:05:27 names `entity-glossary` in its context and quotes its index line, whose purpose the test page repeats, and the person ratified it at 14:06:09; ExitPlanMode at 14:13:15 was let through after the prespec mark of 14:08:34, and raw/2026-10-03/1341/spec.md holds Case 614 and the four defers under `## Deferred`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-19
- 2026-09-10 updated: criterion names the Case's given, not now · raw/2026-09-10/ledger.md#case-40
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L38
- 2026-09-20 updated: the recut to the shape of case 193: the paragraph as Given/When/Then, the flag in context by 188, the pre-spec hook, tests/test_prespec.py in method as a field; pending for the reading (case 265.3) · [[decision-case-265.3]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L28
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the writer of the plan named; purpose set (case 493.2) · [[decision-case-493.2]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L6
