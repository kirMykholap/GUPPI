---
title: "The map in the repository's `CLAUDE.md`: the vault, its librarian, the sprint, and the routes"
type: proposal
status: deprecated
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md"]
superseded_by: [[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]
tags: [harness, process, vault]
---

# Designed 2026-08-17, and not built

The decision behind it, with the admission test in the owner's own words, is
[[the-sprint-belongs-in-the-map-and-the-map-has-an-admission-test]]. **`## Where things are` was deleted to
make room for this rather than corrected into it**
([[where-things-are-is-deleted-now-and-generated-later]]).

## What it would hold, and what it deliberately would not

**In**, because a session that does not know it does the work *wrong*:

- **the vault** — what it is, and that it holds the reasons ([[the-vault-is-compiled-not-retrieved]]);
- **its librarian** — that `wiki/` and the registers have exactly one writer
  ([[the-one-writer-rule-covers-the-registers-too]], [[vault-librarian]]);
- **the sprint** — that one is open, and that `sprint.md` is where it lives. Not its contents.
- **the routes** — `/vault-ask`, `/pre-task`, and the by-hand `rg` recipe, which are already in the file
  and are the replacement for the wikilinks it refuses.

**Out**, because not knowing costs seconds: where `src/` is, where the tests are, where the hooks are.

## What it would take

**A page, and a region.** The map's entries come from a judgement rather than from the filesystem, so this
is *not* a generator's output — which is a correction to the grouping the owner used, where the map, `make
help` and a generated `Where things are` were called one mechanism
([[a-generator-fills-a-marked-region-from-the-tree]]).

**And the page cannot be a rule.** It is descriptive, not imperative, so it fails `rules/`'s admission test
([[the-harness-is-compiled-not-maintained]]). **It therefore waits on `governs:` becoming a property of any
page** ([[governs-becomes-a-property-of-any-page]],
[[the-marker-carries-a-type-and-governs-is-read-as-a-field]]).

## What is open

- **Which category the map's page belongs to.** It is a noun with properties, which argues `entities/`; it
  is also a mechanism with a consequence, which argues `concepts/`. Nobody has decided, and the choice sets
  the marker's type word.
- **Whether the routes stay prose or join the region.** They are the one part of the current file that has
  never gone stale.

## What not building it costs

**The file's own first sentence is wrong and was deliberately left wrong**: it says the file *"is a map and
a handful of rules"*, the map was deleted, and nine rules render. Patching that sentence would have been
another line of unsourced prose from the same author, so it stands as a marker of this gap
([[the-repository-claude-md-after-the-rules-left-it]]).

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

# Built at `013a6d0`, and retired on 2026-08-18 by the owner

**The page exists, it carries `governs: CLAUDE.md`, and its region is the first in this project
rendered from a folder other than `wiki/rules/`**
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]). Both open questions were
closed by the owner the same day: the category is **`concepts/`**, and the routes **stay prose**.

**Retired under one policy rather than as a single call**, after checking that nothing on it lives
only here ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]). The admission table,
the *in* and *out* lists and the reason a rule page was never an option are all on the successor;
the correction about the generator's grouping — the map's entries come from a judgement rather than
from the filesystem — is on [[a-generator-fills-a-marked-region-from-the-tree]] as well as here.

**Its last claim went false the moment it was built.** The file's first sentence, left deliberately
wrong as a marker of this gap, becomes true when the region renders; whether it is then reworded is
the owner's and not the librarian's ([[the-repository-claude-md-after-the-rules-left-it]]).

**One thing this page did not predict and the build produced**: the slice restated two claims that
were hand-written prose five lines above it in the destination, so the mechanism that exists to end
duplication produced one on its first use outside `wiki/rules/`
([[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]],
[[the-maps-region-replaces-the-prose-it-duplicated]]).
