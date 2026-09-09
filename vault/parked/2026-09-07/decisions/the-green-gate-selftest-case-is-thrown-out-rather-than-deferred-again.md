---
title: "The green-gate selftest case is thrown out for good, because it makes the sprint's first criterion unreadable exactly when the criterion is needed"
type: decision
status: current
authority: green-tree-case-deferral
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
supersedes: "[[the-green-gate-selftest-case-is-deferred-and-the-fixture-repair-cannot-reach-it]]"
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "scripts/hook-selftest.ps1"]
tags: [testing, harness, vault]
---

# The ruling, 2026-08-26, in his own words

> **owner:** «Понял. выбрасываем кейс»

**The case `lock allows the librarian on a green gate` is removed from `scripts/hook-selftest.ps1`**,
after being deferred three times.

# The argument that ended it

**The case prints `MISSED` on a red tree.** Criterion 1 of S3 is read off `missed 0`, so this case
makes the criterion unreadable **precisely when the tree is red** — which is the only time anybody
needs to read it ([[failing-loudly-with-the-wrong-diagnosis]]).

**A test that is only wrong when you need it is worse than the absent test**, because its failure is
indistinguishable from the failure it is meant to report.

# What is lost, and it is accepted

**Nothing else can tell a working lock from a lock that refuses everything.** The deferral page it
replaces says so: the case's whole value is that it does *not* run in a fixture, and the sandbox
vault cannot be green ([[the-librarian-lock-hook]],
[[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).

**So the lock's green path goes untested.** That is the price, stated here rather than discovered
later.

# Rejected

**Rejected: a fourth deferral.** The case had been deferred since 2026-08-20 with no repair shape
ever found ([[a-repeated-deferral-names-the-sprint-it-happens-in-or-is-refused]]).

**Rejected: applying the fixture ruling to it**, which the superseded page had already refused — it
would delete the case's only reason to exist while keeping the case.

# What it obliges, and it is not done

**The removal is an edit to `scripts/hook-selftest.ps1`**, which is a session's file. It waits with
the rest of the plan's third phase
([[the-plans-remaining-phase-moves-to-s3-and-the-ritual-runs-whole]]). **Until it lands, the count
`caught 148, missed 0` stands and the case is still in the suite.**
