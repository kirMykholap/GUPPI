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
