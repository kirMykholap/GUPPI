---
title: "A retrospective is a session's end, not a sprint's ritual"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: human
sprint: S2
created: 2026-08-18
sources: ["CLAUDE.md", "[[the-end-of-a-session-is-a-retrospective]]", "[[a-definition-may-render-into-the-repository-claude-md]]", "[[ingest-runs-after-handoff-at-the-end-of-a-session]]"]
decided_by: [[the-end-of-a-session-is-a-retrospective]]
tags: [harness, process, vault]
---

# What travels

<!-- text -->
**"Retrospective" means the end of a session.** The sprint-level ritual is a *sprint retrospective*
and is a different thing — the word meant both for three days and that ambiguity put two live,
contradictory answers in the vault about when `/ingest` runs.
<!-- /text -->

Everything below this line stays on this page — that is the whole mechanism
([[what-travels-from-a-rule-page-is-a-marked-slice]]). The slice carries no `[[wikilink]]`, which
is a verdict and not a preference ([[a-wikilink-inside-a-rendered-slice-is-red]]): the destination
is a file where Obsidian syntax is inert, so a rendered link arrives as punctuation pointing
nowhere. Every citation on this page therefore sits outside the marks above.

**The three lines were not written here.** They are the paragraph that stood at `CLAUDE.md:58-60`,
moved rather than reworded: cut out by line number and spliced into the slice above without an
edit to the wording, the line breaks or the punctuation. That is how the nine rule migrations were
done and the argument is theirs — **rewording a rule while moving it is a change nobody decided,
and it is invisible in the diff of a migration that is supposed to be a move**
([[the-suite-never-runs-against-the-production-database]]).

# What the ambiguity cost, which is why a word earns a page

**The word named both rituals for three days**, and the damage was not cosmetic. It put **two
`current` pages into this corpus giving contradictory answers to one question — when `/ingest`
runs** — each with `basis: human`, because each was a faithful record of what the owner said about
the ritual its author had in mind. One read *"the retrospective"* as the sprint's and moved the
ingest to it; the repository's `CLAUDE.md` read it as the session's. The contradiction was resolved
on 2026-08-17 by retiring the earlier page, and the survivor is
[[ingest-runs-after-handoff-at-the-end-of-a-session]].

**A word that names two cadences is read as whichever one the reader already has in mind.** That
is a retrieval failure rather than a wording failure, which is what makes it a record instead of a
correction — the reasoning is [[the-end-of-a-session-is-a-retrospective]], the decision that
settled the naming and renamed the sprint-level ritual to *sprint retrospective*.

**The sprint retrospective is a term with nothing behind it**, deliberately. Nothing is designed
for it, and the next session to reach a sprint boundary meets that gap rather than an ambiguity —
which is the whole point of the second half of the sentence in the slice.

**What the word does name is built and has its own pages**: the order of the closing ritual is
[[a-session-ends-with-retro-then-handoff-then-ingest]], the step itself is [[the-retro-step]], and
why interrogation and routing are different genres is [[retro-interrogates-and-handoff-routes]].

# Why this is a definition, and why it could not come from `wiki/rules/`

**It is not imperative.** It instructs nobody: it fixes what a word means so that two rituals stop
being confusable. `wiki/rules/` admits what is *imperative and not enforced by a test*
([[the-harness-is-compiled-not-maintained]], [[rules-becomes-a-type-of-its-own]]), and admitting a
definition would empty the admission test that folder stands on — the same objection that keeps
the project description out of it ([[governs-becomes-a-property-of-any-page]]).

