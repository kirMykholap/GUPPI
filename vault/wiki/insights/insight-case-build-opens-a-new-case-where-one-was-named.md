---
type: insight
pattern: case-guppi opens a new top-level Case under a new number where the main agent named an existing Case to change, so the named Case stays as it was and the Cases that name it are built again
status: open
children: ["[[lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own]]", "[[lesson-case-build-rebuilds-a-ratified-case-under-a-new-number-in-plan-mode]]"]
severity: 2
origin: raw/2026-10-16/0342/ledger.md#L20
sprint: plugin
created: 2026-10-16
tags: [case-build, prespec]
---

## Pattern

Two lessons, one cause. In session 0104 the case-guppi of Case 847, asked at /pre-spec to take the push stop task into Case 847, built a new Case 850 and left Case 847 unchanged, so the sibling Cases that named Case 847 went back a second time. In session 0342 the case-guppi of Case 851, sent the /pre-spec findings on that Case ratified in Plan Mode, wrote case-856.md with supersedes marks under an id no guppi caseid printed, and the main agent sent it back to rebuild under 851. In both case-guppi put a new Case number where the main agent had named the Case to change.

## Proposal

One sentence in rule-case-build that case-guppi builds a change under the Case the main agent names, and that a new top-level Case and its id come only from the main agent by guppi caseid. A suggestion, not a decision.

## History

- 2026-10-16 created · raw/2026-10-16/0342/ledger.md#L20
