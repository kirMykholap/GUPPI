---
type: decision
case: "373"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-case-form]]", "[[insight-workflow-ratified-content-changed-on-the-agents-own-finding]]", "[[estimate-case-protocol-loaded]]"]
origin: raw/2026-09-23/1126/ledger.md#case-373
sprint: migration
created: 2026-09-23
tags: [session, workflow, ledger, harness]
---

## Context

The Case schema asks that a Case the person changed be shown again — `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`. It says nothing of the case where the agent itself, after ratification, finds a gap, an error or a wider scope in the signed text; the agent reads the rule as one on the person's changes alone, repairs the text itself — in the Spec or in the files — and names the repair after the fact. It happened twice: in session 1308 the grep of tasks 277.3 found a sixth file, the agent edited it and backfilled the ledger (`lesson-work-mode-check-widened-the-list-and-the-agent-acted`); in session 0034 the agent added a `problem` to Case 359 and removed a sentence from the `context` of Case 361 in the Spec without a showing (`lesson-spec-text-repaired-after-ratification-without-a-showing`). The librarian clustered both into `insight-workflow-ratified-content-changed-on-the-agents-own-finding` (`open`, severity 2), whose proposal is an update of `rule-case-protocol`.
`rule-case-protocol` stands `draft`, changed in this session by Cases 368 and 370 already; the Case touches `estimate-case-protocol-case-form` (`pending`), whose When speaks of a showing again, and `estimate-case-protocol-loaded`, the live reading of the Render (case 187); the other two Estimates of the rule are not touched; the Insight goes `actioned`; both lessons are of other sessions, so no `{addresses:…}` mark (case 284.2); no `create`.

## Problem

The rule of the showing again does not name a change the agent found itself, and signed text changes without a signature.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-373
