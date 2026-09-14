---
type: decision
case: "96"
status: archived
defer: ["[[rule-synthesis]]"]
superseded_by: ["[[decision-case-108]]"]
origin: raw/2026-09-12/ledger.md#case-96
sprint: migration
created: 2026-09-12
tags: [harness, workflow, librarian]
---

## Context

Eighteen `clustered` lessons carry no `## Insight` section, five of them from the last
run. The synthesis sets the `insight` field in the frontmatter, and nothing writes the
section `lessons/schema.md` requires. They are 18 of lint's 128 schema findings.

## Problem

Either the synthesis entry carries the section, or the schema stops asking for it. Both
are a change of what a synthesis entry holds.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-96
- 2026-09-13 superseded by decision-case-108 · [[decision-case-108]]
- 2026-09-13 archived · superseded
- 2026-09-13 archived · cleanup
