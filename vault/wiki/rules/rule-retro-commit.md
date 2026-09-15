---
type: rule
kind: Leaf
purpose: Prevents the handoff from starting on an uncommitted tree
status: built
enforcement: hook
implementation_ref: [guppi/gate.py, tests/test_gate.py, .claude/settings.json]
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-retro-commit-gates]]"]
origin: raw/2026-09-10/ledger.md#case-38.2
sprint: migration
created: 2026-09-10
tags: [session, workflow, hooks, harness, git]
---

## Purpose

Prevents the handoff from starting on an uncommitted tree. An instruction to commit
before handoff is a step an agent can skip; a `PreToolUse` hook cannot be skipped.
The commit is what makes everything the librarian writes afterwards readable as a
separate layer.

## How it works

`uv run guppi gate` runs on `PreToolUse` with the matcher `Skill`. When
`tool_input.skill` is `handoff` and `git status --porcelain` is not empty, it exits
2 with the reason `commit first`, which blocks the call once; when the tree is
clean it exits 0. Any other tool: exit 0; any other skill: exit 0 on the tree — the same hook refuses any skill while a `then` item of the session's Spec has no ledger line (`rule-ledger-write`, case 122). The hook writes nothing and
commits nothing. It sees only calls made through the `Skill` tool, which is how the
Retro skill calls `/handoff`; the handoff skill checks the tree itself for the case
where the person types it.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-10 estimate estimate-retro-commit-gates added · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-09 status: draft → built · cascade
- 2026-09-14 updated: the gate's second refusal, on an unwritten ledger line, named beside the tree check (case 132) · [[decision-case-132]]
