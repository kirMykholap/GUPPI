---
type: decision
case: "736"
status: current
children: ["[[decision-case-736.1]]", "[[decision-case-736.2]]", "[[decision-case-736.3]]"]
origin: raw/2026-10-08/1547/ledger.md#case-736
sprint: migration
created: 2026-10-08
tags: [workflow, harness, tests, session, render]
---

## Problem

No step finds a live text of the vault that a test runs through a check a Case changes, and Work Mode runs only the test files the Spec names, so such a text breaks first at Retro, where the work can only be reverted.

## Recommend

- **Where should the missing step go?**
  - Recommended: (c) both, as two sub-cases: `case-guppi` reads the live texts a test runs through a changed check, and Work Mode runs `make test` in full after the last code task.
  - Answer: agreed, (c).
- **Does this Case also close the Insight?**
  - Recommended: (a) yes, set `insight-workflow-contract-change-leaves-its-derived-text-stale` `actioned` with `addressed_by` naming this Case.
  - Answer: agreed, (a).
- **Which Estimate checks the new step of `case-guppi`?**
  - Recommended: (a) a new Estimate, `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`; the existing one stays `passed`.
  - Answer: agreed, (a).
- **Which Estimate checks the full test run in Work Mode?**
  - Recommended: (a) replace the Criterion of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, with its `purpose` and `method` naming the full run.
  - Answer: agreed, (a).
- **How does the stop on a new red test fit `where-to-stop.md`?**
  - Recommended: (a) a seventh condition for Work Mode only, as a third sub-case, with the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` replaced; Retro keeps its revert.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/1547/ledger.md#case-736
