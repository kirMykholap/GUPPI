# An instrument that hunts a literal excludes the corpus that documents it

**Draft proposal, prepared by the lessons agent on 2026-08-29 from
`raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.
Not written into the vault. The librarian decides whether it becomes a `wiki/proposals/` page and
what its `authority:` is.**

This proposes a change to a file that instructs or arms an agent — `.claude/hooks/record-the-smoke.ps1`
— and it names that plainly rather than describing the effect and leaving the file unsaid.

## What it would be

**Every instrument in this repository that decides something by finding a literal string in text is
given a way to tell an occurrence *of* the marker from an occurrence *about* it** — and the
expected source of the second is this repository's own documentation of the marker.

Today each such instrument meets the problem alone, and four of the five recorded instances were
found only after the instrument had already been wrong for days.

## Why it is raised: the live case is firing right now

**`.claude/hooks/record-the-smoke.ps1` flattens a `PostToolUse` payload's `tool_response` to JSON
and runs `[regex]::Matches($response, 'SMOKE-EXIT:\s*(\d+)')`, last match wins.** It cannot tell a
`make smoke` run from a shell command that merely *printed* the marker.

**Three live pages carry an occurrence that matches that pattern**, one each:

| page | line | text |
|---|---|---|
| `wiki/entities/the-makefile.md` | 83 | `SMOKE-EXIT: 0` |
| `wiki/proposals/make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation.md` | 317 | `SMOKE-EXIT: 0` |
| `wiki/decisions/the-smoke-runner-is-built-first-thing-next-session.md` | 119 | `SMOKE-EXIT: 0` |

So `cat` of any one of the three writes a green smoke row for a run that never happened, and the
gate on `/handoff` reads that row.

**The journal's own count of this is wrong in both halves and the correction matters.** It records
*two pages, two occurrences each*. The occurrence count is two per page only for the bare string;
the **matching** form — a digit after the colon — occurs once each, and it occurs on a third page
the journal does not name.

**Four more live occurrences are one edit away from matching**: `SMOKE-EXIT: <n>` at
`wiki/entities/the-makefile.md:51` and at
`wiki/concepts/a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code.md:20`,
a bare `SMOKE-EXIT:` at the proposal's line 237, and `SMOKE-EXIT 0` with no colon at
`wiki/decisions/the-checks-get-a-single-entry-point-and-make-is-the-revived-candidate.md:58`.
**What keeps those four harmless is an accident of spelling**, which this store has already written
down as a thing not to rely on
([[a-generated-files-marker-escaped-a-red-verdict-by-an-accident-of-spelling]], 2026-08-20, in
`archive/`).

### The agent preparing this draft wrote two false green rows while measuring it

**Two rows stand in `.superpowers/sdd/pre-task-ledger.tsv` at `2026-08-29T22:09:43` and
`2026-08-29T22:09:58`, both `smoke:0`, both written by a read-only `grep` run by this dispatch to
count the occurrences above.** Neither ran a check. The command column on both rows is the grep
itself, which is what makes them recognisable by hand and invisible to the gate.

That is stronger evidence than the journal's instance: **the defect fires on the investigation of
the defect**, and it fires from inside a subagent that holds no write tool at all.

## The family, and it is the store's most-repeated shape

Five recorded instances over seventeen days, of which **one is live in `wiki/lessons/`** and the
rest are in `archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/pages/`:

| date | page | what matched what |
|---|---|---|
| 2026-08-13 | `an-example-inside-a-code-block-satisfies-a-search` (archived) | a scan for a literal satisfied by prose in a comment |
| 2026-08-24 | `a-whole-file-grep-for-a-field-name-is-satisfied-by-that-name-in-prose` (archived) | a field-presence grep satisfied by the field's name in a sentence |
| 2026-08-26 | `a-guard-that-matches-a-phrase-anywhere-flags-the-record-that-discusses-it` (archived) | a guard flagging the record that discusses the phrase |
| 2026-08-29 | `a-comment-quoting-the-literal-a-sweep-looks-for-is-counted-by-that-sweep` (**live**) | `--list` counting the comment that quotes its own literal |
| 2026-08-29 | *this journal* | the smoke recorder counting the pages that document `SMOKE-EXIT:` |

**And the repository has already solved it once, by hand, in one place.** `CLAUDE.md` carves out a
`VAULT-FEEDBACK` fence nested inside another fence, so the block that documents the channel files
nothing. That carve-out is a per-instrument fix written by somebody who had met the problem; nothing
generalises it, so the next instrument met it again.

## What it would take

**Three routes, and they are not equivalent in cost.** None is chosen here.

1. **Make the writer print something a document cannot contain.** `make` emits a marker carrying a
   value no page would ever quote — a run nonce, a process id — and the reader requires it. Cost: it
   breaks the property the marker was designed for, that a human can read the line;
   `wiki/concepts/a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code`
   is the page that would have to change, and it is live and correct about why the marker exists.
2. **Narrow the reader to the command it was launched for.** The payload carries the command string;
   a recorder that refuses to read a marker out of a command that never invoked the runner is a
   condition on data the hook already has. Cost: one condition, and it has to be right about what
   invoking looks like — `make smoke`, `make suite`, `python -m uv run ...`, a `Makefile` recipe
   reached some other way.
3. **Forbid the corpus from spelling the literal.** Rejected in the drafting: it charges the price
   back to correct prose, which is the argument the vault already accepted against a page declaring
   itself exempt from the no-quantity rule
   ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).

**Route 2 is the cheapest and the one this draft would build**, with route 1 named as the fallback
if the command string turns out not to be reliable in the payload.

**The general half is a page rather than a mechanism.** No script can find the next instrument of
this class; what can be written down is the question to ask of one — *name a document in this
repository that would make this fire*, which is the same shape as the question the store already
asks of a new verdict, *name an input that makes this fire and nothing else fire*
([[a-verdict-that-cannot-fire-is-worse-than-no-verdict]], archived).

## What is open

- **Whether the `PostToolUse` payload's command string is dependable enough to condition on.** The
  one page describing that payload says it carries `run_in_background`, a task id and an output path,
  and explicitly says the timing of a second fire is not established. Nobody has checked what the
  command field holds for a `make` invoked through a shell wrapper.
- **What is done with the false rows already standing.** Two were written today by this dispatch;
  the journal names one more at `2026-08-29T08:32:22`. The ledger is append-only by design, so
  striking them is a decision about the ledger and not a repair.
- **Whether the same condition is owed by the other marker.** `SUITE-EXIT:` has the identical shape
  and was not measured. This draft did not count its occurrences in the corpus.
- **Whether a rule page is owed.** The general half would render into the agents and hooks that read
  markers, and this draft does not choose a destination — the owner chooses destinations.

## What it would oblige

- **The recorder's selftest gains a case that plants the marker in a command that ran no check and
  asserts no row is written.** Without it this is a rule a fixture can violate for a week
  ([[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]], live).
- **The case is proved by reading the ledger back**, not by the check returning green
  ([[a-planted-offender-is-proved-by-reading-it-back]], live).
- **`wiki/concepts/a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code`
  gains the limit it does not currently state**: the printed-marker arrangement is sound about
  *trusting* the marker and silent about *who printed it*, and that silence is the whole defect.

## What it would retire

- **`wiki/lessons/a-comment-quoting-the-literal-a-sweep-looks-for-is-counted-by-that-sweep`** — its
  content is carried forward whole as the fourth row of the family table above.

**Nothing else in `wiki/lessons/` is retired by this**, and the three archived siblings are not
resurrected: they are named as provenance, which is what `archive/` is for.
