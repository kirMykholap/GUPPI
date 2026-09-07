---
title: "docs/HANDOFF.md is not retired until every unit vault-units.sh counts carries a verdict"
type: decision
status: current
authority: handoff-retirement-gate
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-13
created: 2026-08-13
sources: ["archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", "docs/superpowers/plans/2026-08-13-second-brain.md"]
tags: [vault, testing]
---

# The old handoff is retired only when its coverage sidecar is complete

**Decided on 2026-08-13.** `docs/HANDOFF.md` — 129 KB, the file every session used to read first —
was copied verbatim into `raw/handoffs/` before any compiling, so that the migration has a floor:
**nothing can be lost, only left uncompiled.**

Every unit of it needs a verdict in the sidecar
`raw/handoffs/2026-08-12-handoff-before-the-vault.coverage.tsv`, in the sense of
[[ingest-is-units-and-verdicts]]. Writing them is deferred; **the deferral is bounded by a gate**:

> **Do not retire `docs/HANDOFF.md` while `bash scripts/vault-coverage.sh` over it reports a unit
> without a verdict.**

**The gate is the script's output, not a number.** The number is whatever
`scripts/vault-units.sh` says today, and it is deliberately not written into this title.

## The gate was met, and the file was retired

On 2026-08-13 `vault-coverage.sh` over the copy in `raw/` printed **332 of 332 units carry a
verdict / INGEST COMPLETE**, and `docs/HANDOFF.md` went from 1307 lines to a 27-line pointer in
`d30b317`. The pointer names the verbatim copy in `raw/`, the sidecar beside it, and the commit
`e872992` where the pre-migration text sits in git.

The repository's `CLAUDE.md` was cut in the same commit, **231 lines to 190** — and stands at
**210** today, because the whole-branch review put back what the cut had dropped, chiefly the only
statement of where our own JavaScript lives ([[javascript-policy]]). A shrinking that removes the
thing a future test would have been written from is not a shrinking.

**This page is therefore a record, not an outstanding obligation** — but the gate itself still
stands for the next source: `raw/notes/` holds two of the owner's working notes with no sidecar at
all, and they are unfinished ingests by this rule. **Still true on 2026-08-14**, three ingests
later: they are the only two sources in the vault without a sidecar.

Rejected: retiring it once the migration "felt complete". That feeling was already wrong once — §1
of the same file was lost entirely on the first pass while the ingest log recorded it as read.

## The count, as dated measurements

| Date | Units | Under which rule |
|---|---|---|
| before 2026-08-13 | **274** | the narrow rule: headings, table rows, and paragraphs or bullets opening in **bold** |
| from 2026-08-13 | **362** | the widened rule: every heading, table row, bullet, numbered item and paragraph opening |

**362 and 332 are the same accounting.** `vault-units.sh` emits 362 lines; `vault-coverage.sh`
excludes the 30 headings from the denominator and so reports "332 of 332". Headings carry verdicts
too — they are simply not counted. Neither number includes anything inside a code fence, which the
unit reader skips entirely ([[vault-scripts]]).

**The count moves whenever the unit rule moves, and that is expected rather than a defect.**
Widening the rule found 88 claims the old one had hidden; a gate pinned to the old number would
have opened while those 88 were unaccounted for. A gate defined by the tool gets *harder* exactly
when the tool gets better, which is the direction a gate should move.

## The journal said 245, and the journal was wrong

§6 of `raw/handoffs/2026-08-13-second-brain-phase-1.md` states 245 units, and **this page's title
and body repeated 245 until 2026-08-13.** It was never the script's output under any rule: the
narrow rule gave 274 on the same file.

`raw/` is immutable, so the correction lives here rather than in the source — what the session
believed at the time is data. **This is the first instance in this vault of a source being *wrong*
rather than merely superseded**, which is a different failure from
[[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]]: there the source was true
once, here it never was. Neither is catchable by coverage; both are caught by reading a unit beside
the page compiled from it.

## Why the gate is a trigger and not a reminder

A deferred item is a debt with no due date unless its condition is written next to the thing that
will meet it; see [[a-deferred-check-must-be-run-when-its-condition-arrives]], which is this
project's most expensive instance of the same shape. Here the condition is a command anyone can
run: `bash scripts/vault-coverage.sh` over the file ([[vault-scripts]]).

# A verdict is counted, and it is never resolved — 2026-08-26

**The rule this page settles is about the presence of a verdict, and the script enforces exactly
that.** It does not ask whether a `page:` verdict names a file that exists, and 802 of the 2149
`page:` verdicts in this vault carry prose after the slug, so they resolve against nothing
([[a-coverage-verdict-is-checked-for-presence-and-never-for-resolvability]]).

**That is a gap in the instrument and not in this decision.** *Every unit accounted for* was met on
every one of those sidecars; what was not asked is a different question, and asking it is a change to
`scripts/vault-coverage.sh` that would start as an advisory.
