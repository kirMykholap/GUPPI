---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of each answer of case-guppi sends back a Case whose recommend misses the title of a question of its rounds in the grill-me form
method: "pytest .guppi/tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, a round out of form whose titles are not required, an answer with no round, and an answer of sub-cases alone whose titles stand in the recommend of its stored parent"
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case, and `agent_transcript_path` holds the agent's earlier outputs with no Case heading, which are its rounds of questions on that Case.

Then:
`uv run --project .guppi guppi casecheck --subagent` takes the title of each question of those rounds from its line `❓ **Q<n>** - **<title>**:`, the title line of the template of `.claude/skills/grill-me/SKILL.md`.
**＋** It takes titles only from a round that the function of `.guppi/guppi/casecheck.py` that judges the form of a round finds in form, the function by which the check sends a round out of form back; a round out of form gives no title.
**＋** A title that no item of a `recommend` opens with, in bold, among the Cases of the answer and the entries of `<plan>.checked.json` under the number alone of each Case of their family that the answer does not hold, is a finding of the top-level Case — of the first Case of the answer when it holds sub-cases alone — that names the title, sent back and stored as any other finding.
**－** An answer with no earlier round gives no such finding.
**－** A title asked in more than one round is looked for once.
**－** The words of an item after its title are not judged.
**－** A round out of form that came back unchanged, passed the check of its form and was shown gives no title either.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
