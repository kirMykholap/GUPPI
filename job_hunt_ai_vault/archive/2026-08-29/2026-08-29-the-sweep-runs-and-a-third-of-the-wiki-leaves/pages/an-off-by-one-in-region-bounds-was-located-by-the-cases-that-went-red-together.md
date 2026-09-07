---
title: "An off-by-one in region bounds put every first measurement outside its own region, and the cases that went red together located it"
type: lesson
status: archived
authority: region-bounds-off-by-one
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-measure.py", "scripts/vault-measure-selftest.py"]
tags: [harness, testing, vault]
---

# The defect

**`scripts/vault-measure.py` computed a region's bounds one line short**, so the **first**
measurement written into a region landed outside it. The refresh pass then walked past a gauge it
could not see — a write that succeeded and a read that found nothing.

**Fourteen selftest cases went red at once and located it.**

# What the fourteen are worth

**A single case would have said the same thing and pointed nowhere.** Fourteen failures sharing one
property — every one involving the first line of a region — is a description of the bug rather than
a report of it, and the diagnosis came out of the pattern instead of out of a debugger.

**This is the return on writing cases per behaviour rather than per feature.** The suite reported
`caught 59, missed 0` afterwards, and each of the five refusal guards, removed in turn, reddened
only its own cases: 2, 2, 1, 1, 2 — so the case set is tight as well as dense
([[vault-measure-py]], [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

# The class

**A boundary that is written to and read back by the same code will agree with itself.** The write
put the number where its own bounds said, and only a reader with an independent idea of where the
region starts — here, the fourteen assertions — could disagree with it.
