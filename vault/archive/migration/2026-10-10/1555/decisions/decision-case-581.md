---
type: decision
case: "581"
status: archived
children: ["[[decision-case-581.1]]", "[[decision-case-581.2]]"]
origin: raw/2026-10-01/1441/ledger.md#case-581
sprint: migration
created: 2026-10-01
tags: [session, workflow, harness, hooks]
---

## Problem

The loop after the findings of `/pre-spec` forbids any text in the chat while an answer of a `case-guppi` is out. But each answer opens a turn of its own, and each turn ends with a reply, so the clause cannot hold and its Estimate failed. The question was what the main agent may write in those turns, how that line gets past the end-of-reply check when an answer brings a round, whether the same allowance covers waits outside the loop, and what to do with the check's stated reason that the loop runs in one turn.

## Recommend

- **What the main agent may write while it waits**
  - Recommended: (a) one short line in each waiting turn: the turn that sends the fixes and each turn opened by an answer while another is still out end with one line that names the Cases that have answered and those still out, and nothing of what an answer says, and no question.
  - Answer: (a).
- **How the waiting line gets past the end-of-reply check**
  - Recommended: (a) the line opens with a fixed bold label such as `**Waiting:**`, which the check accepts as it stands, with no code change.
  - Answer: (a).
- **Waits outside the loop after the findings**
  - Recommended: (a) only the loop after the findings: only step 2 of `/pre-spec` changes, and waits in ordinary Plan Mode stay as they are.
  - Answer: (a).
- **The check's stated reason that the loop runs in one turn**
  - Recommended: (a) correct the reason everywhere, behaviour unchanged: a second part of the Case rewrites the reason on `rule-case-check` and in the docstrings of `guppi/casecheck.py`, and replaces the promise of the check whole with the same behaviour and the true reason, read again in a later session.
  - Answer: (a).

## History

- 2026-10-01 created · raw/2026-10-01/1441/ledger.md#case-581
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
