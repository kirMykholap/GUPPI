---
title: "The renamed-vault case is graded on the question it asks, and not on a property nobody chose for it"
type: decision
status: current
authority: renamed-vault-case-scope
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The ruling, 2026-08-19

> **owner: `the vault is renamed` is graded on the one question it asks.**

The case exists to prove **discovery finds a vault whose name is nothing like ours and carries
spaces** ([[the-vault-directory]]). With the sandbox no longer renaming the vault, the case fails —
and **the half it exists for passes**: the check found `a vault with spaces` and named it in every
message, which is visible in the very output that fails the case.

What fails is a **second property the case was asserting without meaning to**: that the corpus does
not name its own directory. That property is false eleven times over
([[the-corpus-names-the-vault-directory-and-a-rename-is-a-rewrite]]).

**Rejected: having the mutation rewrite the eleven citations as it renames.** That restores the green
and hides the finding, which is the worst of the three outcomes: a suite that repairs the evidence it
was about to produce.

**Rejected: leaving the case red.** A standing red is a suite nobody reads, and this one would be red
for a true statement about the corpus rather than for a defect.

# What it obliges

**A case asserts what it was written to assert, and anything else it happens to require is a finding
rather than a failure.** The distinction is what let this one produce a lint entry instead of a fix:
the second property was real, unrecorded, and worth a page.

**Narrowing a gate's assertion is the owner's, not a session's** — the session recorded the honest
reading and did not take it ([[ask-before-weakening-or-working-around-a-rule]]).
