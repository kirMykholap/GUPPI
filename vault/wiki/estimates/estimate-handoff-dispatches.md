---
type: estimate
kind: QA
status: pending
target: rule-handoff
origin: raw/2026-09-10/ledger.md#case-38.3
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Context

A handoff written from the artifacts says nothing the artifacts do not; one that skips the librarian leaves the ledger unmaterialized.

## Criterion

After a live /handoff: the first turn's context holds git status --porcelain and
the skill stops on a dirty tree; event_log.md carries a handoff line; handoff.md
gained a document with the three sections, written without read-tool calls on the
artifacts; the librarian-guppi agent was dispatched with the date and its report
was shown unchanged; no commit followed.

## Method

one reading by hand at the first /handoff, recorded in the estimate line

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.3
