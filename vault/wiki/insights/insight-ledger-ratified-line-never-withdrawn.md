---
type: insight
pattern: The ledger only grows, so a decision line of a first ratification is never withdrawn; a Case built again with a target dropped or renamed needs a new number whose line supersedes the old one, and no rule of case-guppi and no check of a rebuilt Case says so before the Spec hook finds the line with no item.
status: open
children: ["[[lesson-ledger-a-dropped-item-needs-a-superseding-sub-case]]", "[[lesson-case-build-renamed-a-slug-of-a-ratified-case-under-its-old-number]]", "[[lesson-case-build-splits-a-ratified-leaf-case]]", "[[lesson-ledger-rebuilt-create-keeps-the-stale-ref]]"]
severity: 1
addressed_by: "[[decision-case-725.1]]"
origin: raw/2026-10-05/1616/ledger.md#L41
sprint: migration
created: 2026-10-05
tags: [workflow, session, harness]
---

## Pattern

The ledger only grows: the hook appends no line it holds, and only a supersedes block retires an entry. In session 2300 the rebuilt 445.5 dropped a create whose line already stood in the ledger, and 445.7 took a new id that superseded it. In session 1616 case-guppi renamed the create of Case 663 and kept the number; the re-ratification added a second create line beside the first, the Spec hook refused the first line with no item in the plan, and Case 668 with {supersedes:case 663} replaced it. A target renamed or dropped in a ratified Case passes every check until the Spec hook.

## Proposal

A suggestion, not a decision. Let the check of a rebuilt Case compare its targets with the decision lines the ledger already holds for its number, and send back a target renamed or dropped with the line that a new number with a supersedes tag must carry; or say so in the frame of case-guppi (rule-ledger-line-withdrawn-on-re-ratification was deleted by case 671.2).

## History

- 2026-10-05 created · raw/2026-10-05/1616/ledger.md#L41
- 2026-10-05 updated: actioned: the check of the file case-guppi writes sends back a ratified Case built again without the item of one of its lines, with the new number and the marks (case 671.1) · [[decision-case-671.1]]
- 2026-10-07 updated: child lesson-case-build-splits-a-ratified-leaf-case added; open again, the pattern came back after case 671.1 (synthesis) · raw/2026-10-07/1804/ledger.md#L28
- 2026-10-08 updated: actioned: a ratified Case built again without one of its targets or in another shape goes back with a new number, and a second behaviour of a ratified Case with no sub-cases is built as a new Case beside it (cases 610.1, 671.1, 725.1) · [[decision-case-742]]
- 2026-10-09 updated: child lesson-ledger-rebuilt-create-keeps-the-stale-ref added, reopened (synthesis) · raw/2026-10-08/2352/ledger.md#L41
