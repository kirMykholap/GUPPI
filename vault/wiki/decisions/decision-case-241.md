---
type: decision
case: "241"
status: current
create: ["[[entity-sprint]]"]
update: ["[[entity-sprint-migration]]", "[[rule-sprint]]", glossary]
origin: raw/2026-09-18/1252/ledger.md#case-241
sprint: migration
created: 2026-09-18
tags: [sprint, workflow, session, harness, librarian]
---

## Context

`entity-sprint-migration` is the one live Entity, `kind: MOC` with empty `children`; its `estimates` are the Definition of done, its `## Milestones` the Slices (cases 209.2, 229.1). `guppi sprint` finds the page by the prefix `entity-sprint-` (`sprint_page` in `guppi/sprint.py`); the slug `entity-sprint`, without the dash, does not match the prefix — the code does not change. The glossary (the Sprint row) and the Purpose of `rule-sprint` call the sprint "an Entity MOC `entity-sprint-<id>`". By the definitions of 240.1 the sprint "migration" is a thing with no parts named, a Leaf; the kind "sprint" is a MOC over it. `generate` writes `children` on a parent only at a `create` with `ref`, not at an `update` of the child — so `children` of `entity-sprint` and `parent` of `entity-sprint-migration` are written in the blocks here, against the sentence of `case-schema.md` that calls them derivable — derivable only on the `ref` path, which an existing child has no way to take. The vault asked: `entity-sprint` is free, live and archive; the near pages are `entity-sprint-migration` and `rule-sprint`; no MOC over the sprints exists; the tags `sprint`, `workflow`. The Case touches the sprint pages, the glossary and the Purpose of `rule-sprint`; no Estimate.

## Problem

The sprint by id is recorded as a MOC without children, and the kind "sprint" does not exist; the next sprint has nothing to hang on, and the page contradicts the definition of 240.1.

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#case-241
