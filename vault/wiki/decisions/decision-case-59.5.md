---
type: decision
case: "59.5"
status: current
update: [case-schema, rule-case-protocol, rule-brief, rule-retro, rule-spec-capture]
origin: raw/2026-09-12/ledger.md#case-59.5
sprint: migration
created: 2026-09-12
tags: [session, workflow, ledger, harness, librarian, render, hooks]
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

`case-schema.md` ("The short form of Retro") and `rule-case-protocol` allow the short
form at Retro only; `rule-retro` appends such a Case under `## Retro`.
**＋** `index.md` §5: a `defer` with an existing target appends `deferred_by`; without one
the librarian creates a placeholder born with `deferred_by`; `guppi generate` does both
(case 52.3). Not changed.
**＋** `guppi materialize` marks a Case `incomplete` for a missing `given` or `when` only
when a kind other than `defer` is among its lines (case 56). Not changed.
**＋** `rule-brief` Render: "Deferred: at most seven items. Rank by the `severity` of a
related Insight, then by the number of times the item was postponed. Take that number from
the previous brief and add one." The source of the items is not named; the librarian
takes them from the handoff today.
**＋** The brief of 2026-09-11 carries seven deferred items; four of them are no page: item
2 (`/grill-me` without a page), 3 (`git pull` without upstream, owner's decision 11.1),
4 (`gh` not logged in, 11.2), 5 (the fate of `vault/parked/`, `vault/archive/`,
`docs/superpowers/`, `docs/HANDOFF.md`, `docs/migration/rule-*.md`, the 2026-08 docs).
All four are "Slice 5" by the brief or the owner.
**＋** `sprint.md` is not a page and has no schema; the librarian changes it only when the
handoff says; nothing forbids Work Mode under a ratified Case.
**＋** The frontier grammar of 59.2 closes a deferred item as `[-] … · defer case N`, each
with the number of its own Case.
**＋** `rule-retro` and `rule-spec-capture` name the `## Retro` heading for the short-form
Cases of Retro; `materialize` reads Cases by their `## Case N` headings wherever they sit.
**＋** Two pages deferred by one decision under one context stay one Case (case 29:
`rule-work-mode` and `rule-subagent-guppi`).
**－** The items this session defers are chosen at its close, not here.

## When

The owner closes the discussion of Plan Mode with items left open, or Retro ends an item
in a defer; later a deferred decision is taken up; later still the librarian writes the
brief.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-59.5
