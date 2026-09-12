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
the first session start after this one, the diff of the pages the librarian changed
is in the agent's first turn, the files match their pages, `render --check` exits 0;
the reading records whether the `CLAUDE.md` loaded by that session is the text the
hook wrote (a marker sentence added by the librarian's run), or the text before it.

## Method

pytest in `tests/test_render.py`; the live reading by hand at the next session's
first turn, written into the estimate line.

## History

- 2026-09-12 created · [[decision-case-59.7]]
