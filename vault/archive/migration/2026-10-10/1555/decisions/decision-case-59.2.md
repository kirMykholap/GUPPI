---
type: decision
case: "59.2"
status: archived
create: ["[[estimate-hi-writes-frontier]]"]
update: ["[[rule-skill-hi]]", "[[rule-prespec]]", "[[estimate-prespec-reconciles]]", "[[rule-case-protocol]]", index]
origin: raw/2026-09-12/ledger.md#case-59.2
sprint: migration
created: 2026-09-12
tags: [session, harness, workflow, ledger]
---

## Context

Plan Mode leaves four things behind: the Frontier it opened with, the ledger lines the
Stop hook wrote at each ratification, the Spec the human approved, and the Decision pages
the librarian generates from both. In sessions G and H the four drifted: three decision
lines had no item under their Case in the Spec (`lesson-spec-then-items-unchecked-against-
ledger-lines`); the Frontier lived in the agent's memory and a plan was closed on one item
of it (`lesson-plan-mode-exited-per-frontier-item`); a Decision page shows its targets as
two lists aligned by position, unreadable; the items left over at the end of a session are
carried by the brief's counter, not by a decision.

## Problem

Each drift has a mechanical check or a form that removes it, and none is written. The
sub-cases below fix one each; they share this context and are ratified apart. In Work
Mode a fork is not a return to Plan Mode: the subagent stops, the fork is written as a
Case in the short form, shown at Retro, appended to the Spec with a `defer`, and the plan
stays unfinished until the next session (the owner, 2026-09-12; a clause of
`rule-work-mode`, Slice 3b).

## Given

`rule-skill-hi` (MOC, `built`, `render`, governs `.claude/skills/hi/SKILL.md`) says
"Assemble the Frontier from the above and present it as a list … Wait for the human to
pick the order or defer items"; its Estimate `estimate-hi-no-read-calls` (`passed`) checks
the loading and the `hi` line, not what the agent writes.
**＋** `rule-case-protocol` (Render in `CLAUDE.md`) says "Plan Mode does not end while a
Frontier item is neither ratified nor deferred" and names no file.
**＋** `rule-prespec` gains `guppi pretask --check <plan>` by case 59.1; `guppi/pretask.py`
already reads the session's window from the event log.
**＋** `index.md` §1 lists the files of `raw/<date>/`: `ledger.md`, `event_log.md`,
`spec.md`, `plan.md`, `handoff.md`, `materialize.yaml`; no `frontier.md`.
**＋** The date of the file is the date of the session's `hi`, as for the ledger across
midnight (case 55.1).
**－** A Work Mode fork does not reopen Plan Mode (case 59, the owner): the file is written
once per session and only closed afterwards; no second-entry clause.
**－** The librarian does not read `frontier.md`; it is not one of its four inputs.

## When

The person invokes `/hi`, and later the agent or the person invokes `/pre-task`.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-59.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
