---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether ask-guppi at the first /pre-spec of a session checks, for each Case that adds a file that is no page, that its context names each search and reading for the folders that hold that file, greps the code and the tests for the calls that walk a folder, and names in a finding each reader of such a folder that the Case does not name
method: "by hand, after the first /pre-spec on the Render of rule-prespec and rule-ask that holds the question on the readers of the folders of a new file, whose plan holds a Case that adds a file that is no page of vault/wiki/: the findings of ask-guppi under that question and its Grep of .guppi/guppi/ and .guppi/tests/, read in its agent transcript under ~/.claude/projects/ against the Criterion; the count and the transcript in the estimate line"
checked: 2026-11-04
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, rendered from `rule-prespec`; the agent follows `.claude/agents/ask-guppi.md`, rendered from `rule-ask`; and a Case of the plan has a line in its `tasks` block that adds a file that is no page of the vault.

Then:
`ask-guppi` reads the `tasks` block of each Case of the plan, as the dispatch of `.claude/skills/pre-spec/SKILL.md` tells it, and answers, for a Case with such a line, whether its `context` names each search and reading that `.claude/agents/case-guppi.md` sets for the folders that hold the new file.
**＋** A search or a reading that the `context` misses is a finding that names the Case and what it misses.
**＋** Beside its other searches, it runs one Grep of `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`, and reads around its line each hit whose folder holds the new file.
**＋** Each reader that takes every file of such a folder and that the Case does not name is a finding that names the Case and the reader.
**－** A plan with no such Case starts no such Grep for the calls that walk a folder, and the question says "none".
**－** At the confirmation of its findings, the agent runs no such Grep.
**－** The other Greps and Reads of the code that a finding needs are outside this promise: `estimate-ask-searches-at-prespec` reads them.

## Result

2026-11-04, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
