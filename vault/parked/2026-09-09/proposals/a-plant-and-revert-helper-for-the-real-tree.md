---
title: "A plant-and-revert helper for the real tree, where the sandbox has one and the real tree has nothing"
type: proposal
status: current
authority: real-tree-plant-harness
basis: inference
sprint: S3
created: 2026-08-26
decided_by: [[the-lessons-collector-is-a-reading-dispatch-and-the-librarian-writes-what-it-returns]]
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check-selftest.sh"]
tags: [harness, testing, vault]
---

# What it would be

**A helper that plants an offender in the real tree, runs the check, and reverts — as one
operation.** The sandbox already has `diff -rq` to prove it came back clean; the real tree has
nothing, and every proof done against it so far has been a sequence of hand steps whose revert is
the step most easily forgotten.

# Why the real tree gets planted at all

**Three refusals were verified by planting offenders in the real tree, in both directions**, on
2026-08-23 — because a sandbox that does not hold 653 pages cannot answer *does this produce a false
refusal today*. That question is asked of the corpus, not of a fixture
([[vault-archive-sh]], [[a-fixture-owns-every-end-of-what-it-asserts]]).

# What it is narrow about, and the collector said so itself

**It closes the plant half of a thirteen-page family and nothing else.** The family is about proofs
run against live state; the other half — knowing what the live state was before the plant — is a
different problem and this does not touch it.

**Its own worked example is one this session produced**: a mutation that flipped a condition to
`if false` ran the other branch and was redone through `git stash`
([[a-guard-is-removed-whole-or-the-proof-is-not-a-proof]]). A helper whose revert is `git stash pop`
would have made the second attempt the first one.

# What is open

- **What it may plant.** Planting inside `wiki/` makes the librarian's own one-writer guarantee
  briefly false, and the guard hook cannot tell who is writing
  ([[the-librarian-writes-unattended]]).
- **What happens when the check crashes mid-run.** A revert that does not run leaves a planted
  offender in the corpus, which is worse than the hand method it replaces.
- **Whether it belongs in `scripts/` at all**, or is a step inside the selftest that already owns
  the sandbox.

# Its `decided_by:` will need re-pointing

**It names the decision that created the collector**, because no per-topic ruling exists for it. The
field moves the day the owner rules on this proposal.
