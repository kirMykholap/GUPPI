---
type: rule
kind: MOC
purpose: Prevents a session being handed over without a settled account of what happened
status: draft
children: [rule-retro, rule-retro-commit, rule-handoff]
estimates: [estimate-end-of-work-order]
origin: raw/2026-09-10/ledger.md#case-38
sprint: migration
created: 2026-09-10
tags: [session, workflow]
---

## Purpose

Prevents a session being handed over without a settled account of what happened. It
also prevents the librarian's writes from being indistinguishable from the
session's own, by forcing a commit between the two. Three steps: the Retro
conversation, the commit gate on the way to handoff, then handoff itself.

## Estimates

- [[estimate-end-of-work-order]]

## Children

1. [[rule-retro]]
2. [[rule-retro-commit]]
3. [[rule-handoff]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
- 2026-09-10 estimate estimate-end-of-work-order added · raw/2026-09-10/ledger.md#case-38
