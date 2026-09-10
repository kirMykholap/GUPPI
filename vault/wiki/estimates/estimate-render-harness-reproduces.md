---
type: estimate
kind: QA
status: passed
target: rule-render-harness
origin: raw/2026-09-09/ledger.md#case-18.1
sprint: migration
created: 2026-09-09
tags: [harness, render]
---

## Context

The renderer is what makes a Rule page the source of a harness file. The unit cases pin
the contract on a temp vault; the live reading proves that the hand-kept copies of
Slice 1 were identical to their pages, since the first render changes nothing but the
outer markers it drops.

## Criterion

Against a temp vault: a full MOC with two partial children renders to the MOC's Render
text with each child marker replaced by the child's block, in child order, outer markers
dropped; a partial page splices between its markers in an existing file and leaves the
markers; a partial target without markers exits 1 with nothing written; a full page whose children include a page without `enforcement: render` renders as if that child were absent, and exits 1 with nothing written when its text carries a marker line for it; `--check` on a
differing file exits 1, names it, writes nothing, and exits 0 on an identical one.
Against the live vault: after `uv run guppi render`, `git diff --stat` shows only the two
dropped marker lines of `.claude/skills/hi/SKILL.md` and no change to `CLAUDE.md`, and
`uv run guppi render --check` then exits 0.

## Method

pytest in `tests/test_render.py` against a temp vault; the live reading once by hand,
written into the estimate line.

## Result

Passing, 2026-09-09, session D. `tests/test_render.py`: 12 tests green (44 in the suite).
Live: `guppi render --check` before the first render named only
`.claude/skills/hi/SKILL.md`; after `guppi render`, `git diff --stat` showed that file
alone, 2 deletions — the `<!-- rule-skill-hi -->` and `<!-- /rule-skill-hi -->` lines —
and `CLAUDE.md` untouched; `--check` then exited 0.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.1
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-10 updated: criterion: a full page with a child that is not a render page renders without it, and errors on a marker line for it · raw/2026-09-10/ledger.md#case-36.2
