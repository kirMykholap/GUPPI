---
type: lesson
kind: error
root_cause: the `change` string of a Spec item is prose that lands in History and log.md verbatim, a body section lint reads like any other; the agent checked the quoted form in the Criterion it was fixing and not in the sentence describing the fix — every string of a `then` block that a page receives (`change`, `purpose`, `sections`) needs the code span, not only the section the Case is about
status: new
origin: raw/2026-09-20/0958/ledger.md#L1
sprint: migration
created: 2026-09-20
tags: [workflow, harness, librarian]
---

## Trigger

the `change` of Case 262 on `estimate-generate-renames` — "the two placeholders `[[decision-case-N]]` of the Criterion in code spans" — went into the page's History as written, and lint raised the same `ref: body names decision-case-N` the Case had just cured in the Criterion; the fourth time on this class (130.1, 140, 160)

## Root cause

the `change` string of a Spec item is prose that lands in History and log.md verbatim, a body section lint reads like any other; the agent checked the quoted form in the Criterion it was fixing and not in the sentence describing the fix — every string of a `then` block that a page receives (`change`, `purpose`, `sections`) needs the code span, not only the section the Case is about

## History

- 2026-09-20 created · raw/2026-09-20/0958/ledger.md#L1
- 2026-09-20 updated: the placeholder of the Trigger in a code span — the lesson no longer carries the bare link it is about (case 275) · [[decision-case-275]]
