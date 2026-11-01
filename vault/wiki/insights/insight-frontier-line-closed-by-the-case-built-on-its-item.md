---
type: insight
pattern: the main agent closes a Frontier line `· case N` because a Case was built on its item and ratified, not because a decision line of that Case takes the item off its list — an update of the sprint page for a sprint item, a decision line that names the page and retires its defer for a backlog item — so guppi prespec --check finds the closer false and the line is closed again
status: open
children: ["[[lesson-frontier-sprint-line-closed-by-a-case-that-updates-no-sprint-page]]", "[[lesson-frontier-closed-a-backlog-item-deferred-again-as-a-case]]", "[[lesson-frontier-backlog-line-closed-by-a-case-that-keeps-its-defer]]"]
severity: 3
origin: raw/2026-11-01/1721/ledger.md#L34
sprint: plugin
created: 2026-11-01
tags: [orchestration, session, prespec, sprint]
---

## Pattern

Three sessions closed a Frontier line by the Case built on its item where that Case did not take the item off its list: 1913 closed the milestone line C1 `· sprint · case 769` with no update of the sprint page; 1713 closed the backlog line C9 `· case 934` where Case 934 only deferred rule-spec-capture again; 1721 closed the backlog line C8 `· case 988` where the person chose in Case 988 that the defer of rule-ratification stays. Each time guppi prespec --check printed frontier findings and the line was closed again.

## Proposal

A suggestion: orchestration.md could state once, for every kind of Frontier line, that a line closes `· case N` only when a decision line of Case N does what ends that kind of item, and otherwise closes by the closer of an item left as it stands; or the main agent could run the frontier check of guppi prespec --check right after it closes a line.

## History

- 2026-11-01 created · raw/2026-11-01/1721/ledger.md#L34
