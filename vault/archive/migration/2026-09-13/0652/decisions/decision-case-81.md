---
type: decision
case: "81"
status: archived
defer: [rule-case-protocol]
superseded_by: [decision-case-86]
origin: raw/2026-09-12/ledger.md#case-81
sprint: migration
created: 2026-09-12
tags: [session, workflow, ledger]
---

## Context

Case 72.1 says a Leaf `create` carries `method`, `kind` (`QA` by default) and `slug`
(only on a collision). On the item `kind` and `slug` already belong to the target
page, so the code of 72.3 and 72.5 and the texts of `case-schema.md`, `index.md` §7
and the glossary write `estimate_kind` and `estimate_slug`. The agent resolved the
fork in Work Mode instead of returning it.

## Problem

The ratified wording and the written wording differ in two field names; nobody signed
`estimate_kind` and `estimate_slug`. The next Plan Mode ratifies them or reverts to a
form where `kind` and `slug` are unambiguous.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-81
- 2026-09-12 superseded by decision-case-86 · [[decision-case-86]]
- 2026-09-13 archived · superseded
- 2026-09-13 archived · cleanup
