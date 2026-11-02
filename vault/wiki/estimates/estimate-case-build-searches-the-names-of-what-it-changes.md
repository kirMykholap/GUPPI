---
type: estimate
kind: QA
status: failed
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

2026-11-02, Work Mode of session 1337, the case-guppi transcript of Case 1001 of session 0254, ~/.claude/projects/c--PROJECTS-GUPPI/68effdf4-70dd-447d-bafe-0ca629e82241/subagents/agent-a025e5a81b4e802ee.jsonl, on the Render of commit 5d709203 that names the search; Case 1000 never answered with a summary and is not judged: 0 of 1 Case met the Criterion; one Grep per slug, not one Grep of all the names (rule-morph L94, the Estimate L221); entity-sprint-plugin never searched over vault/wiki/ (L204, L216); rule-permissions and rule-guppi-config searched only over .guppi/tests (L297, L396), and their other names (settings.json, guppi.toml, config.py, commands.py, test_config.py, test_commands.py, guppi test, guppi style) never searched; no Grep of the purpose lines; of the 15 hits of rule-morph 5 read whole, 3 read to line 40, the rest seen through content Greps, all 15 named in context

## History

- 2026-10-31 created · [[decision-case-967.2]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/0141/ledger.md#L17
- 2026-11-01 updated: the Criterion replaced whole — the block read whole, again at the final check, and no word on a created page; pending again after the failed reading of session 0141 · [[decision-case-986]]
- 2026-11-02 status: pending → failed · raw/2026-11-01/2227/ledger.md#L20
- 2026-11-02 renamed from `estimate-case-build-reads-the-link-graph-of-what-it-changes` · [[decision-case-999.2]]
- 2026-11-02 updated: renamed and the Criterion replaced whole — case-guppi searches the names of what it changes, since the graph of links is dropped; pending again after the failed reading of session 2227 · [[decision-case-999.2]]
- 2026-11-02 status: pending → failed · raw/2026-11-02/1337/ledger.md#L17
