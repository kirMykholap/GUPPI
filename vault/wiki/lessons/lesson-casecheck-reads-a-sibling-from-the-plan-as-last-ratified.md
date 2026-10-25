---
type: lesson
kind: error
root_cause: "`other_blocks` of .guppi/guppi/casecheck.py takes the `then` block of another Case from the plan, where Case 883 stood as ratified before /pre-spec, while `unread_sentences` looks for the part that Case wrote in a Read of its current file `cases/case-883.md`, which /pre-spec had changed, so the part of a sibling built again can never be found until that sibling is ratified again"
status: new
origin: raw/2026-10-17/2307/ledger.md#L48
sprint: plugin
created: 2026-10-17
tags: [case-build, hooks, prespec]
---

## Trigger

at /pre-spec of session 2307 the Stop check of rule-case-check refused the showing of Case 881 three times with "case 881.24: entity-glossary: the sentence around a pair was not read whole", though its case-guppi read `entity-glossary` and the file of Case 883 whole each in one Read

## Root cause

`other_blocks` of .guppi/guppi/casecheck.py takes the `then` block of another Case from the plan, where Case 883 stood as ratified before /pre-spec, while `unread_sentences` looks for the part that Case wrote in a Read of its current file `cases/case-883.md`, which /pre-spec had changed, so the part of a sibling built again can never be found until that sibling is ratified again

## History

- 2026-10-26 created · raw/2026-10-17/2307/ledger.md#L48
