---
type: decision
case: "344"
status: current
update: ["[[estimate-prespec-binds-a-sprint-line]]"]
supersedes: ["[[decision-case-338.1]]"]
origin: raw/2026-09-22/2046/ledger.md#case-344
sprint: migration
created: 2026-09-22
tags: [harness, workflow, sprint]
---

## Context

Case 338.1 of the conserved Spec brings the Criterion of `estimate-prespec-binds-a-sprint-line` to what the code does after case 335: the test runs on the source segment of a Frontier line — the one before the closer — and not on every segment. It changes the `When` and the `－` line and leaves the `method` field in the old wording: the last case of the run there still reads "a line without sprint among its segments". After 335 that case distinguishes nothing. The case that does is a line where the word `sprint` stands inside the slug of a title while the source segment is another word — the false positive `prespec --check` prints today on line C6 of session 1724, whose source is `brief` and whose title holds `estimate-sprint-migration-index-dissolved`.
The page stands `passed`, its target is `rule-prespec`. Case 335 of the same Spec changes `prespec.check_frontier` and `estimate-prespec-checks-the-plan`, not this page. The page carries no `estimates` field of its own.

## Problem

The Criterion moves to the source segment while the `method` still tells the reader to run the old case; a reading taken by that method measures what the code no longer distinguishes.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#case-344
