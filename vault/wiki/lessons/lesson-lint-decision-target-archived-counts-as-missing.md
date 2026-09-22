---
type: lesson
kind: error
root_cause: check_decision, written in session H for case 52.1, looks a target_slug up in by_slug, the live pages, while check_refs resolves every other slug against live and archived pages; a decision stays current when its target is archived, so the lookup must use the same known set; one-line fix under the line of case 52.1
status: clustered
insight: "[[insight-harness-one-rule-implemented-twice-drifts]]"
origin: raw/2026-09-11/ledger.md#L78
sprint: migration
created: 2026-09-11
tags: [harness, workflow]
---

## Trigger

after the librarian archived the 21 Estimates of Cases 53.1 and 53.2, guppi lint reported 25 decision findings "target_slug … names no live page" on decision-case-47, 48, 53.1 and 53.2, whose targets are those archived pages

## Root cause

check_decision, written in session H for case 52.1, looks a target_slug up in by_slug, the live pages, while check_refs resolves every other slug against live and archived pages; a decision stays current when its target is archived, so the lookup must use the same known set; one-line fix under the line of case 52.1

## History

- 2026-09-12 created · raw/2026-09-11/ledger.md#L78
- 2026-09-23 updated: clustered by librarian: one rule of the pipeline implemented twice and drifting, with lesson-prespec-a-second-copy-of-a-matching-rule-drifts · raw/2026-09-22/2046/ledger.md#L37
