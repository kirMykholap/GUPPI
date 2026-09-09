---
title: "A `[[wikilink]]` inside a rendered slice is red rather than an advisory"
type: decision
status: archived
authority: wikilink-in-slice
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-inject.sh"]
tags: [harness, vault, testing]
---

# Decided by the owner on 2026-08-18: red

**It was already his stated rule and nothing held it.** The 2026-08-17 brief raised it as the one
thing owed a verdict, after measuring that sixteen `current` pages cited a page archived that day
and six of them were rule pages — none of whose citations travelled, because no wikilink sat inside
any `<!-- text -->` slice. That was luck rather than a mechanism.

**It holds now, in `slice_of`, at `e83ce28`.** Rejected: an advisory, which would leave the author
of the first offending slice with a green run and a dead link in a file that cannot resolve one.

## Where the question is asked, and why not everywhere

**Outside fences and outside code spans**, like every other content rule in that script. A slice
that *documents* the form — this corpus writes about its own markup constantly — is describing a
link rather than shipping one, and a rule that could not tell the two apart would make the vault
unable to write about itself ([[an-example-inside-a-code-block-satisfies-a-search]]).

## The stated ground is conditional and the rule is not, and that is deliberate

The reason given is that **Obsidian syntax is inert at the destination**: a rendered `[[link]]`
arrives in a plain file as punctuation pointing nowhere. That ground holds only while the
destination is outside the vault. **Nothing governs a file inside the vault today**, so the
unconditional red is correct now — and the day something does, this is the page to re-read rather
than the script. The same conditional already has a selftest case waiting to look like a bug when
it fires ([[governs-is-a-path-from-the-repository-root]]).

## What it obliges on any page that carries a slice

**Every citation goes outside the slice.** A page whose argument needs its links puts them in the
prose around the marked text, which is where the rest of a rule page's substance already lives
([[what-travels-from-a-rule-page-is-a-marked-slice]],
[[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]).

**The mirror verdict landed with it**: a slice on a page carrying no `governs:` is red too
([[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]).
