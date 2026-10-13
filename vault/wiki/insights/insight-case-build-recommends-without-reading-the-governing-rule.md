---
type: insight
pattern: case-guppi builds its recommended option from the item's own words and does not check it against the rule of the vault that governs what the option changes, so the recommendation breaks that rule and the Case is built again
status: actioned
children: ["[[lesson-case-build-made-an-always-red-check-required]]", "[[lesson-case-build-recommended-a-trigger-that-keeps-the-defect]]"]
severity: 0
addressed_by: "[[decision-case-798.1]]"
origin: raw/2026-10-12/2349/ledger.md#L57
sprint: plugin
created: 2026-10-12
tags: [case-build, ci, github, prespec]
---

## Pattern

Two lessons, one cause. In session 1449 case-guppi recommended for Case 777 to drop only the transcript words from a When line, judged against the item's words and not against the rule on methods in rule-case-protocol (case 670.4), and the Case was built again as Case 779. In session 2349 case-guppi recommended style, test and lint as required checks on main without reading what make lint prints at the Baseline or rule-lint, which calls lint a signal and not a gate, and Case 794 replaced 787.1. In both the recommended option was not read against the rule that governs what it changes.

## Proposal

One sentence in rule-case-build: before case-guppi recommends an option, it names the rule pages that govern what the option changes and the output of the Baseline that the option rests on, and reads each against the option; context names them. A suggestion, not a decision.

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#L57
- 2026-10-13 updated: actioned: case-guppi reads the rule that governs what each option changes on every item, and the last output of a check an option rests on (cases 798.1, 798.2) · [[decision-case-798.1]]
