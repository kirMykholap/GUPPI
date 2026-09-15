---
type: decision
case: "150"
status: archived
update: ["[[rule-retro]]"]
superseded_by: ["[[decision-case-169.3]]"]
origin: raw/2026-09-14/1633/ledger.md#case-150
sprint: migration
created: 2026-09-14
tags: [session, workflow, harness, render]
---

## Context

The lesson of O: `retro/SKILL.md` carries `disable-model-invocation: true`; a typed `/retro` is expanded as a prompt, the Skill tool is not called, `guppi gate` does not see it — neither the check of 122 nor the `retro` mark; `rule-event-log` and `gate.MARKS` promise three marks, the second never appears.

## Problem

The owner allows the agent to start the Retro itself after Work Mode: the Retro stops at the lessons and the readings anyway, and `/handoff` stands behind the gate. Decide: remove the flag — one mechanism for the three skills, no code change.

## Given

`rule-retro` `built`, `enforcement: render`, `governs: .claude/skills/retro/SKILL.md`, `estimates: [estimate-retro-loads]` `passed` (126); the Render, line 31: `disable-model-invocation: true`; the body: `Tests: !`make test``, `Style: !`make style``, `Ledger: !`uv run guppi tail``.
**＋** `rule-event-log` `built`: the marks `pretask`, `retro`, `handoff` are written by `guppi gate` on `PreToolUse Skill`; `gate.MARKS` holds `retro`; `test_retro_and_handoff_leave_their_marks` expects both marks.
**＋** `gate.py`: the gate of 122 — "any skill while the Spec is ahead of the ledger"; `/handoff` and `/pre-task` without the flag pass through the Skill tool and get their PostToolUse lines and marks (sessions N, O).
**＋** `rule-retro-commit`: `/handoff` on a dirty tree is refused; the Retro calls `/handoff` through the Skill tool.
**＋** The lesson of O stays `new`: the fact about the flag holds; after this Case it is history.
**－** The glossary "`/retro` (the person)" does not change: the person can still type `/retro`; the agent may now call it too — after Work Mode, when the tasks of the Spec are ticked.
**－** `rule-event-log`, `gate.py`, the tests — unchanged.

## Criterion

- [[estimate-retro-loads]] § case 150

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-150
- 2026-09-15 superseded by decision-case-169.3 · [[decision-case-169.3]]
- 2026-09-15 archived · superseded
- 2026-09-15 archived · cleanup
