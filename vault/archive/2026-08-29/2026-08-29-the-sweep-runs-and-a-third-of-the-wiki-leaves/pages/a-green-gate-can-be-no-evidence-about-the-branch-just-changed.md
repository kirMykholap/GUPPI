---
title: "A green gate can be no evidence at all about the branch you just changed"
type: lesson
status: archived
authority: unexercised-branch
basis: measurement
sprint: S2
created: 2026-08-22
sources: ["archive/2026-08-21/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The measurement

**`govsplit()` was made to return nothing, and `bash scripts/vault-check.sh` printed byte-identical
output and exited 0.** The function had just been written; the run said nothing about it.

**Because every rule page in this corpus governs the file its own region already sits in.** Rule 11
compares the region's address against the page's destinations, and no page in the tree makes those
two differ — so the branch is **unreached by the whole corpus**, not merely unlikely to fire.

**Three selftest cases now reach it**, and the selftest count moved by exactly three, from
`caught 144, missed 0` to `caught 147, missed 0` ([[a-case-that-passes-before-the-change-tests-nothing]]).

# It is a third failure shape, and the store already holds the other two

| shape | what is wrong | where |
|---|---|---|
| the verdict cannot fire at all | unreachable by construction; a second report of another rule | [[a-verdict-that-cannot-fire-is-worse-than-no-verdict]] |
| the assertion cannot see the channel | an advisory prints where the exit code never changes | [[a-clean-run-cannot-test-an-advisory-exemption]] |
| **the verdict can fire and no input in the tree makes it** | the gate is green about a class it never examined | this page |

**The third is the quiet one.** The first two are found by asking *when could this fire*; this one
passes that question and still proves nothing, because the answer is *on an input the corpus does not
contain* ([[a-gate-guarantees-agreement-never-truth]]).

# What is unaddressed, and it was found by accident

**Nothing enumerates which other verdicts the tree fails to exercise.** This one surfaced because a
session deliberately broke a function it had just written, which is not a procedure anybody has
written down ([[reverting-the-code-tells-you-whether-a-test-tests-anything]]).

**The general form is the lesson and the gap is open.** A per-verdict coverage reading — which rules
of `vault-check.sh` are reached by the real corpus and which only by the selftest — is named here
and designed nowhere.

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*
