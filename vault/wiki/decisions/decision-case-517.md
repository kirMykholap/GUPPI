---
type: decision
case: "517"
status: current
defer: ["[[rule-documentation]]"]
origin: raw/2026-09-29/1432/ledger.md#case-517
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness, librarian, render]
---

## Context

The reading of `estimate-documentation-completes` failed: the librarian's run of commit ff62585 read beyond its list — the tail of `log.md`, the head of the old `brief.md`, a git diff of `sprint.md` and `backlog.md`, a grep of `sprint.md` and a count of `[x]` in the 0137 Spec. The brief of that run carried it to session 1432 as a Case item. In session 1432 the person put it off before any Case was built on it.

## Problem

Whether the librarian's list of reads is too narrow for what its run needs, or the run strays from it, and what changes: the list in `rule-documentation` or the run.

## Deferred

### [[rule-documentation]]

Decide why the librarian's run reads beyond its list — the tail of log.md, the old brief, a git diff of sprint.md and backlog.md, a count of the Spec's ticks — and whether the list or the run changes; the reading of estimate-documentation-completes failed on the run of ff62585; put off in session 1432

## History

- 2026-09-29 created · raw/2026-09-29/1432/ledger.md#case-517
