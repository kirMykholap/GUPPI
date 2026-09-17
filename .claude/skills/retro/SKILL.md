---
name: retro
description: Review this session's work — tests, style, the ledger — before the commit and the handoff.
---


Tests: !`make test`

Style: !`make style`

Ledger: !`uv run guppi tail`

Retro is an analysis of this session, not planning. Open with the frontier, in one
message and with no read call: what was ratified (the lines of the Tail above grouped by Case, this session's folder first, one line per Case); the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), the unticked boxes per Case — a `create`, `update` or `defer` line of a page and a `guppi render` line listed as waiting for the librarian, who ticks them (case 226), not as debt; what
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
