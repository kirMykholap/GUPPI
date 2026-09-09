---
title: "A cosmetic change is load-bearing when a test greps the output"
type: lesson
status: archived
authority: cosmetic-change-retest
basis: measurement
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The instance

**The filename advisory was reformatted after the suite had been run** — one name per line instead
of a comma-run ([[the-filename-advisory-prints-one-name-per-line]]). The change touched no logic and
no verdict, and it is exactly the kind that gets committed without a re-run.

**A selftest case greps that output.** The suite was run again: **112 caught, 0 missed**. It
survived — on a day that had already found a *"measured"* figure nobody measured
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

# Why the category *cosmetic* is the hazard

**"Cosmetic" is a claim about the code, and the test is downstream of the output.** For any script
whose contract is what it prints, the output *is* the interface — so a formatting change is an
interface change, and the only thing that distinguishes a safe one from a breaking one is which
strings somebody matched on.

**And the instruments that police an advisory can only read the text**, because an advisory does not
move the exit code ([[a-clean-run-cannot-test-an-advisory-exemption]]). The more of a check's
behaviour is carried in prose rather than in status, the more of its formatting is load-bearing.

**The cost of the rule is a rerun.** The cost of not having it is a green suite testing a string
that no longer exists — which is the same failure this store records from the other side, a case
that cannot fire ([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).

# A second instance, 2026-08-19, and the pair is what makes the rule readable

**Changing the `ruleclaim` verdict's wording broke an existing selftest case**
([[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]]). **Changing the filename
advisory's heading broke nothing** ([[the-filename-advisory-prints-one-name-per-line]]).

**The difference was knowable only by grepping the suite.** Both are message edits inside the same
script, in the same session, and nothing about either one announces which of them a test depends on.

**Both were caught before the commit, and by different instruments** — one by a grep of the suite for
the message text, one by the suite itself, run against the pre-change scripts
([[a-case-that-passes-before-the-change-tests-nothing]]). That pairing is the practical rule: **grep
the message before you change it, and run the suite after**, because the grep is cheap and the suite
is the only thing that answers for the case you did not think to grep.

# A third instance, 2026-08-23, and this time the session had priced the risk one phase away

**A message was deleted rather than reworded, and a selftest case grepped it.** Removing the
hardcoded status pair from `scripts/vault-check.sh` took the sentence *"the schema has only current
and deprecated"* with it; the case `a status the schema lacks` greps the gate's output for
`status 'draft'`, and the suite went from `caught 158, missed 0` to `caught 157, missed 1`
([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

**The behaviour never lapsed.** The gate still reddened an illegal status; only the string the case
matched on had gone. **This page's rule — grep the message before you change it, run the suite
after — would have caught it at the first half**, for the price of one grep.

**The uncomfortable part is that the risk was written down and scheduled.** The plan the session was
executing names this exact hazard under phase H1, where the gate's messages get a `--json`
envelope — and the session walked into it in phase B, four phases earlier, without recognising it.
**Pricing a risk into a later phase is not a defence against meeting it in an earlier one**
([[knowing-a-rule-is-not-a-mechanism]]).

**And the coupling is now written down as a property of the suite rather than as an incident**:
`scripts/vault-check-selftest.sh` greps the gate's output, so **any** reshaping of its messages is a
rewrite of the suite — the `--json` envelope of phase H1 most of all. **Exit code 2 is already taken
by a usage error**, so a new machine surface cannot signal through it either
([[the-gate-exits-on-a-usage-error-with-a-code-of-its-own]]).

**What the suite ran on that day is a separate finding**: it ran at all only because a librarian
dispatched for something else flagged an unrelated case
([[a-local-proof-that-a-new-verdict-fires-is-not-a-regression-run-of-the-old-ones]]).
