---
title: "An advisory word on a continuation line inflates the count the brief reports"
type: lesson
status: current
authority: advisory-continuation-defect
basis: measurement
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-check.sh"]
tags: [vault, harness, testing]
---

# The failure

**Two advisories in `scripts/vault-check.sh` printed the word `advisory:` on their continuation
lines** — the quote advisory and the `decided_by:` shortfall — against the owner's ruling of
2026-08-18 that **only the headline carries it**.

**The brief reports `grep -c 'advisory:'` as the count of advisories.** Measured before and after the
repair on 2026-08-29: the count read **54** where the true number is **30**.

**Both were written after that ruling and copied the wrong shape from each other.** The filename
advisory — the one the ruling was made for — has obeyed it throughout
([[the-filename-advisory-prints-one-name-per-line]]).

# Why it was invisible

**The output is correct to read and wrong to count.** A person reading the gate's output sees the same
advisories either way; only a counter is misled, and the counter is in a different file
([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]).

**Nothing checks it.** The ruling lives in a comment beside the filename advisory and in this store's
prose, and there is no verdict, no case and no lint that asks whether a continuation line carries the
word. **A check for exactly that is owed and unbuilt.**

# The general shape

**A ruling about the *shape* of output is a contract with whoever greps it**, and it needs an
instrument for the same reason any other rule does — a rule with nothing behind it is one a fixture can
violate for a week ([[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]]).

**And a figure a brief reports must be traceable to the command that produces it.** The count was wrong
in every brief that carried it for as long as the two advisories existed, and no reader could have told
([[a-subtotal-read-as-a-total]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
