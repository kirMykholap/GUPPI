---
type: decision
case: "358"
status: archived
update: ["[[decision-case-347]]", "[[rule-decisions-schema]]", "[[estimate-decisions-schema-checked]]"]
origin: raw/2026-09-23/0034/ledger.md#case-358
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness, render, schema]
---

## Context

Case 347 was built on the person's remark that `/carry` does not name the brief's path and the agent greps for it. At 21:49:49 a lesson in the ledger recorded that the agent took the remark as a finding and did not check it against the event log. At 21:55:09 Case 347 was ratified. Then the agent rewrote its `context` in the Spec to cite the event log instead of the remark: at 20:43:03 a grep over `.claude/agents/librarian-guppi.md`, at 20:43:05 `sed -n '77,92p'` of the same file. The librarian wrote `decision-case-347` from the edited Spec. The earlier text stands in no file: the Spec of 2046 was first committed in `8e618d1`, after the edit, so only the chat of that session held it. The edited text is checked: lines 945–946 of `vault/raw/2026-09-22/event_log.md` match in time and command; the `rule-brief` markers stand on lines 77 and 93 in commit `c1e6c36`; step 1 of `.claude/skills/carry/SKILL.md` names `vault/wiki/brief.md` in full, and step 3 commits it by name. The edit touched neither `given`, `when`, `then` nor the `then` block.
`decision-case-347` stands `current`; `rule-carry-over` and `estimate-carry-over-writes` are not touched.

## Problem

A text stands on a Decision page that nobody signed.

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#case-358
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
