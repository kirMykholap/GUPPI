---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when its Case changes what a step writes, copies or shows or adds a path to it, reads each step and skill that reads that output or does the same step, the steps after it and the new path included, and, where a function of .guppi/guppi/ does the step, each place that calls it or makes the same judgment on another input, and names each one in context or enters it in the Case
method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on following a step into the code of .guppi/guppi/: the findings of ask-guppi at that /pre-spec, read in the agent transcript of that ask-guppi under ~/.claude/projects/, for a Case that changes a step and misses a step, a skill or a place of code that reads its output or does the same step, the count and the transcript in the estimate line"
checked: 2026-11-02
origin: raw/2026-10-30/0304/ledger.md#case-924
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent, a hook or a function of `.guppi/guppi/` writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

Then:
It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
**＋** Where a function of `.guppi/guppi/` does the step, it also searches `.guppi/guppi/` for the name of that function and of the function it judges by.
**＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
**＋** Where a function of `.guppi/guppi/` does the step, it reads each place that calls that function or the function it judges by, and each other place that makes the same judgment on another input, such as the value a plan writes and the value a live page keeps.
**＋** Each step, skill or place of code that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
**－** A hit in a History line, in `log.md` or in `brief.md` is not read.

## Result

2026-11-02, Work Mode of session 2227, the findings of ask-guppi at the pre-spec of session 2038, ~/.claude/projects/c--PROJECTS-GUPPI/dbf67938-c4f7-44d4-8502-a6d55d47c17a/subagents/agent-a03b5d7a30c71b7d9.jsonl line 264 (confirmation line 276, no new finding): 4 of 11 findings are a Case that changes a step and misses one that reads its output or does the same step — 1.1 Case 990 changed ONLY_THE_PERSON of rule-prespec-onward and missed ## The acknowledging reply of rule-orchestration; 1.2 Case 991.1 missed the same closer in ## The short form of rule-orchestration; 1.3 Case 991.1 missed the take-back sentence of ## Showing and signing a Case; 3.1 Case 991.1 did not name deferred_pages of prespec.py, by which check_backlog_line judges

## History

- 2026-10-30 created · [[decision-case-924]]
- 2026-10-30 status: pending → failed · raw/2026-10-30/2005/ledger.md#L54
- 2026-10-31 updated: pending again after the failed reading of session 2005, the Criterion written back unchanged; the method waits for the /pre-spec of the first session on the Render with the sentence on a new member of a list · [[decision-case-948.2]]
- 2026-10-31 updated: the method reads the findings of any such /pre-spec in the agent transcript of ask-guppi, the Criterion written back unchanged · [[decision-case-960.3]]
- 2026-10-31 status: pending → failed · raw/2026-10-31/0431/ledger.md#L43
- 2026-10-31 updated: pending again after the failed reading of session 0431, the Criterion written back unchanged; the method waits for the /pre-spec of the first session on the Render that follows a step to the one who carries it out · [[decision-case-966]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/0141/ledger.md#L18
- 2026-11-01 updated: the Criterion replaced whole — the readers of a changed step include the places of the harness code; pending again after the failed reading of session 0141 · [[decision-case-985]]
- 2026-11-02 status: pending → failed · raw/2026-11-01/2227/ledger.md#L19
