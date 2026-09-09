---
title: "A measurement taken while other work runs against the same disk measures nothing"
type: lesson
status: archived
authority: measurement-under-load
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The spread was larger than the effect

**Three runs of `bash scripts/vault-check.sh` on an unchanged tree, on 2026-08-24: 25.3, 16.2 and
19.3 seconds real.** The antivirus exclusion the runs were meant to evaluate could not produce an
effect that large, so **none of the three says anything about it**
([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

# And the subject was wrong before the noise was

**`vault-check.sh` reads the vault and builds no sandbox**, so an exclusion aimed at a sandbox path
could not touch it. **The proposal's subject is the suite**, whose sandboxes are `mktemp -d` under
the system temp directory ([[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]]).

**Both sandboxes land in the system temp directory rather than the harness's own.** `mktemp -d`
resolves to `C:\Users\kir\AppData\Local\Temp` and so does `[System.IO.Path]::GetTempPath()`, so an
exclusion aimed at `...\Temp\claude` would have covered neither.

# The one run that was the right subject was contaminated too

**`bash scripts/vault-check-selftest.sh`: caught 168, missed 0, exit 0, 34m8s real / 19m50s user /
43m22s sys at 562 files, against a recorded 27m15s / 15m11s / 32m51s at 543.** While it ran, the
hook selftest ran twice, the gate three times, the injector twice, and two commits landed — all
against the same disk.

**The one reading that survives is a ratio, and it did not move**: `sys`/`user` was 2.16 before and
is 2.19 now. That is what you would expect if the exclusion did nothing, **and it is not clean
evidence**, because concurrent work inflates both terms
([[a-loss-measured-between-different-quantities-is-not-a-loss]]).

# The honest reading, and it is the whole lesson

**Not measured yet.** A measurement needs an idle machine, and this one costs 34 minutes at full
idle — takeable at the start of any session, and taken at the end of none
([[measure-before-optimising-and-count-processes-not-pages]],
[[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).
