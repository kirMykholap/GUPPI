---
type: decision
case: "754"
status: current
create: ["[[estimate-case-build-reads-the-test-code-over-a-changed-text]]"]
update: ["[[rule-case-build]]", "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"]
origin: raw/2026-10-10/1508/ledger.md#case-754
sprint: migration
created: 2026-10-10
tags: [workflow, harness, tests, session, ledger]
---

## Problem

When a Case changes a live text that a test reads, nothing makes `case-guppi` read the test's own code over the new text. A claim that the test still passes is then signed on the check functions alone, and the test breaks first at Retro.

## Recommend

- **A new promise or the old one widened**
  - Recommended: (a) a new Estimate, `estimate-case-build-reads-the-test-code-over-a-changed-text`, beside the old one, which stays as it is.
  - Answer: agreed, (a).
- **Which changed texts the step covers**
  - Recommended: (a) any live file of `vault/` or `.claude/` that the Case changes, by a page `update` or by the render of its rule, when a test reads that file.
  - Answer: agreed, (a).
- **How far the reading of the test goes**
  - Recommended: (a) the whole path the text takes: the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `guppi/` they call.
  - Answer: agreed, (a).
- **What enters the Case, and whether the Insight closes**
  - Recommended: (a) each place where the new text would fail the test enters the Case as a task that changes the test or the text, or `context` says why it stands; the Insight is set `actioned`, with `addressed_by` naming this Case.
  - Answer: agreed, (a).

## History

- 2026-10-10 created · raw/2026-10-10/1508/ledger.md#case-754
