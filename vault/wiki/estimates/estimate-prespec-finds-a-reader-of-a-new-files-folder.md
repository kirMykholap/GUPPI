---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether ask-guppi at the first /pre-spec of a session checks, for each Case that adds a file that is no page, that its context names each search and reading for the folders that hold that file, greps the code and the tests for the calls that walk a folder, and names in a finding each reader of such a folder that the Case does not name
method: "by hand, after the first /pre-spec on the Render of rule-prespec and rule-ask that holds the question on the readers of the folders of a new file, whose plan holds a Case that adds a file that is no page of vault/wiki/: the findings of ask-guppi under that question and its Grep of .guppi/guppi/ and .guppi/tests/, read in its agent transcript under ~/.claude/projects/ against the Criterion; the count and the transcript in the estimate line"
checked: 2026-11-04
origin: raw/2026-11-01/2227/ledger.md#case-995.2
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness]
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

2026-11-04, /hi of session 0358, the same ask-guppi transcript of the pre-spec of session 1825, agent-a514162d0e931e8f2.jsonl: 1 Case of the plan adds a file that is no page (1020, two pictures into plugin/assets/); question 4 answered with 2 findings that name Case 1020: finding 9, the searches of the bare names assets and plugin its context misses, and finding 10, the reader .gitattributes line 27 it does not name; the folder-walk Grep os\.walk|rglob|\.glob\(|iterdir over .guppi/guppi and .guppi/tests ran at L195, L197, L203 (one Grep over both), L213 and L215, five calls where the Criterion names one, and the hits in ship.py, test_guppi_package.py and test_check.py were read around their lines at L223 to L239; at the confirmation after L430, two Reads of the case files and no Grep

## History

- 2026-11-02 created · [[decision-case-995.2]]
- 2026-11-03 updated: the Criterion replaced whole — a plan with no Case that adds a new file starts no folder-walk Grep, and the other searches of the code stand outside this promise · [[decision-case-1015.2]]
- 2026-11-04 status: pending → passed · raw/2026-11-04/0358/ledger.md#L2
