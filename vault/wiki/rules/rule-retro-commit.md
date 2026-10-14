---
type: rule
kind: Leaf
purpose: Prevents the handoff from starting on an uncommitted tree
status: built
enforcement: hook
implementation_ref: [guppi/gate.py, tests/test_gate.py, .claude/settings.json]
parent: "[[rule-end-of-work]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, hooks, harness, git]
core: true
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
clean it exits 0. Any other tool: exit 0; any other skill: exit 0 on the tree — the same hook refuses any skill while a `then` item of the session's Spec has no ledger line, as `rule-ledger-write` sets it. The hook writes nothing and
commits nothing. It sees the agent's calls through the `Skill` tool, and — registered on `UserPromptSubmit` as well — the person's typed `/pre-spec`, `/retro` or `/handoff`: the payload's `prompt`, trimmed, with or without arguments, gets the same two checks and the same mark; a refusal is exit 2 with the reason for the person — the client blocks the typed prompt — and asks them to have the agent end its reply with the LEDGER block, or to commit; any other prompt is exit 0 with no output and no mark. A `/retro` — typed or called through `Skill` — in a session with nothing to review is refused: a `hi` but no `spec.md` in the session's folder, no plan file named by the event log, and no `- decision[`, `- estimate[` or `- lesson[` line in the session's ledger window; exit 2 with the reason `nothing to review`, the client blocks the prompt, no mark — on the agent's call the reason says that the refusal is a stop of `rule-where-to-stop`, with no call in a next reply; `/pre-spec` and `/handoff` are not affected. The handoff skill still checks the tree itself, a second net.

## History

- 2026-10-14 shipped with GUPPI
