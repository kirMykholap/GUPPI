---
type: decision
case: "1008"
status: current
defer: ["[[estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]]"]
origin: raw/2026-11-02/2035/ledger.md#case-1008
sprint: plugin
created: 2026-11-02
tags: [session, workflow, harness]
---

## Context

The person put off C4 of the Frontier of session 2035, as the brief of session 1548 proposed. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` stands `pending` with target `rule-work-mode`, last read on 2026-10-31 in session 0431. Its `method` waits for the first load of `/work` while `uv run --project .guppi guppi check` exits 1, read in the transcript of its session. Session 1548 loaded `/work` in the VS Code extension, which handed the `!` commands to the agent as instructions. Session 2035 also runs in the VS Code extension, and `guppi check` exits 0 by the brief.

## Problem

No Case of this session sets when or in which client the first load of `/work` on a red check is read.

## Deferred

### [[estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]]

Whether /work loads while guppi check or guppi test finds something, writes the baseline before the first change and runs the tasks of the Spec in order; waits for the first load of /work in the Claude Code CLI while guppi check exits 1; put off at /hi of session 2035

## History

- 2026-11-02 created · raw/2026-11-02/2035/ledger.md#case-1008
