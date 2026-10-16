---
type: decision
case: "865"
status: current
children: ["[[decision-case-865.1]]", "[[decision-case-865.2]]", "[[decision-case-865.3]]", "[[decision-case-865.4]]"]
origin: raw/2026-10-16/2104/ledger.md#case-865
sprint: plugin
created: 2026-10-16
tags: [session, hooks, harness, ledger, workflow]
---

## Problem

A `defer` of a Lesson or a Decision page writes no `deferred_by`, so `backlog.md` never lists the item, and nothing in the session refuses such a defer.

## Recommend

- **What should a defer of a Decision page or a Lesson do?**
  - Recommended: (a) refuse it: `/pre-spec` reports it and `generate` fails the entry alone, whether the page exists or not, and the person defers the rule or entity page whose change would settle the matter.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) one part per piece of code, each with its own check text rewritten, both reading one shared function.
  - Answer: agreed, (a).
- **At which moments is such a defer refused?**
  - Recommended: (a) also at ratification, in both hooks: the hook of `rule-spec-write` does not write the short defer, and the hook of `rule-ledger-write` does not write its line; `/pre-spec` and `generate` keep the check; four parts.
  - Answer: (a).

## History

- 2026-10-17 created · raw/2026-10-16/2104/ledger.md#case-865
