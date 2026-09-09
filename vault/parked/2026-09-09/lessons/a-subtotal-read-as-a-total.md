---
title: "A subtotal read as a total, and the true figure was already on the record"
type: lesson
status: current
authority: subtotal-as-total
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-check-selftest.sh"]
tags: [harness, testing, process]
---

# The incident

**A plan described the selftest suite by a number that was the sum of five dispatcher functions the
session happened to enumerate.** Six more dispatchers and sixteen cases written inline were never
counted.

**The true figure matched the last recorded run**, which the session had in front of it while
writing the wrong one.

# Why the check was available and not made

**A total that can be read from a run is never derived by adding up parts.** The suite prints how
many cases it caught; the previous reading was in the corpus. The addition was done because the five
functions were what the session was looking at.

**A subtotal and a total are indistinguishable once written down**, which is what makes this
expensive rather than merely wrong: the number went into a plan and was approved.

# The repair

**Read the figure off the instrument, or say the instrument was not run.** That is what `--list`
now makes cheap — a case count without a thirty-eight-minute run
([[a-printed-register-cannot-drift-and-a-maintained-one-always-has]]).
