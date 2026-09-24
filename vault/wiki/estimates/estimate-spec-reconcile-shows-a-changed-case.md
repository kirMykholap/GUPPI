---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-reconcile]]"
purpose: An edit of a ratified Case that changes what the scripts apply is shown whole in the first reply after it
method: uv run pytest tests/test_ratified.py -k reconcile; the live reading by hand, the first edit of a ratified Case in a session
origin: raw/2026-09-23/1859/ledger.md#case-387.3
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow]
---

## Criterion

When:
The agent edits the plan file with `Edit`, `Write` or `MultiEdit`, and `uv run guppi ratified --edit` on `PostToolUse` compares each Case of the ratified copy with its section in the plan file; then the `Stop` hook `uv run guppi ratified`, after the write of 387.2 in the same run, reads the first reply after the edit.

Then:
The compared parts are the ids of the Case and its sub-cases, `given`, `when`, `then`, the `then` block and the `tasks` block, byte for byte once the line ends are made the same; the name, `context` and `problem` are not compared.
**＋** A Case whose compared parts differ: `additionalContext` names the parts and tells the agent to show the Case whole for ratification; the hook marks Case N as waiting for its showing.
**＋** A Case whose name, `context` or `problem` alone differ: no message and no mark.
**＋** At `Stop`, a marked Case that the reply does not show whole: exit 2 with the reason; the mark is cleared either way, so a later reply — an answer to a question of the person — is not refused; on the re-fire (`stop_hook_active`) exit 0.
**－** An edit of another file, or of the plan file outside a ratified Case — its title, `## Deferred` — is not compared.
**－** A Case not yet in the ratified copy is not compared.

## History

- 2026-09-24 created · [[decision-case-387.3]]
