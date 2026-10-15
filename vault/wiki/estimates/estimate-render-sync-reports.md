---
type: estimate
kind: QA
status: passed
target: "[[rule-render-harness]]"
purpose: At session start guppi render --sync shows the diff of each governed file that parted from its page and writes the page's text back, and is silent when every file matches
method: pytest .guppi/tests/test_render.py, plus by hand at the first turn of a later session
checked: 2026-09-29
origin: raw/2026-09-12/ledger.md#case-59.7
sprint: migration
created: 2026-09-12
tags: [harness, render, hooks]
---

## Criterion

When:
A session starts, and the `SessionStart` hook of `.claude/settings.json` runs `uv run --project .guppi guppi render --sync` over the governed files.

Then:
For each governed file that differs from its render, stdout holds a unified diff, the file as it is and then the rendered text, and the rendered text is written. The diff reaches the agent's first turn.
**＋** An identical file is neither printed nor written.
**＋** On a render error, one line goes to stderr, nothing is written, and the exit is 0.
**＋** At a session start after a librarian's run that rendered, the hook prints nothing and writes nothing, and `uv run --project .guppi guppi render --check` then exits 0.
**＋** At a session start after a governed file and its page have parted, the diff of that file is in the first turn, and the page's text is written back.

## Result

2026-09-29, uv run pytest tests/test_render.py: 34 passed; by hand, the first turn of session 1134 after the librarian's run of 0137: no diff, git status clean, render --check exit 0

## History

- 2026-09-12 created · [[decision-case-59.7]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L166
- 2026-09-12 updated: the live clause is read against a tree the librarian already rendered (case 89.3) · [[decision-case-89.3]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L44
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-29 updated: the Criterion replaced whole — the unit and live paragraph as When and Then; purpose and method set, Context and Method out (case 498.2) · [[decision-case-498.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L47
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
