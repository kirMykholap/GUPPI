---
type: decision
case: "954"
status: current
children: ["[[decision-case-954.1]]", "[[decision-case-954.2]]", "[[decision-case-954.3]]"]
origin: raw/2026-10-31/0128/ledger.md#case-954
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, hooks]
---

## Problem

The hook that keeps `ask-guppi` out of the Decision pages was never seen to refuse a real call, since `ask-guppi` never makes one; the main agent may not start `ask-guppi` outside `/pre-spec` to make one on purpose, and the frame of `ask-guppi` names no reason to make one.

## Recommend

- **What to do with the deferred reading**
  - Recommended: (b) a test by hand in this session's Work Mode, method changed.
  - Answer: agreed, (b).
- **How the trial reaches `ask-guppi` outside `/pre-spec`**
  - Recommended: (b) the Case also changes the sentence of `rule-orchestration`.
  - Answer: agreed, (b).
- **How the change to the rule is checked**
  - Recommended: (a) a new check, read by the trial itself.
  - Answer: agreed, (a).
- **How wide the exception is**
  - Recommended: (b) only a test of a hook that judges the calls of `ask-guppi` itself.
  - Answer: agreed, (b).
- **When the trial runs**
  - Recommended: (a) the trial waits for the first Work Mode after that render.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, a finding that the frame of `ask-guppi` forbids the call the trial asks for, and that the rule says that frame names no reason for it; the person chose that Case 954 also changes the frame of `ask-guppi`, so that it names one reason to try such a call, the hook trial a ratified Case names, the call made to be refused and the page never read, with an Estimate of its own.
  - Taken: Case 954.3 updates `rule-ask` and `rule-search-leaves-out-decisions` and creates `estimate-ask-tries-a-decision-call-only-for-a-hook-trial`.
- **Change**
  - Asked: at `/pre-spec`, findings that the exception allowed a task but not a Work reading, that an `update` of the `method` alone leaves the `read` box with nothing to read, that the `then` of Case 954.1 named a backlog reading its `method` does not take, and that the `method` of the new check of Case 954.2 named no session.
  - Taken: the exception and the `when` of Case 954.2 cover the Work reading of an Estimate too; Case 954.1 writes its Criterion back word for word and sets it `pending`; each new `method` names the session whose brief puts the reading under Work.

## History

- 2026-10-31 created · raw/2026-10-31/0128/ledger.md#case-954
