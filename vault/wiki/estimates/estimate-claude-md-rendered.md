---
type: estimate
kind: QA
status: passed
target: rule-claude-md
origin: raw/2026-09-12/ledger.md#case-71.1
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Context

Signed as the nested Estimate of `rule-claude-md` in Case 59.8 (session I,
2026-09-12), kept by Case 66; no paired `create` line was written, so the page is
born of Case 71.1 with the criterion of 59.8 unchanged.

## Criterion

After `uv run guppi render`, `CLAUDE.md` equals the Render of `rule-claude-md` with
the text of `rule-case-protocol` between its markers; the diff of that render holds
the text those two pages gained since the file was last written, and nothing else;
`guppi render --check` then exits 0; every session after it loads the same text,
the two `@` imports expanded (case 88.2).

### case 73.10

When:
A session starts with `CLAUDE.md`.

Then:
The Migration paragraph says the approved plan is copied to
`vault/raw/<date>/<hi HHMM>/spec.md`.

### case 88.2

When:
The first `uv run guppi render` after `rule-claude-md` or `rule-case-protocol` changed.

Then:
`CLAUDE.md` equals the Render of `rule-claude-md` with the text of `rule-case-protocol`
between its markers.
**＋** The diff holds the text those two pages gained since the file was last written,
and nothing else.
**＋** `guppi render --check` then exits 0, and every session after it loads the same
text with the two `@` imports expanded.

## Method

the live reading at the first render after the page exists, by hand, written into
the estimate line; `tests/test_render.py` already pins a full page with a partial
child.

## Result

live 2026-09-13 session L: CLAUDE.md was not among the files render --sync wrote, so it still equals the render of rule-claude-md with rule-case-protocol between its markers made at the start of session K; render --check exits 0; the session loaded it with glossary.md and case-schema.md expanded inline, and its Migration paragraph names vault/raw/<date>/<hi HHMM>/spec.md (73.10)

## History

- 2026-09-12 created · [[decision-case-71.1]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L153
- 2026-09-12 criterion: case 73.10 added · [[decision-case-73.10]]
- 2026-09-12 criterion: case 88.2 added · [[decision-case-88.2]]
- 2026-09-12 updated: the stale live clause of case 59.8 leaves the Criterion prose (case 88.2) · [[decision-case-88.2]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L49
