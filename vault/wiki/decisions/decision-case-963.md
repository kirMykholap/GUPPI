---
type: decision
case: "963"
status: current
defer: ["[[rule-estimates-schema]]"]
origin: raw/2026-10-31/0431/ledger.md#case-963
sprint: plugin
created: 2026-10-31
tags: [harness, render, schema]
---

## Context

At /hi of session 0431 the person asked whether an Estimate that checks one action should be told apart from one that promises a lasting behaviour, so that one-time Estimates leave after the close of their sprint and only behaviour stays. A scan of the frontmatter of the 332 live Estimates found 5 on the live sprint page, which go to the archive with it at the close, and few one-time checks on rules or entities, such as `estimate-guppi-keeps-no-defer-of-its-shape` and `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`; the 332 Criteria were not read one by one. A one-time Estimate on a page with `core: true` keeps that page `draft` while it is pending, and `ships` of `.guppi/guppi/ship.py` takes it into the clean version once it passes. The person liked both ways the main agent named, a one-time Estimate on the live sprint page and a marker in its frontmatter, said they may be joined, and put the item off to the next session.

## Problem

No Case of this session decides how a one-time Estimate is told apart from one that promises a lasting behaviour.

## Deferred

### [[rule-estimates-schema]]

Tell one-time Estimates apart from those that promise a lasting behaviour: a one-time Estimate targets the live sprint page and carries a marker such as once: true, so it leaves at the close of the sprint, keeps no page with core: true draft and does not ship; and a pass over the live Estimates sorts them; put off at /hi of session 0431

## History

- 2026-10-31 created · raw/2026-10-31/0431/ledger.md#case-963
