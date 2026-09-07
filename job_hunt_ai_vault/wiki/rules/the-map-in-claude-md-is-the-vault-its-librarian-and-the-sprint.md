---
title: "The map rendered into the repository's `CLAUDE.md`: the vault, its librarian, and the sprint"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: human
sprint: S2
created: 2026-08-18
sources: ["CLAUDE.md", "scripts/vault-inject.sh", "[[the-map-in-claude-md-and-its-admission-test]]", "[[the-sprint-belongs-in-the-map-and-the-map-has-an-admission-test]]"]
decided_by: [[the-sprint-belongs-in-the-map-and-the-map-has-an-admission-test]]
supersedes: [[the-map-in-claude-md-and-its-admission-test]]
tags: [harness, process, vault]
---

# What travels

<!-- text -->
**The vault holds the reasons.** It is the top-level directory containing a `wiki/`, and it
carries what exists, what was decided and why, how each mechanism is built, and what has burned
us. None of that is repeated here: ask it before deciding anything it may have decided already.

**It has exactly one writer.** The librarian writes `wiki/` and the registers — `index.md`,
`tags.md`, `sprint.md`, `log.md`. A session does not edit them by hand; when an answer comes back
wrong it reports the miss and lets the librarian write.

**Work belongs to a sprint, and the vault's `sprint.md` is where that sprint lives** — which one
is open, its goal, and the command each acceptance criterion is decided by. Work outside an open
sprint is work nobody agreed to. Read the contents there; they are never copied here.
<!-- /text -->

Everything below this line stays on this page — that is the whole mechanism
([[what-travels-from-a-rule-page-is-a-marked-slice]]). The slice carries no `[[wikilink]]` by
construction, and every citation on this page sits outside it: see *What a slice may not carry*
below.

# What it admits, and what it refuses

The test is the owner's, agreed 2026-08-17 and quoted in his own words on
[[the-sprint-belongs-in-the-map-and-the-map-has-an-admission-test]]:

> **An entry earns its place if a session that does not know it does the work *wrong*, not merely
> slowly.**

| Candidate | Verdict |
|---|---|
| the vault | **in** — not knowing it exists costs every reason the session produced ([[the-vault-is-compiled-not-retrieved]]) |
| its librarian | **in** — a session that writes `wiki/` by hand breaks the one-writer property ([[the-one-writer-rule-covers-the-registers-too]], [[vault-librarian]]) |
| the sprint | **in** — work outside an open sprint has happened for a whole day and nothing stopped it ([[a-gate-that-refuses-work-without-an-open-sprint]]) |
| where `src/` is, where the tests are, where the hooks are | **out** — not knowing costs seconds of `ls`, which is slower and not wrong |

**The sprint entry carries the fact and never the contents**, and that is the property that keeps
this region from becoming the next `## Where things are`: a goal, a criterion or a milestone copied
here would drift the day it changed, and a copy that has drifted is repaired by deletion rather
than by correction ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]],
[[where-things-are-is-deleted-now-and-generated-later]]).

**The vault entry names the discovery rule rather than a directory name.** The name is what Obsidian
shows the owner, it is his, and it changed four times in the session that created the vault
([[the-vault-directory]]). It is fixed from 2026-08-17 for `governs:` **and for nothing else**, so a
rendered region that hard-codes it would be one more thing to edit on a rename. What stands in the
slice is a description — *the top-level directory containing a `wiki/`* — and not the shell idiom
the discovery scripts share, so it adds no further copy of that command.

# Why this is a `concepts/` page — closed by the owner, 2026-08-18

The design left the category open: *"it is a noun with properties, which argues `entities/`; it is
also a mechanism with a consequence, which argues `concepts/`"*
([[the-map-in-claude-md-and-its-admission-test]]). **The owner closed it as `concepts/`**, on two
arguments put to him and accepted:

