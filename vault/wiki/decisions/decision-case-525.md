---
type: decision
case: "525"
status: current
defer: ["[[rule-documentation]]"]
supersedes: ["[[decision-case-517]]"]
origin: raw/2026-09-29/1753/ledger.md#case-525
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness, librarian, render]
---

## Context

`estimate-documentation-completes` failed: the librarian's run of ff62585 read beyond its input list. It read the tail of `log.md`, the head of the old `brief.md`, a git diff of `sprint.md` and `backlog.md`, and a grep of `sprint.md`. Case 517 of session 1432 put the item off. The run d8c1f17 of that session reported two more breaks of its own. It listed a folder under `vault/archive/`, and it read the head of the old `brief.md`. The person put the item off again at the close of Plan Mode in session 1753.

## Problem

The librarian reads files outside its input list, and `estimate-documentation-completes` stays failed.

## Deferred

### [[rule-documentation]]

The librarian reads beyond its input list: the run ff62585 read the tail of log.md, the old brief.md, git diffs and a grep of sprint.md; the run d8c1f17 listed an archive folder and read the old brief.md; estimate-documentation-completes stays failed

## History

- 2026-09-29 created · raw/2026-09-29/1753/ledger.md#case-525
