---
type: decision
case: "73.8"
status: current
update: [rule-documentation]
origin: raw/2026-09-12/ledger.md#case-73.8
sprint: migration
created: 2026-09-12
tags: [session, workflow, harness, librarian, render]
---

## Context

Sessions I and J both fall on 2026-09-12. `raw/<date>/` keys the Spec, the Frontier and
the handoff by date, so the second session appends its plan under the first session's
approved Spec, its Frontier as a second section of the first session's file, and its
handoff under a `---`. The owner: one session, one Spec.

## Problem

Where the per-session artifacts of a session live when the date already holds a
session's, and how every hook and script finds them.

## Given

`guppi/event.py` `log_path` is `raw/<date>/event_log.md`; `guppi/ledger.py`
`hi_recorded` finds the `hi` line after this session's `session-start` across dates
(case 55.1); the `hi` line carries the time and no session id.
**＋** `guppi spec` writes `raw/<date>/spec.md`, appending under `---` and a stamp
(`rule-spec-capture`); `/hi` writes `raw/<date>/frontier.md` (`rule-skill-hi`);
`pretask --check` reads `raw/<hi date>/frontier.md` (`rule-pretask`); `materialize`
reads `raw/<date>/spec.md` (`rule-materialize`); Retro appends under `## Deferred` of
`raw/<date>/spec.md` (`rule-retro`); `/handoff` writes `raw/<today>/handoff.md`, `---`
before a new document (`rule-handoff`); the librarian's first input is
`raw/<today>/handoff.md` (`rule-documentation`); `rule-case-protocol` and
`rule-claude-md` name `raw/<date>/spec.md` and `frontier.md` in their Renders;
`index.md` §1 lists the six files of `raw/<date>/`; the glossary rows `Spec` and
`Working files` name the date.
**＋** Today: `raw/2026-09-12/spec.md` (session I, approved 10:48:13), `frontier.md`
(F1–F18 of I, F19–F33 of J appended), `handoff.md` (I); session I's `hi` at 04:54:19,
session J's at 11:56:22. This Plan Mode's ExitPlanMode fires the old hook, so J's plan
lands under I's Spec before Work Mode moves it.
**＋** Case 63 (Slice 3c, deferred): the raw lifecycle — archival of an applied date by
run stamp, `decided_by`, the tail `/hi` prints. This Case narrows what 3c archives; it
does not take 63 up.
**＋** The folder name is the `hi` time, `HHMM`, ratified by the owner over a session
letter: mechanical, sortable, found by every hook from the event log.
**－** `ledger.md`, `event_log.md`, `materialize.yaml`, `origin` pointers and lint's
grep targets do not move. `rule-brief` and `rule-index-check` name `handoff.md`
without a path and do not change.

## Criterion

- [[estimate-documentation-completes]] § case 73.8

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-73.8
