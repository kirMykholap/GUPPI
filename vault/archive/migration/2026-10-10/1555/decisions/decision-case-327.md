---
type: decision
case: "327"
status: archived
update: ["[[rule-prespec]]", "[[estimate-prespec-checks-the-plan]]"]
origin: raw/2026-09-22/1724/ledger.md#case-327
sprint: migration
created: 2026-09-22
tags: [session, workflow, harness, tests]
---

## Context

`check_tasks` finds the task line of an Estimate by substring: `slug in line` over every line of the `tasks` block. `generate` matches otherwise — `READ_LINE` takes the first backticked slug of a `- [ ] read …` line and compares it for equality. The gap passes two things: a `read` line naming several Estimates (line 959 of the 1121 Spec names three), and an Estimate the block names by an `update` line alone, with no reading line at all. In the first the reading of the first slug closes the box for all three, while the other readings tick nothing and say nothing; in the second there is no reading line and pre-spec is content. The form — one line per reading, by its slug — is written in the Case schema; nothing guards it.
`rule-prespec` stands `built` with six Estimates, one per finding; the promise of the `tasks` block is `estimate-prespec-checks-the-plan`, `passed`, whose Criterion also covers the finding for a missing `tasks` block, so the Case changes a part of it with a `replace` pair (case 296). Case 325.1 of this session writes its own pair into the same Render, at the clause that follows this one; the anchors do not overlap.

## Problem

Two scripts disagree on what the task line of a reading is, and both forms fall through the gap: a line of three slugs, and an Estimate with no line of its own. The check must judge as the ticker ticks.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-327
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
