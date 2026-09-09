---
title: "The repository's `CLAUDE.md` after the rules left it: rendered regions, no map, and the prose that is still there on purpose"
type: entity
status: current
authority: claude-md-scope
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md"]
tags: [harness, process, vault]
supersedes: [[claude-md-is-a-map-and-four-rules]]
---

# What the file is, measured on disk at `814472a`

**Restructured on 2026-08-17, in one session, in three commits.** Two sections merged into one, one
section deleted, nine marked regions, and a heading that no longer states a count.

| What it holds now | How |
|---|---|
| the project description and the stack | hand-written prose, and staying — the owner ruled that a *sourced* assertion is legitimate here ([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]) |
| the rules and the routes into the vault, in one section | the sections *"Where the rest of the knowledge is"* and *"Four rules that cannot wait for a question"* merged; the heading no longer counts anything ([[a-stated-count-drifts-from-the-list-it-heads]]) |
| nine rules | rendered from `wiki/rules/` into nine marked regions ([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]) |
| the language rule | one region, one page, because a rule ships one piece of text or it is two rules ([[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]]) |
| the by-hand `rg` recipe | hand-written prose, and it cannot render: a fenced block inside a `<!-- text -->` slice is dropped ([[the-injector-drops-a-fenced-block-inside-a-slice]]) |
| the commands | hand-written prose, and **drifting** — see below |

**`## Where things are` is gone.** Deleted, not corrected, on the owner's decision, with a generator
to fill the gap later ([[where-things-are-is-deleted-now-and-generated-later]]).

## Two things in it are known wrong and were deliberately not patched

**The first sentence still says the file *"is a map and a handful of rules"*.** The map was deleted
in the same session and nine rules render rather than being written. It was left standing on purpose:
patching it would have been another sentence of unsourced prose from the same author, and the shape
that fixes it is the map's own region, which is unbuilt
([[the-map-in-claude-md-and-its-admission-test]]).

**`## Commands` says `vault-check.sh` takes `~2 s` and the measured figure is `4.9 s`** — a list that
drifted from reality inside the same session that changed it. That block is what the `Makefile`
decision is for ([[the-command-list-moves-into-a-makefile]]), and until the generator exists the
number stays wrong on the record rather than corrected in place
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

## What this replaces, and what it does not

It supersedes [[claude-md-is-a-map-and-four-rules]], which described the file as it stood from
2026-08-14: a description, the language rule, the commands, four rules typed into a numbered list,
and a map of where things are. **Three of those five are no longer true**, and the retirement was
owed to *"the session that performs the change"* by [[the-repository-claude-md-becomes-a-dispatch-table]].
That session was 2026-08-17.

**What carries over unchanged**, and is not re-argued here: the test that chose which rules belong in
this file at all — *obeying them late is the same as not obeying them at all* — and the refusal of
`[[wikilinks]]` in it, which resolve inside Obsidian and are inert outside. Both are on the retired
page, which is where to read them.

**The dispatch-table decision is not met by this.** The file still points at `/vault-ask` and
`/pre-task` and carries rendered rules; it is not yet a table of callable things, and rule 5b passes
vacuously because no wikilink is left to check
([[claude-md-may-point-and-may-not-assert]]).

# What the file gained on 2026-08-18: a tenth region, and a blank line in every one

**It changed twice.** Measured with `wc -l` at each commit:

| Commit | Lines |
|---|---|
| `e51d390` / `e83ce28` — before the map | **116** |
| `013a6d0` / `97895a9` — the map's region in, three lines of prose out | **128** |
| `b311f0f` — ten regions each gain a blank line | **138** |

*(The journal of 2026-08-18 records **116** as the count *"before the separator change"*; measured
here, 116 is the count before the **map**, and 128 is the count before the separator. The number is
right and the boundary it names is one change early.)*

**A tenth region, and the first rendered from outside `wiki/rules/`**:
[[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]], a `concepts/` page carrying
`governs: CLAUDE.md`, marked as a `concept:` pair.

**Three lines of prose were removed and arrive rendered instead**, verified present in the region
before the old text was dropped ([[the-maps-region-replaces-the-prose-it-duplicated]]).

