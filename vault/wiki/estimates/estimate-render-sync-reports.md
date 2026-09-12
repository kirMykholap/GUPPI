---
type: estimate
kind: QA
status: pending
target: rule-render-harness
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

unit: tests/test_render.py green in the 47 of uv run pytest tests/test_render.py tests/test_generate.py; live 2026-09-12 session K, the first session start after case 59.7: the SessionStart hook printed a unified diff of the six governed files the librarian's run of session J had left behind — CLAUDE.md, .claude/agents/librarian-guppi.md and the hi, pre-task, retro and handoff skills — wrote the rendered text into them, and uv run guppi render --check now exits 0; the CLAUDE.md this session loaded is the text the hook wrote, not the text before it: the system prompt carries the raw/<date>/<hi HHMM>/spec.md wording of case 73 and the decision-line grammar of case 75.1, both written into rule-claude-md and rule-case-protocol after the file was last rendered

## History

- 2026-09-12 created · [[decision-case-59.7]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L166
- 2026-09-12 updated: the live clause is read against a tree the librarian already rendered (case 89.3) · [[decision-case-89.3]]