**So it renders from the folder its record belongs to**, and the shape was licensed on 2026-08-18:
a **definition** may reach the repository's `CLAUDE.md` through a region, beside an imperative and
a *sourced* assertion ([[a-definition-may-render-into-the-repository-claude-md]],
[[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]). That ruling names this
paragraph as the case that forced it.

**`concepts/` was the owner's call and predates this page**, recorded on
[[the-end-of-a-session-is-a-retrospective]] and carried as a row on
[[what-the-harness-build-waits-on]]. It is also the right side of the schema's own line: a word
whose ambiguity produced two contradictory records is a mechanism with a consequence, not a noun
with properties, and no seventh folder was ever available for renderable records
([[the-folder-set-is-closed-and-tasks-is-not-in-it]]).

# Where it renders

`governs: CLAUDE.md` — the repository's file, a path from the repository root and resolved against
nothing else, never the vault's own `CLAUDE.md` ([[governs-is-a-path-from-the-repository-root]]).
The text lands in a paired comment named for this page's type and slug, alone on its line at column
zero ([[a-region-is-a-paired-comment-named-for-a-rule]]), spelled `concept:` because the marker
carries the record's type in the singular ([[the-marker-carries-the-records-type]]).

**Its place in the file is where the paragraph already stood**: between the region for the closing
ritual and the region for the vault-feedback rule. That is not incidental. The slice defines the
word the region above it uses, and a reader who meets *retro* in the ritual and *retrospective*
here is the reader the two contradictory pages were written for.

**Three adjacent regions is exactly the case the separator exists for.** A rendered region carries
one blank line after its slice, written by the injector, because the blank line *between* two
regions is stripped along with the markers before the file reaches the model
([[the-injector-writes-the-separator-inside-the-region]]). It is not typed onto this page and must
not be: the writer emits it and drops the region body wholesale, so it is idempotent.

**The page and its region belong in one change, and this page arrived first.** The librarian writes
`wiki/`; marking the region and running the injector are the session's. Until that happens the
injector reports that `CLAUDE.md` carries no region for this page and rule 12 is red — the expected
state of a half-finished landing, not a defect in the page
([[a-check-asks-by-running-the-writer-it-checks]]).

# What is owed at the destination and cannot be asked of the gate

**The gate compares this region against this page and guarantees agreement, never truth**
([[a-gate-guarantees-agreement-never-truth]]) — and it is blind to what the file *around* the
region says. The check that answers that is read in the destination, before the region lands:
**read the rendered slice against the file it lands in**
([[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]]), and remove the typed paragraph
only after the rendered one is verified present
([[the-maps-region-replaces-the-prose-it-duplicated]],
[[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

**This landing is the safer half of that lesson rather than a repeat of it.** The duplicate the
lesson records was produced by a page written *fresh* beside prose that already existed; here the
prose is moved out, so the source lines are deleted by construction — the invariant the nine
migrations carried without stating it. What it inherits instead is the ordering: verified, then
deleted, and never the reverse.

# What this page does not claim

**It carries no `authority:`, deliberately.** Whether a non-rule page may own a question *and*
render is unruled, and the check's frontmatter pass keeps that gate narrow on purpose rather than
answering it from inside a script ([[authority-beside-governs-on-a-non-rule-page-is-unruled]]).
Claiming one here would answer it by accident from the other side, as the first non-rule renderer
also declined to do ([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]).

**And `end-of-session-ritual-name` is not this page's to take.** It belongs to
[[the-end-of-a-session-is-a-retrospective]], which decided the naming; this page holds the text the
repository reads. Two `current` pages on one slug would be a contradiction, and a decision and the
record stating it sharing a slug is the exact shape the rules-only `authority:` gate was written
against.

**What this page does not answer**: whether the *sprint retrospective* is ever designed, what the
project description's folder will be, and whether the eleventh region moves S2's criterion 6 —
that criterion is read on the files by the owner and by nobody else.

# This is a rules page from 2026-08-21, and the section arguing it could not be is spent

**The section headed *Why this is a definition, and why it could not come from `wiki/rules/`* is
false from this date.** It argued that the folder admits what is *imperative and not enforced by a
test*, and that admitting a definition would empty that admission test. The owner replaced the test
at the retro of 2026-08-21: **a page that renders its text into another file is a rule**, whatever
its grammatical mood ([[governs-is-a-property-of-wiki-rules-alone]]). The argument is left standing
as the reasoning that put this page in `concepts/` between 2026-08-18 and 2026-08-21, and this
section is the correction rather than a rewrite of it.

**The move was a folder move and not a rename.** `type: concept` became `type: rule` and no other
line of the frontmatter changed; the filename is the address here, and it did not move, so every
inbound link resolves exactly as before ([[a-title-corrected-in-place-is-not-a-supersession]]).

**What did move is the type word in the marker**, which the injector derives from the folder rather
than from the page ([[the-marker-carries-the-records-type]],
[[a-marker-with-its-type-is-a-complete-address]]). The region for this page in the repository's
`CLAUDE.md` is a `concept:` pair until the session rewrites it as a `rule:` pair, and until then the
injector reports that the file carries no region for this page — the expected state of a
half-finished move ([[a-check-asks-by-running-the-writer-it-checks]]).

**The section headed *What this page does not claim* is half spent.** *"It carries no `authority:`,
deliberately"* is still true and is now the folder's rule rather than a declined question: a rule
answers with `governs:`, and `authority:` beside it is forbidden on any page
([[authority-beside-governs-is-forbidden-on-any-page]],
[[authority-becomes-the-index-and-is-required-outside-rules]]). What is spent is the reason given —
that the shape was *unruled* and that claiming a slug would answer the question by accident. It was
ruled on 2026-08-18 and the field is now forbidden here by the schema, which lists it in neither
block. The clause about `end-of-session-ritual-name` belonging to
[[the-end-of-a-session-is-a-retrospective]] stands untouched.
