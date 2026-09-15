---
type: decision
case: "165.2"
status: archived
defer: ["[[rule-page-generation]]"]
superseded_by: ["[[decision-case-166.1]]"]
origin: raw/2026-09-15/1448/ledger.md#case-165.2
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger]
---

## Context

The derived sections of a Rule, Entity, Lesson and Insight — `## Estimates`, `## Children`, `## Parent`, `## Implementation`, `## Code`, `## Insight`, `## Addressed by` — copy the ref fields of the frontmatter as wikilinks. Since 148.1 the fields are quoted wikilinks that Obsidian's graph, backlinks and Bases see on their own; `target` of an Estimate already lives in the field alone, with no section. `generate` builds the sections at `create`, rebuilds two of them on `update`, derives two on every write; `cleanup` rebuilds two; the schemas require them; five live pages show a section that differs from its field (`rule-lint`, `rule-render-harness`, `rule-hook-registry` on `## Parent`; `rule-event-log`, `rule-ledger-write` on `## Implementation`), and lint is silent.

## Problem

Seven derived sections in five schemas, in `generate`, `cleanup`, `lint`, the tests and on every live and archived page are a copy that drifts and needs code to keep; removing them is a session of its own — schemas, scripts, a one-off migration over `wiki/` and `archive/`, and a supersedes of the parts of 114 and 164 that derive `## Insight` and `## Addressed by`. The owner chose the removal over deriving the sections on every write (165.1, not taken).

## History

- 2026-09-15 created · raw/2026-09-15/1448/ledger.md#case-165.2
- 2026-09-15 superseded by decision-case-166.1 · [[decision-case-166.1]]
- 2026-09-15 archived · superseded
- 2026-09-15 archived · cleanup
