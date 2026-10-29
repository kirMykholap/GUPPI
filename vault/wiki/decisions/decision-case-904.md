---
type: decision
case: "904"
status: current
children: ["[[decision-case-904.1]]", "[[decision-case-904.2]]", "[[decision-case-904.3]]"]
origin: raw/2026-10-29/1930/ledger.md#case-904
sprint: plugin
created: 2026-10-29
tags: [hooks, harness, workflow, session]
---

## Problem

The check of `case-guppi` and the test of the example keep a fallback path whose condition is met, and two promises say that a later Case removes it, a sentence false in any project that installs GUPPI.

## Recommend

- **Is the old path of the check removed, and how do the tests follow?**
  - Recommended: (a) remove it; the test helper writes the Case into its file first, and the tests of the old path go or assert that nothing is stored.
  - Answer: agreed, (a).
- **How does the sentence of `rule-spec-reconcile` on the old path leave?**
  - Recommended: (a) the whole `## How it works` leaves the page by hand, its facts in the docstring of `.guppi/guppi/ratified.py`.
  - Answer: agreed, (a).
- **Does the shape check lose its line on the old path?**
  - Recommended: (a) a part of its own replaces the Criterion, the line reworded to a file that holds sub-cases alone.
  - Answer: agreed, (a).
- **What does the example test do when `case-example.md` is missing?**
  - Recommended: (a) both tests fail with a message that names the file.
  - Answer: agreed, (a).
- **Which page lists the example test as its code?**
  - Recommended: (a) `rule-case-example`, in `implementation_ref`.
  - Answer: agreed, (a).
- **Change**
  - Asked: a finding of `/pre-spec`, which the person agreed to: in a `then` line of Case 904.1, "that file" pointed at `<plan>.checked.json`, which the hook writes.
  - Taken: the line ends "the hook writes no file of a Case".

## History

- 2026-10-29 created · raw/2026-10-29/1930/ledger.md#case-904
