---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on the note of the hook of rule-case-check that lists the files that name what its Case changes, reads each listed file whose purpose line or path speaks of that change by Read or by a Grep whose path is it, or names it in context, enters each file the change makes false in the Case, and gives each file outside vault/wiki/ that a task changes a task line of its own with its path in the first code span, a line that opens with a command such as a render line kept in its own form
method: "by hand, after the /pre-spec of the session that sets this method: the agent transcript of each case-guppi of that session under ~/.claude/projects/ that got the note of the hook of rule-case-check, for each listed file whose purpose line or path speaks of what its Case changes whether the agent read it by Read or by a Grep whose path is it, or named it in context; and its case file, whether each task line that changes a file outside vault/wiki/ holds its path in its first code span and changes no other such file, a line that opens with a code span holding a command, such as a render line, left out; the count and the transcripts in the estimate line"
checked: 2026-11-25
origin: raw/2026-10-31/1831/ledger.md#case-967.2
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, gets from the `SubagentStop` hook of `rule-case-check` the note that lists the files that name a page or a file its Case changes, and answers again.

Then:
For each listed file whose purpose line or path speaks of what its Case changes, it reads that file by a `Read` call of it, or by a `Grep` call whose `path` is it, whole or in parts as `rule-case-build` sets for its kind of text, or the `context` of the Case names the file and says why it stands.
**＋** Each file that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
**＋** In its case file, a file of the repository outside `vault/wiki/` that a task changes has a task line of its own that opens with the path in a code span.
**－** A listed file whose purpose line and path speak of something else needs no read and no line in `context`.
**－** A task line that opens with a code span holding a command, such as `uv run --project .guppi guppi render` with the rendered file in its second span, keeps the form `vault/wiki/case-schema.md` sets for it.

## Result

2026-11-25, Retro of session 0605, the agent transcripts under ~/.claude/projects/c--PROJECTS-GUPPI/16ad52b9-2613-43c4-8115-f092d2d530c2/subagents/ and the case files of vault/raw/2026-11-25/0605/cases/: the note of rule-case-check came to the builds of Cases 1045 (11 files, agent-a2707248a424a313e.jsonl L223), 1046 (20, then 1, agent-ad8d1780561c59324.jsonl L124, L266, L319), 1047 (2, agent-a00b5d9702448d958.jsonl L106), 1048 (3, agent-aa62b4efab1bbbd90.jsonl L162), 1049 (138 for 1049.1, 125 for 1049.2, agent-ac87edb9fd0dbc08c.jsonl L407) and 1051 (204, L319 of the 1046 agent); a script over those transcripts and case files found each listed file of 1047 and 1048 named in context; of 1045, 5 read or named and 6 neither, a Purpose or root cause about /hi, hooks or the librarian and not about the cut of a path; of 1049.1 17 read or named and of 1051 9 named by path, the rest judged in context by group, by their purpose lines and paths, with a reason; the files of 1049.1 and 1051 whose slugs speak of what the Case changes — the estimate-clean-branch-* and estimate-sprint-* pages — were checked by hand and stand named by kind in context, such as "the other four speak of --check, the Spec ticks, the moves of items and a closed sprint"; each other file was judged by its purpose line in the note and not read; each task line of 1045, 1049.1 and 1051 that changes a file outside vault/wiki/ holds its path in its first code span and changes no other such file

## History

- 2026-10-31 created · [[decision-case-967.2]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/0141/ledger.md#L17
- 2026-11-01 updated: the Criterion replaced whole — the block read whole, again at the final check, and no word on a created page; pending again after the failed reading of session 0141 · [[decision-case-986]]
- 2026-11-02 status: pending → failed · raw/2026-11-01/2227/ledger.md#L20
- 2026-11-02 renamed from `estimate-case-build-reads-the-link-graph-of-what-it-changes` · [[decision-case-999.2]]
- 2026-11-02 updated: renamed and the Criterion replaced whole — case-guppi searches the names of what it changes, since the graph of links is dropped; pending again after the failed reading of session 2227 · [[decision-case-999.2]]
- 2026-11-02 status: pending → failed · raw/2026-11-02/1337/ledger.md#L17
- 2026-11-02 updated: the Criterion replaced whole — case-guppi answers the note of the hook on each file that names what its Case changes; purpose and method set anew · [[decision-case-1005.2]]
- 2026-11-02 updated: the Criterion replaced whole — the note of a name, and one changed file per task line · [[decision-case-1010.3]]
- 2026-11-03 updated: the Criterion replaced whole — case-guppi answers the list by the purpose line or the path of each file · [[decision-case-1011.2]]
- 2026-11-04 status: pending → failed · raw/2026-11-04/0358/ledger.md#L3
- 2026-11-20 deferred · [[decision-case-1038]]
- 2026-11-25 defer by decision-case-1038 superseded · [[decision-case-1047]]
- 2026-11-25 updated: pending again after the failed reading, the Criterion unchanged; read on the builds of a later session · [[decision-case-1047]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0605/ledger.md#L25
