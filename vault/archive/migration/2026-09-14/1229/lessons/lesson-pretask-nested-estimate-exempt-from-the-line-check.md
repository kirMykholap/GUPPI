---
type: lesson
kind: error
root_cause: index.md §5 requires a paired create line for a Leaf's Estimate and materialize.find_item builds the nested entry only from that line, but pretask.items_of marks a nested estimate as covered by its parent's line "since case 53.1" — a Case about lessons having no paired Estimate, not about Leaf creates — so the check stayed silent when the agent wrote no paired line, and the two Estimates were signed in the Spec and never logged
status: archived
insight: insight-ledger-line-written-unchecked
origin: raw/2026-09-12/ledger.md#L109
sprint: migration
created: 2026-09-12
tags: [harness, workflow]
---

## Trigger

F23 of session J: estimate-governed-files-hook-refuses (case 59.6) and estimate-claude-md-rendered (case 59.8) sit as nested estimate blocks under the create of their Rule in the then blocks of the Spec of session I; both Rule pages exist with estimates: [], neither Estimate has a yaml entry or a page, and the ledger of session I holds no create line for either; guppi pretask --check of session I reported nothing

## Root cause

index.md §5 requires a paired create line for a Leaf's Estimate and materialize.find_item builds the nested entry only from that line, but pretask.items_of marks a nested estimate as covered by its parent's line "since case 53.1" — a Case about lessons having no paired Estimate, not about Leaf creates — so the check stayed silent when the agent wrote no paired line, and the two Estimates were signed in the Spec and never logged

## Insight

- [[insight-ledger-line-written-unchecked]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L109
- 2026-09-12 updated: clustered by librarian: a ledger line is unchecked until materialize, with lesson-ledger-preview-in-ratification-taken-for-the-record · raw/2026-09-12/ledger.md#L109
- 2026-09-14 insight section derived
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
