---
title: "The injector removes a region whose rule folded into a page that renders nowhere"
type: proposal
status: current
authority: injector-orphan-region-removal
basis: code
sprint: S3
created: 2026-08-26
sources: ["scripts/vault-inject.sh", "scripts/vault-check.sh", "CLAUDE.md"]
tags: [harness, vault, record-schema]
---

# The hole, read off the script

**`scripts/vault-inject.sh` removes a generated file only under `render: whole`.** Its removal branch
is guarded by `[ "$render" = "whole" ]`, and under `region` a retired rule is handled by `continue` —
the page is skipped and nothing is written.

**The comment beside it states the assumption that makes the skip sufficient**: under `region` the
successor rewrites the same region, so the retired text is overwritten. **That holds only while there
is a successor and the successor renders.**

**When a rule FOLDS into a page that renders nowhere, neither is true.** The successor is an ordinary
`decisions/` or `concepts/` page carrying the text as prose; it has no `governs:`, so it renders
nothing, and the region in the destination is never rewritten by anything.

**And the retired page is not even reached.** The injector's walk is
`find "$VAULT/wiki" … | xargs grep -l '^governs:'`, so a page that has lost the field is never
opened. A fold removes `governs:` in the same edit that deprecates the page, which means the removal
branch could not fire even if it were widened to `region` — **the page has already left the
population the branch is written over.**

# How it was found, 2026-08-26

**[[our-javascript-does-not-choose-which-rows-are-on-screen]] folded into [[javascript-policy]]** on
the owner's ruling ([[the-javascript-rule-becomes-a-decision-and-leaves-wiki-rules]]). The rule page
was deprecated, lost `governs:` and `render:`, and moved to `archive/`.

**`bash scripts/vault-inject.sh` then reported *0 region(s) rewritten, 0 file(s) generated, 0 removed,
0 problem(s)*, and the paired comment was still at `CLAUDE.md:102`.** The orphaned region was caught
by rule 11 of the gate — *the region resolves to …, which does not exist; a region with no page
behind it renders nothing* ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]) —
and **cut by hand.**

**The observation itself is already recorded** on
[[a-deprecated-rule-does-not-render]] and [[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]].
**This page is the design those two do not carry.**

# What it would take, and the three shapes are not equivalent

| shape | what it changes | what it costs |
|---|---|---|
| **A. a sweep in the injector** | after the page walk, sweep every governed destination for regions whose slug resolves to no live page, and cut them | a second reader of the governed set, in the script that already refuses to hold one |
| **B. `governs:` survives the retirement** | a folding rule keeps `governs:` and `render:` until its region is gone, so the existing branch reaches it and is widened to `region` | a `deprecated` page carrying `governs:` is a state the schema permits and nothing tests |
| **C. a workflow rule and no code** | the session that folds a rule removes the region in the same change, and the gate's red is the reminder | nothing to build; the failure stays live between the fold and the edit |

**Shape A is the one that fits the mechanism and is the one that costs the most.** The injector walks
**pages to files** and the gate walks **files to pages**, and that split is deliberate: content
belongs to the writer and address belongs to the sweep
([[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]]). A sweep in the injector
gives it a second copy of the governed set, which is the thing that already went wrong once
([[a-copied-list-drifts-and-a-sweep-cannot]]).

**There is a precedent for A and it names its own residual.** The `whole` mode already sweeps — but
only the directories that live `whole`-mode pages generate into, and the script says outright that a
directory losing its last such page stops being swept. **The `region` case has no equivalent anchor
at all**, because a region's destination is a file with a life of its own and no directory is "the
injector's".

**Shape B is the cheapest and the least honest.** It leaves a `deprecated` page carrying `governs:`
inside `archive/`, which nothing in this store checks, sweeps or reads — and it puts the page in a
state no schema forbids and no case exercises, which is how `quantity:` got in
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).

**Shape C is what happened this time**, and it is what is in force until one of the others is built.

# Why it is not built, and the reason is the loudness

**The failure is caught, named, and points at the exact file and slug.** Rule 11 reddens the gate
with the destination path, the line, and the page it resolved to; `make smoke` runs the gate, and a
red gate blocks nothing but is read at every retro
([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).

**So this is a convenience rather than a correctness hole**, which is the whole reason it waits. The
class of defect that gets built first here is the silent one — the `whole`-mode leftover this hole's
sibling covers is silent, and that is why *it* has code
([[an-instrument-that-fails-towards-nothing-to-do]]).

# What is open

- **whether a fold is common enough to mechanise.** It has happened once. A second occurrence is the
  natural trigger, and this page is what makes the second one recognisable as a repeat
  ([[a-file-class-is-pinned-after-it-costs-something]] is the same admission shape, one subject over);
- **whether shape A can be built without giving the injector a second governed set** — for instance
  by having the gate, which already sweeps the files and already finds these, do the cutting;
- **whether the gate may write at all.** It is a reader today, and rule 12 already runs the injector
  rather than reimplementing it ([[a-check-asks-by-running-the-writer-it-checks]]); a gate that
  removes text is a different kind of thing and nobody has ruled on it.

# What it would oblige

**A selftest case per direction**, because a removal branch that fires on the wrong page deletes text
somebody wrote. The existing `whole`-mode removal has one; this one would need the mirror plus a case
proving a **live** region is left alone.

**And it must not fire on a region whose page is merely absent from the working tree.** A rule page
mid-rename, or a corpus half-checked-out, would look identical to a fold — which is why the trigger
has to be *the page is deprecated or gone AND a live page claims its text*, not *the slug does not
resolve*.
