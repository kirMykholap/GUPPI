---
title: "The conditional-delivery gate covers any departure from unconditional delivery, wherever the rule goes"
type: decision
status: archived
authority: conditional-delivery-gate-scope
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md"]
tags: [harness, process, vault]
---

# The ruling, 2026-08-26

*(the owner selected it, against enumerating the three delivery modes.)*

**The gate of 2026-08-18 gains one dated line: its subject is *any* departure from unconditional
delivery, not the one transition it was written for.** A rule leaving the repository's `CLAUDE.md`
must clear the gate wherever it is going.

**The specific safety test stays attached to `paths:` scoping** — *the dangerous action must force a
matching read* — because a hook has its own trigger and reads no file
([[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]]).

# What it covers retrospectively

**The `/pre-task` move of 2026-08-20 into a hook message** falls inside the widened subject. It had
a direct ruling of its own, so nothing is reopened
([[the-pre-task-rule-leaves-claude-md-for-a-hook-message]]); what changes is that the next move of
that shape is not outside the gate by accident.

# Rejected

**Rejected: writing the three delivery modes into the gate as an enumeration.** The list would have
to be extended by every delivery mechanism anyone invents, and a list that must be extended goes
false without saying so ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]). The
predicate is stated instead: *did the rule stop arriving unconditionally?*

# Why the gap existed at all

**The gate was written for one transition and read as if it covered the class.** `CLAUDE.md` →
`.claude/rules/` with a `paths:` scope was the case in front of whoever wrote it; `CLAUDE.md` → a
hook message is a different transition and was never named
([[a-rule-reaches-a-session-by-several-routes-and-only-one-transition-had-a-gate]]).
