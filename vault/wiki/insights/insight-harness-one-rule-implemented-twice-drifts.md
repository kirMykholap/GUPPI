---
type: insight
pattern: A judgment the pipeline makes in two places is implemented twice — a check re-states what a writer, a ticker or another check does — and the two copies drift apart, with no test about the difference between them.
status: actioned
children: ["[[lesson-prespec-a-second-copy-of-a-matching-rule-drifts]]", "[[lesson-lint-decision-target-archived-counts-as-missing]]"]
severity: 0
addressed_by: "[[decision-case-360]]"
origin: raw/2026-09-22/2046/ledger.md#L37
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Pattern

Two lessons where one rule lived in two implementations and they drifted.

`lesson-lint-decision-target-archived-counts-as-missing`: `check_decision` resolved a
`target_slug` against the live pages while `check_refs` resolved every other slug against live
and archived pages. After the librarian archived the 21 Estimates of Cases 53.1 and 53.2, lint
reported 25 decision findings for targets that are archived and whose decisions are current.

`lesson-prespec-a-second-copy-of-a-matching-rule-drifts`: `check_tasks` matched a reading's task
line by substring while `generate` ticked it by `READ_LINE`, and the classification of the four
forms of a `method` was open-coded in `check_method` where pre-spec needed the same judgment
(cases 327, 331). The repair was to import the one pattern in both places —
`generate.READ_LINE`, `lint.names_a_form` — and `generate.replace_once` was lifted out for the
same reason when pre-spec came to simulate the pairs of a Spec (case 351).

In both, the suite was green while the copies disagreed: every test was about one side.

## Proposal

A suggestion, not a decision.

Where a check judges the same text as a writer, a ticker or another check, the pattern or the
predicate lives in one module and both sides import it; a second implementation of the one rule
is a defect on the day it is written, not on the day it disagrees.

Where the two sides cannot share the code, a test runs both over the same input and asserts
they answer alike, so the drift fails the suite instead of a session.

Neither half is decided here.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#L37
- 2026-09-23 updated: actioned by rule-one-judgment-one-implementation (case 360) · [[decision-case-360]]
