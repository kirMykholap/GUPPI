---
type: decision
case: "783"
status: current
children: ["[[decision-case-783.1]]", "[[decision-case-783.2]]"]
origin: raw/2026-10-12/2252/ledger.md#case-783
sprint: plugin
created: 2026-10-12
tags: [harness, workflow, ledger, session]
---

## Problem

A defer of an Estimate with no page makes `guppi generate` write a stand-in check page whose status the check page format does not allow. Nothing in the session reports such a defer.

## Recommend

- **What should a defer of a check that has no page do?**
  - Recommended: (a) defer the page the check would test: a defer never makes a stand-in check page, and a defer of a check with no page that reaches `guppi generate` fails there alone.
  - Answer: agreed, (a).
- **Should this Case also fix the stand-in Insight page?**
  - Recommended: (a) leave the Insight out; `context` notes the defect as found and not fixed.
  - Answer: agreed, (a).
- **What catches a defer of a check with no page before the librarian's run?**
  - Recommended: (a) `/pre-spec` reports it, by the same test of whether a page exists that the step before `guppi generate` uses for a defer, and `guppi generate` refuses it as a backstop.
  - Answer: agreed, (a).
- **Which existing checks should cover the two changes?**
  - Recommended: (a) two parts, each rewriting one existing check: `guppi generate` fails the defer and `estimate-generate-writes` is rewritten; `/pre-spec` reports it, the rule for short Cases gains one sentence, and `estimate-prespec-checks-the-form-of-an-item` is rewritten.
  - Answer: agreed, (a).

## History

- 2026-10-12 created · raw/2026-10-12/2252/ledger.md#case-783
