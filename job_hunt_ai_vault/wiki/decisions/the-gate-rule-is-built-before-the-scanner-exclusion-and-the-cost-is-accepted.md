---
title: "The gate rule delegating to the measure writer is built before the scanner exclusion, and the suite cost is accepted"
type: decision
status: current
authority: gate-rule-build-order
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check.sh"]
tags: [vault, harness, testing]
---

# The ruling, 2026-08-26

> **owner:** «можем строить E2 с лишними минутами, ничего страшного»

**Build the gate rule that delegates to `scripts/vault-measure.py` now, and accept the suite cost**,
rather than taking the ratified scanner exclusion first
([[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]]).

# The cost he was asked about was wrong by a factor of eight

**Asked with the cost stated as roughly four minutes**, extrapolated from rule 13's 1.5 s.

**Measured afterwards: 0.28 s per gate run, about 50 seconds over the suite's roughly 171 gate
runs.** The estimate was eight times too high
([[a-cost-measured-on-a-script-is-not-the-cost-it-adds-to-what-runs-it]]).

**The ruling is not reopened by that.** He accepted a cost larger than the one incurred, and the
decision stands on the smaller figure as much as on the larger one. **What is recorded is that the
question was put with a number nobody had measured** — the price of asking permission from an
estimate rather than from a reading.

# What it does not overturn

**The scanner exclusion is still first for the *narrowing* work.** That proposal's own order —
measure, then exclude, then narrow the gate — is untouched; what this ruling settles is that a new
rule need not wait behind it ([[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]],
[[the-gate-flag-fork-is-recorded-and-nothing-is-built]]).

# Rejected

**Rejected: doing the scanner exclusion first and adding the rule afterwards.** It would have left
the measure region with no check while the corpus began carrying regions, which is the window the
rule exists to close ([[the-gate-delegates-by-running-the-writer-it-checks-and-reads-lines-not-exit-codes]]).
