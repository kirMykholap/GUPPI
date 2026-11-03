---
type: estimate
kind: QA
status: passed
target: "[[rule-render-harness]]"
purpose: At session start guppi render --sync shows the diff of each governed file that parted from its page and writes the page's text back, and is silent when every file matches
method: pytest .guppi/tests/test_render.py, plus by hand at the first turn of a later session
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render, hooks]
core: true
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

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
