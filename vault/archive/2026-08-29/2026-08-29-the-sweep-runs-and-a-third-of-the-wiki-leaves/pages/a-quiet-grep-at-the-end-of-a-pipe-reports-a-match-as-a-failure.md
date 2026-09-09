---
title: "A quiet grep at the end of a pipe under `pipefail` reports a found match as a failure"
type: lesson
status: archived
authority: sigpipe-under-pipefail
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, process]
---

# The mechanism

`grep -q` **exits on its first match** and closes the pipe. The `printf` upstream is still writing,
dies of `SIGPIPE`, and under `set -o pipefail` **the pipeline's status becomes 141** — so a match
that was FOUND reads as a test that FAILED.

**Measured on one output under one `set -uo pipefail`, back to back:**

| form | verdict |
|---|---|
| `printf '%s' "$out" \| grep -q ...` | `FALSE (status 141)` |
| `grep -q ... <<<"$out"` | `TRUE` |

**A herestring is a file descriptor and cannot be broken this way.** That is the fix, and it is the
whole fix: all nine occurrences were rewritten and no piped shape is left —
`grep -c "printf '%s' ..."` returns 0.

# Where it sat, and why it fired now

**In `scripts/vault-check-selftest.sh`, in nine places**, and it was already there at `HEAD` before
the session that found it. **It fired now because the corpus grew by 22 pages at the previous
ingest** and the output outran the pipe buffer.

**So it is timing-dependent — a flake rather than a fixed miss, which is worse**, because a flake
gets re-run and forgiven.

**How it surfaced:** the case *the generator lists a new page* reported MISSED while the output it
had itself captured contained `## concepts (71)` and the row
`| [[a-page-the-generator-must-list]] |`. The generator had listed the page. Re-run by hand in the
real tree: `exit=0, listed=1`, identical with the session's schema changes and with them stashed —
so the case was not reporting on the generator at all
([[a-test-that-fails-for-its-own-reasons-proves-nothing]]).

# One of the nine failed towards green, and that is the dangerous one

`! printf '%s' "$out" | grep -qF "$forbid"` — **a SIGPIPE makes the negation TRUE, so a forbidden
string that IS present reads as absent.** A false CAUGHT, in the direction of passing, on the one
case shape written to prove that something must **not** appear.

**A verdict that cannot fire is worse than no verdict** ([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]),
and this is that failure arriving through the plumbing rather than through the predicate.

# The family it belongs to

**It is the other half of [[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]].** There the
**last** stage's status is taken for the whole; here the **first** stage's death is — which is
exactly what `pipefail` is for, and exactly wrong when the last stage is a quiet grep.

**The shape to look for is a quiet grep at the end of a pipe under `pipefail`.** It is greppable, and
that is the whole of the defence.

# The same class met again through a closed pipe — 2026-08-24

**`bash scripts/vault-check-selftest.sh --list | head -1` prints
`sed: couldn't flush stdout: Permission denied`.** `head` closes the pipe after the first line and
the writer upstream is told so by the platform, in a message that reads like a permissions defect.

**It is not a defect and nothing is wrong with the command.** The family is the same: a normal
outcome at the end of a pipe surfacing as an error because the pipeline reports the last thing that
happened rather than the thing that was asked.

**Recorded so the next reader does not go looking for a file the tool cannot write.**
