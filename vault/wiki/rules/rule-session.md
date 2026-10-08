---
type: rule
kind: MOC
purpose: Prevents a phase of the session from running out of its turn, or a session from ending with a phase that left no mark
status: built
children: ["[[rule-session-start]]", "[[rule-plan-mode]]", "[[rule-work-mode]]", "[[rule-end-of-work]]", "[[rule-documentation]]", "[[rule-skill-sprint-open]]", "[[rule-skill-sprint-close]]"]
estimates: ["[[estimate-session-phases-in-order]]"]
origin: raw/2026-09-22/1121/ledger.md#case-316
sprint: migration
created: 2026-09-22
tags: [session, workflow]
---

## Purpose

Prevents a phase of the session from running out of its turn. A session is five phases in one order: Session Start, Plan Mode, Work Mode, End of Work, Documentation. Each child holds its own mechanism and its own Estimate; this MOC holds what none of them owns — that the chain ran whole, in order. The guards of the order live in the children: the ledger hook refuses a line in a session no `/hi` opened; the pre-spec hook refuses `ExitPlanMode` before `/pre-spec` ran; `guppi gate` refuses `/handoff` on a dirty tree; `rule-close` keeps the librarian's commit out of the session's. The marks each phase leaves stand in the session folder and in `git log`, and they ascend in time. A session conserved by `/carry` stops after Plan Mode and leaves `carry.md`: the last three phases have no mark, and that is the second lawful ending, not a break in the order (case 190.3).

## History

- 2026-09-22 created · [[decision-case-316]]
- 2026-10-01 status: draft → built · cascade
- 2026-10-09 child rule-skill-sprint-open added · [[decision-case-743.6]]
- 2026-10-09 child rule-skill-sprint-close added · [[decision-case-743.8]]
