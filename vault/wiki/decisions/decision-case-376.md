---
type: decision
case: "376"
status: current
create: ["[[estimate-retro-runs-on-to-the-handoff]]"]
update: ["[[rule-retro]]"]
supersedes: ["[[decision-case-375]]"]
origin: raw/2026-09-23/1355/ledger.md#case-376
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness, render]
---

## Context

The Render of `rule-retro` sets the report of `/retro` in two places. The Retro opens with the frontier: what was ratified by the Tail, the unticked boxes of the Spec and what the agent noticed during Work Mode. It closes with three lists: the ratifications, what got done, what did not. In session 1126 the person found two defects: the ratifications stand twice, and the unticked boxes of the Spec stand apart from what is not done. `rule-retro` stands `built`, deferred by Case 375 and taken up here; `estimate-retro-loads` speaks of the readings, not of the form of the report, and is not touched; the form of the report gets an Estimate of its own, whose Criterion the item writes itself, so that it does not depend on whether Work Mode builds the code of 378.2 before the librarian. Shown again in the model of Case 378.

## Problem

The report of `/retro` names the same ratifications twice and splits what is not done into two places, so the person reads more and finds the open work in two lists.

## Given

`rule-retro` — the Render `.claude/skills/retro/SKILL.md`: the opening message and the close of the report.
**＋** `/retro` — the skill, the render of `rule-retro`.
**＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, with its unticked boxes.
**＋** `uv run guppi tail` — the Tail with the decision lines of the session.
**＋** `estimate-retro-runs-on-to-the-handoff` — the new promise.

## History

- 2026-09-23 created · raw/2026-09-23/1355/ledger.md#case-376
