---
type: decision
case: "1011"
status: current
children: ["[[decision-case-1011.1]]", "[[decision-case-1011.2]]", "[[decision-case-1011.3]]", "[[decision-case-1011.4]]"]
origin: raw/2026-11-02/2155/ledger.md#case-1011
sprint: plugin
created: 2026-11-02
tags: [hooks, harness, workflow, session, case-build, ledger]
---

## Problem

The limit of 20 files is a guess, and it counts files the agent has already read, so a page with many Estimates gets a note with only a count while few unread files remain; and `case-guppi` reads the Criterion of every Estimate of a changed page, whatever that Estimate speaks of.

## Recommend

- **What the Case does with the limit of 20 files**
  - Recommended: (b) keep 20, and count only the files the agent has not read.
  - Answer: (b) at first; the person then said that no fixed number makes sense, since any number is a guess, and the question "What replaces the limit of 20 files" replaced this choice.
- **What count the note of a broad name gives**
  - Recommended: (a) the count of the unread files, with words that say so.
  - Answer: not answered; replaced by "What replaces the limit of 20 files".
- **What the note of names asks of the agent**
  - Recommended: (a) keep the note as a pointer, as today.
  - Answer: not answered; the person asked that the hook point to the files by their purpose and require no reading of everything, with `/pre-spec` to show a miss; replaced by "What replaces the limit of 20 files".
- **Which Estimates of a changed page the agent reads**
  - Recommended: (a) a separate item, not this Case.
  - Answer: (b), in this Case, so the question is settled at once.
- **What replaces the limit of 20 files**
  - Recommended: (a) one list per Case, with no number and no duty per file.
  - Answer: (a).

## History

- 2026-11-03 created · raw/2026-11-02/2155/ledger.md#case-1011
