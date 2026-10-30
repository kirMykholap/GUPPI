---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when its Case changes what a step writes, copies or shows or adds a path to it, reads each step and skill that reads that output or does the same step, the steps after it and the new path included, and names each one in context or enters it in the Case
method: "by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line; after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on the readers of a changed step: the findings of ask-guppi at that /pre-spec read for a Case that changes a step and misses a step or skill that reads its output or does the same step, the count in the estimate line"
checked: 2026-10-30
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

2026-10-30, Work readings of session 2005: the findings of ask-guppi (agent a99449af17e45bd35) at the /pre-spec of session 1713, the first session on the Render with the sentence on the readers of a changed step: 1 of 8 findings is a Case that changes a step and misses a text that reads its output or does the same step — finding 1.2, Case 931 adds drop to the update items and leaves line 30 of case-schema.md, the keys the hook of rule-spec-write reads, and the sentence of rule-materialize that lists the lifted keys

## History

- 2026-10-30 created · [[decision-case-924]]
- 2026-10-30 status: pending → failed · raw/2026-10-30/2005/ledger.md#L54