- **An entity page names one subject; the map names several and describes none of them.** Measured
  on 2026-08-18 with `ls job_hunt_ai_vault/wiki/entities/*.md | wc -l`: **23 pages**, each about a
  single named thing — a tool, a file, a directory, an agent. The closest counter-cases are
  [[vault-scripts]] and [[session-hooks]], and they hold rather than break the argument: each names
  a set of one kind under one owner, which is still one subject. The map's subjects are of
  different kinds, and it is not a description of any of them — a reader who wants the vault
  described goes to [[the-vault-is-compiled-not-retrieved]], and one who wants the librarian goes to
  [[vault-librarian]].
- **What the map is worth is the judgement, not the list.** Its value is a single editorial ruling
  about what a session must not fail to know, with a consequence attached — the entries the ruling
  refuses do not appear, whatever a reader would find convenient. That is the schema's own line
  between the folders: *an entity is a noun with properties, a concept is a mechanism with
  consequences*.

**And it sets the marker's type word**, because the type in a marker is the singular of the folder
([[the-marker-carries-the-records-type]], [[a-marker-with-its-type-is-a-complete-address]]). This
page's region is therefore a `concept:` pair, not an `entity:` one.

# The routes stay prose — closed by the owner, 2026-08-18

The design's second open question was *"whether the routes stay prose or join the region"*. **They
stay prose.** `/vault-ask`, `/pre-task` and the by-hand `rg` recipe are hand-written in the
repository's `CLAUDE.md` and are outside this region.

**The reason is the strongest evidence any text in that file has**: they are the one part of it that
has never gone stale, in a file whose staleness has its own register and whose register keeps growing
([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]). A mechanism that exists to stop
drift does not improve text that has been correct since the day it was written, and moving it would
cost a page, a region and a selftest's worth of check time for no defect.

**One earlier argument for the same conclusion has expired, and the decision does not rest on it.**
The recipe was said to be unable to render at all, because a fenced block inside a `<!-- text -->`
slice was dropped on the way to the destination — measured, and recorded on
[[the-injector-drops-a-fenced-block-inside-a-slice]] and
[[the-repository-claude-md-after-the-rules-left-it]]. **At `e83ce28` a fence inside a slice survives
into the destination.** That page states the old behaviour and is `basis: code` against code that
has changed; correcting it belongs to the ingest of this session and is not done here.

**`/pre-task` is a route and also a rendered rule**, and the two are different things in that file:
the imperative is [[a-pre-task-runs-before-anything-non-trivial]] and renders into its own region,
while the pointer paragraph beside it stays prose, because the file keeps its own pointers
([[the-repository-claude-md-becomes-a-dispatch-table]]).

# What made a descriptive page renderable at all

**Until `e83ce28`, this page could not have existed.** `scripts/vault-inject.sh` globbed
`wiki/rules/` alone and every `governs:` branch of the check was gated on that folder, so a
`concepts/` page carrying `governs:` was neither rendered nor refused — a green that examined
nothing ([[a-page-outside-wiki-rules-carrying-governs-is-silently-inert]]). That commit widened the
walk to `wiki/*/*.md`, took the destination from the field, and put the record's type into the
marker ([[governs-becomes-a-property-of-any-page]], [[the-marker-carries-the-records-type]]).

**And a rule page was never an option for this text.** `wiki/rules/` admits what is *imperative and
not enforced by a test* ([[the-harness-is-compiled-not-maintained]], [[rules-becomes-a-type-of-its-own]]);
the map instructs nobody. Admitting it there would empty the admission test that folder stands on,
which is the same objection that kept the project description out of it
([[governs-becomes-a-property-of-any-page]]).

**What the owner has now ruled may render, in the order he ruled it:** an imperative, from
`wiki/rules/`; a *sourced* assertion, which is what keeps the project description in that file
([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]); and, on 2026-08-18, **a
definition**. The third is what admits this page: the map asserts nothing about the tree beyond
naming what it names, and defines what a session is expected to know before it starts.

# What a slice may not carry

