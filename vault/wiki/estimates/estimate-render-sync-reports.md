---
type: estimate
kind: QA
status: passed
target: "[[rule-render-harness]]"
origin: raw/2026-09-12/ledger.md#case-59.7
sprint: migration
created: 2026-09-12
tags: [harness, render, hooks]
ref: rule-render-harness
---

## Context

A rendered file lagged its page for a session at a time, and a hand edit to one was
invisible until `render --check` named the file (case 56). The sync at session start
closes both gaps if its output reaches the agent.

## Criterion

Unit: `guppi render --sync` against a temp vault prints a unified diff for a governed
file that differs and writes the rendered text; prints and writes nothing for an
identical one; on a render error prints to stderr, writes nothing, exits 0. Live: at
a session start after a librarian run that rendered, the hook prints nothing and
writes nothing and `render --check` exits 0; at a session start after a governed file
and its page have parted, the diff of that file is in the agent's first turn and the
page's text is written back (case 89.3).

## Method

pytest in `tests/test_render.py`; the live reading by hand at the next session's
first turn, written into the estimate line.

## Result

live 2026-09-13 session L start, after the librarian of K rendered nothing: the SessionStart hook printed the unified diff of the three governed files whose pages had parted — .claude/settings.json, .claude/agents/librarian-guppi.md, .claude/skills/pre-task/SKILL.md — into the first turn and wrote the pages' text back (git status M on the three, git diff --stat 23 insertions 8 deletions); uv run guppi render --check then exited 0 with no output; the three were committed as 44e4e37

## History

- 2026-09-12 created · [[decision-case-59.7]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L166
- 2026-09-12 updated: the live clause is read against a tree the librarian already rendered (case 89.3) · [[decision-case-89.3]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L44
