---
type: lesson
kind: error
root_cause: the bare-link check of case 264.2 accepts a slug a create of the same plan carries, but a Decision page is written by generate and no create carries it, so a Case cannot link its own Decision page; an earlier Spec (case 256) did so before the check existed
status: archived
insight: "[[insight-workflow-case-schema-silent-on-what-the-scripts-accept]]"
origin: raw/2026-09-25/1228/ledger.md#L36
sprint: migration
created: 2026-09-25
tags: [session, workflow]
---

## Trigger

Case 419.3 set addressed_by to "[[decision-case-419.3]]" on an Insight; the Stop hook of rule-spec-write refused it after the ratification as a wikilink that names no page

## Root cause

the bare-link check of case 264.2 accepts a slug a create of the same plan carries, but a Decision page is written by generate and no create carries it, so a Case cannot link its own Decision page; an earlier Spec (case 256) did so before the check existed

## History

- 2026-09-25 created · raw/2026-09-25/1228/ledger.md#L36
- 2026-09-25 updated: clustered into insight-workflow-case-schema-silent-on-what-the-scripts-accept · raw/2026-09-25/1228/ledger.md#L36
- 2026-09-25 archived · insight actioned
- 2026-09-25 archived · cleanup