**A `[[wikilink]]` inside a `<!-- text -->` slice is red, enforced in `scripts/vault-inject.sh` on
2026-08-18.** The destination is a file where Obsidian syntax is inert, so a rendered link arrives
as dead punctuation pointing nowhere. It is asked outside fences and outside code spans, like every
other content rule in that script. This page's slice carries none, and the citations that would have
been inside it are the table and the sections above.

**A slice on a page with no `governs:` is red for the mirror reason** — text marked to ship that
nothing delivers still reads as governed. This page carries `governs: CLAUDE.md`, so it is not that
case ([[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]]).

# The file's own first sentence becomes true when this renders

The repository's `CLAUDE.md` opens its rules section with

> **This file is a map and a handful of rules for how to work.**

**That sentence was left deliberately wrong.** `## Where things are` was deleted rather than
corrected, and patching the sentence would have been one more line of unsourced prose from the same
author, so it was left standing as a marker of this gap
([[the-repository-claude-md-after-the-rules-left-it]],
[[where-things-are-is-deleted-now-and-generated-later]]).

**It becomes true again the moment this page renders**: the file carries a map, and the map has a
page behind it that the gate compares against. **Whether the sentence is then reworded is the
owner's**, not the librarian's — the prose of that file is not `wiki/`, and nothing here touches it.

**One overlap is named rather than fixed.** The paragraph directly under that sentence already says
part of what this slice says — *"Everything else is in the vault — what was decided and why, how
each mechanism works, what exists, what burned us"*. Two texts saying one thing, one rendered and
one typed, is the exact shape this mechanism exists to end. Which of them goes is a decision about
that file and belongs to the session marking the region and to the owner reviewing it.

# Where it renders

`governs: CLAUDE.md` — a path from the repository root, resolved against nothing else
([[governs-is-a-path-from-the-repository-root]]). The text lands in a paired comment named for this
page's type and slug, alone on its line at column zero
([[a-region-is-a-paired-comment-named-for-a-rule]]).

**The page and its region belong in one change, and this page arrived first.** The librarian writes
`wiki/`; marking the region and running the injector are the session's, in the same commit. Until
that happens the injector reports that `CLAUDE.md` carries no region for this page, and rule 12 of
`vault-check.sh` is red — the expected state of a half-finished landing, not a defect in the page
([[a-check-asks-by-running-the-writer-it-checks]]).

# What this page does not claim, and what is owed elsewhere

**It carries no `authority:`, deliberately.** Whether a `concepts/` page may own an `authority:`
*and* render is a shape nothing in the vault rules on, and the check's frontmatter pass keeps that
gate narrow on purpose rather than answering the question by accident. Claiming one here would
answer it by accident from the other side. The questions this page's subject touches are already
owned: `map-admission` by [[the-sprint-belongs-in-the-map-and-the-map-has-an-admission-test]] and
`claude-md-scope` by [[the-repository-claude-md-after-the-rules-left-it]].

**The design page is not retired here, and its disposition is the owner's.**
[[the-map-in-claude-md-and-its-admission-test]] closes with *"retired with `superseded_by:` the day
it is built or refused"* ([[proposals-are-a-folder-not-a-status]]), and it was built today.
**Nothing about it was changed**: the owner set the opposite precedent on
[[marked-regions-and-the-prose-outside-them]], which was built and kept `current` with the librarian's
reasoning on the record, and he has explicitly deferred the same question on
[[the-marker-carries-a-type-and-governs-is-read-as-a-field]] — *"we decide when it is built"*. So the
disposition of the design page is **due, and it is his**.

**What this page does not answer**: whether `docs/` joins the governed set, whether the region for
the project description is next, and what happens to the map if a fourth entry is ever proposed —
the admission test decides that, and the test is on the decision page rather than here.

# Three corrections and one disposition, from the ingest of 2026-08-18

**The design page is retired.** [[the-map-in-claude-md-and-its-admission-test]] is `deprecated` in
`archive/` with `superseded_by:` pointing here, on the owner's one-policy call and after the check
that nothing on it lives only there ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).
The paragraph above, which says its disposition is due and his, is left standing as the state on the
day this page was written.

