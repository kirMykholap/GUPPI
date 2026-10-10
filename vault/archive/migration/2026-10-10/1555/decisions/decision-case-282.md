---
type: decision
case: "282"
status: archived
update: ["[[rule-retro]]", "[[estimate-retro-loads]]"]
origin: raw/2026-09-20/1749/ledger.md#case-282
sprint: migration
created: 2026-09-20
tags: [session, workflow, harness, render]
---

## Context

Retro counts the unticked `tasks` lines of the Spec: the page lines, the `render`, `sprint` and `read` lines with their reading in the ledger wait for the librarian, the rest is debt (233.2, 253.2, 270.3). When a Case of the session is superseded by another (`{supersedes:case N}` in the ledger), its yaml entries are marked `superseded_by` and never applied, its lines in the Spec stay `[ ]` for good — and Retro counts them as debt: the 1308 handoff passed line 783 of the superseded 274.2 to the next session as a check. In this session the same waits for 278.
`rule-retro` `draft`, `estimate-retro-loads` `pending` by 270.3 and read at this session's Retro — the reading covers the new line too; the other Estimates of `rule-retro` untouched; an `update` with a `ref`, no vault query due. Found by pre-spec of this session.

## Problem

The lines of a Case whose work moved into the superseding Case are counted as a debt that does not exist.

## History

- 2026-09-20 created · raw/2026-09-20/1749/ledger.md#case-282
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
