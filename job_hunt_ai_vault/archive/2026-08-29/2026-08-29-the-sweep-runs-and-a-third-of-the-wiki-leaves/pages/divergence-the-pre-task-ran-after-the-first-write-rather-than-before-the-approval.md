---
title: "DIVERGENCE: the `/pre-task` ran after the session's first write rather than between the plan and its approval"
type: decision
status: archived
authority: pre-task-order-divergence
binding: divergence
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", ".claude/hooks/check-the-plan.ps1"]
tags: [process, harness, agents]
---

# What happened

**The ritual ran, and it ran late.** The rule places `/pre-task` between the plan and its approval,
and before the first write where work starts without a plan
([[a-pre-task-runs-between-the-plan-and-its-approval]]). This session had no plan until the plan
file, **so the plan file was the first write** — and the hook on `PreToolUse:Write` is what caught
the omission.

**The dispatch then ran before the approval**, so the ritual's purpose was served. Its ordering was
not.

# Why it looked unnecessary at the time

**The session read the rule as binding on a plan that already existed, and it had none.** A
discussion that turns into a plan file has no moment that feels like *between the plan and its
approval* until the file is being written.

# What it teaches

**Nothing about the rule's text and everything about its trigger.** The by-hand form of the rule has
already been recorded as missing ([[the-pre-task-was-skipped-and-the-rule-has-no-by-hand-form]]),
and this is the neighbouring case: the rule has no form for a session whose first artefact is the
plan itself.

**The hook is what recovered it**, which is the argument the enforcement was built on
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]).
