---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again
status: built
enforcement: hook
implementation_ref: [guppi/ratified.py, tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-reconcile-shows-a-changed-case]]"]
deferred_by: ["[[decision-case-412]]"]
origin: raw/2026-09-23/1859/ledger.md#case-387.3
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow, session]
---

## Purpose

Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again. The prose of a Case — its name, `context` and `problem` — is Russian in the ratified copy and English in the approved Spec, so it is not compared; everything the scripts apply is.

## How it works

`uv run guppi ratified --edit` on `PostToolUse` of `Edit`, `Write` and `MultiEdit` on the plan file: it compares each Case of the ratified copy `<plan>.ratified.md` with its section in the plan — the ids, `given`, `when`, `then`, the `then` block and the `tasks` block — and, for a Case whose parts differ, returns them in `additionalContext` with the order to show the Case whole, and marks the Case as waiting for its showing; a change of the name, `context` or `problem` alone gets no message and no mark. `uv run guppi ratified` on `Stop`, after its write, exits 2 when a marked Case is not shown whole in the reply, and clears the mark either way; on the re-fire (`stop_hook_active`) exit 0. The comparison is one function of `guppi/ratified.py`; `guppi prespec --check` imports it.

## History

- 2026-09-24 created · [[decision-case-387.3]]
- 2026-09-24 estimate estimate-spec-reconcile-shows-a-changed-case added · [[decision-case-387.3]]
- 2026-09-24 status: draft → built · cascade
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 deferred · [[decision-case-412]]
