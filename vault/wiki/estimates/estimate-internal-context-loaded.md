---
type: estimate
kind: QA
status: passed
target: rule-internal-context
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Context

`@`-imports inside a skill body are the one mechanism here that the old harness never
used; whether they expand the way they do in `CLAUDE.md` is exactly what this check
settles.

## Criterion

The text of `sprint.md` and `brief.md` is present in the first turn's context.

## Method

One reading at a session start, by hand.

## Result

Passing. Both texts were present in the first turn, expanded by the `@`-imports inside
the skill body (2026-09-09 16:11, session B).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
