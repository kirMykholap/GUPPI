---
type: decision
case: "354.4"
status: archived
update: ["[[rule-brief]]", "[[estimate-brief-written]]"]
origin: raw/2026-09-23/0034/ledger.md#case-354.4
sprint: migration
created: 2026-09-23
tags: [harness, workflow, librarian]
---

## Context

A session that passes over a milestone item closes its Frontier line `[-] … · sprint` (case 310.5). No page keeps a trace of it: `deferred_by` does not grow, and `frontier.md` goes to the archive with its session. `rule-work-mode` and `rule-subagent-guppi` have stood in Slice 3b since 2026-09-12: 19 defers before 310.5 and one pass by `· sprint` after it. The trace of these passes is only in the 33 archived `frontier.md` files.
`rule-sprint` stands `built` and changes Milestones and Backlog only by the `update` of a Case; `rule-page-generation` stands `draft`, and `generate` is the only writer to `wiki/`; the vault answers that no page sets a threshold or moves an item by itself, and that the three counts of today are separate. The Estimates of `rule-sprint` — `estimate-sprint-renders-the-backlog` on the render, `estimate-sprint-checks-the-file` on `--check`, `estimate-sprint-ticks-the-spec` on the ticks — do not speak of a move and are not touched; the move is a step after the cascade, so `estimate-generate-cascades` is not touched.

## Problem

A sprint item can be passed over without end, and nothing takes it off the agenda. A script must count the passes in a row and move the item to the Backlog at three, with no judgment of the agent.

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#case-354.4
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
