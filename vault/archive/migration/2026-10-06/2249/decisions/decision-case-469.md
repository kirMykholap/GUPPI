---
type: decision
case: "469"
status: archived
defer: ["[[rule-page-generation]]"]
superseded_by: ["[[decision-case-683]]"]
origin: raw/2026-09-27/2050/ledger.md#case-469
sprint: migration
created: 2026-09-27
tags: [harness, workflow, ledger]
---

## Context

After case 467.3, `generate.clear_deferred_by` clears a defer only from the pages the superseding Case names, so a Decision that deferred two pages can be superseded twice, by two Cases. The cascade archives a superseded Decision in the run of its first supersede, and `guppi cleanup` moves it to `vault/archive/`. At the second supersede, `generate.decision` finds the page in the archive and sets its `status` to `superseded` again. `cleanup` moves a page whose status is no longer `archived` back to `vault/wiki/decisions/`, and the cascade of the next run archives it again. The page makes a round trip and gains two History lines, with no change of meaning.

## Problem

Whether a supersede of an archived Decision keeps its `archived` status and only appends to `superseded_by`, or the round trip stays as it is.

## Deferred

### [[rule-page-generation]]

A supersede of a Decision already archived keeps it archived and only appends the superseding Case to its superseded_by, so cleanup does not bring it back from the archive (seen in session 2050, after case 467.3)

## History

- 2026-09-27 created · raw/2026-09-27/2050/ledger.md#case-469
- 2026-10-06 superseded by decision-case-683 · [[decision-case-683]]
- 2026-10-06 archived · superseded
- 2026-10-06 archived · cleanup
