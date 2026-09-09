---
title: "The rule server is a hook of its own, and not a branch inside the one that already runs"
type: decision
status: current
authority: rule-server-hook
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: serve-the-rule-ps1-is-registered-on-pretooluse
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", ".claude/hooks/serve-the-rule.ps1", ".claude/hooks/ask-the-vault.ps1"]
tags: [harness, agents, vault]
---

# Context

**`.claude/hooks/ask-the-vault.ps1` already sits on `PreToolUse` with `Edit|Write`**, already finds
the vault, already normalises and classifies a path, and is built as a chain that selects exactly one
note. The session measured all of that and recommended putting the rule lookup inside it.

**Thirteen hooks stand around a session** and the store carries a live proposal to merge them into one
pipeline ([[the-hooks-merge-into-a-common-pipeline]]), so a fourteenth program is a step away from
that direction.

**Files this touches:** `.claude/hooks/serve-the-rule.ps1`, `.claude/hooks/ask-the-vault.ps1`,
`.claude/settings.json`, `.claude/hooks/pre-task-state.ps1`.

# The question

**Does the rule lookup become a branch in `ask-the-vault.ps1`, or a hook of its own?**

# How it works after

**A hook of its own.** `.claude/hooks/serve-the-rule.ps1` is registered separately on `PreToolUse`
with `Edit|Write` and prints a note naming the rules that govern the file being written
([[the-rule-server-hook]]).

**Two further grounds were found after the ruling and both hold.** `ask-the-vault.ps1` is a chain that
picks exactly one note, by its own design and its own comment, and this mechanism must be able to
speak on the same edit that trips one of those. And it needs a `Read` matcher that script does not
have, so it is a separate `settings.json` entry whatever happens. A third, weaker one: if the lookup
breaks, the pre-task net keeps working.

**The cost is a fourteenth program**, and the merge proposal gains a fourteenth counter-example
without gaining a design.

# Recommendation

**The session recommended the branch and was overruled.** Its argument was that every piece of
machinery the branch needs already exists in the other file; the owner's is that the mechanism is
complex enough to deserve its own home. The two grounds found afterwards say the branch would not
have worked as proposed, so the ruling is right on facts the session did not have when it
recommended.

**Rejected: a branch inside `ask-the-vault.ps1`.**

# Ratification

**owner, 2026-08-30:** «Может мы создадим отдельный хук для этого. Механизм копмлексный, как будто
заслуживает отдлеьного хука.»

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
