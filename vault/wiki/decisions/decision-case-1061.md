---
type: decision
case: "1061"
status: current
create: ["[[estimate-work-mode-runs-the-style-check-before-a-stop]]"]
update: ["[[rule-work-mode]]"]
origin: raw/2026-11-25/2003/ledger.md#case-1061
sprint: plugin
created: 2026-11-25
tags: [session, workflow, harness, render]
---

## Problem

A copy or other work handed to the person at a stop can carry a style finding, since no style check runs before the stop.

## Recommend

- **Where should the style check run before a copy reaches the person?**
  - Recommended: (a) Work Mode runs the style check before every stop task.
  - Answer: agreed, (a).
- **What Work Mode does with a style finding in a file the session did not change**
  - Recommended: (a) before a `stop:` task the agent fixes the findings in the files the session changed, writes a finding in any other file as a line of `handoff.md`, and stops as usual.
  - Answer: agreed, (a).
- **What the reading of the new Estimate takes**
  - Recommended: (a) the `method` waits for the first `/work` with a `stop:` task that loads after the render and reads its transcript, as `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` does; it stays `pending` until then.
  - Answer: agreed, (a).
- **Change**
  - Asked: `/pre-spec` found that the `context` says `guppi ship` runs no `ruff check`, while the docstring of `.guppi/guppi/ship.py` says the copy passes the commands of the key `style`.
  - Taken: the code was read; `ship` runs only `ruff format .guppi`, and the docstring holds for a working tree whose code passes `ruff check`, so the `context` names the code and says why the docstring stands.

## History

- 2026-11-26 created · raw/2026-11-25/2003/ledger.md#case-1061
