---
type: estimate
kind: QA
status: passed
target: "[[rule-claude-md]]"
purpose: CLAUDE.md equals the Render of rule-claude-md with each child between its markers, and every session loads that text
method: uv run guppi render and guppi render --check after the build, plus one reading of CLAUDE.md at the next session start, by hand
checked: 2026-09-20
origin: raw/2026-09-12/ledger.md#case-71.1
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Criterion

Given:
The conditions of 272.1.

When:
The first `uv run guppi render` after `rule-claude-md` or any of its children changed, and a session start with `CLAUDE.md`.

Then:
`CLAUDE.md` equals the Render of `rule-claude-md` with the text of each child — `rule-language`, `rule-agent-writing` — between its markers; the diff of that render holds only the text those pages gained since the file was last written; `guppi render --check` then exits 0.
**＋** The first paragraph says the vault is the only memory (272.1); "What is loaded here" names one import, `glossary.md`, and says the Case schema arrives at `/hi`; `index.md` is not imported.
**＋** Every session loads the same text, its `@` import expanded.
**－** `CLAUDE.md` holds no `rule-case-protocol` marker, no import of `case-schema.md` and no line on the Case form; the `children` of `rule-claude-md` are `rule-language` and `rule-agent-writing`.

## Result

2026-09-20, uv run guppi render --check exit 0 at the start of session 1749, CLAUDE.md read by hand: markers rule-language (41–45) and rule-agent-writing (47–53) only, no rule-case-protocol marker, no import of case-schema.md; the first paragraph says the vault is the only memory; What is loaded here names one import, glossary.md, and the schema at /hi; children of rule-claude-md are rule-language and rule-agent-writing

## History

- 2026-09-12 created · [[decision-case-71.1]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L153
- 2026-09-12 criterion: case 73.10 added · [[decision-case-73.10]]
- 2026-09-12 criterion: case 88.2 added · [[decision-case-88.2]]
- 2026-09-12 updated: the stale live clause of case 59.8 leaves the Criterion prose (case 88.2) · [[decision-case-88.2]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L49
- 2026-09-14 status: passed → passed · raw/2026-09-14/1229/ledger.md#L2
- 2026-09-20 updated: the recut to the shape of case 193 — purpose, method, the Criterion replaced whole; three children spliced, the memory sentence (case 272.1) · [[decision-case-272.1]]
- 2026-09-20 updated: the Criterion replaced whole — the text of 272.1 plus no protocol in CLAUDE.md, one import (case 273.3) · [[decision-case-273.3]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L2
