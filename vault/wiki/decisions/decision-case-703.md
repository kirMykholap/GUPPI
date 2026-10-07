---
type: decision
case: "703"
status: current
children: ["[[decision-case-703.1]]", "[[decision-case-703.2]]", "[[decision-case-703.3]]"]
origin: raw/2026-10-07/0636/ledger.md#case-703
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow, session, ledger]
---

## Problem

A tag that `tags.md` does not hold can reach a page through a lesson line or a Case, and nothing stops it before the librarian's run.

## Recommend

- **Whether a check stops an unlisted tag, and where**
  - Recommended: (a) two checks: the check of the Case file sends back a `create` with an unlisted tag, and the ledger hook refuses a new lesson line with one; both read the list through one shared function.
  - Answer: agreed, (a).
- **Which tags count as listed**
  - Recommended: (a) a row of `tags.md`, or a tag declared by a `tag` line of a Case of this session.
  - Answer: agreed, (a).
- **What happens to a line with an unlisted tag**
  - Recommended: (a) refuse the line until the tag is fixed: exit 2 with one stderr line, or a finding sent back to `case-guppi`.
  - Answer: agreed, (a).
- **Which lines the check covers**
  - Recommended: (a) lesson lines, `create` lines and a `set` of `tags` in an `update`; the tags of an Insight are left out.
  - Answer: agreed, (a).
- **One promise or two**
  - Recommended: (a) two sub-cases, each with a new Estimate: `estimate-case-check-sends-back-an-unlisted-tag` and `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`.
  - Answer: agreed, (a).
- **Which `tag` lines of this session count as declared**
  - Recommended: (a) a `tag` line in the same Case file, or in a Case of this session that is already approved, a decision line of it standing in the session's ledger.
  - Answer: agreed, (a).
- **What the checks do when `tags.md` is missing**
  - Recommended: (a) no `tags.md`, no tag judged.
  - Answer: agreed, (a).
- **Change**
  - Asked: from `/work` to the end of Retro no Case is ratified, so a lesson there takes a tag of `tags.md`, and the new tag goes as a line of the handoff to a later session; the stderr line says so, and `context` no longer claims without that condition that no refusal loses a line.
  - Taken: the stderr line of Case 703.2 and the new text of `rule-ledger-write` say so, and `context` says that only the new tag waits.

## History

- 2026-10-07 created · raw/2026-10-07/0636/ledger.md#case-703
