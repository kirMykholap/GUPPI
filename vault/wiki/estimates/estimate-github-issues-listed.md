---
type: estimate
kind: QA
status: pending
target: rule-github-issues
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

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
