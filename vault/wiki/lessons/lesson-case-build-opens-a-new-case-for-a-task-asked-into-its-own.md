---
type: lesson
kind: error
root_cause: case-guppi may open a new top-level Case where the main agent named an existing one, and the sibling Cases built again in parallel learn the new id only after every case-guppi has answered
status: new
origin: raw/2026-10-16/0104/ledger.md#L20
sprint: plugin
created: 2026-10-16
tags: [case-build, prespec]
---

## Trigger

at /pre-spec the case-guppi of Case 847, asked to take the push stop: task into Case 847, built a new Case 850 and left Case 847 unchanged, while Cases 841, 843 and 846, built again in the same message, named Case 847 as the holder of the push and went back a second time

## Root cause

case-guppi may open a new top-level Case where the main agent named an existing one, and the sibling Cases built again in parallel learn the new id only after every case-guppi has answered

## History

- 2026-10-16 created · raw/2026-10-16/0104/ledger.md#L20
