---
type: decision
case: "595"
status: archived
children: ["[[decision-case-595.1]]", "[[decision-case-595.2]]", "[[decision-case-595.3]]", "[[decision-case-595.4]]", "[[decision-case-595.5]]", "[[decision-case-595.6]]", "[[decision-case-595.7]]", "[[decision-case-595.8]]", "[[decision-case-595.9]]", "[[decision-case-595.10]]", "[[decision-case-595.11]]", "[[decision-case-595.12]]", "[[decision-case-595.13]]", "[[decision-case-595.14]]", "[[decision-case-595.15]]", "[[decision-case-595.16]]", "[[decision-case-595.17]]", "[[decision-case-595.18]]", "[[decision-case-595.19]]", "[[decision-case-595.20]]", "[[decision-case-595.21]]"]
origin: raw/2026-10-02/1834/ledger.md#case-595
sprint: migration
created: 2026-10-02
tags: [session, workflow, harness, ledger, render, hooks]
---

## Problem

The main agent loads the form of a Case it does not build, and the design that moves its own rules into a file of their own was put off twice. At `/pre-spec` it sends fixes to the agents that rebuild the Cases before the person has answered the report's questions, so the chat moves on, new rounds arrive, and an answer may change a fix already sent.

## Recommend

- **Its own Case, or part of the whole move**
  - Recommended: (a) its own Case on `rule-prespec` now, the move left in the backlog.
  - Answer: (b) part of the whole move, now.
- **A report with no question, or a question left unanswered**
  - Recommended: (a) send at once when the report has no question; otherwise hold everything until every question is answered, ask a skipped question again, then send every fix and answer together, one message to each `case-guppi`.
  - Answer: (a).
- **The agents' own questions that come back**
  - Recommended: (a) keep step 2 of the loop as written; the change touches only the first step.
  - Answer: (a).
- **The names of the two new rules and their files**
  - Recommended: (a) `rule-orchestration` rendered into `vault/wiki/orchestration.md`, a new `rule-ratification` rendered into `vault/wiki/ratification.md`, both under `rule-plan-mode`, both loaded by `/hi` in place of `case-schema.md`.
  - Answer: the person first asked whether two files load at `/hi` in place of `case-schema.md`, whether `case-schema.md` goes to `case-guppi` alone, and whether its text moves or is referred to. Told that it is moved, each sentence in one file only, and that `case-schema.md` keeps its name, the person agreed with (a).
- **Where the loop after the findings lives**
  - Recommended: (a) the loop stays in the pre-spec skill, and `orchestration.md` points to it.
  - Answer: (a).
- **How the text of `case-schema.md` is shared out**
  - Recommended: (a) by who acts, sentence by sentence; a sentence both agents need goes to the shared file.
  - Answer: (a).
- **How the checks of the moved behaviours move**
  - Recommended: (b) each moved check is renamed and moved to its new rule, keeping its history and results; the script rewrites every mention.
  - Answer: (b).

## History

- 2026-10-02 created · raw/2026-10-02/1834/ledger.md#case-595
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
