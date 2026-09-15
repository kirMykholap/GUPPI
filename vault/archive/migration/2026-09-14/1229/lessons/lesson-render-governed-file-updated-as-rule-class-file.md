---
type: lesson
kind: error
root_cause: CLAUDE.md is both a Rule-class file, changed by hand through a file item, and a rendered file governed by rule-case-protocol; nothing says which of its sections is which, and pre-task does not check that a file item on a governed path comes with an update of the governing rule
status: archived
insight: "[[insight-workflow-contract-change-leaves-its-derived-text-stale]]"
origin: raw/2026-09-12/ledger.md#L12
sprint: migration
created: 2026-09-12
tags: [harness, render, workflow]
---

## Trigger

case 56 changed the Case protocol paragraph of CLAUDE.md by hand as a file update; rule-case-protocol, whose Render that paragraph is, was not updated; at the next /hi guppi render --check names CLAUDE.md, and a render would drop the ratified Retro sentence

## Root cause

CLAUDE.md is both a Rule-class file, changed by hand through a file item, and a rendered file governed by rule-case-protocol; nothing says which of its sections is which, and pre-task does not check that a file item on a governed path comes with an update of the governing rule

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L12
- 2026-09-12 updated: clustered by librarian: a change leaves its derived text stale, with lesson-estimates-criterion-stale-after-contract-change · raw/2026-09-12/ledger.md#L12
- 2026-09-14 insight section derived
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
