---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: Whether the check of each answer of case-guppi sends back a Case whose recommend misses the title of a question of its rounds
method: "pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, an answer with no round; then by hand the first Case the hook sends back for a missing title"
origin: raw/2026-09-30/1306/ledger.md#case-544.3
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case, and `agent_transcript_path` holds the agent's earlier outputs with no Case heading, which are its rounds of questions on that Case.

Then:
`uv run guppi casecheck --subagent` takes the title of each question of those rounds from its line `❓ **Q<n>** - **<title>**:`, the title line of the template of `.claude/skills/grill-me/SKILL.md`.
**＋** A title that no item of a `recommend` of the top-level Case or of its sub-cases in the answer opens with, in bold, is a finding of the top-level Case that names the title, sent back and stored as any other finding.
**－** An answer with no earlier round gives no such finding.
**－** A title asked in more than one round is looked for once.
**－** The words of an item after its title are not judged.

## History

- 2026-09-30 created · [[decision-case-544.3]]
