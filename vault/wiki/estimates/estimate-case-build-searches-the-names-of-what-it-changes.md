---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on each note of the hook of rule-case-check on a file that names a page or a file its Case changes, reads that file by Read or by a Grep whose path is it, or names it in context with the reason it stands, enters each file the change makes false in the Case, and writes in a code span of its task line the path of each file outside vault/wiki/ that a task changes
method: "by hand, after the /pre-spec of the first session in which the hook of rule-case-check sends case-guppi a note on a file that names what its Case changes, on the Render of rule-case-build that answers that note: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each note, whether the agent read the file by Read or by a Grep whose path is it, or named it in context, and its case file, whether each task line writes in a code span the path of each file outside vault/wiki/ that it changes; the count and the transcripts in the estimate line"
checked: 2026-11-02
origin: raw/2026-10-31/1831/ledger.md#case-967.2
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, gets from the `SubagentStop` hook of `rule-case-check` a note on a file that names a page or a file its Case changes, and answers again.

Then:
It reads that file by a `Read` call of it, or by a `Grep` call whose `path` is it, whole or in parts as `rule-case-build` sets for its kind of text, or the `context` of the Case names the file and says why it stands.
**＋** Each file that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
**＋** A task line that changes a file of the repository outside `vault/wiki/` writes its path in a code span.

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
- 2026-11-02 updated: the Criterion replaced whole — case-guppi answers the note of the hook on each file that names what its Case changes; purpose and method set anew · [[decision-case-1005.2]]
