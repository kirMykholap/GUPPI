---
type: estimate
kind: QA
status: pending
target: rule-skill-hi
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Context

The whole point of the skill is that the context is present before the agent's first turn.
A read-tool call for the brief or the sprint means a substitution did not resolve, and the
frame of the skill is broken regardless of which child failed.

## Criterion

After `/hi` the context holds `sprint.md`, `brief.md`, the current branch, `git status` and
the issue list (or `gh`'s message) with no read-tool call having occurred, and
`raw/<date>/event_log.md` carries a `hi` line.

## Method

One reading at a session start, by hand, recorded in the estimate line.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
