---
type: decision
case: "953"
status: current
update: ["[[rule-spec-capture]]"]
supersedes: ["[[decision-case-934]]"]
origin: raw/2026-10-31/0128/ledger.md#case-953
sprint: plugin
created: 2026-10-31
tags: [session, hooks, harness, workflow]
---

## Problem

The approval of a long plan is withheld in the Claude Code CLI, and nobody knows whether Claude Code or the terminal is at fault, so no Case can fix it yet.

## Recommend

- **What to do with the deferred item**
  - Recommended: (a) run the test in this session's Work Mode, by hand, its result recorded by a lesson line.
  - Answer: agreed, (a).
- **Where the test runs, and with which plan**
  - Recommended: (b) in an empty folder with no GUPPI, with the text of the plan that failed.
  - Answer: agreed, (b).
- **How this Case is checked**
  - Recommended: (a) by `estimate-backlog-renders`, with no new Estimate.
  - Answer: agreed, (a).
- **Change**
  - Asked: finding 6 of `/pre-spec`: name the lesson of the first failure in `given`, and record the result as a new fact under a slug that names what the test found, the librarian's index check judging a duplicate.
  - Taken: `given` names the lesson and `rule-index-check`; the `then` line and the lesson task say so.
- **Change**
  - Asked: finding 8 of `/pre-spec`: the `then` states what `.guppi/tests/test_backlog.py` checks, and a task runs that test.
  - Taken: the `then` line names the test over a made-up vault, and a task runs it against `estimate-backlog-renders`.

## History

- 2026-10-31 created · raw/2026-10-31/0128/ledger.md#case-953
