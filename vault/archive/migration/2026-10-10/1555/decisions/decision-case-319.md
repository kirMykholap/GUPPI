---
type: decision
case: "319"
status: archived
update: ["[[entity-sprint-migration]]"]
origin: raw/2026-09-22/1121/ledger.md#case-319
sprint: migration
created: 2026-09-22
tags: [sprint, workflow]
---

## Context

The architecture catches a duplicate three times, and all three are at the moment of the decision: `rule-ask` before a `create` without `ref`, `pre-spec` before the Spec is approved, and the index check of the librarian, who may turn a `create` into an `update`. Two things are missing. The vault query asks "does this exist" but not "what of this already exists that the thing could use"; and the relation "A uses B" is written nowhere: `parent`/`children` is decomposition, `applies_to`/`rules` (case 305) is Rule → Entity only, and an Entity → Entity edge does not exist. So nobody can ask what a change to a module breaks, and the next agent sees no example of reuse. The Backlog line "the product model … `ask-guppi` through Entities" (session 1119) is about the same thing but names neither the edge nor the check. Pages: `entity-sprint-migration` `draft`, changed in this session by 310.2 and 318; the change is in `## Backlog` and touches no Estimate (case 296).

## Problem

The shape of reuse was worked out in this session and is lost by the next one unless the Backlog names its cut.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-319
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
