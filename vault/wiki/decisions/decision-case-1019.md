---
type: decision
case: "1019"
status: current
children: ["[[decision-case-1019.1]]", "[[decision-case-1019.2]]", "[[decision-case-1019.3]]", "[[decision-case-1019.4]]"]
origin: raw/2026-11-03/1825/ledger.md#case-1019
sprint: plugin
created: 2026-11-03
tags: [sprint, case-build, session, harness, workflow, librarian, ledger]
---

## Problem

A check whose `method` reads the transcript of a later session cannot be read. `/hi` may not open an earlier transcript, and the end-of-session review of that later session does not take it, so the check stays open. A lasting check that names one of our sessions would also ship that name in the clean version.

## Recommend

- **What happens to this check**
  - Recommended: (b) a method that reads the Case file alone.
  - Answer: none of the options; the person does not accept that a transcript cannot be read after `/hi`, which makes it impossible to read what can and should be read, and asked for a fix.
- **Which checks the Case covers**
  - Recommended: (a) this check only.
  - Answer: not answered; replaced by the question "What happens to this check's own reading" and later by "Whether the split becomes a rule".
- **Who reads the transcript of an earlier session**
  - Recommended: (a) `/hi` reads the transcript itself, in parts.
  - Answer: agreed, (a).
- **What happens to this check's own reading**
  - Recommended: (b) a task of this session reads it now.
  - Answer: agreed, (b).
- **How the change is checked**
  - Recommended: (a) replace the text of `estimate-hi-takes-its-readings`.
  - Answer: agreed, (a).
- **How the session start finds the transcript**
  - Recommended: (a) the step finds it by the stamp.
  - Answer: agreed, (a), after the person asked how such a check reaches the clean version and asked for a one-off check of the transcript beside a lasting check.
- **How this check is split**
  - Recommended: (a) a lasting check and a one-off check.
  - Answer: agreed, (a).
- **Whether the split becomes a rule**
  - Recommended: (a) this check only.
  - Answer: agreed, (a); and a separate backlog item asks whether checks should be made this way.
- **Where the backlog item stands**
  - Recommended: (a) a line in the backlog of the sprint page.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, the finding that `rule-raw-archive` says nothing reads an archived session, while Case 1019.1 reads the first line of an archived `spec.md`; the person agreed to option (a), that Case 1019.1 updates the Purpose of `rule-raw-archive`.
  - Taken: Case 1019.1 updates the Purpose of `rule-raw-archive`: nothing changes an archived session, and `/hi` may still read the first line of its `spec.md`. The fixes of the other findings of `/pre-spec` are taken as well: the archived path of `spec.md` and the place of `subagents/` are named in both texts, the `A` step says it does not open that chat, the `context` names the other lasting Estimates that read a transcript, and the `when` and `then` of Case 1019.4 speak of the test of `guppi backlog`.

## History

- 2026-11-03 created · raw/2026-11-03/1825/ledger.md#case-1019
