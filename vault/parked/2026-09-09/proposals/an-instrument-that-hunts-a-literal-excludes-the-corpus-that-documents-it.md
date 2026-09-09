---
title: "An instrument that hunts a literal excludes the corpus that documents it"
type: proposal
status: current
authority: literal-hunting-instrument
basis: measurement
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md", "docs/an-instrument-that-hunts-a-literal-excludes-the-corpus-that-documents-it.md", ".claude/hooks/record-the-smoke.ps1"]
tags: [harness, testing, vault]
---

# What it would be

**Every instrument here that decides something by finding a literal string in text is given a way to
tell an occurrence *of* the marker from an occurrence *about* it** — and the expected source of the
second is this repository's own documentation of the marker.

Today each such instrument meets the problem alone, and four of the five recorded instances were found
only after the instrument had been wrong for days.

**This is the compilation of the draft `docs/an-instrument-that-hunts-a-literal-excludes-the-corpus-that-documents-it.md`,
written by [[the-lessons-agent]] on its first run.** It proposes a change to a file that arms an
agent — `.claude/hooks/record-the-smoke.ps1` — and names it plainly rather than describing the effect.

# Why it is raised: the live case is firing now

**`record-the-smoke.ps1:90` runs `[regex]::Matches($response, 'SMOKE-EXIT:\s*(\d+)')` over a command's
output, last match wins.** It cannot tell a `make smoke` run from a shell command that merely
*printed* the marker. `cat` of a page that documents the marker writes a green smoke row for a run
that never happened, and the gate on `/handoff` reads that row
([[the-smoke-gate-hooks]], [[the-gate-on-handoff-refuses-and-is-argued-against-the-refusal-test]]).

**Three live pages carry the matching form once each** — a digit after the colon:
`wiki/entities/the-makefile.md:83`,
`wiki/proposals/make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation.md:317`,
and `wiki/decisions/the-smoke-runner-is-built-first-thing-next-session.md:119`.

**The journal's own count of this is wrong in both halves**, and the correction is the point: it
records *two pages, two occurrences each*. Two-per-page is true of the bare string; the **matching**
form occurs once each, on **three** pages, one of which the journal does not name.

**Four more live occurrences are one edit from matching** — `SMOKE-EXIT: <n>` twice, a bare
`SMOKE-EXIT:`, and `SMOKE-EXIT 0` with no colon. **What keeps those harmless is an accident of
spelling**, which this store has already written down as a thing not to rely on.

## The agent measuring it wrote two false green rows while measuring it

**`.superpowers/sdd/pre-task-ledger.tsv` carries rows at `2026-08-29T22:09:43` and
`2026-08-29T22:09:58`, both `smoke:0`, both written by a read-only `grep`** run to count the
occurrences above. No check ran. **The defect fires on the investigation of the defect, from inside a
subagent that holds no write tool at all** — which is stronger evidence than the journal's own
instance, and it means **three false green rows stand today**, not one.

# The family, and it is this store's most-repeated shape

Five instances in seventeen days. One is live in `wiki/lessons/`; the rest are in
`archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/pages/`.

| date | page | what matched what |
|---|---|---|
| 2026-08-13 | `an-example-inside-a-code-block-satisfies-a-search` (archived) | a scan for a literal satisfied by prose in a comment |
| 2026-08-24 | `a-whole-file-grep-for-a-field-name-is-satisfied-by-that-name-in-prose` (archived) | a field-presence grep satisfied by the field's name in a sentence |
| 2026-08-26 | `a-guard-that-matches-a-phrase-anywhere-flags-the-record-that-discusses-it` (archived) | a guard flagging the record that discusses the phrase |
| 2026-08-29 | [[a-comment-quoting-the-literal-a-sweep-looks-for-is-counted-by-that-sweep]] (**live**) | `--list` counting the comment that quotes its own literal |
| 2026-08-29 | this journal | the smoke recorder counting the pages that document `SMOKE-EXIT:` |

**The repository has already solved it once, by hand, in one place.** `CLAUDE.md` carves out a
`VAULT-FEEDBACK` fence nested inside another fence, so the block documenting the channel files
nothing. Nothing generalises that carve-out, so the next instrument met the problem again.

# What it would take: three routes, none chosen

1. **Make the writer print something a document cannot contain** — a run nonce, a process id — and
   require it. **Cost: it breaks the property the marker exists for**, that a human can read the line
   ([[a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code]]).
2. **Narrow the reader to the command it was launched for.** The payload carries the command string; a
   recorder that refuses a marker out of a command that never invoked the runner is a condition on
   data the hook already has. **The cheapest, and the one this draft would build**, with route 1 as
   the fallback.
3. **Forbid the corpus from spelling the literal.** *Rejected in the drafting* — it charges the price
   back to correct prose, the argument already accepted against a page declaring itself exempt
   ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).

**The general half is a page rather than a mechanism.** No script can find the next instrument of this
class; what can be written down is the question to ask of one — *name a document in this repository
that would make this fire* — which is the same shape as the question already asked of a new verdict
([[the-unreachable-verdict-is-dropped-and-replaced]]).

# What is open

- **Whether the `PostToolUse` payload's command string is dependable enough to condition on.** The one
  page describing that payload says the timing of a second fire is not established, and nobody has
  checked what the field holds for `make` reached through a wrapper.
- **What is done with the three false rows already standing.** The ledger is append-only by design, so
  striking them is a decision about the ledger and not a repair ([[the-pre-task-ledger]]).
- **Whether `SUITE-EXIT:` owes the same condition.** Identical shape, not measured.
- **Whether a rule page is owed**, and for what destination. Destinations are the owner's to choose.

# What it would oblige

- **The recorder's selftest gains a case planting the marker in a command that ran no check**, and
  asserting no row is written — otherwise this is a rule a fixture can violate for a week
  ([[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]]).
- **The case is proved by reading the ledger back**, not by the check returning green
  ([[a-planted-offender-is-proved-by-reading-it-back]]).
- **[[a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code]] gains the
  limit it does not state**: the arrangement is sound about *trusting* the marker and silent about
  *who printed it*, and that silence is the whole defect.

# What it would retire

**[[a-comment-quoting-the-literal-a-sweep-looks-for-is-counted-by-that-sweep]], and nothing else** —
its content is carried forward whole as the fourth row above. **It is not retired by this ingest**:
the drain of `lessons/` into `proposals/` is itself an unbuilt design, and retiring a lesson on the
strength of a proposal nobody has accepted would execute it
([[lessons-become-a-queue-drained-into-proposals]]).

**The three archived siblings are not resurrected.** They are named as provenance, which is what
`archive/` is for.

*(Compiled from the lessons agent's draft, itself prepared from
`raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
