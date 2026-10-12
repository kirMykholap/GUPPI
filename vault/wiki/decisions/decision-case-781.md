---
type: decision
case: "781"
status: current
children: ["[[decision-case-781.1]]", "[[decision-case-781.2]]", "[[decision-case-781.3]]", "[[decision-case-781.4]]", "[[decision-case-781.5]]", "[[decision-case-781.6]]", "[[decision-case-781.7]]", "[[decision-case-781.8]]", "[[decision-case-781.9]]"]
origin: raw/2026-10-12/1604/ledger.md#case-781
sprint: plugin
created: 2026-10-12
tags: [session, workflow, ledger, harness, render, librarian, schema]
---

## Problem

A check that can only be read after an outside event cannot be written. A reading that `/hi` cannot take turns into a decision at the start of the next session, though nothing about it needs deciding at once.

## Recommend

- **May a check wait for an event other than the close of a sprint?**
  - Recommended: (b) allow any event the method names; `/pre-spec` stops reporting it, and the brief keeps the reading out of Work until the event has happened.
  - Answer: agreed, (b).
- **What should `/hi` do with a Work reading it cannot take?**
  - Recommended: (b) the path the person proposed: the reading stays in Work, the librarian flags it in the brief, and at the next `/hi` a line proposes to defer it into the backlog.
  - Answer: agreed, (b).
- **Should this Case add a `/pre-spec` check on the wording of a check?**
  - Recommended: (a) leave it out.
  - Answer: agreed, (a).
- **How does a check name the event it waits for?**
  - Recommended: (a) a fixed opening inside the method: a part that opens with "after" and the event, then a colon; one function in `guppi/lint.py` judges it.
  - Answer: agreed, (a).
- **Who sees that the event has happened, and who then reads the check?**
  - Recommended: (a) the librarian at its run looks for the event in the ledger, git log, handoff and files, and once it sees the event puts the reading under Work or Ask; that session's `/hi` or Work Mode reads it.
  - Answer: agreed, (a).
- **What does Retro do with a new check whose event has not happened yet?**
  - Recommended: (a) leave it pending, as for the sprint page; the handoff names it with its event; Retro reads it if the event happens in the same session.
  - Answer: agreed, (a).
- **One Case with parts, or two Cases?**
  - Recommended: (a) one Case with six parts.
  - Answer: agreed, (a); replaced by the later questions that set the parts again.
- **How are the new checks on Retro and the librarian read?**
  - Recommended: (a) at this session's Retro, from the new rule text in the plan.
  - Answer: agreed, (a).
- **How does a put-off check reach the backlog?**
  - Recommended: (a) a defer marks a check `deferred_by` as it marks a rule, the format for check pages allows the field, and the brief leaves a put-off check out of Work; one more part.
  - Answer: agreed, (a).
- **The handoff report also changes**
  - Recommended: (a) one more part: the handoff names a new check whose event has not happened, with its event, and its check is replaced.
  - Answer: agreed, (a).
- **Retro's waiting check replaces an existing check**
  - Recommended: (a) rewrite `estimate-retro-loads` with one more exception, read at this session's Retro.
  - Answer: agreed, (a).
- **The two librarian parts share one existing check**
  - Recommended: (a) merge the two librarian parts into one that replaces the Criterion of `estimate-brief-written`, its method a reading at this session's Retro.
  - Answer: agreed, (a).
- **Allowing a check to be put off needs its own part**
  - Recommended: (a) one more part for the format, which replaces the Criterion of `estimate-estimates-schema-checked`; the Case has eight parts.
  - Answer: agreed, (a).
- **What happens to a check whose change is taken back?**
  - Recommended: (a) a take-back marks the check too: it stands in the backlog and stays out of Work until a Case takes it up.
  - Answer: agreed, (a).

## History

- 2026-10-12 created · raw/2026-10-12/1604/ledger.md#case-781
