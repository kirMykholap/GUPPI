---
title: "Measuring a copy of a script placed somewhere else measures nothing, and it fails towards success"
type: lesson
status: current
authority: relocated-script-measurement
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-inject.sh"]
tags: [harness, testing, vault]
---

# The incident

**`scripts/vault-inject.sh` starts with a `cd` to its own parent directory and resolves `governs:`
against the working directory.** A copy of it placed in a scratch directory therefore found no
destination to write, did nothing, and finished in 0.8 s.

**0.8 s reads exactly like a spectacular improvement.** The instrument failed towards *nothing to
do*, which is the direction that gets published.

**Setting an environment variable to point at the vault does not repair it.** The copy has to sit
beside the original.

# The general shape

**A script that locates its inputs relative to itself cannot be measured anywhere but where it
lives.** That is not a defect of the script — resolving relative to itself is what makes two rules
agree about where the vault is — it is a constraint on how it is timed
([[the-selftest-sandbox-is-a-mirror-rather-than-a-renamed-copy]]).

# The guard

**A measurement harness asserts what it expects the subject to have done**, so a run that did
nothing is red instead of fast
([[an-assertion-inside-a-measurement-harness-catches-a-broken-instrument]]). Here that is a count of
files rewritten: zero is a broken instrument, not a result.
