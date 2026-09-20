---
type: decision
case: "255"
status: current
update: ["[[rule-spec-capture]]", "[[estimate-spec-capture-offers-the-fork]]"]
origin: raw/2026-09-20/0527/ledger.md#case-255
sprint: migration
created: 2026-09-20
tags: [session, hooks, harness, workflow]
---

## Context

`rule-spec-capture` is a Leaf, `enforcement: hook`, code `guppi/spec.py`, the `PostToolUse` hook on `ExitPlanMode`. It appends the approved plan to `raw/<date>/<hi HHMM>/spec.md` and then prints one line on stdout with exit 0 — the fork: Work Mode on the Spec or `/carry`, with the session folder and the Spec file (case 190.5). The page says the hook "prints the fork into the context". Two Estimates: `estimate-spec-capture-appends` — the writing of the Spec, untouched by this Case; `estimate-spec-capture-offers-the-fork` — `passed` 2026-09-16 on one pytest, "the live print in the client is read at the next ExitPlanMode", a reading nobody took. Twice, in sessions 2054 and 2253, the line was not in the `ExitPlanMode` result; the agent asked the fork from memory of the rule. The Claude Code documentation: for `PostToolUse` the exit-0 stdout of a hook goes to the debug log and not to the context; a JSON `hookSpecificOutput.additionalContext` reaches the context; exit 2 shows stderr as a warning. The lesson `lesson-hooks-posttooluse-stdout-not-in-context` is written.

## Problem

The promise of 190.5 — the hook prints the fork into the agent's context — was never kept live: the line goes where the agent does not see it. The test checks the text of stdout, not the shape the client reads, so the Estimate passed on a mechanism that does not work. The Case chooses how the line reaches the agent and rewrites the Criterion so that a live reading closes it.

## History

- 2026-09-20 created · raw/2026-09-20/0527/ledger.md#case-255
