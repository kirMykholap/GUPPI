---
title: "The page list is a query, and the conclusion of the generated catalogue outlived its mechanism"
type: decision
status: archived
authority: catalogue-generation
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "pages.base", "scripts/vault-catalogue.sh", "scripts/vault-check.sh"]
tags: [vault, retrieval]
supersedes: [[the-catalogue-is-generated-not-maintained]]
---

# Decided by the owner on 2026-08-17: use Bases

**The conclusion of [[the-catalogue-is-generated-not-maintained]] stands and its mechanism is
gone.** That page's claim was: *both artefacts exist — `index.md` answers where do I start, and a
separate artefact answers what is there at all — and the old objection reaches only a catalogue
somebody maintains.* All of that survives. What it named as the way to hold the list was a
**generated file guarded by rule 9**, and that is what was replaced.

`catalogue.md` is deleted. The list is `pages.base` ([[pages-base]]), an Obsidian base — a query
rather than an answer, evaluated when it is opened.

**Rejected: keeping the generated file.** Nothing but rule 9 and two lines of `index.md` ever read
it, and no agent ever did.

## Why this is a supersession and not a correction

The old page's conclusion survived its mechanism, which is exactly the shape that earns a successor
rather than an edit: the *claim* changed, not the wording of a title
([[a-title-corrected-in-place-is-not-a-supersession]]). A reader who greps `rule 9` or
`catalogue.md` should land on a page that names what replaced them, not on a current page that is
half true.

## What it obliged, all in one change

- **Rule 9 of `vault-check.sh` is retired**, and its number is not reused
  ([[a-retired-rule-number-is-never-reused]]).
- **The selftest's `regen_catalogue` wrapper is gone with it** — and with it the measured **43
  seconds of the suite's 201** that the wrapper cost
  ([[a-rule-over-every-page-makes-every-test-fragile]]).
- **`scripts/vault-catalogue.sh` survives and only prints.** It exists because a base is
  unreadable to every reader of this repository except Obsidian ([[vault-scripts]]).
- **The write ritual is now inject, then check.** There is no catalogue step.

## `--write` is refused rather than ignored

`bash scripts/vault-catalogue.sh --write` exits **2** with a message, instead of quietly printing
to stdout. A caller still passing that flag believes a file is being kept up to date; printing
instead would look like success and leave the belief intact. Removing the flag silently would do
the same. **The refusal is the message.**

## What was paid for it

Two things the generated file gave are gone, and both are worth naming rather than discovering
later.

- **The cheap proof after an audit.** On 2026-08-15 a regeneration that came back byte-identical
  after `/vault-lint` rewrote sixteen pages proved, in a diff of nothing, that no `title`,
  `status`, `sprint` or `tags` line had moved. A query cannot make that assertion, because it
  produces no artefact to compare ([[the-audit-is-dispatched-after-the-writes]]).
- **A worked instance of a generated artefact as an assertion about its inputs.** The pattern still
  holds elsewhere; this store simply has one fewer example of it.

Against that: a query **cannot be stale at all**, which is the failure class the whole gate exists
for, and it costs nothing per run.

## The header lied about itself for one run

The script's printed header went on saying *run `--write`* and *rule 9 fails* after both had been
retired, and nothing caught it — [[generated-text-can-lie-about-the-mechanism-that-generates-it]].

## The agent half owes a `governs` column — deferred 2026-08-17

**The Obsidian half exists as a named view.** The owner built a `harness` view on `pages.base` with a
`type == "rule"` filter, two extra columns and a `file.name` sort, and it answers *which rules exist and
what each governs*.

**`scripts/vault-catalogue.sh` has no such column, and that is about five lines.** So **the reader who most
needs *which rules render into this file* is the one who cannot get it** — an agent, which has no editor,
and which is exactly the audience this decision's split was designed for
([[pages-base]], [[vault-scripts]]).

**Deferred with the cost stated** ([[what-the-harness-build-waits-on]]). Until it lands, an agent answers
that question with `rg "^governs:" wiki/rules`, which works and is not written down anywhere a reader would
find it.

## And the `binding:` column is the same gap, on a field with a live reader — 2026-08-22

**The deferral above is extended rather than given a page of its own**, on the recommendation of the
`- miss:` that found it: the gap is identical and the closing words above already state its cost.

**`/pre-task` phase 1 is specified to keep only `decisions/` pages carrying `binding: prohibition`,
and the catalogue prints no such column** — Page, Authority, Title, Status, Sprint, Tags. **So phase
1 as written cannot be performed from the catalogue alone**, and the agent carries a second `grep`
over one folder to do it ([[the-pre-task-agent]], [[a-decision-declares-whether-it-binds]]).

**This one has a reader today, which the `governs` column did not.** The repair is the same size —
one script call or about five lines of `awk`, since `bash scripts/vault-authority.sh` already caches
`binding` per page — and the reader who most needs it is again the one who cannot get it: an agent,
which has no editor ([[vault-scripts]]).

**Deferred with the cost stated, and nothing in `wiki/` states the catalogue's column set anywhere
else.** That absence is why the gap was found by running the ritual rather than by reading.
