---
title: "An archive path repeats the session slug and reaches the Windows path limit"
type: lesson
status: archived
authority: archive-path-length
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["scripts/vault-archive.sh", "archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md"]
tags: [vault, harness, process]
---

# The incident

**An archived journal's path carries the session slug at two levels** —
`archive/<date>/<slug>/handoffs/<slug>.coverage.tsv` — and with a journal name of 78 characters it
reaches **240 characters** before the working copy's own prefix is added.

**Git refused to index the file: `Filename too long`.** It was unblocked by setting
`core.longpaths true`, which is a per-repository configuration and travels with nothing.

# Why nothing caught it

**Nothing in this project measures a path's length.** The rule that governs names deliberately
leaves length unbounded — but it is a rule about a **title**, and a title is not a path
([[the-length-of-a-title-is-unbounded-and-no-check-measures-it]]).

**The two ends of the growth are independent and both are encouraged.** Descriptive slugs are the
search surface and are meant to be long ([[a-title-names-what-is-counted-instead-of-counting-it]]);
the archive layout repeats the slug so that a directory is self-describing
([[vault-archive-sh]]). Neither side is wrong on its own, and the product of them is what fails.

# What follows

**A long journal name is the input a session controls, and it is the cheap end to hold.** `/handoff`
picks the filename, so a shorter slug there is free, while changing the archive layout moves every
path already written.

**`core.longpaths true` is the local repair and not a fix.** It is set in this clone; a fresh clone on
Windows meets the same wall, and nothing announces it.
