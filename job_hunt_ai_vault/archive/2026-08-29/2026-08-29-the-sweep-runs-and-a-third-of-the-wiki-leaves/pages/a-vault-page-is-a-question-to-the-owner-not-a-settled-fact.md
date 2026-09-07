---
title: "A `current` vault page was treated as settled fact, and it cost a decision that had to be unmade"
type: lesson
status: archived
authority: settled-fact-assumption
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md"]
tags: [vault, process]
---

# The incident: `governs:` decided two opposite ways an hour apart

**First:** dual-root resolution, with ambiguity as a hard error. Designed, argued in writing, and
built.

**Then:** removed entirely, once the owner lifted the constraint the whole design rested on — the
vault directory's name is fixed from now on, so `governs:` is simply a path from the repository
root ([[governs-is-a-path-from-the-repository-root]]).

**The reversal was right.** What went wrong was earlier: the first decision was built on
[[the-vault-directory]] — a `current` page, `basis: code` — **treated as settled fact rather than
as a question worth one line to the owner.** That page records a constraint the owner chose; a
constraint the owner chose is a constraint the owner can lift, and asking cost one sentence.

# The rule

**A page tells you what was decided, not what must remain true.** Before designing *around* a
recorded constraint — especially an expensive design, and dual-root resolution with an ambiguity
error was expensive — check whether the constraint still has an owner behind it.

The `basis:` field is the instrument for this and it points the right way here:
[[the-vault-directory]] is `basis: code`, which means *it follows from the scripts as they stand*.
It does not mean *the owner requires this*. A page on `human` is the owner's word; a page on `code`
is a description of the tree, and the tree is changeable.

**The cost of asking is one line. The cost of not asking, measured here, was a designed, argued and
implemented mechanism thrown away the same afternoon** — and it was found by a `/pre-task` rather
than by the session's own reading ([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

# The second self-contradiction of the same day

The one-writer rule was read two ways in one session and acted on both times, and the session did
not notice it was holding two readings until a hook made it explicit
([[the-hook-was-stricter-than-the-rule-it-enforced]]). Different mechanism, same root: **a written
rule was consulted as an answer instead of as evidence.**
