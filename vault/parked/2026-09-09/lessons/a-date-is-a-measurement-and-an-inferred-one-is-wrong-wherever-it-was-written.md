---
title: "A date is a measurement, and an inferred one is wrong in every place the session wrote it"
type: lesson
status: current
authority: date-measurement
basis: measurement
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "job_hunt_ai_vault/log.md", "job_hunt_ai_vault/sprint.md"]
tags: [process, vault, harness]
---

# The incident, 2026-08-23

**A session inferred today's date from the previous session's date and was wrong by a day for its
whole length.** The previous session was the **first** of 2026-08-23; this was the second. It
believed it was 2026-08-24 and wrote that everywhere.

**Nothing was consulted.** Not the clock, not `git log`, not the brief's own `# Brief — 2026-08-23`
heading, which was open in front of it.

# Where it landed, counted at the retro

Forty-four places, and the spread is the point rather than the total: nine schema comments, three
script comment blocks, four feedback lines, seven lines of `sprint.md`, seven of `log.md`, two
registers, three `decisions/` pages, and a `decided:` frontmatter field.

**One of them cannot be repaired.** The message of commit `ad839d4` says the ingest was *committed
a day late*, and git history is not rewritten here.

# Three of them were not dates and a grep for the digits would have missed them

**They were intervals computed from the wrong date**: *one day old*, *the day-old page*, and a
citation that after repair would have read as a page rejecting its own ruling. **So the corpus would
have been left asserting things no line said**, with every date string correct.

**That is the generalisable half of the repair.** A wrong date propagates into arithmetic, and the
arithmetic keeps the wrong answer after the date is fixed. Repairing one means re-reading every
sentence that *reasons* from a date, not only every sentence that prints one.

# How it was caught, and it is the same shape as the other catches this store has recorded

**A subagent whose environment reported the real date reported the conflict rather than conforming
to the brief it was given.** An agent that had simply obeyed would have written the wrong date into
its own output and confirmed the error. **The instruction that makes this possible is in the
dispatch**: an agent told to read its environment rather than to trust the brief has something to
disagree with.

# The rule

**A date is a measurement and is read, never derived.** This store's own standing rule is that a
count is written with its date or not written at all
([[a-title-names-what-is-counted-instead-of-counting-it]],
[[the-date-of-a-correction-note-is-the-date-the-text-became-false]]) — and the session treated the
one number every record carries as the one number it did not have to measure.

**Two sessions in one day is the case that breaks the inference.** Yesterday's journal plus one is
right most of the time, which is what makes it dangerous: it fails on exactly the days when more
work happened than usual.
