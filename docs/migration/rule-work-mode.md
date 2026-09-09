---
type: rule
kind: MOC
purpose: Prevents implementation starting before the plan, branch and baseline exist
status: draft
children: [rule-executable-plan-hook, rule-executable-plan, rule-branch-commit, rule-subagent-dispatch, rule-harness-tests]
estimates: [estimate-work-mode-chain]
origin: TBD
sprint: TBD
created: TBD
tags: [session, workflow, implementation]
---

## Purpose

Prevents implementation starting before the plan, the branch and the baseline commit
exist — and prevents any of those three being skipped because someone was in a hurry.

## How it works

### The workflow is the hook chain

This MOC does not describe a skill that walks through steps. **The hooks are the workflow.**
Each one fires on the previous one's completion, so the order is enforced by the harness
rather than by an agent remembering it. The MOC exists for us: to read, to search, and to
have somewhere to attach the Estimate that checks the chain holds.

Hook messages are not inline strings. They are rendered from rule pages into files under
`.claude/`, and the hook substitutes the text — so the wording is ratified content like
everything else, and changing it goes through a decision.

### The chain

Exiting Plan Mode → `to-executable-plan` → branch + commit → `subagent-guppi` → `/retro`.

Automatic steps with no human checkpoint between them. That is deliberate: the Spec
was ratified, and the executable plan is a mechanical derivation from it — tasks, code,
checkboxes. There is nothing new to approve. If the derivation turns out to be wrong,
that surfaces as an ordinary Case during the work.

### Why the branch comes after the plan

Plan Mode is pure conversation; nothing needs isolating while it happens. The branch is
created once there is something to isolate, and the first commit carries `spec.md` and
`plan.md` — a baseline that has the agreement in it but none of the work yet.

Its lifetime follows the **plan**, not the session. Plan finished — merge and delete in the
same session. Plan unfinished — stay on it; the next session reads that from `git branch`
and picks up where it left off.

## Children

1. **[[rule-executable-plan-hook]]** — `hook`. Fires on exit from Plan Mode. Requires
   `to-executable-plan`.

2. **[[rule-executable-plan]]** — `render` → the `to-executable-plan` skill. Breaks the
   Spec into tasks: complete code with the test first, exact paths, checkboxes,
   parallelization markers. Adapted from `writing-plans`; the plan carries the code, so
   execution is transcription and verification rather than invention.

3. **[[rule-branch-commit]]** — `hook`, PostToolUse on the plan being written. Creates the
   branch and commits `spec.md` and `plan.md`.

4. **[[rule-subagent-dispatch]]** — `hook`. Fires once the branch exists. Requires
   `/subagent-guppi`.

   The skill itself is **[[rule-subagent-guppi]]** — a MOC rendering into the skill file,
   with its own children covering task dispatch, review and model selection. Calling
   `/retro` when the last task is ticked is part of it, not a separate rule here.

5. **[[rule-harness-tests]]** — `hook`, PreToolUse on `/retro`. Starts the harness test
   suite **in the background** and lets the call through.

   In the background because Retro is a conversation: the person reads what happened and
   asks questions while the suite runs, rather than waiting on it first. The result lands
   during that conversation.

   This is the last thing Work Mode does. What happens with a red result belongs to
   [[rule-end-of-work]] — it is a matter for the Retro conversation, not for this chain.

## Estimates

- [[estimate-work-mode-chain]] — QA. Exiting Plan Mode produces an executable plan, a
  branch and a baseline commit in that order; subagents are not dispatched until all three
  exist; and `/retro` does not begin without the harness suite having been started.

## During the work

Contract changes and Estimate results arising mid-work are ordinary Cases with ordinary
ledger lines — the `- estimate[...]` line carries its result as text, since a measurement
taken after the tests were written exists nowhere else.

## What happens next

The dispatcher calls `/retro`; the hook above starts the harness suite in the background
and Work Mode ends there. Everything from the Retro conversation onward is
[[rule-end-of-work]].

## History

- TBD created
