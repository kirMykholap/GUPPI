---
type: rule
kind: MOC
purpose: Prevents implementation drifting from the ratified plan while it is being executed
status: draft
enforcement: render
governs: .claude/skills/subagent-guppi/SKILL.md
render_mode: full
parent: rule-work-mode
children: [rule-task-dispatch, rule-task-review, rule-branch-review, rule-model-tiers]
estimates: [estimate-subagent-guppi-execution]
origin: TBD
sprint: TBD
created: TBD
tags: [work-mode, subagents, review]
---

## Purpose

Prevents implementation drifting from the ratified plan while it is being executed —
by giving each task a subagent that transcribes rather than invents, and by reviewing
against the plan rather than against taste.

Adapted from `subagent-driven-development`. What we changed is recorded below; the rest is
kept because it earned its place in someone else's practice.

## How it works

### The plan already contains the code

`to-executable-plan` wrote complete code into every task — the test first, then the
implementation, with exact paths. **RED/GREEN is a property of the plan, not a cycle
performed at runtime.** A subagent transcribes the test, confirms it fails, transcribes the
implementation, confirms it passes. It does not design anything.

This is what makes the cheapest model tier appropriate for most tasks: transcription and
verification, not invention.

### Name collision, resolved

Upstream uses "ledger" for the list of minor review findings deferred rather than fixed.
**Ours is the record of ratified decisions.** Two different things under one word in the
same prompt would be a genuine hazard, so theirs is called **parked findings** everywhere
in our version.

### Findings are triaged by the main agent, ratified at Retro

Upstream lets the agent decide which findings to fix and which to park, with no human in
the loop. We do not stop mid-work to ask either — but nothing the agent decided stays
unratified: **every triage decision is recorded and reviewed at Retro**, alongside the rest
of the session's decisions.

Parking a finding is a `defer`; parking a bug also opens a GitHub issue, since a deferred
bug that exists only in the vault is invisible to the next Frontier.

### Subagents never decide

A subagent that hits a fork — "to do this I would also have to change that" — stops and
returns. The main agent raises it as an ordinary Case. A subagent that takes a measurement
returns the number; the main agent writes the `- estimate[...]` ledger line.

**Subagents never write to the ledger.** Only the main agent does.

## Children

1. **[[rule-task-dispatch]]** — `render: partial`. Read the plan once, extract every task
   with its full text and context. One fresh subagent per task, given exactly what that
   task needs and nothing more. It transcribes the test, verifies it fails, transcribes the
   implementation, verifies it passes, reports back.

   **Verifying the test fails is not a formality.** A test that passes before the
   implementation exists is a broken test, and catching that costs nothing here versus
   hours later.

   Tick the checkbox in `plan.md` — the checkbox is the state log.

2. **[[rule-task-review]]** — `render: partial`. Capture `BASE_SHA` and `HEAD_SHA` around
   each task and dispatch a reviewer with both, plus the task text from the plan. Two
   stages: spec compliance first, code quality second. Compliance before taste, because a
   beautifully written wrong thing is still wrong.

3. **[[rule-branch-review]]** — `render: partial`. After every task is ticked, one review of
   the whole branch on the most capable tier, reading a prepared review package rather than
   re-deriving diffs from git.

   **Findings go to a single fix subagent with the complete list**, never one fixer per
   finding. Upstream's stated reason holds: per-finding fixers each rebuild context and
   rerun the suite, and in a real session that wave cost more than all the implementation
   tasks combined. Then exactly one scoped re-review.

4. **[[rule-model-tiers]]** — `render: partial`. Choose by turns, not by token price. Plan
   contains complete code → cheapest tier, since the work is transcription. Task described
   in prose → mid tier floor. Reviewers → mid tier floor. Whole-branch review → most
   capable available.

## Estimates

- [[estimate-subagent-guppi-execution]] — QA. Every task in the plan is either ticked or
  reported blocked; no subagent wrote a ledger line; a mid-task fork produced a Case rather
  than a silent change; and the branch review dispatched one fix subagent rather than one
  per finding.

## What happens next

When the last task is ticked, this skill calls `/retro`. A PreToolUse hook catches that and
starts the harness suite in the background — see [[rule-work-mode]] and
[[rule-end-of-work]].

## History

- TBD created
