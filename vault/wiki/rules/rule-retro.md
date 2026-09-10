---
type: rule
kind: Leaf
purpose: Prevents a session from closing on work nobody reviewed, or on a change that traces to no decision
status: draft
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

Retro looks at this session only. Discuss what happened with the person in the Case
form. Edit code only when the edit finishes work that traces to a line of today's
ledger. Any other change is new scope: write a `- decision[case N][defer][slug]`
line instead and, when it is a bug, a `- lesson[error][...]` line too. `gh` is not
available: name a deferred bug in the handoff, so the brief carries it. Red tests
are a `lesson[error]` whose root cause says why Retro was reached with a
regression; the handoff still needs green. Do not run `make lint` here: the vault
is written after handoff, by the librarian.

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
