---
type: rule
kind: Leaf
purpose: Prevents a session from closing on work nobody reviewed, or on a change that traces to no decision
status: draft
enforcement: render
governs: .claude/skills/retro/SKILL.md
render_mode: full
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-retro-loads]]"]
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Purpose

Prevents a session from closing on work nobody reviewed, or on a change that traces
to no decision. Retro is a conversation over this session only. The tests and the
style check load before the first turn, so the person reads the result instead of
waiting for it. The scope rule is mechanical: an edit is allowed when it finishes work a line of this session's ledger ratified, and is new scope otherwise. Retro opens by two paths, both behind `guppi gate`: the person's typed `/retro` on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`; each checks the Spec against the ledger and leaves the mark `retro`, and a refused typed prompt is not expanded (case 169.3, supersedes 150).

## Render

<!-- rule-retro -->
---
name: retro
description: Review this session's work — tests, style, the ledger — before the commit and the handoff.
---


Tests: !`make test`

Style: !`make style`

Ledger: !`uv run guppi tail`

Retro is an analysis of this session, not planning. Open with the frontier, in one
message and with no read call: what was ratified (the lines of the Tail above grouped by Case, this session's folder first, one line per Case); the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), the unticked boxes
per Case; what
you noticed during Work Mode, as a numbered list — bugs, forks, a contract that
turned out imprecise. The person adds their own observations. Every item, theirs or
yours, ends in one of four ways: a `- lesson[...]` line; a `- estimate[...]` line, a
reading of an Estimate whose work is finished; a short defer; or a note for the
handoff. Retro ratifies no other decision: a `create`, `update` or `delete` waits for
the next Plan Mode.

A short defer is a Case in the short form, appended to `vault/raw/<date>/<hi HHMM>/spec.md` under the `## Deferred` heading before its ledger line: `## Case N`, `context`, `problem`,
and a `defer` block with `purpose`; no `recommend`, `given`, `when` or `then`. A defer
line without its Case is marked incomplete by materialize.

Edit code only when the edit finishes work that traces to a line of this session's ledger.
Red tests: fix now when the fix finishes ratified work; otherwise save the change
with `git diff` into `raw/<hi date>/<hi HHMM>/patch-<slug>.diff`, the session's folder, revert it, and write a short
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
- 2026-09-12 updated: Retro reads and appends the session's Spec (case 73.6) · [[decision-case-73.6]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-13 updated: Retro reads the session ledgers of the day (and the date-level one while it exists); the revert patch goes to the session folder (case 109.1) · [[decision-case-109.1]]
- 2026-09-14 deferred · [[decision-case-118]]
- 2026-09-14 defer by decision-case-118 superseded · [[decision-case-126]]
- 2026-09-14 updated: the Retro ledger is the unmaterialized tail printed by guppi tail, not a cat over a date-level file the model of case 103 no longer has (case 126) · [[decision-case-126]]
- 2026-09-14 updated: the scope rule names this session's ledger, as 109.1 promised (case 132) · [[decision-case-132]]
- 2026-09-14 updated: the Recorded line dropped; guppi gate writes the stamped retro mark (case 136.1) · [[decision-case-136.1]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: disable-model-invocation dropped: a typed or agent-called /retro passes the Skill tool, so guppi gate sees it and writes the retro mark (case 150) · [[decision-case-150]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-15 updated: the two paths of Retro, typed and called, both behind the gate; supersedes 150 (case 169.3) · [[decision-case-169.3]]
