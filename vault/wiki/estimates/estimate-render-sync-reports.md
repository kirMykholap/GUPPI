---
type: estimate
kind: QA
status: pending
target: "[[rule-render-harness]]"
purpose: At session start guppi render --sync shows the diff of each governed file that parted from its page and writes the page's text back, and is silent when every file matches
method: pytest tests/test_render.py, plus by hand at the first turn of a later session
origin: raw/2026-09-12/ledger.md#case-59.7
sprint: migration
created: 2026-09-12
tags: [harness, render, hooks]
---

## Criterion

When:
A session starts, and the `SessionStart` hook of `.claude/settings.json` runs `uv run guppi render --sync` over the governed files.

Then:
For each governed file that differs from its render, stdout holds a unified diff, the file as it is and then the rendered text, and the rendered text is written. The diff reaches the agent's first turn.
**＋** An identical file is neither printed nor written.
**＋** On a render error, one line goes to stderr, nothing is written, and the exit is 0.
**＋** At a session start after a librarian's run that rendered, the hook prints nothing and writes nothing, and `uv run guppi render --check` then exits 0.
**＋** At a session start after a governed file and its page have parted, the diff of that file is in the first turn, and the page's text is written back.

## Result

live 2026-09-13 session L start, after the librarian of K rendered nothing: the SessionStart hook printed the unified diff of the three governed files whose pages had parted — .claude/settings.json, .claude/agents/librarian-guppi.md, .claude/skills/pre-task/SKILL.md — into the first turn and wrote the pages' text back (git status M on the three, git diff --stat 23 insertions 8 deletions); uv run guppi render --check then exited 0 with no output; the three were committed as 44e4e37

## History

- 2026-09-12 created · [[decision-case-59.7]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L166
- 2026-09-12 updated: the live clause is read against a tree the librarian already rendered (case 89.3) · [[decision-case-89.3]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L44
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-29 updated: the Criterion replaced whole — the unit and live paragraph as When and Then; purpose and method set, Context and Method out (case 498.2) · [[decision-case-498.2]]
