---
title: "A generator fills a marked region from the tree rather than from a page, and the wants it serves are named rather than counted"
type: proposal
status: current
authority: tree-sourced-region
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-inject.sh"]
decided_by: [[where-things-are-is-deleted-now-and-generated-later]]
tags: [harness, process, vault]
---

# Designed 2026-08-17, and it is one mechanism behind three separate wants

**The injector fills a region from a vault page. This fills a region from the tree.** Same markers, same
gate, a different source of truth — because some of what a harness file should say is a fact about the
repository rather than a claim somebody decided.

**Three things are waiting on it, and the owner's *dropped now, generated later* is waiting on exactly
this:**

| Consumer | What the region would hold |
|---|---|
| `## Where things are` | the layout, read off the tree ([[where-things-are-is-deleted-now-and-generated-later]]) |
| `## Commands` / `make help` | the pipelines, read off the `Makefile` ([[a-makefile-holds-the-projects-pipelines]]) |
| the map | the entities a session must know — read off nothing, so **this one is a page after all** ([[the-map-in-claude-md-and-its-admission-test]]) |

**Building it once serves the first two.** The third is included in the owner's grouping and is not
actually of the same kind: the map's entries come from a judgement, not from the filesystem. That
distinction is worth keeping in view before the work starts, because a generator that has to be told what
to say is not a generator.

## What it would take

- **A generator per region**, keyed by the region's slug, run before the gate the way `vault-inject.sh` is;
- **the gate's comparison unchanged** — rule 12 already asks by running the writer, so it works for any
  writer ([[a-check-asks-by-running-the-writer-it-checks]]);
- **input from a file, never from a command argument** ([[prose-does-not-survive-a-shell-command-string]]);
- selftest cases: the region regenerates identically over an unchanged tree, and reddens over a changed one.

## What is open

- **Where the generators live**, and whether they are one script with a dispatch or one per region.
- **Whether a generated region and a page-rendered region are distinguishable in the marker.** They must be,
  or a reader cannot tell which correction to make — edit the page, or change the tree. The `[type]:`
  design gives a natural answer only if `generated` becomes a pseudo-type, which the closed six-type set
  forbids ([[the-marker-carries-a-type-and-governs-is-read-as-a-field]]).
- **Whether the injector and the generators are one pass.** They should be, on the cost measured today
  ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

## What not building it costs

**`## Commands` is drifting now**, and it drifted inside the session that changed what it describes: it
claims `vault-check.sh` takes `~2 s`, measured at `4.9 s`
([[the-repository-claude-md-after-the-rules-left-it]]). **The layout block is already deleted rather than
corrected**, so a session finds `src/` by looking until this exists.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).
