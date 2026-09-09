---
title: "`pages.base` — the list of every page, held as a query instead of as rows"
type: entity
status: current
authority: page-list-artefact
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "pages.base", "scripts/vault-catalogue.sh"]
tags: [vault, retrieval]
---

# What it is

**Appeared 2026-08-17**, at the vault root, replacing `catalogue.md`
([[the-page-list-is-a-query-not-a-generated-file]]). It is an **Obsidian base**: five views over
`wiki/`, filtering and grouping by `type`, `status`, `sprint`, `tags`, `authority` and `governs`.

The Bases core plugin was already enabled in this vault — `"bases": true` — so nothing had to be
installed for it to work.

**A base is evaluated when it is opened.** There is no generated copy, nothing to regenerate, no
staleness rule and nothing to diff. A page that exists is in the list the moment it exists.

## Only one reader of this repository can read it

Obsidian renders it; every agent here sees a small YAML file that answers nothing. That asymmetry
is why `scripts/vault-catalogue.sh` survives the file it used to write: it prints the same list to
a terminal, and it is how the librarian, a reviewer and any subagent get the whole list
([[vault-scripts]]).

## The syntax was confirmed by the editor, not by a document

**Obsidian normalised the file on first open** and added `sort` and `columnSize` keys of its own.
That is how two mistakes in the first draft were found: **filters must be an object carrying one of
`and` / `or` / `not`**, and **note properties are written bare** rather than namespaced. The draft
was wrong on both counts and the editor said so by rewriting it.

## Its line endings are deliberately unpinned

Git warned *"LF will be replaced by CRLF"* on the first `git add`, because `.gitattributes` says
nothing about `*.base`. **It is left that way on purpose**: a file class earns its pin after it has
cost something ([[a-file-class-is-pinned-after-it-costs-something]]), and this one has cost nothing
— Obsidian reads either ending and no script reads the file at all. Recorded so the next reader
meets the warning already explained instead of cold.

## What it does not do

It is **not** an entry point for a topic query. Retrieval here is still `ripgrep` first and the
wikilinks out of whatever it finds ([[the-index-is-a-map-not-a-catalogue]]); this answers the one
question grep cannot, which is *what is there at all*.

It also cannot rescue an orphan, and for a new reason rather than by a rule: the danger that made
`catalogue.md` stay out of the link register was that it linked to every page in `wiki/` and would
have left rule 5 running, passing and proving nothing. **A base holds no wikilinks**, so there is
nothing for the orphan rule to be fooled by.

## It stopped being a review item on 2026-08-17

**Unchanged in kind, changed in standing.** The owner decided that a session commits it without
discussion and never treats a change to it as something to explain
([[pages-base-is-not-a-review-item]]). It stays tracked in git.

**The change was earned by two false alarms in one day.** Obsidian rewrote the `harness` view's state
while the librarian was writing pages beside it — a `type == "rule"` filter, two extra columns and a
`file.name` sort — and the librarian correctly declined to revert somebody else's edit and then reported
it as an alarm twice ([[staging-by-wildcard-sweeps-the-other-partys-edit]]).

**So a dirty `pages.base` is no longer evidence of anything**, and that is the whole content of the
change: the file is the owner's editor writing the owner's file.

# The `Every page` view showed one folder of six, and the owner rewrote it — 2026-08-30

**The view named `Every page` was filtered to `wiki/decisions`.** A name that promises the whole store
over a filter that selects a sixth of it is the shape a reader trusts and should not: found while
checking the claim that this base replaces the catalogue, and it does not while a view lies about its
own scope.

**The owner edited the file during the session.** `Every page` now filters `wiki/rules`, sorts by
`authority` and shows a `governs` column — **an editing view for the family work rather than a
catalogue**, and it is in the commit as his.

**Nothing about that is an alarm**, by the ruling above: the file is his and a session commits it
without discussion.

**What the incident leaves standing is that a view's name is not a check.** No instrument compares a
view's title against its filter, and the only reader that can see either is Obsidian. **An agent still
runs `bash scripts/vault-catalogue.sh`**, which since 2026-08-30 prints the six live folders and no
archive — 131,604 bytes against 201,927 ([[vault-scripts]]).

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
