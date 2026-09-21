---
type: estimate
kind: QA
status: pending
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
`CLAUDE.md` is the Render of `rule-claude-md` whole (`render_mode: full`), the children `rule-language` and `rule-agent-writing` in their markers; the hook refuses a hand edit.
**＋** Each item of "Migration mode" is a Rule with its own Render: `rule-internal-context`, `rule-ledger-write`, `rule-retro`, `rule-handoff`, `rule-documentation`, `rule-spec-capture`; "`make style` clean before the commit" is in the Render of `rule-retro`.
**＋** The glossary and the schema arrive with `/hi` (273.3, 288.1); the one rule stands in the schema (288.2).
**＋** `guppi render --check` keeps the file equal to the page.

When:
The first `uv run guppi render` after `rule-claude-md` changed, and the start of the next session with `CLAUDE.md`.

Then:
`CLAUDE.md` is: `# GUPPI`; one paragraph — a Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into; the vault is `vault/`, its map `vault/wiki/index.md`, its terms `vault/wiki/glossary.md`; a working session opens with `/hi`; then the text of `rule-language` and `rule-agent-writing` in their markers.
**＋** `render --check` after the render exits 0; every session and every subagent loads this text.
**－** No `@` import, no "What is loaded here", no paragraph on `index.md`, no "Migration mode", no "Commands", no one rule and no sentence on memory — the one rule is in the schema; the `children` of `rule-claude-md` are `rule-language` and `rule-agent-writing`.

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
- 2026-09-21 updated: the Criterion replaced whole — the title, the description and the two markers, nothing else (case 288.3) · [[decision-case-288.3]]
