---
type: decision
case: "544"
status: current
children: ["[[decision-case-544.1]]", "[[decision-case-544.2]]", "[[decision-case-544.3]]", "[[decision-case-544.4]]", "[[decision-case-544.5]]", "[[decision-case-544.6]]", "[[decision-case-544.7]]", "[[decision-case-544.8]]", "[[decision-case-544.9]]", "[[decision-case-544.10]]", "[[decision-case-544.11]]"]
origin: raw/2026-09-30/1306/ledger.md#case-544
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, hooks, ledger, tests, render, schema]
---

## Problem

`case-guppi` can build a Case that departs from the option the person chose, and it can sign a claim about every text in the vault after reading only the pages it named. Two sub-cases of one Case can also contradict each other on one page. All three faults are found only at pre-spec, after ratification. The choices the person makes in the rounds are held by no page. The Decision page shows only the problem, and a Case with sub-cases has no page of its own.

## History

- 2026-09-30 created · raw/2026-09-30/1306/ledger.md#case-544
