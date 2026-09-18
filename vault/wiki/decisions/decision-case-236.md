---
type: decision
case: "236"
status: current
update: ["[[rule-sprint]]", "[[estimate-sprint-renders-the-backlog]]"]
origin: raw/2026-09-18/1252/ledger.md#case-236
sprint: migration
created: 2026-09-18
tags: [session, workflow, harness, librarian, sprint]
---

## Context

`rule-sprint` (`draft`) governs `guppi/sprint.py`: `guppi sprint` writes `vault/wiki/sprint.md` from the page `entity-sprint-<id>`; a closed milestone is one line `### [x] <name>`, the current one renders whole with its items, statuses and `deferred_by`, each later one is one line `### [ ] <name> — N items` (case 229.2). Today the line of Slice 4 says "1 item" and Slice 5 "3 items", and the reader of `sprint.md` cannot see what the items are without opening the page. The page holds them word for word; only the render loses them. The Case touches one Estimate, `estimate-sprint-renders-the-backlog` (`pending`); it does not touch `estimate-sprint-checks-the-file` — `--check` compares this same render and does not change.

## Problem

The collapsed line exists so that `/hi` takes the Frontier from the current milestone only and the file stays short, but a count without names hides the plan: what stands in the queue after Slice 3b cannot be read from `sprint.md`. The question is how to show the items of a later milestone without blurring the edge of the current one.

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#case-236
