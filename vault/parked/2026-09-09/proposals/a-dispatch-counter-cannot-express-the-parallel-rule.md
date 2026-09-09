---
title: "A dispatch counter cannot express the parallel-dispatch rule, and that is what closes it"
type: proposal
status: current
authority: parallel-dispatch-counter-argument
basis: inference
sprint: S3
created: 2026-08-25
decided_by: [[the-parallel-dispatch-rule-closes-by-a-page]]
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", ".claude/hooks/lock-the-librarian.ps1", "job_hunt_ai_vault/wiki/rules/dispatch-librarians-in-parallel-only-for-reading.md"]
tags: [vault, agents, harness]
---

# The claim this page exists to carry

**The rule forbids a parallel fan-out that may write, and a counter can only see dispatches.** What
separates a legal fan-out from an illegal one is what the agents will do, which no count of
concurrent dispatches contains ([[dispatch-librarians-in-parallel-only-for-reading]]).

**Reading in parallel is explicitly permitted and has been exercised** — six read-only scouts, one per
folder, ran against `wiki/` on 2026-08-20 and nothing wrote
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]]). **So a counter that reddens on
concurrency reddens correct work.**

# Why the payload cannot supply the missing half

**A `PreToolUse` payload does not say who is writing** ([[session-hooks]],
[[the-librarian-writes-unattended]]). The lock that exists narrows on `subagent_type:
vault-librarian` and protects the write half rather than restricting the read half
([[the-librarian-lock-hook]]).

# The alternative, and why it is refused rather than deferred

**A declared dispatch mode** — the caller marks a dispatch as read-only, and the lock counts only the
write ones — **is a self-declaration**. The party the rule constrains supplies the value the rule is
enforced by, which is the shape a field was minted and withdrawn for here, twice false while it stood
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[an-instrument-that-contains-its-own-answers-can-be-gamed]]).

# What the rule rests on instead

**The failure it prevents leaves no trace, which is why the argument had to be written down.** A lost
update to a register leaves nothing in a diff, a log or the gate — the losing write never happened and
the result passes every rule ([[parallel-librarians-break-the-one-writer-property]]).

**So the closure is this argument, not an instrument**, and the owner ordered it written as a page of
its own ([[the-parallel-dispatch-rule-closes-by-a-page]],
[[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]).

# What is open

**Whether a page of argument satisfies acceptance criterion 1** is the owner's reading, and nothing
here reads it. **And there is no register recording that this rule closed this way**
([[the-rule-closure-register-carries-a-case-name-or-a-decision]]).
