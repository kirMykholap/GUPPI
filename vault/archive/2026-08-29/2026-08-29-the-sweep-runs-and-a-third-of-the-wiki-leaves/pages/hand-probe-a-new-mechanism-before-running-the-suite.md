---
title: "Hand-probe a new mechanism before running the suite on it"
type: lesson
status: archived
authority: hand-probe-before-suite
basis: measurement
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-inject.sh", "scripts/vault-check-selftest.sh", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [testing, process]
---

# The incident, and the arithmetic under it

**Nine failure paths of `scripts/vault-inject.sh` were exercised against an isolated vault in about
a minute** — by hand, one command each, before a single selftest case was written for them.

The comparison that justifies it happened the same morning: **the first selftest run of the day
cost five minutes to report a single failure that had nothing to do with the change under test.**
The suite is ~200 s per run and the wrappers couple cases to each other
([[a-rule-over-every-page-makes-every-test-fragile]]), so a run does not tell you about your change
— it tells you about the tree.

And the probe found its own defect first: **a wrongly-written probe was caught in seconds rather
than in a seven-minute run.**

## Why this is not "write fewer tests"

The selftest cases were written afterwards, all of them. What the hand probe buys is **the order**:
the mechanism is known to work on its nine paths before the expensive instrument is pointed at it,
so any red the suite then shows is about the suite or the tree, and the ambiguity that costs the
five minutes never arises.

It is the same move as putting a known-good subject through a new instrument before trusting its
silence ([[a-known-good-component-locates-the-fault-in-the-harness]],
[[a-test-that-fails-for-its-own-reasons-proves-nothing]]) — from the other end: here the instrument
is known good and the **subject** is what gets established first.

**The cost is a minute and the thing it buys is attribution.**

## It paid again on 2026-08-17, and this time it found something no test could

**Four states were measured in seconds against an eight-minute run**, and the same habit found the
injector's fenced-block defect: a slice of three lines rendered as one, with `1 region(s) rewritten,
0 problem(s)` printed ([[the-injector-drops-a-fenced-block-inside-a-slice]]).

**No existing test would have caught it, and no test could have**, because **no rule ships a code block
yet** — the case does not exist in the corpus, so the suite had nothing to be wrong about. That is the
sharper version of this lesson: a hand probe explores states the corpus has not reached, and a suite over
the corpus cannot.

**The arithmetic moved against the suite, too.** It now costs **8m04s**, so the ratio the page argues from
is worse than when it was written ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

## It paid twice in one session — 2026-08-23, and the arithmetic is now thirty minutes against seconds

**The first probe of the schema changes planted new pages and failed on three unrelated things at
once**: the tag count, orphanhood, and an `authority:` slug that was in no family. None of those was
what the probe was about.

**Two of its apparently passing red cases could have been passing for those reasons.** A case that
plants a defect and reads a red gate cannot tell which red it read, and three spare defects were
sitting in the fixture ([[a-case-that-fails-for-its-own-reason-tests-nothing-either]],
[[a-clean-case-built-on-a-helper-that-plants-a-red-tree-can-never-be-green]]).

**Rebuilt to mutate real pages instead of planting new ones**, which removes every one of those
three failure modes at a stroke: a real page already has its tags, its inbound links and its
registered slug ([[a-tree-broken-for-a-real-reason-is-a-better-fixture-than-a-planted-offender]]).

**Each proof cost seconds. The suite costs about thirty minutes** on the corpus as it stood that day
([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]). The ratio is what
makes this a habit rather than a preference, and it has grown by an order of magnitude since this
page was written.