**The separator is inside each region**, written by the injector
([[the-injector-writes-the-separator-inside-the-region]]) — because the blank line *between* two
regions is stripped along with the markers before the file reaches the model, measured at **1354 of
7213 bytes on disk and none of what is read**
([[block-comments-are-stripped-before-claude-md-reaches-the-model]]).

**Two things this section corrects on the record.** The file is **pure LF** in the working tree —
`tr -cd '\r' < CLAUDE.md | wc -c` is `0`, and `*.md text eol=lf` has been pinned since 2026-08-17
([[markdown-is-pinned-to-lf]], [[a-subagents-most-believable-sentence-is-the-one-to-measure]]). And
**the `rg` recipe's mechanical excuse is gone**: a fenced block inside a slice survives from
`e83ce28` ([[a-fenced-block-inside-a-slice-survives-into-the-destination]]). It stays prose on the
owner's reason — the routes are the one part of this file that has never gone stale.

**The first sentence still says the file *"is a map and a handful of rules"*, and it is now true
again.** It was left deliberately wrong as a marker of the missing map; whether it is reworded is
the owner's, and the prose of this file is not the librarian's to edit.

## An eleventh region, and a criterion for what stays — 2026-08-18, second session

**The eleventh region is the definition of *retrospective***, the second rendered from outside
`wiki/rules/` and the first whose source paragraph already stood in this file
([[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]],
[[a-definition-may-render-into-the-repository-claude-md]]). The diff of the destination is three
insertions and no deletions — the two markers and the separator — because the prose was cut out with
`sed` and spliced in unchanged.

**Measured at `c521a10`: the eleven regions carry 3,637 bytes of slice text**, roughly 850 tokens,
against 7,371 bytes of file. That figure is recorded as a measurement and explicitly not as the
ground for moving anything ([[the-ast-rule-moves-to-prove-the-mechanism]]).

**What belongs in this file now has a criterion**: what bootstraps the asking, plus what is
irreversible if missed — it sorts all nine rules without a remainder
([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]]). **The first rule it
sorts out is the JavaScript one**, agreed for removal and not yet removed
([[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]]).

**The `## Language` region gained a sentence at this ingest**, on the owner's decision that the
register instruction joins the language rule's slice rather than standing beside it
([[english-terms-are-not-transliterated-into-cyrillic]],
[[english-in-the-repository-russian-with-the-owner]]).

## A rule left the file, and every count on this page above moved — 2026-08-20

**The AST boundary rule moved to conditional delivery.** `wc -l CLAUDE.md` went **145 to 139**, and
the rules rendering into it went **from nine to eight**; the file carries **ten regions in all**,
having carried eleven — the map and the definition of *retrospective* are the other two
([[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]],
[[the-generated-ast-boundaries-rule-file]]).

**So the row reading *nine rules | rendered from `wiki/rules/` into nine marked regions* is a
reading of 2026-08-17** and is left standing as one
([[the-region-coverage-figure-is-dated-where-it-stands]],
[[a-stated-count-drifts-from-the-list-it-heads]]). What is true today is the paragraph you are
reading.

**Nothing else on this page changed.** The prose that is here on purpose is here on the same
reasons: the project description stays as a sourced assertion, the `rg` recipe stays on the owner's
reason, and `## Commands` is still drifting. **The two things known wrong are unchanged**, and the
first sentence still says the file *"is a map and a handful of rules"* — which remains true and
remains the owner's to reword.

**What this move does not do is make the file a dispatch table**
([[the-repository-claude-md-becomes-a-dispatch-table]]). One rule left; eight are still rendered
into it, and the criterion for what belongs there is untouched
([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]]).

# `## Commands` became a pointer, and the obligation beside it is still typed — 2026-08-26

**The section now points at `make help` instead of listing four commands**, which removes the
drifting `~2 s` figure it carried for `vault-check.sh` ([[the-makefile]]).

**The pre-commit obligation moved with it and is now worded against `make style`.**

**It is still a typed assertion outside every marked region**, so it can go false exactly the way the
`~2 s` figure did and nothing would say so. **Rendering it from a `wiki/rules/` page is decided-and-
not-built**, and it is the shape this file's own history argues for
([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]).
