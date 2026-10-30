---
type: decision
case: "937"
status: current
children: ["[[decision-case-937.1]]", "[[decision-case-937.2]]", "[[decision-case-937.3]]"]
origin: raw/2026-10-30/2005/ledger.md#case-937
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, hooks]
---

## Problem

No closer fits a backlog item that a Case of the session defers again with a new wording. The agent takes `[x] … · backlog · case N`, which the check reads as a Case that takes the item off the backlog, or `kept`, which says that no Case stands.

## Recommend

- **Which closer a backlog item takes when a Case defers it again**
  - Recommended: (a) `[-] … · backlog · defer case N`, with the check changed to accept it.
  - Answer: agreed, (a).
- **What the check asks of the Case that the closer names**
  - Recommended: (a) a `defer` of a page that the title names, and the mark `{supersedes:case M}` for each Case M of that page's `deferred_by`.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) two sub-cases. One replaces the Criterion of `estimate-prespec-checks-the-frontier`, which a test run reads. The other creates an Estimate on `rule-orchestration`, read at Retro against the new text in the Spec. `estimate-hi-writes-frontier` stays as it is.
  - Answer: agreed, (a).
- **Which closer a backlog item takes after a take-back**
  - Recommended: (a) the take-back keeps `kept`.
  - Answer: (a).
- **Which slugs of a Frontier line the shared function takes**
  - Recommended: (a) the title only, the text before the first ` · `, with spaces trimmed inside the backticks.
  - Answer: agreed, (a).
- **Change**
  - Asked: a finding of `/pre-spec`: the new check of 937.1 reads the slugs of a title by no shared function, while `deferred_pages` and `frontier_marks` already read them.
  - Taken: 937.1 adds one function in `.guppi/guppi/generate.py` that takes the slugs of a title, and `frontier_marks`, `deferred_pages` and the new check import it.
- **Change**
  - Asked: a finding of `/pre-spec`, which the person agreed to fix: `check_backlog` of `.guppi/guppi/casecheck.py` calls the same `defer` mode, and the Criterion of `estimate-case-check-requires-a-backlog-item-decided-on-its-page` is replaced and read by a test.
  - Taken: the new sub-case 937.3.

## History

- 2026-10-30 created · raw/2026-10-30/2005/ledger.md#case-937
