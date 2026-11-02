---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi searches in one Grep that prints only file paths for all the names of each page and file its Case changes that exists before the Case, again at the check of the finished Case for each one it has not searched, prints the purpose lines of the pages on that list, and opens each file that bears on the change
method: "by hand, after the /pre-spec of a session whose case-guppi runs on the Render of rule-case-build that searches the names of each page and file a Case changes: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether one Grep that prints file paths covers all the names of each existing page and file the tasks of the Case change, whether a Grep printed the purpose lines of the pages on its list, and whether each file that bears on the change is opened or named in context; the count and the transcripts in the estimate line"
checked: 2026-11-02
origin: raw/2026-10-31/1831/ledger.md#case-967.2
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and answers with its summary.

Then:
For each page and file the Case changes that exists before the Case, it searches in one Grep that prints only the paths of the files, over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`, for all its names.
**＋** The names of a page are its slug, the file name of each path of its `governs`, `implementation_ref` and `code_ref`, the name of the agent or of the skill with its slash whose file its `governs` names, and `guppi <command>` for each command that `COMMANDS` of `.guppi/guppi/cli.py` maps to a module of those paths; the names of a file are its file name and the agent, skill or command it carries.
**＋** It prints the purpose line of each page on that list by one more Grep over those pages.
**＋** It opens each file of the list whose purpose line, or whose path where it has none, bears on the change.
**＋** At the check of the finished Case, it searches the names of each page and file the tasks of the Case change that it has not searched in that build.
**＋** Each file that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
**－** A hit in `log.md` or `brief.md` is not opened.

## Result

2026-11-02, Work Mode of session 2227, the case-guppi transcripts of session 2038 under ~/.claude/projects/c--PROJECTS-GUPPI/dbf67938-c4f7-44d4-8502-a6d55d47c17a/subagents/: 0 of 2 standing Cases read the whole block of each existing page and file they change; Case 991 (agent-a6bd04c630130c59a.jsonl L163) read the block of rule-orchestration with limit 80, stopping at line 4819 before its end, the other four blocks whole and the three Estimate blocks at the check of the finished Case (L388); Case 992 (agent-ac588540e75613222.jsonl L338) cut the same block at the same line and never looked up the block of vault/wiki/orchestration.md, which its render task changes; neither context says anything of a page it creates; Case 990, superseded whole by 992, not judged

## History

- 2026-10-31 created · [[decision-case-967.2]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/0141/ledger.md#L17
- 2026-11-01 updated: the Criterion replaced whole — the block read whole, again at the final check, and no word on a created page; pending again after the failed reading of session 0141 · [[decision-case-986]]
- 2026-11-02 status: pending → failed · raw/2026-11-01/2227/ledger.md#L20
- 2026-11-02 renamed from `estimate-case-build-reads-the-link-graph-of-what-it-changes` · [[decision-case-999.2]]
- 2026-11-02 updated: renamed and the Criterion replaced whole — case-guppi searches the names of what it changes, since the graph of links is dropped; pending again after the failed reading of session 2227 · [[decision-case-999.2]]
