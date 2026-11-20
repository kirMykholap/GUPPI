---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on the note of the hook of rule-case-check that lists the files that name what its Case changes, reads each listed file whose purpose line or path speaks of that change by Read or by a Grep whose path is it, or names it in context, enters each file the change makes false in the Case, and gives each file outside vault/wiki/ that a task changes a task line of its own with its path in the first code span, a line that opens with a command such as a render line kept in its own form
method: "by hand, after the /pre-spec of the first session in which the hook of rule-case-check sends case-guppi the note that lists the files that name what its Case changes, on the Render of rule-case-build that sets the answer to that note: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each listed file whose purpose line or path speaks of what its Case changes whether the agent read it by Read or by a Grep whose path is it, or named it in context; and its case file, whether each task line that changes a file outside vault/wiki/ holds its path in its first code span and changes no other such file, a line that opens with a code span holding a command, such as a render line, left out; the count and the transcripts in the estimate line"
checked: 2026-11-04
deferred_by: ["[[decision-case-1038]]"]
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

2026-11-04, /hi of session 0358, the case-guppi transcripts of session 0316, the first session on the Render of 14a82de8 in which the hook sent the note, ~/.claude/projects/c--PROJECTS-GUPPI/5c8c941f-70e2-416c-8f86-83ce2f6f7765/subagents/: Case 1015 (agent-a42461338786a960b.jsonl, note at L304, 47 files) did not meet the Criterion: after the note it read estimate-prespec-reconciles.md (Grep L307) and orchestration.md (Grep L309), and its context names those two and estimate-prespec-confirms-the-findings-once with a reason, but vault/wiki/rules/rule-search-leaves-out-decisions.md, .claude/rules/search-leaves-out-decisions.md and .guppi/guppi/grepguard.py, whose paths speak of the searches the Case widens, were neither read by a Read or a Grep whose path is each nor named in context, which gives one reason for the other listed files; Cases 1016 (54 files), 1017 (862 and 2 files) and 1018 (207 files) not judged file by file; in the four case files each task line that changes a file outside vault/wiki/ opens with its path in the first code span and changes no other such file

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