**A third option for the category was named and knowingly refused**, and it is not in the section
above: **no map page at all, with four existing pages each growing a slice.** Refused because then
no page owns the question *what must a session know*, and the fifth candidate entry would have
nowhere to be decided. The admission test needs a place to be applied, and a test with no page is a
test nobody runs.

**The entities argument was put to the owner more strongly than the corpus supports.** All 23 pages
in `entities/` were described as being each about one named thing; **two of them title a set rather
than a thing** — [[vault-scripts]] and [[session-hooks]]. The count is right and the conclusion
survives, and the overstatement is recorded because the argument was accepted on that wording
([[a-subagents-most-believable-sentence-is-the-one-to-measure]]).

**The overlap named above was resolved rather than left.** The duplicated prose was removed from
`CLAUDE.md` and arrives rendered, verified present in the region before the old text was dropped
([[the-maps-region-replaces-the-prose-it-duplicated]]) — and the fact that the mechanism produced a
duplicate on its first use outside `wiki/rules/` is its own lesson
([[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]]).

**The slice carries no `[[wikilink]]` because it may not**, from `e83ce28`
([[a-wikilink-inside-a-rendered-slice-is-red]]), and it carries one blank line after it, written by
the injector ([[the-injector-writes-the-separator-inside-the-region]]).

# This is a rules page from 2026-08-21, and the category argument is spent

**The two sections headed *Why this is a `concepts/` page — closed by the owner, 2026-08-18* and
*What made a descriptive page renderable at all* are false in their conclusion from this date.** The
owner reopened and reversed the category at the retro of 2026-08-21: **a page that renders its text
into another file is a rule** ([[governs-is-a-property-of-wiki-rules-alone]]). Both sections are
left standing as the reasoning that held between 2026-08-18 and 2026-08-21, and this section is the
correction rather than a rewrite of them.

**The argument they turned on was the folder's admission test, and the test itself changed.**
`wiki/rules/` was read as admitting what is *imperative and not enforced by a test*, so a map — which
instructs nobody — would have emptied it ([[the-harness-is-compiled-not-maintained]],
[[rules-becomes-a-type-of-its-own]]). The folder now admits on **delivery**: it is the one category
whose text is written to be rendered elsewhere, and carrying `governs:` is what satisfies that. The
entities-against-concepts comparison in the first of those sections is unaffected and simply no
longer decides anything — neither folder is the answer.

**What was overturned is a ruling of the owner's own**, and the retired decision that licensed this
page is [[governs-becomes-a-property-of-any-page]], now in `archive/`. It was right that three
licensed records had nowhere to render from in 2026-08-17, and right to refuse both a seventh folder
and a widened `wiki/rules/` on the tests the project had then; what it produced was two pages that
were rules in everything but their folder, and this was the first of them.

**The move was a folder move and not a rename.** `type: concept` became `type: rule`, `supersedes:`,
`governs:`, `render:` and every other line stayed as they were, and the filename — which is the
address — did not move ([[a-title-corrected-in-place-is-not-a-supersession]]). The title still says
*rendered into the repository's `CLAUDE.md`*, which is true and is what the folder is now for.

**What did move is the type word in the marker.** The injector derives it from the folder, so this
page's region is a `rule:` pair from now on and the `concept:` pair standing in `CLAUDE.md` is the
session's to rewrite ([[the-marker-carries-the-records-type]],
[[a-marker-with-its-type-is-a-complete-address]], [[a-check-asks-by-running-the-writer-it-checks]]).
The sentence in *What made a descriptive page renderable at all* saying this page's region is
*"a `concept:` pair, not an `entity:` one"* is spent with it.

**The section headed *What this page does not claim* is half spent, in the same way.** *"It carries
no `authority:`, deliberately"* is still true and is now the folder's rule rather than a shape
nothing had ruled on ([[authority-beside-governs-is-forbidden-on-any-page]],
[[authority-becomes-the-index-and-is-required-outside-rules]]). The slugs it names as already owned
elsewhere — `map-admission` and `claude-md-scope` — are untouched.
