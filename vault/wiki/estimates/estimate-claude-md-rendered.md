---
type: estimate
kind: QA
status: pending
target: "[[rule-claude-md]]"
purpose: CLAUDE.md equals the Render of rule-claude-md with each child between its markers, and every session loads that text
method: uv run guppi render and guppi render --check after the build, plus one reading of CLAUDE.md at the next session start, by hand
checked: 2026-09-29
origin: raw/2026-09-12/ledger.md#case-71.1
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Criterion

When:
`guppi render` writes `CLAUDE.md` from `rule-claude-md` and its children, and a session or a subagent starts and loads the file.

Then:
`CLAUDE.md` is: `# GUPPI`; one paragraph, "A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. The vault is vault/; its terms are vault/wiki/glossary.md. A working session opens with /hi.", whose words the file holds with the folder, the path and the skill in code spans; then the text of `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers.
**＋** `render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
**＋** Every session and every subagent loads this text.
**－** No `@` import, no "What is loaded here", no paragraph on `index.md`, no "Migration mode", no "Commands", no one rule and no sentence on memory — the one rule is in `vault/wiki/ratification.md`; the `children` of `rule-claude-md` are `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation`.

## Result

2026-09-29, session 1134: uv run guppi render --check exit 0; CLAUDE.md read at session start: # GUPPI, the one paragraph with vault/, the glossary path and /hi in code spans, then rule-language, rule-agent-writing and rule-one-judgment-one-implementation in their markers; no @ import, no one rule

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
- 2026-09-21 status: pending → passed · raw/2026-09-21/1315/ledger.md#L2
- 2026-09-23 updated: the Criterion names the third child and drops index.md, gone since case 318 (case 360) · [[decision-case-360]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L34
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the history of Migration mode out (case 492.2) · [[decision-case-492.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L41
- 2026-10-02 updated: the Criterion replaced whole - the one rule is in ratification.md (case 595.21) · [[decision-case-595.21]]
