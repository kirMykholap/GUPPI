---
title: "The AST rule moves to prove the mechanism, and not for what the move saves"
type: decision
status: current
authority: ast-move-ground
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "CLAUDE.md"]
tags: [harness, testing, agents]
---

# The ground the owner gave, 2026-08-18

> **owner: the AST move goes ahead to prove the mechanism, not to save context.**
> *"Better to test it on one rule than on ten later."*

**The move is a rehearsal with one subject.** Conditional delivery is a change of guarantee
([[a-rule-moving-to-conditional-delivery-needs-its-page-first]]), and the only rule of that file
which passes the safety criterion is [[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]]
([[moving-a-rule-into-claude-rules-with-a-paths-scope]]). Moving it buys the measurement of a
mechanism that would otherwise be tested for the first time on a batch.

**The saving was measured and is explicitly not the reason.** The eleven regions of the repository's
`CLAUDE.md` are **3,637 bytes** of slice text — reproduced at `c521a10` — roughly 850 tokens, and
the AST rule's own share is about 45 of them. The owner ruled that this arithmetic stays out of the
ground for the decision, and it is recorded here as a measurement rather than as an argument.

## What it still waits on

**Probe 2 — whether a path-scoped rule reaches a subagent that reads a matching file.** Every task
here is reviewed by a subagent, so a move made on the documented half alone would be a rule that
silently does not arrive for the reviewer ([[the-conditional-delivery-probe]],
[[claude-code-loads-a-rules-file-at-launch-and-a-scoped-one-on-a-read]]). **The measurement decides
what wiring the move needs, not whether it happens** — that half is settled here.

**And the `whole` delivery mode**, because the destination is a generated file rather than a file
carrying a region ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).

## What it waits on has changed, and the ground has not — 2026-08-19

**Probe 2 is answered and is no longer what this move waits on.** A path-scoped rule **does** reach a
subagent that reads a matching file, measured, with no wiring owed
([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]).

**What it waits on now is a guard.** Probe 4 measured that after a `/compact` an Edit on a matching path
proceeds with no re-read and with no rule in context
([[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]), so **the move does not go
ahead on the strength of *whoever edits it will have read it***
([[the-guard-is-not-built-and-the-ast-move-now-waits-on-it]],
[[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]]).

**The ground above is untouched.** The move is still a rehearsal with one subject and still not about the
context it saves — and the measurement that produced the guard is exactly the kind of thing *"better to
test it on one rule than on ten later"* was meant to buy.

# The rejected alternative is named for this move, and the strict reading is satisfied rather than argued — 2026-08-20

**The rejected alternative for this move is leaving the rule in `CLAUDE.md`.** The gate names it in
advance for the whole class — *"leave both in `CLAUDE.md`"* — and states the terms it is rejected on
([[a-rule-moving-to-conditional-delivery-needs-its-page-first]]):

> **Unconditional delivery costs context and nothing else; conditional delivery costs a rule that
> does not arrive.**

**That price is paid knowingly here.** A rule that does not arrive is the whole risk of the move,
which is why it is taken on one rule rather than on a batch — the ground above, unchanged — and why
it went ahead only once something re-delivers the rule after a `/compact`
([[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]],
[[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]).

## Why this section exists, and what it deliberately does not settle

**What this page rejected until today was the context-saving argument, explicitly and on the owner's
ruling** — the arithmetic above is recorded as a measurement and not as a reason. That is not the
same object as the alternative the gate names, and on a strict reading of the gate — *a dated
`decisions/` page with a rejected alternative before any rule moves* — this page did not carry one
for this move.

**Both readings were available.** Strictly, the gate wants the rejected alternative named on the
move's own dated page, and until this section it was not. Loosely, the gate named it in advance for
the class and nothing further was owed.

**Neither reading was ruled on.** The session closed the gap at the cost of one section rather than
deciding whether it was a gap — the strict reading is **satisfied rather than argued**, and which
reading the gate carries is left open for whoever brings the second move to it. Recording that the
question was not answered is the point: a section written to end an argument would have hidden a
choice nobody made ([[ask-before-weakening-or-working-around-a-rule]]).
