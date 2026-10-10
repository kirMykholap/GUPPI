---
type: decision
case: "169.2"
status: archived
update: ["[[rule-hook-registry]]"]
origin: raw/2026-09-15/1448/ledger.md#case-169.2
sprint: migration
created: 2026-09-15
tags: [hooks, harness, render]
---

## Context

`guppi gate` is the `PreToolUse` hook on the `Skill` tool: before `/pre-task`, `/retro` and `/handoff` it checks the Spec against the ledger (122), for `/handoff` the cleanness of the tree, and, letting the call through, leaves the mark `retro`/`handoff`/`pretask` in the event log (136.1). It sees only calls through the `Skill` tool — the agent's way of calling a skill. When the person types the command, the client expands it into the prompt, no tool is called, and no `PreToolUse` hook sees it. Case 150 removed `disable-model-invocation` and signed that both paths go through `Skill`; the reading showed the opposite: the typed `/retro` without a mark and without the gate, the agent's call with both. Two lessons and the refused Insight name one cause and propose one thing: a typed command has an event of its own — `UserPromptSubmit`, where `guppi event prompt` already reads the prompt for `/hi`. By the hooks reference of Claude Code a `UserPromptSubmit` hook with exit 2 blocks the prompt and shows its stderr to the person.

## Problem

A typed `/retro` or `/handoff` bypasses the check of the Spec against the ledger and the mark; `rule-retro` stands `draft` on the false block 150.

## Given

`rule-retro-commit` (`built`, `hook`, `implementation_ref: [guppi/gate.py, tests/test_gate.py, .claude/settings.json]`, `estimates: [estimate-retro-commit-gates]`): "It sees only calls made through the `Skill` tool … the handoff skill checks the tree itself for the case where the person types it".
**＋** `gate.run`: `skill_of(payload)` reads `tool_input.skill`; without it exit 0; `spec_check`, `dirty` and `mark` are functions bound to no payload type.
**＋** `rule-hook-registry` (`built`, `render` → `.claude/settings.json`): `UserPromptSubmit` carries one command, `uv run guppi event prompt`; the hooks of one event run in list order.
**＋** `rule-event-log`: "The hook never fails the session … exit code is 0"; the paragraph on the marks names `guppi gate` on `PreToolUse Skill`.
**＋** `rule-ledger-write` (122): the paragraph on the gate names `PreToolUse Skill` and the refusal text "end this reply in text with the LEDGER block, then call /<skill> in the next reply".
**＋** `rule-retro` (`draft`, `render` → `SKILL.md`, `estimates: [estimate-retro-loads]`, `failed` on 150): block 150 — "the call goes through the Skill tool" for both paths; the Result — the typed path without mark and gate.
**＋** The hooks reference of Claude Code: the `UserPromptSubmit` payload carries `prompt`; exit 2 blocks the prompt and shows stderr to the person; stdout goes to the context.
**＋** `tests/test_gate.py`: payloads with `tool_name: Skill`; a payload with `prompt` is not tested.
**－** `guppi event prompt` and `/hi` do not change; the tree check inside the `/handoff` skill stays as a second net.

## Criterion

- [[estimate-hook-registry-rendered]] § case 169.2

## History

- 2026-09-15 created · raw/2026-09-15/1448/ledger.md#case-169.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
