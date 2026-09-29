---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: Whether lint reports a code fence with text after its closing run, or left open at the end of a section, in a live page, by the judgment pre-spec runs
method: uv run pytest tests/test_lint.py -k fence
checked: 2026-09-29
origin: raw/2026-09-28/2229/ledger.md#case-487.2
sprint: migration
created: 2026-09-28
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi lint` reads the sections of the live pages under `vault/wiki/<category>/`.

Then:
Lint reports each live page that `fence_breaks` of `guppi/materialize.py` judges broken with one `fence` finding per break, naming the page, its heading and the faulty line or the open end.
**＋** A `fence` finding sets exit 1, like any other finding.
**＋** `guppi/lint.py` imports the judgment and holds no second copy of the pattern.
**－** A harness file on disk is not read for fences: `render --check` compares it with its Render.
**－** Nothing is written.

## Result

2026-09-29, uv run pytest tests/test_lint.py -k fence: 3 passed; guppi/lint.py imports fence_breaks, no fence pattern of its own

## History

- 2026-09-29 created · [[decision-case-487.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L26
