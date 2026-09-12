---
type: lesson
kind: error
root_cause: pre-task runs once, before Work Mode, against the code as it stands then; a Case that changes the checker leaves its own Spec judged by the old one, and nothing re-runs the check after the new code exists, so the Spec that ratifies a rule is the one document the rule never sees
status: new
origin: raw/2026-09-12/ledger.md#L209
sprint: migration
created: 2026-09-12
tags: [harness, workflow, session]
---

## Trigger

cases 85.1, 88.1, 89.4 and 87 of this Spec change the contract of a page with two Estimates and named no estimate_slug; guppi pretask --check passed them at the close of Plan Mode, and the fifth form finding that would have caught them was written in Work Mode by case 90.2 of the same Spec; four items had to be added to a Spec the owner had already approved

## Root cause

pre-task runs once, before Work Mode, against the code as it stands then; a Case that changes the checker leaves its own Spec judged by the old one, and nothing re-runs the check after the new code exists, so the Spec that ratifies a rule is the one document the rule never sees

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L209
