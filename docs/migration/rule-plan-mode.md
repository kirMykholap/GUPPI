---
type: rule
kind: MOC
purpose: Prevents work being planned against stale or contradictory vault state
status: draft
children: [rule-case-protocol, rule-ask, rule-pretask-hook, rule-pretask]
estimates: [estimate-plan-mode-verified]
origin: TBD
sprint: TBD
created: TBD
tags: [session, workflow, planning]
---

## Purpose

Prevents work being planned against stale or contradictory vault state — deciding to build
something that already exists, or ratifying a set of decisions that conflict with each
other or with what is already there.

## How it works

Plan Mode itself is Claude Code's, not ours: the agent explores without touching files,
then proposes a plan and waits for approval. Nothing needs to be built for that. What we
add is the Case protocol inside it and two points of verification against the vault.

**Exiting Plan Mode is Spec approval.** The Spec is not a separate artifact we assemble —
it is Claude Code's plan approval, carrying our ratified Cases. That mechanic is why there
is no `rule-spec` here: nothing to implement, only to describe.

### Two verification points, not one

**Per Case, at `create` without a `ref`** — `/ask` against the category index. Answers
whether this already exists, what conflicts, which tags fit, whether the slug is free. The
result goes in the Case's `now`, so the human ratifies with it in hand.

Cheap: one index read, a few thousand tokens, and only for `create` without `ref` —
`update` Cases arrive from the Frontier already carrying one.

**Once, before the Spec is written** — the `pre-task` skill. A different question: not "does
this exist" but "does this set of decisions hold together, and against the vault". Findings
are discussed as ordinary Cases.

The hook that triggers it **recommends, it does not block.** A session may legitimately
start from a plan already reconciled with the vault in an earlier session, and blocking
would make that impossible.

### Ordering

The Case protocol has to be loaded before anything else can happen — it defines the format
the other rules assume. `/ask` before the hook that recommends `pre-task`, because
`pre-task` calls it.

## Children

1. **[[rule-case-protocol]]** — `render: partial` → `CLAUDE.md`. The six Case sections, the
   atomicity test, sub-case splitting, and *never move to the next Case until this one is
   ratified or deferred*. Also carries the Frontier rule: Plan Mode does not end while
   Frontier items remain unratified and undeferred. This is instruction, not enforcement —
   there is no hook that could check "did you finish the Frontier", so it is written where
   the agent always sees it.

   Includes the line that sends the agent to `/ask` on a `create` without a `ref`.

2. **[[rule-ask]]** — `render` → the `/ask` skill. The universal search over the category
   indexes, used by both the per-Case check and by `pre-task`. One tool, two moments: by
   intent before a decision exists, by finished content afterwards.

3. **[[rule-pretask-hook]]** — `hook`. Fires as the plan artifact is about to be written.
   Emits a message recommending `pre-task`. Does not block.

4. **[[rule-pretask]]** — `render` → the `pre-task` skill. The reconciliation workflow:
   `/ask` across the whole Spec, surface contradictions with the vault and between
   decisions, hand anything found back as Cases.

   Keep this skill short. It is loaded every time the hook fires, so its length is paid
   every session.

## Estimates

- [[estimate-plan-mode-verified]] — QA. A `create` decision for something already present
  in the vault does not reach the Spec unflagged; and the pre-task hook fires before the
  plan artifact is written without preventing it from being written.

## What happens next

Exiting Plan Mode is the boundary. The hook chain that follows — executable plan, branch,
commit, subagent dispatch — belongs to [[rule-work-mode]].

## History

- TBD created
