---
type: decision
case: "639"
status: archived
update: ["[[rule-ask]]", "[[estimate-ask-finds]]"]
origin: raw/2026-10-05/0109/ledger.md#case-639
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Problem

The first answer of `ask-guppi` at `/pre-spec` still writes a paragraph of what holds under a question, mostly about the clash with another Case that it did not find. The frame forbids this, but it does not say what stands under a question when nothing is found. Both answers also ended their list of what was not checked with a note on a search rule they broke, and neither the frame nor the check speaks of such a note.

## Recommend

- **How the answer is kept free of a paragraph of what holds**
  - Recommended: (a) say it plainly: under each question stand only its numbered findings, or "none" alone. No sentence on what was checked and found sound, and this includes a clash with another Case that was not found. The check gets the same line. No code changes.
  - Answer: (a).
- **Whether a note on a rule the agent broke may stay in the answer**
  - Recommended: (b) allow it: the list of what was not checked may end with one line for each rule the agent broke in its search, saying whether a finding rests on it. The rule and the check say so.
  - Answer: (b).

## History

- 2026-10-05 created · raw/2026-10-05/0109/ledger.md#case-639
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
