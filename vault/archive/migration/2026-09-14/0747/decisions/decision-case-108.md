---
type: decision
case: "108"
status: archived
defer: [rule-synthesis]
supersedes: [decision-case-96]
superseded_by: [decision-case-114]
origin: raw/2026-09-13/ledger.md#case-108
sprint: migration
created: 2026-09-13
tags: [harness, workflow, librarian]
---

## Context

Twenty `clustered` lessons carry no `## Insight` section. The synthesis sets the `insight` field in the frontmatter, and nothing writes the section `lessons/schema.md` requires. They are 20 of lint's 125 schema findings. Deferred as 96 in session K, with its `purpose` cut short in the yaml and on `decision-case-96`.

## Problem

Either the synthesis entry carries the section, or the schema stops asking for it. Both are a change of what a synthesis entry holds.

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#case-108
- 2026-09-14 superseded by decision-case-114 · [[decision-case-114]]
- 2026-09-14 archived · superseded
- 2026-09-14 archived · cleanup
