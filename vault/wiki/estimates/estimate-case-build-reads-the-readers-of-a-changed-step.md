---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when its Case changes what a step writes, copies or shows or adds a path to it, reads each step and skill that reads that output or does the same step, the steps after it and the new path included, and names each one in context or enters it in the Case
method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on following a step to the one who carries it out: the findings of ask-guppi at that /pre-spec, read in the agent transcript of that ask-guppi under ~/.claude/projects/, for a Case that changes a step and misses a step or skill that reads its output or does the same step, the count and the transcript in the estimate line"
checked: 2026-11-01
origin: raw/2026-10-30/0304/ledger.md#case-924
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

Then:
It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
**＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
**＋** Each step or skill that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
**－** A hit in a History line, in `log.md` or in `brief.md` is not read.

## Result

2026-11-01, Work Mode of session 0141, the findings of ask-guppi at the pre-spec of session 2307, ~/.claude/projects/c--PROJECTS-GUPPI/8d8876d7-f627-4f65-95f7-cb7b7172cd46/subagents/agent-a5ddd2830f464981b.jsonl line 331: 1 of 7 findings is a Case that changes a step and misses one that does the same step — finding 2.1, Case 972 changes the wait check of pre-spec for a create and an update with set method and missed the kept method of an update that replaces the Criterion whole, the kept_method_waits path of prespec.py

## History

- 2026-10-30 created · [[decision-case-924]]
- 2026-10-30 status: pending → failed · raw/2026-10-30/2005/ledger.md#L54
- 2026-10-31 updated: pending again after the failed reading of session 2005, the Criterion written back unchanged; the method waits for the /pre-spec of the first session on the Render with the sentence on a new member of a list · [[decision-case-948.2]]
- 2026-10-31 updated: the method reads the findings of any such /pre-spec in the agent transcript of ask-guppi, the Criterion written back unchanged · [[decision-case-960.3]]
- 2026-10-31 status: pending → failed · raw/2026-10-31/0431/ledger.md#L43
- 2026-10-31 updated: pending again after the failed reading of session 0431, the Criterion written back unchanged; the method waits for the /pre-spec of the first session on the Render that follows a step to the one who carries it out · [[decision-case-966]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/0141/ledger.md#L18
