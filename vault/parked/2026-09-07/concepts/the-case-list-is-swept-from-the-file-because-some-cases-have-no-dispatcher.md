---
title: "The case list is swept from the suite's file, because the cases written inline have no dispatcher"
type: concept
status: current
authority: case-list-sweep
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The obvious implementation is the wrong one

**Walking the dispatchers and printing instead of running is what a reader reaches for first.** It
cannot see the cases written inline in the archive, catalogue and units sections, which call
`report` directly and belong to no dispatcher at all.

**It would understate the suite by sixteen while reading as a complete list**, which is the failure
direction a register has: a short list nobody can tell is short.

# So the list is swept out of the file

**`--list` reads the suite's own source and prints the case names it finds**, dispatched and inline
alike. The invariant it exists for is that the list and the run agree, and it held on the first
paired reading ([[a-printed-register-cannot-drift-and-a-maintained-one-always-has]]).

# What the sweep still cannot see

**A case reached by a route the sweep does not recognise is invisible to it**, and nothing reports
that. Completeness is not what a derived list proves; agreement with the code is.
