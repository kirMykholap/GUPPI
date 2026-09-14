---
type: lesson
kind: error
root_cause: a decision update on a Rule page has no step that lists the Estimates whose criterion quotes the changed wording; until lint or the generator does it, the acknowledging reply must grep estimates/ for the words the contract dropped
status: clustered
insight: insight-workflow-contract-change-leaves-its-derived-text-stale
origin: raw/2026-09-09/ledger.md#L49
sprint: migration
created: 2026-09-09
tags: [workflow, ledger]
---

## Trigger

case 15.1 redefined a ledger record as a line in a LEDGER block; the criteria of estimate-session-start-context and estimate-case-protocol-loaded still described the bare-line contract and the first stopped discriminating a session with /hi from one without; found by hand while filling their Result, fixed by cases 16.1 and 16.2

## Root cause

a decision update on a Rule page has no step that lists the Estimates whose criterion quotes the changed wording; until lint or the generator does it, the acknowledging reply must grep estimates/ for the words the contract dropped

## Insight

- [[insight-workflow-contract-change-leaves-its-derived-text-stale]]

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#L49
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-12 updated: clustered by librarian: a change leaves its derived text stale, with lesson-render-governed-file-updated-as-rule-class-file · raw/2026-09-12/ledger.md#L12
- 2026-09-14 insight section derived
- 2026-09-14 updated: tags filled (case 113) · [[decision-case-113]]
