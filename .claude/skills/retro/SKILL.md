---
name: retro
description: Review this session's work — tests, style, the ledger — before the commit and the handoff.
---


Tests: !`make test`

Style: !`make style`

Ledger: !`uv run guppi tail`

Retro is an analysis of this session, not planning. Open with the frontier, in one
message and with no read call: the list of what is not done, numbered: the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), per Case — a `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the Tail above listed as waiting for the librarian, whose scripts tick them (cases 226, 250, 270), not as debt — a `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, listed as waiting for a later session, neither debt nor the librarian's (case 428.4) — another `read` line without its line in the Tail is debt, and the lines of a Case a `{supersedes:case N}` line of the Tail names are not counted at all, its work stands under the superseding Case (case 282); what
you noticed during Work Mode, in the same list — bugs, forks, a contract that
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

Take the readings of the Estimates whose work is finished and that this session neither creates nor updates — by a decision line of its slug, or by an `update` that renames a page to it — and write their lines; name in the handoff any Estimate whose reading cannot be taken yet, and every Estimate this session creates or updates. A reading measures the Criterion the page carries at the moment of the reading, the one ratified last, and its line is written only when the work that Criterion names is built. What a session changes, it does not measure: an Estimate this session creates or updates has no reading in this session, built or not, and the ledger hook refuses one (case 428.1); the `read` line of its old Criterion in an earlier Spec is not debt and is not read, and the reading of the new Criterion closes it in a later session, at the moment its `method` names (cases 283, 428.3).

Close with three lists: every ratification of this session, one line per Case, by the Tail above grouped by Case, this session's folder first, a Case a `{supersedes:case N}` line names not counted; what
got done; what is not done — the opening list by its numbers, each item with the end it took. When the person approves, commit (`make style` clean,
`make test` green), then call `/handoff`.
