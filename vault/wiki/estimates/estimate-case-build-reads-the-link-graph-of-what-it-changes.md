---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi reads whole, for each page and file its Case changes that exists before the Case, its block in .guppi/links.md, again at the check of the finished Case for each one whose block it has not read, opens each neighbour whose purpose line bears on the change, and says nothing of a page it creates
method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on reading the block of .guppi/links.md again at the check of the finished Case: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether a Grep of .guppi/links.md and a Read from its line cover the whole block of each existing page and file the tasks of the Case change, and whether each neighbour that bears on the change is opened or named in context; the count and the transcripts in the estimate line"
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
For each page and file the Case changes that exists before the Case, it finds the line `## <slug or path>` of its block in `.guppi/links.md` by a Grep with the line number, and reads the block whole, from that line to the next line that opens with `## `.
**＋** At the check of the finished Case, it lists each page and file that the tasks of the Case change, and reads the block of each one whose block it has not read in that build.
**＋** From each block it judges, by what each neighbour is for, which neighbours bear on the change.
**＋** It opens each neighbour whose purpose line bears on the change, whole or in parts as the Render sets for its kind of text.
**＋** Each neighbour that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
**－** Where `.guppi/links.md` is missing or holds no block of a page or file that exists before the Case, the `context` of the Case says so.
**－** A page or file the Case creates has no block, and the `context` of the Case says nothing of it.

## Result

2026-11-02, Work Mode of session 2227, the case-guppi transcripts of session 2038 under ~/.claude/projects/c--PROJECTS-GUPPI/dbf67938-c4f7-44d4-8502-a6d55d47c17a/subagents/: 0 of 2 standing Cases read the whole block of each existing page and file they change; Case 991 (agent-a6bd04c630130c59a.jsonl L163) read the block of rule-orchestration with limit 80, stopping at line 4819 before its end, the other four blocks whole and the three Estimate blocks at the check of the finished Case (L388); Case 992 (agent-ac588540e75613222.jsonl L338) cut the same block at the same line and never looked up the block of vault/wiki/orchestration.md, which its render task changes; neither context says anything of a page it creates; Case 990, superseded whole by 992, not judged

## History

- 2026-10-31 created · [[decision-case-967.2]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/0141/ledger.md#L17
- 2026-11-01 updated: the Criterion replaced whole — the block read whole, again at the final check, and no word on a created page; pending again after the failed reading of session 0141 · [[decision-case-986]]
- 2026-11-02 status: pending → failed · raw/2026-11-01/2227/ledger.md#L20
