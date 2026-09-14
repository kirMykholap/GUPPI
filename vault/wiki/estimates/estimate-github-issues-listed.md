---
type: estimate
kind: QA
status: passed
target: "[[rule-github-issues]]"
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness, github]
---

## Context

`gh` fails on authentication, unlike anything else in the skill, and on 2026-09-09 it is
not logged in. The rule is satisfied by the list or by the named reason there is none;
what must not happen is a silent blank.

## Criterion

The open-issue list, or `gh`'s own message naming why there is none, is in context and
the skill completes either way.

## Method

One reading at a session start, by hand, in the current `gh` state.

## Result

Passing. `gh`'s own message (`To get started with GitHub CLI, please run: gh auth
login`) was in context and the skill completed (2026-09-09, session B).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
