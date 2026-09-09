---
title: "A marker is detected loosely and judged strictly, so a typo is wrong rather than invisible"
type: concept
status: current
authority: marker-detection
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-check.sh"]
tags: [harness, testing]
---

# The pattern that matches only the exact form is the wrong pattern

If the scanner recognised **only** `<!-- rule: slug -->`, then `<!--rule: slug-->`,
`<!-- rule:slug -->` and `<!-- rule: slug--->` would each match nothing at all. The file would
report **no region**, not a broken one — and no region is an advisory, which nobody acts on
([[a-governed-file-with-no-region-is-an-advisory]]).

**A typo would be invisible rather than wrong.** The author would see a green run and believe the
region was being rendered; the injector would write nothing into it, forever.

So the scanner takes anything that **looks like** a marker — the loose net — and then judges it
against the exact form. What is not exactly the form is named **malformed**, by name and by line.

## Why this generalises

It is the same asymmetry as reading versus writing a path
([[governs-is-a-path-from-the-repository-root]]): **a detector should be generous and a judge
should not.** Narrowing the detector to the thing you want moves every near-miss out of the report
and into silence, and silence is indistinguishable from correctness.

This store has met the inverse mistake too — a rule tightened until it rejected legal input, which
was worse than the defect it fixed ([[vault-scripts]], on the verdict grammar). The two failures
are the same knob turned opposite ways: **the question is always which side of the boundary the
loud answer is on.**

# The net widened on 2026-08-18 and the judge did not

**Detection now takes anything shaped like `<!-- word: … -->`** — including a capitalised word and a
word this vault has never heard of — and only then asks whether the word names a type this vault
has. The scanner's net used to be the literal string `rule`.

**Narrowing the net to the known words instead would have moved every typo in the *type* word into
silence**, which is the same failure this page was written about one field earlier: a
`<!-- concpet: x -->` would report *no region* rather than a broken one, and no region is an
advisory nobody acts on ([[a-governed-file-with-no-region-is-an-advisory]]).

**The judge is where the type is checked, and legality is derived rather than listed**: a word is
legal because its folder exists, which rule 1 already sweeps
([[the-type-words-are-swept-off-the-tree-and-never-listed]],
[[a-marker-with-its-type-is-a-complete-address]]).

**One designed verdict was dropped here rather than added.** *A marker whose type disagrees with its
page's `type:`* cannot fire, because the type picks the folder and rule 2 enforces the folder; what
replaced it names the folder a slug is actually in
([[the-unreachable-verdict-is-dropped-and-replaced]],
[[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).
