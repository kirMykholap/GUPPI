---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: Whether the check of each answer of case-guppi sends back a Case whose recommend misses the title of a question of its rounds in the grill-me form
method: "pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, a round out of form whose titles are not required, an answer with no round, and an answer of sub-cases alone whose titles stand in the recommend of its stored parent; then by hand a Case the hook sends back for a missing title"
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
**＋** It takes titles only from a round that the function of `guppi/casecheck.py` that judges the form of a round finds in form, the function the check of 601.1 sends a round back by; a round out of form gives no title.
**＋** A title that no item of a `recommend` opens with, in bold, among the Cases of the answer and the entries of `<plan>.checked.json` under the number alone of each Case of their family that the answer does not hold, is a finding of the top-level Case — of the first Case of the answer when it holds sub-cases alone — that names the title, sent back and stored as any other finding.
**－** An answer with no earlier round gives no such finding.
**－** A title asked in more than one round is looked for once.
**－** The words of an item after its title are not judged.
**－** A round out of form that came back unchanged, passed the check of its form and was shown gives no title either.

## History

- 2026-09-30 created · [[decision-case-544.3]]
- 2026-10-03 updated: the Criterion replaced whole — only a round in form gives the titles recommend must hold (case 601.5) · [[decision-case-601.5]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 updated: the Criterion replaced whole — a title held in the stored recommend of a Case of the family that the answer does not hold is no finding (case 629.4) · [[decision-case-629.4]]
