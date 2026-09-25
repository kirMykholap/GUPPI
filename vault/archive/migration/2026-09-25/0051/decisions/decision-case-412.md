---
type: decision
case: "412"
status: archived
defer: ["[[rule-prespec]]", "[[rule-prespec]]", "[[rule-spec-write]]", "[[rule-spec-reconcile]]", "[[rule-spec-reconcile]]", "[[rule-spec-reconcile]]"]
supersedes: ["[[decision-case-407.1]]", "[[decision-case-407.5]]", "[[decision-case-407.2]]", "[[decision-case-407.3]]", "[[decision-case-407.4]]", "[[decision-case-410]]"]
superseded_by: ["[[decision-case-414.1]]"]
origin: raw/2026-09-24/2214/ledger.md#case-412
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness, hooks]
---

## Context

Case 407 was ratified in this session and leaves the Spec by this Case. Its mechanism: `prespec --check --case N` checks one Case without the Frontier and the translation; the `Stop` hook of `rule-spec-write` runs it on each Case it writes and gives the findings back by exit 2; a `PreToolUse` guard of `rule-spec-reconcile` refuses every edit of the plan by the agent but its creation and the part below `## Deferred`; the agent writes the name, `context`, `problem`, `given` and the task lines that are no items through a `Write` of `<plan>.fragment.md`, which the guard refuses, merges into the plan and checks; the comparison with the ratified copy drops `given` and the task lines that are no items. The full text of Case 407 stands in the ratified copy of this plan. The pre-spec of this session found in it what the next session answers first: a `given` written unshown still reaches the Decision page, against the purposes of `rule-spec-write` and `rule-spec-reconcile`; the `ratification` row of the Case schema keeps clauses on an edit of the plan and a `DIFF` of it, and a new task line on a file changes the scope; `is_plan` takes the fragment and the plan of a subagent for plan files; the finding of a ledger line that does not parse names no Case; `estimate-case-protocol-checks-its-frame` reads a changed `given` before a showing again, which would no longer happen; an exit 2 after the acknowledging reply makes the agent go on after its `LEDGER` block; no page says whether `guppi ledger` writes its lines before `guppi ratified` checks them at the same `Stop`; in Plan Mode the client may ask the person before a `Write` outside the plan file, by `lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt`. The question of Case 410 — when the prose of a Case is translated — waits for the same mechanism and is taken in here.

## Problem

How the Spec is written by hooks alone, with each Case checked at once: decided in a later session, with the findings above answered.

## Deferred

### [[rule-prespec]]

The check of one Case, prespec --check --case N, run by the hooks after each ratified Case (case 407.1, 407.5)

### [[rule-prespec]]

The check of one Case, prespec --check --case N, run by the hooks after each ratified Case (case 407.1, 407.5)

### [[rule-spec-write]]

The Stop hook checks each Case it writes and gives the findings back (case 407.2)

### [[rule-spec-reconcile]]

The agent writes into the plan only through a fragment the guard merges and checks; when the prose of a Case is translated (cases 407.3, 407.4, 410)

### [[rule-spec-reconcile]]

The agent writes into the plan only through a fragment the guard merges and checks; when the prose of a Case is translated (cases 407.3, 407.4, 410)

### [[rule-spec-reconcile]]

The agent writes into the plan only through a fragment the guard merges and checks; when the prose of a Case is translated (cases 407.3, 407.4, 410)

## History

- 2026-09-25 created · raw/2026-09-24/2214/ledger.md#case-412
- 2026-09-25 superseded by decision-case-414.1 · [[decision-case-414.1]]
- 2026-09-25 archived · superseded
- 2026-09-25 archived · cleanup
