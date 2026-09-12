---
type: rule
kind: Leaf
purpose: Prevents a session from closing on work nobody reviewed, or on a change that traces to no decision
status: built
enforcement: render
governs: .claude/skills/retro/SKILL.md
render_mode: full
parent: rule-end-of-work
estimates: [estimate-retro-loads]
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Purpose

Prevents a session from closing on work nobody reviewed, or on a change that traces
to no decision. Retro is a conversation over this session only. The tests and the
style check load before the first turn, so the person reads the result instead of
waiting for it. The scope rule is mechanical: an edit is allowed when it finishes
work a line of today's ledger ratified, and is new scope otherwise.

## Render

<!-- rule-retro -->
---
name: retro
description: Review this session's work — tests, style, the ledger — before the commit and the handoff.
disable-model-invocation: true
---
Recorded: !`uv run guppi event retro --session "${CLAUDE_SESSION_ID:-}"`

Tests: !`make test`

Style: !`make style`

Ledger of today: !`cat "vault/raw/$(date +%F)/ledger.md"`

Retro is an analysis of this session, not planning. Open with the frontier, in one
message and with no read call: what was ratified (the ledger lines of today grouped
by Case, one line per Case); the `tasks` of `raw/<date>/spec.md`, the unticked boxes
per Case; what
you noticed during Work Mode, as a numbered list — bugs, forks, a contract that
turned out imprecise. The person adds their own observations. Every item, theirs or
yours, ends in one of four ways: a `- lesson[...]` line; a `- estimate[...]` line, a
reading of an Estimate whose work is finished; a short defer; or a note for the
handoff. Retro ratifies no other decision: a `create`, `update` or `delete` waits for
the next Plan Mode.

A short defer is a Case in the short form, appended to `vault/raw/<date>/spec.md`
under the `## Deferred` heading before its ledger line: `## Case N`, `context`, `problem`,
and a `defer` block with `purpose`; no `recommend`, `given`, `when` or `then`. A defer
line without its Case is marked incomplete by materialize.

Edit code only when the edit finishes work that traces to a line of today's ledger.
Red tests: fix now when the fix finishes ratified work; otherwise save the change
with `git diff` into `raw/<date>/patch-<slug>.diff`, revert it, and write a short
defer naming the patch. Either way write a `- lesson[error][...]` line whose root
cause says why Retro was reached with a regression; the handoff still needs green.
`gh` is not available: name a deferred bug in the handoff, so the brief carries it.
Do not run `make lint` here: the vault is written after handoff, by the librarian.

Take the readings of this session's Estimates whose work is finished and write their
lines; name in the handoff any Estimate whose reading cannot be taken yet.

Close with three lists: every ratification of this session, one line each; what
got done; what did not. When the person approves, commit (`make style` clean,
`make test` green), then call `/handoff`.
<!-- /rule-retro -->

## Estimates

- [[estimate-retro-loads]]

## Parent

- [[rule-end-of-work]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 estimate estimate-retro-loads added · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 updated: Retro ends with the commit, then /handoff (the Render of case 38.1 already carries it) · raw/2026-09-10/ledger.md#case-40
- 2026-09-10 deferred · raw/2026-09-10/ledger.md#case-50
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 deferred_by decision-case-50 set · [[decision-case-52.3]]
- 2026-09-11 updated: a Retro Case is appended to spec.md under ## Retro before its ledger line; a bare defer is forbidden · [[decision-case-52.2]]
- 2026-09-11 defer by decision-case-50 superseded · [[decision-case-56]]
- 2026-09-11 updated: Retro opens with the frontier; every item ends as a lesson, a reading, a short defer or a handoff note; red tests are fixed or reverted into a patch; readings are a step · [[decision-case-56]]
- 2026-09-11 status: built → draft · cascade
- 2026-09-12 updated: Retro counts the unticked tasks of spec.md instead of judging done against the Spec (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: the short-form Cases of Retro go under · [[decision-case-59.5]]
- 2026-09-12 status: draft → built · cascade
