---
title: "An estimate can be wrong in its reasoning and not only in its number"
type: lesson
status: archived
authority: estimate-reasoning-error
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["scripts/vault-check-selftest.sh", "archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md"]
tags: [testing, harness, process]
---

# The incident

**The narrowed suite's floor was estimated at about six minutes, reasoned as sixteen inline cases at
one full gate run each.** Measured 2026-08-26 on a 682-file corpus:
`bash scripts/vault-check-selftest.sh --only <a pattern matching nothing>` takes **101 seconds**,
exit 0, reporting `caught 1, missed 0` with 177 cases skipped.

**The number was wrong by a factor of three and a half. The reasoning was wrong about what the
inline cases do** — they do not each copy the corpus and run the gate.

# Why the reasoning matters more than the number here

**The same reasoning is what makes people believe narrowing the suite cannot help.** If every inline
case really did cost a full gate run, the floor would dominate any slice and narrowing would buy
almost nothing; the whole subset design would be pointless
([[the-suite-gets-a-subset-mode-that-issues-no-verdict]]).

**A wrong number is corrected by measuring once. A wrong model keeps producing wrong numbers**, and
it produces them confidently, because it explains itself.

# What the floor figure does and does not mean

**It is the cost of the inline cases whose verdicts the filter drops but whose work it cannot skip.**

**It does NOT mean a useful slice costs 101 seconds** — the named cases are added on top, and a
filtered run is not a reading of the suite, as the script's own line says
([[a-truncated-report-hides-the-line-it-was-run-for]]).

**One reading, one machine, one corpus size.** The corpus is the term that grows, so this figure ages
the way every other suite figure here has
([[every-recorded-fix-for-the-suite-attacks-a-constant-and-the-corpus-is-the-term-that-grows]]).

# What follows

**An estimate offered before a run is worth stating as reasoning, not only as a number**, because the
reasoning is the part a reader can check without paying for the run. This one was stated as a number
with the reasoning attached, which is what made the error findable at all.

**The estimate was the session's own and not the vault's.** Nothing here had recorded a floor, so
nothing was contradicted — which is why the correction is written down rather than assumed to be
somebody else's ([[a-negative-measurement-that-is-not-written-down-gets-proposed-again]]).
