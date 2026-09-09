---
title: "A replaced shape reads as no replacement when only the shape moved"
type: lesson
status: archived
authority: shape-substitution
basis: human
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md"]
tags: [process, agents, harness]
---

# The incident

**The owner chose the filename verdict's output from a multi-line preview and received a single
comma-run.** The house style of the two advisories beside it won, silently. Nobody decided to
override him; the shipped form simply matched the neighbours
([[the-filename-advisory-prints-one-name-per-line]]).

**Neither a question nor a notification happened**, and both were owed: replacing an approved shape
is a question ([[narrowing-a-scope-notifies-and-widening-it-asks]]). It was confessed unprompted at
the retrospective and corrected the same session.

# Why this substitution is harder to see than the others

**The content was identical.** Every name the owner approved was in the output, spelled the same
way, in the same order. What changed was the arrangement — and an approval is normally checked by
looking for the content.

**So the diff a reviewer runs does not fire.** A dropped item is missing, a renamed thing is
misspelled, but a reflowed list looks like the thing that was approved with the formatting settled
later. **That is how a substitution passes for no substitution.**

# The general rule

**Shape is content when it was shown.** A preview shown and chosen from is an approved artefact,
including its arrangement; anything the implementation changes about it is a replacement and asks.

**The house style is the likeliest thief.** It applies itself with no author and no announcement,
which is precisely why it produces changes nobody made
([[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]]). In this instance the arrangement
was load-bearing twice over — it is what keeps the advisory count honest, and a selftest case greps
it ([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]).
