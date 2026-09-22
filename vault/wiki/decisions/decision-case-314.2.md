---
type: decision
case: "314.2"
status: current
create: ["[[estimate-prespec-binds-a-sprint-line]]"]
update: ["[[rule-prespec]]"]
origin: raw/2026-09-22/1121/ledger.md#case-314.2
sprint: migration
created: 2026-09-22
tags: [harness, workflow, sprint, session]
---

## Context

A Frontier line carries its source — `- [ ] C2 — <title> · sprint` — and is closed by replacing the tail: `· case N`, `· work`, `· defer case N`. The source is lost at the close, so nothing can tell afterwards that the line came from the sprint page. That is the one place where "an item of the sprint was decided" is written down mechanically: in 0014 the Cases 304–306 finished themes 1–3 and left their lines on the sprint page untouched, and no script could say so — the brief's Flags named it by hand. Pages: `rule-skill-hi` `built`, of its two Estimates the Case touches `estimate-hi-writes-frontier` (`passed`); `rule-prespec` `built`, its five Estimates untouched, one new one added; `estimate-prespec-binds-a-sprint-line` is free by the Grep over `estimates/`, the nearest is `estimate-prespec-checks-the-plan` — the plan against the ledger, another promise.

## Problem

The close of a Frontier line drops its source, so no check can ask the one question that matters: a sprint item was decided this session — did its Case change the sprint page?

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-314.2
