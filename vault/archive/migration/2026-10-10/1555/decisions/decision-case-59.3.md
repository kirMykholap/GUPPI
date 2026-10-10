---
type: decision
case: "59.3"
status: archived
update: ["[[rule-case-protocol]]", case-schema, index, "[[rule-retro]]", "[[rule-spec-capture]]", "[[rule-prespec]]", "[[estimate-prespec-reconciles]]"]
origin: raw/2026-09-12/ledger.md#case-59.3
sprint: migration
created: 2026-09-12
tags: [session, workflow, ledger, harness, render, hooks]
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

`rule-case-protocol` (Render in `CLAUDE.md`) says the page content is the `then` block
under the Case in the Spec and names no `tasks`; `case-schema.md` says the same under "The
`then` block lives in the Spec".
**＋** `index.md` §1 lists `plan.md — executable plan` under `raw/<date>/` and §9 draws
the chain "→ executable plan → branch + baseline commit → subagents → harness tests";
`rule-work-mode` is a `draft` placeholder (Slice 3b), its draft in `docs/migration/`
derives `plan.md` from the Spec by the skill `to-executable-plan`.
**＋** `rule-retro` Render says "what got done and what did not, against the Spec" with
nothing to count; `estimate-retro-loads` (`pending`) reads "done against the Spec" and
still holds.
**＋** `rule-spec-capture` names two writers of `spec.md`: the hook at approval and the
agent at Retro under `## Retro`.
**＋** `guppi materialize` reads the quoted sections and the `then` blocks by heading; a
`tasks` block is a fenced block with another tag, which it ignores today.
**＋** `guppi pretask --check` (59.1, 59.2) parses the plan by the same headings.
**－** The Spec of this session is written this way from Case 58 on; the Specs of earlier
dates are not rewritten.
**－** The Work Mode draft (`docs/migration/rule-work-mode.md`) is a draft, not a page; it
is reconciled when Slice 3b forms its Cases.

## When

A Case is ratified in Plan Mode; later the plan is approved, worked and reviewed at Retro.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-59.3
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
