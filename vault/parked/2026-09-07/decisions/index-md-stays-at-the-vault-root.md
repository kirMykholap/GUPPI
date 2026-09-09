---
title: "index.md stays at the vault root, because it is a part for the agent and not the knowledge base itself"
type: decision
status: current
authority: index-location
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-15
created: 2026-08-15
sources: ["raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md", "scripts/vault-check.sh"]
tags: [vault, retrieval]
---

# Where the map lives

**Decided by the owner on 2026-08-15.** Both of his 2026-08-13 notes ask for `wiki/index.md`; the
file has always sat at the vault root, beside `tags.md`, `sprint.md` and `log.md`, and from today
that is a decision rather than a divergence
([[the-owners-instructions-note-and-what-was-built-from-it]],
[[the-owners-method-note-and-what-was-built-from-it]]).

**His reason, in his words: it is a part for the agent, not the knowledge base itself.**
`wiki/` holds pages — things somebody compiled from a source, each with frontmatter, a category
and a `sources:` line. `index.md` is none of those. It is a map *of* the pages, and it belongs
with the other files that are about the store rather than in it.

**Rejected: `wiki/index.md`.** A map filed among the pages would be a page by every mechanical
test the store applies — and would fail all of them: no `type:` that agrees with a folder, no
`basis`, no tags, a link to everything it names. Rule 2 would have to gain an exception, and an
exception in a structural check is where the next silent pass comes from
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

## The line this draws, and the three files on the same side of it

| At the vault root | Under `wiki/` |
|---|---|
| `index.md` — the map: categories, naming, the current sprint, hub pages | pages, and only pages |
| `tags.md` — the dictionary and its aliases | |
| `sprint.md` — the goal and its acceptance criteria | |
| `log.md` — what the librarian did | |
| `catalogue.md` — generated, every page in one table ([[the-catalogue-is-generated-not-maintained]]) | |
| `CLAUDE.md` — the schema | |
| `brief.md` — derived, never a source | |

Two of those are already load-bearing at that path: rule 1 of `vault-check.sh` fails if
`index.md`, `tags.md`, `log.md` or `CLAUDE.md` is missing from the root, and the link register
rule 5 reads for reachability is exactly `index.md`, `tags.md` and `sprint.md` — an allowlist
([[vault-scripts]]).

## What it does not decide

**What `index.md` contains** is a different question and a different page:
[[the-index-is-a-map-not-a-catalogue]]. The note's phrase «автоматически обновляемый каталог всех
страниц» asked for two things at once — a location and a shape — and they were settled separately,
on the same day, for different reasons.

## One row of that table is stale — 2026-08-17

**`catalogue.md` no longer exists.** Its row is left in place because the table is about *what sits
at the vault root and why*, and the file did sit there from 2026-08-15 to 2026-08-17. What occupies
that slot now is **`pages.base`**, at the same path, for the same reason, and it changes nothing
about this page's line: it is not a page under `wiki/` ([[pages-base]],
[[the-page-list-is-a-query-not-a-generated-file]]).

The link register rule 5 reads is unchanged — `index.md`, `tags.md`, `sprint.md` — and the reason
the old file was kept out of it has dissolved rather than moved: a base holds no wikilinks, so
there is nothing for the orphan rule to be fooled by.
