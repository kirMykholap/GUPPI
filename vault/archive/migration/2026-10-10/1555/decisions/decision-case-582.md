---
type: decision
case: "582"
status: archived
update: ["[[estimate-ask-finds]]"]
origin: raw/2026-10-01/1725/ledger.md#case-582
sprint: migration
created: 2026-10-01
tags: [session, workflow, harness]
---

## Problem

The Criterion of `estimate-ask-finds` forbids anything after the five lines. A general note of Claude Code, which the vault does not control, makes `ask-guppi` add a list of file paths there in some answers. The check fails on text that breaks nothing. The question was whether the frame forbids the list or the check allows it.

## Recommend

- **Forbid the file list in the frame, or allow it in the check**
  - Recommended: (a) the frame forbids the list, with one sentence that sets aside the general note as the frame of `case-guppi` does, and the check stays strict.
  - Answer: (b) the check allows the list. Before answering, the person asked two things. First, whether anyone uses the list, or whether it only repeats what is already in the context. The answer: the list is not otherwise in the main agent's context, but it repeats the pages the five lines name, and no rule reads it. Second, whether the vault should compete with an instruction of Claude Code it cannot change, or whether the list breaks anything. The answer: nothing breaks, and the choice is only how strict the form of the answer is. The person then chose to accept the list.
- **Does this Case also cover the librarian's file list**
  - Recommended: (a) only `ask-guppi`; the librarian's list stays, and it can be an item of its own later.
  - Answer: (a) only `ask-guppi`.

## History

- 2026-10-01 created · raw/2026-10-01/1725/ledger.md#case-582
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
