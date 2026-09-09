---
title: "A date typed into a docstring is a measurement, and it goes wrong silently"
type: lesson
status: current
authority: hand-typed-date
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "scripts/lessons-queue.py"]
tags: [process, testing, harness]
---

# The incident, 2026-08-26

**`2024-08-24` was typed where `2026-08-24` was meant**, into the docstring of
`scripts/lessons-queue.py`. It was caught only by re-reading the edit.

# Why nothing else would have caught it

**A date in prose has no reader.** Nothing parses it, nothing compares it against the commit that
carries it, and it is syntactically perfect — so no linter, no test and no gate has an opinion.

**And it reads as authoritative.** A dated line is the store's own device for saying *this was true
then*; a wrong date makes a correct statement point at the wrong day, which is worse than an undated
one ([[the-region-coverage-figure-is-dated-where-it-stands]]).

**The two-year error is the lucky case.** A one-day error would have survived the re-reading.

# What follows

**A date written by hand is a number written by hand**, and this store's standing rule about numbers
applies to it: name what is counted rather than counting it, and where a number must be written, take
it from the thing that knows ([[a-title-names-what-is-counted-instead-of-counting-it]],
[[a-stated-count-drifts-from-the-list-it-heads]]).

**Read back an edit that carries a date.** That is what caught this one and it is the only instrument
there is.
