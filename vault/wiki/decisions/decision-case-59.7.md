---
type: decision
case: "59.7"
status: current
create: [estimate-render-sync-reports]
update: [rule-render-harness, rule-hook-registry, rule-skill-hi]
origin: raw/2026-09-12/ledger.md#case-59.7
sprint: migration
created: 2026-09-12
tags: [harness, render, hooks, session]
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

`rule-render-harness` (Leaf, `built`, enforcement `check`, `guppi/render.py`,
`tests/test_render.py`, parent `rule-harness`) has `--check` and the plain write; its
Estimate `estimate-render-harness-reproduces` (`passed`) reads the unit cases and one live
reading of 2026-09-09.
**＋** `guppi/render.py` has `plan`, `differing` and `write_all`; a diff is `difflib` of the
standard library, no dependency.
**＋** `rule-hook-registry` Render lists one `SessionStart` hook, `uv run guppi event
session-start`.
**＋** `lesson-hooks-sessionstart-cannot-block`: exit 2 is a no-op there. The stdout of a
`SessionStart` hook is added to the context, by Claude Code's hook contract; not yet
measured here.
**＋** The brief of every session since Slice 2 opened with "run `guppi render` for the
pages the librarian changed, then commit"; the files lag the pages for a whole session.
**＋** `guppi gate` refuses `/handoff` on a dirty tree; the rendered files are committed at
Retro with the session's work.
**－** The librarian's run changes pages after the hook ran; the files lag until the next
`SessionStart`, and `make lint` at the brief still reports them. Not changed here.
**－** `--check` stays as it is for `make lint`.

## When

A session starts; later the agent reads its first turn.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-59.7
