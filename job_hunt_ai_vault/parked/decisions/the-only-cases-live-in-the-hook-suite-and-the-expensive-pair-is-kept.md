---
title: "The `--only` cases live in the hook suite, and the expensive pair is kept"
type: decision
status: current
authority: only-case-placement
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/hook-selftest.ps1", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The ruling, 2026-08-29

**Owner selected: `scripts/hook-selftest.ps1` is the home for the `--only` contract cases.**
The alternative was a case *inside* `scripts/vault-check-selftest.sh` itself, which would have cost a
whole run of that suite per case.

**And he selected keeping the expensive pair**, which took `hook-selftest.ps1` from 55 s to 2m47s and
`make smoke` from about three minutes to about four. **Rejected: dropping the positive half**, which
would have left a `--only` implementation that refuses everything passing every other case
([[a-case-that-passes-before-the-change-tests-nothing]]).

# What the cost is, and what it is not

**Measured beside the change:** one case through `--only` costs **1m57s**; the gate alone costs
**23 s**; almost the whole increase is the single case that lets a suite run *proceed* and therefore
pays for a sandbox copy of the tree and two gate runs.

**It means `make smoke` grows; it does not mean the suite itself got slower.** The suite's own whole
run read 29m12s at 194 cases the same day.

**The journal gives the hook suite's new case count three different ways** — 217, 210 and 204 — and
they are recorded as they stand rather than reconciled ([[vault-scripts]]).

# What the pair is for

**A narrow run that matches nothing used to print `caught 1, missed 0` and exit 0**, so a typo in a
`--only` pattern read as a pass. An unmatched substring now refuses with exit 2 **before the sandbox
is built** ([[a-narrow-suite-run-that-matches-no-case-still-prints-a-catch]]).

**Both halves are needed because a refusal is only correct if something still passes.** The negative
half proves an unmatched pattern refuses; the positive half proves a matched one runs.

**It caught the session's own mistake inside the hour it landed.** A pattern with an alternation was
passed to the suite while testing the advisory cases; the new refusal returned exit 2 and named the
reason. Before that morning it would have printed `caught 1, missed 0` and exited 0.

# The back-fill that travelled with it

**The one-off `processed` back-fill is the librarian's, at the next `/ingest`** — over the roughly 44
decisions already named in a live `decided_by:`. He selected that in the same turn
([[the-librarian-sets-processed-when-it-writes-decided-by-and-the-archiver-reads-each-field]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
