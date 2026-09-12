---
type: estimate
kind: QA
status: failed
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
dropped marker lines of `.claude/skills/hi/SKILL.md`; after `rule-claude-md` exists, the
first render changes `CLAUDE.md` by its marker lines only (case 59.8); and
`uv run guppi render --check` then exits 0.

## Method

pytest in `tests/test_render.py` against a temp vault; the live reading once by hand,
written into the estimate line.

## Result

unit: tests/test_render.py green in the 211; live 2026-09-12 session J: after uv run guppi render, git diff --stat shows six files, not the two dropped marker lines of hi/SKILL.md — hi/SKILL.md changed by the text of 59.2 and 59.7, CLAUDE.md by 37 lines of 59.5, 59.6, 62, 66, settings.json by the guard and render --sync hooks, the librarian agent and two skills by their Cases; render --check then exits 0; the two live clauses describe a tree the librarian's run of session I had already left

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.1
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-10 updated: criterion: a full page with a child that is not a render page renders without it, and errors on a marker line for it · raw/2026-09-10/ledger.md#case-36.2
- 2026-09-12 updated: CLAUDE.md is a full render target; pending for the next session's render (cases 59.8, 66) · [[decision-case-66]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L154
