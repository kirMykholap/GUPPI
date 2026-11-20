---
type: decision
case: "1029"
status: current
children: ["[[decision-case-1029.1]]", "[[decision-case-1029.2]]", "[[decision-case-1029.3]]", "[[decision-case-1029.4]]"]
origin: raw/2026-11-04/0807/ledger.md#case-1029
sprint: plugin
created: 2026-11-04
tags: [session, workflow, harness, hooks, sprint]
---

## Problem

Every Case costs the same build, whatever it changes, and no count shows where the time goes. The person wants the main agent to dispatch `case-guppi` at a chosen effort, a measure of what that gives, and a decision on keeping it.

## Recommend

- **Which level for which Case**
  - Recommended: (a) three kinds by what the Case changes, `low`, `medium` and `high`, the person's word overriding.
  - Answer: agreed, (a).
- **The model at the dispatch**
  - Recommended: (b) `sonnet` only on the person's word for a session.
  - Answer: (a) effort only; the call passes no model.
- **Raising the level during a Case**
  - Recommended: (b) a new dispatch one level up only when the Case proves to be of a higher kind.
  - Answer: (a) no raise; the level chosen at the dispatch holds to the end of the Case.
- **Whether `ask-guppi` enters this Case**
  - Recommended: (a) it stays out.
  - Answer: agreed, (a).
- **How the time and tokens are measured**
  - Recommended: (a) a command with a test.
  - Answer: agreed, (a).
- **When the trial ends**
  - Recommended: (a) at the close of the sprint `plugin`, a check on the sprint page waiting for the person's answer.
  - Answer: agreed, (a).
- **The rest of the brief item**
  - Recommended: (a) left to the decision after the trial.
  - Answer: agreed, (a).
- **The page of the new command**
  - Recommended: (a) add the paths to `rule-context-size`.
  - Answer: agreed, (a).
- **Change**
  - Asked: by the line Other Case of Case 1031, whose round the person answered (a), the Criterion that Case 1029.2 writes drops the promise and the split from its forks, and its lines on a fix that adds a second behaviour, on a new Case beside a ratified one and on a change asked on a named Case give way to one pointer to `estimate-case-build-settles-form-by-itself`.
  - Taken: the Criterion of Case 1029.2 changed so; each other word of it stands.

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#case-1029
