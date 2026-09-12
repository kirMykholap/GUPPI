---
type: estimate
kind: QA
status: pending
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
the text of `rule-case-protocol` between its markers; the first such render leaves
a `git diff` of marker lines only; `guppi render --check` then exits 0; every
session after it loads the same text, the two `@` imports expanded.

### case 73.10

When:
A session starts with `CLAUDE.md`.

Then:
The Migration paragraph says the approved plan is copied to
`vault/raw/<date>/<hi HHMM>/spec.md`.

## Method

the live reading at the first render after the page exists, by hand, written into
the estimate line; `tests/test_render.py` already pins a full page with a partial
child.

## Result

live 2026-09-12 session J, the first uv run guppi render after rule-claude-md exists: CLAUDE.md equals the Render with rule-case-protocol spliced between its markers and render --check exits 0; the git diff is not marker lines only — a full render drops the outer markers by design (estimate-render-harness-reproduces, unit), and the diff holds 37 lines of the Case protocol that Cases 59.5, 59.6, 62 and 66 wrote into the Render of rule-case-protocol after the file was last written by hand; the clause was written against a file the page had already left

## History

- 2026-09-12 created · [[decision-case-71.1]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L153
- 2026-09-12 criterion: case 73.10 added · [[decision-case-73.10]]
