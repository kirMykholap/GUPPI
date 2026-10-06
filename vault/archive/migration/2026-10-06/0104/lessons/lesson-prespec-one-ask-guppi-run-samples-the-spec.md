---
type: lesson
kind: error
root_cause: /pre-spec dispatches ask-guppi once per session and takes its answer as the check of the whole Spec, while one model run over some twenty sub-cases returns a sample of the findings, not all of them; and a Case built again on a finding is checked only by its own case-guppi (case 561.1), so a fix, and a sub-case born of a finding, reach the approved Spec with no second reading against the vault
status: archived
insight: "[[insight-prespec-after-findings-loop-unruled]]"
origin: raw/2026-10-04/1934/ledger.md#L4
sprint: migration
created: 2026-10-04
tags: [workflow, session]
---

## Trigger

at the /pre-spec of session 1934 ask-guppi checked the conserved Spec of session 1439, whose own /pre-spec had run ask-guppi once and found 10 findings, and found 12 findings in Cases 627-629; 8 of them stand on sub-cases that stood in the plan at the 1439 run (627.1, 627.2, 628.1, 628.2, 628.3, 628.7, 628.9) and that run did not name them; 2 stand on 628.10 and 628.12, written at 19:32 from the 1439 findings after that run; 1 is the fix of a 1439 finding, the selector -k session_clash of 629.1, which -k clash still matches as a substring

## Root cause

/pre-spec dispatches ask-guppi once per session and takes its answer as the check of the whole Spec, while one model run over some twenty sub-cases returns a sample of the findings, not all of them; and a Case built again on a finding is checked only by its own case-guppi (case 561.1), so a fix, and a sub-case born of a finding, reach the approved Spec with no second reading against the vault

## History

- 2026-10-04 created · raw/2026-10-04/1934/ledger.md#L4
- 2026-10-04 updated: clustered under insight-prespec-after-findings-loop-unruled (synthesis) · raw/2026-10-04/1934/ledger.md#L4
- 2026-10-06 archived · insight actioned
- 2026-10-06 archived · cleanup
