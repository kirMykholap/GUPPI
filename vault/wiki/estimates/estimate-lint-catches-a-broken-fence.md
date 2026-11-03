---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: Whether lint reports a code fence with text after its closing run, or left open at the end of a section, in a live page, by the judgment pre-spec runs
method: uv run --project .guppi pytest .guppi/tests/test_lint.py -k fence
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi lint` reads the sections of the live pages under `vault/wiki/<category>/`.

Then:
Lint reports each live page that `fence_breaks` of `.guppi/guppi/materialize.py` judges broken with one `fence` finding per break, naming the page, its heading and the faulty line or the open end.
**＋** A `fence` finding sets exit 1, like any other finding.
**＋** `.guppi/guppi/lint.py` imports the judgment and holds no second copy of the pattern.
**－** A harness file on disk is not read for fences: `render --check` compares it with its Render.
**－** Nothing is written.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
