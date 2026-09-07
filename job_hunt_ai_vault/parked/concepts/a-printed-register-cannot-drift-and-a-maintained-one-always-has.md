---
title: "A printed register cannot drift, and a maintained one always has"
type: concept
status: current
authority: derived-register-proof
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh"]
tags: [harness, vault, testing]
---

# The mechanism

**`bash scripts/vault-check.sh --rules` sweeps the gate's own headings and prints them.**
**`bash scripts/vault-check-selftest.sh --list` sweeps the suite's own file and prints its cases.**
Neither is written by hand and neither can disagree with the thing it describes, because it is read
out of it.

**This is the same shape as a check that asks its question by running the writer it checks**
([[a-check-asks-by-running-the-writer-it-checks]]) — the register and its subject cannot diverge
when one is derived from the other in the moment of asking.

# How a register is proved derived, and it is not by counting

**The case that proves it is a mutation.** Remove a heading in the sandbox and require the row to
vanish. Counting the printed output against the same headings the feature reads is green under any
implementation — including a list typed in by hand — so it proves nothing at all
([[the-selftest-is-a-mutation-test-of-the-gate]],
[[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

# What neither of them proves, stated because it is the hole

**Neither proves the register is complete.** A rule the gate can emit with no heading is invisible
to `--rules`; a case reached by some route the sweep does not recognise is invisible to `--list`.
**Nothing reports either.**

**And the invariant that a printed list matches the run is worth having anyway**: the first paired
reading of the suite agreed exactly, and an agreement that is checked is the only kind that
survives.
