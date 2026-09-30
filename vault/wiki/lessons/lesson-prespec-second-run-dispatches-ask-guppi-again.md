---
type: lesson
kind: error
root_cause: the skill pre-spec dispatches ask-guppi at every run and says nothing of a run after fixes, so a second run checks the whole plan again instead of only the Cases built again, and the person is not told the cost before it starts
status: clustered
insight: "[[insight-prespec-after-findings-loop-unruled]]"
origin: raw/2026-09-30/2042/ledger.md#L36
sprint: migration
created: 2026-09-30
tags: [workflow, session]
---

## Trigger

in session 2042 /pre-spec was run a second time after the Cases were built again on its findings, the main agent dispatched ask-guppi over the whole plan again for eight minutes, and the person asked why it was called again

## Root cause

the skill pre-spec dispatches ask-guppi at every run and says nothing of a run after fixes, so a second run checks the whole plan again instead of only the Cases built again, and the person is not told the cost before it starts

## History

- 2026-09-30 created · raw/2026-09-30/2042/ledger.md#L36
- 2026-09-30 updated: clustered under insight-prespec-after-findings-loop-unruled (synthesis) · raw/2026-09-30/2042/ledger.md#L36
