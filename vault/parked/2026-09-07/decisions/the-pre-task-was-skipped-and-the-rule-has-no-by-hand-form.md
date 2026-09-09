---
title: "The `/pre-task` was skipped because the ritual was unavailable, and the rule has no by-hand form"
type: decision
status: current
authority: pre-task-fallback-gap
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "CLAUDE.md"]
tags: [process, agents, harness]
---

# The divergence, recorded 2026-08-19

**What the rule says:** `/pre-task` runs before implementing anything non-trivial, and before
touching an area not touched this session ([[a-pre-task-runs-before-anything-non-trivial]]).

**What was done:** it was not run, while the session changed `scripts/vault-check-selftest.sh` by 149
insertions and 82 deletions and promoted a frontmatter field across six schemas.

**What was done instead:** the vault was read by hand, with the two `rg` commands the repository's
`CLAUDE.md` prescribes when an agent cannot be dispatched.

**Rejected: dispatching the librarian**, which a session instruction forbade outright.

# Why it looked unnecessary, and the part worth keeping

**The session instruction made the ritual literally unavailable, and the by-hand paragraph reads as
its substitute.** It is not one.

**The by-hand recipe substitutes for `/vault-ask` and not for `/pre-task`**, and the two differ in
exactly the way that matters: one asks about a **topic**, the other checks a **plan** against what is
already decided ([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]],
[[deriving-what-the-vault-already-holds-costs-a-round]]). A topic lookup cannot surface a constraint
you did not know to name, which is the whole value of the ritual.

**The rule has no by-hand form, and that is the divergence's cause rather than its excuse.** Every
other rule of that file either survives the agent being unavailable or says what to do instead; this
one does neither.

# What it obliges, and the fork is the owner's

The repository's `CLAUDE.md` fallback paragraph is one of two things and not both:

- **it says what a session does instead of `/pre-task`** when no agent can be dispatched — a
  by-hand form of the plan check, distinct from the topic lookup already written there; or
- **the rule says non-trivial work does not proceed without the librarian**, and an unavailable
  agent stops the work rather than licensing it.

**Neither is the librarian's to choose** ([[the-librarian-writes-unattended]]). It is filed here with
its divergence attached so the next reader meets the gap and the evidence for it in one place, rather
than a rule that looks complete ([[knowing-a-rule-is-not-a-mechanism]]).
