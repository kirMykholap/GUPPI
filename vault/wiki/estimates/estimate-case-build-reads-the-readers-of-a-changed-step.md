---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether no step, skill or place of code that reads the output of a step a Case changes, or does the same step, and that the change makes false, gets past the approved Spec unnamed by both case-guppi and /pre-spec and comes to light in the Work Mode or Retro of that session or of the session after it
method: "by hand, after the Retro of the session that follows a session whose approved Spec holds a Case of case-guppi that changes what a step writes, copies or shows or adds a path on which a step does so: the Work Mode and Retro of both sessions, read in their ledgers and in the transcripts of their main agents under ~/.claude/projects/, for a step, a skill or a place of code that reads the output of the changed step or does the same step, that the change makes false and that no Case and no context of the approved Spec named, such as a Case built again in Work Mode, a task added by hand, a red test or check or an error lesson for it, the count and the transcripts in the estimate line"
checked: 2026-11-02
origin: raw/2026-10-30/0304/ledger.md#case-924
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
The person approves the Spec of a session whose Cases `case-guppi` built, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, and checked by `/pre-spec`, and a Case of that Spec changes what a step of a skill, an agent, a hook or a function of `.guppi/guppi/` writes, copies or shows, or adds a path on which a step does so.

Then:
Each step, skill or place of code that reads that output or does the same step, and that the change makes false, stands in a Case of the approved Spec, or the `context` of a Case names it and says why it stands.
**＋** A reader that a finding of `/pre-spec` named and that a Case built again took in counts as found.
**＋** No such reader comes to light in the Work Mode or the Retro of that session or of the session after it, by a Case built again, a task added by hand, a red test or check, or an `error` lesson.
**－** A text in a History line, in `log.md` or in `brief.md` is not such a reader.

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
- 2026-11-02 updated: the Criterion replaced whole — a missed reader of a changed step counts only when it gets past the approved Spec and comes to light in that session or the session after it; pending again after the failed reading of session 2227 · [[decision-case-998]]
