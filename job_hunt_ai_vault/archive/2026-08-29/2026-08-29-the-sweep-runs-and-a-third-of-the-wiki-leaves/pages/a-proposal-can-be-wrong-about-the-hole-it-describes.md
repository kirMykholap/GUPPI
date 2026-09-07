---
title: "A proposal can be wrong about the hole it describes, and nothing corrects it before it is built"
type: lesson
status: archived
authority: proposal-defects
basis: measurement
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-check.sh"]
tags: [vault, testing, process]
---

# Three defects in one unbuilt page, all found before a line was written

The proposal behind the address verdict was written on 2026-08-17 by a librarian reading a journal, and
it was wrong three ways. A `/pre-task` reading the code found all three
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

| What it said | What the code said |
|---|---|
| **Touches** `vault-inject.sh` and `vault-check-selftest.sh` | the join belongs in `vault-check.sh` — which its own *What it would take* paragraph correctly identified, and its Touches line contradicted |
| *"the fifth verdict of rule 12"*, repeated by `sprint.md` and by [[what-the-harness-build-waits-on]] | rule 12 by design contains **no logic of its own** — it asks by running the injector, so an address verdict cannot live in it ([[the-address-verdict-joins-an-existing-rule-instead-of-becoming-its-own]]) |
| the hole is *"a region carrying a rule's slug in a different governed file"* | **that case is already red** — the injector reports the absence in the right file. The hole is the **leftover duplicate** ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]) |

**The third is the expensive one.** A selftest case built from that sentence would have passed **with the
new code reverted** ([[a-test-built-from-a-specification-can-pass-without-the-code]]).

## Why a proposal is a distinct hazard, and not just another stale page

**A proposal is the one page type that describes something nobody can check.** A concept can be read
against the mechanism, an entity against the tree, a lesson against the incident. A proposal describes a
mechanism that does not exist, so **its only reviewer is the session that finally builds it** — by which
time the proposal has been cited elsewhere as though it were a specification, which is exactly what
`sprint.md` and the harness register did with the rule-12 misattribution.

It is the same failure family as an intent note compiled as testimony
([[an-intent-note-compiled-as-testimony-describes-things-nobody-built]]) and a design that stopped being
right when its frame moved ([[a-proposal-must-be-rechecked-when-the-frame-changes]]). What is new here is
that all three defects were **inside the proposal's own reasoning** rather than caused by the world
changing under it.

## What the store has no answer for

**No page records how a proposal's own defect is corrected before the proposal is built.** The three
corrections above are corrections to a page that retires the day the work lands, and the natural place to
put them — the proposal — is the page being retired. They are here instead, on the lesson, because a
lesson outlives the mechanism.

**The cheap discipline, until something better exists: a `/pre-task` reads the code before the proposal.**
That is what happened here, and it cost one dispatch against a test that would have proved nothing.
