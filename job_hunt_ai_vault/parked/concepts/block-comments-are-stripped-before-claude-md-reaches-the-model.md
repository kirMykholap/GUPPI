---
title: "Block-level HTML comments are stripped from `CLAUDE.md` before it reaches the model, and the blank line between adjacent regions goes with them"
type: concept
status: current
authority: marker-context-cost
basis: measurement
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "CLAUDE.md"]
tags: [harness, agents, vault]
---

# Measured 2026-08-18, on this session's own injected copy

**The markers cost nothing in context.** In the repository's `CLAUDE.md` they are **1354 of 7213
bytes on disk** and **none** of what the model is given: block-level HTML comments are removed
before the file arrives.

**This is the first evidence anywhere that the marker design is free to read**, and it arrived after
the design was chosen. The mechanism was argued and built on other grounds entirely — a region has
to be addressable, and the address has to be visible in the file
([[a-region-is-a-paired-comment-named-for-a-rule]], [[a-marker-with-its-type-is-a-complete-address]])
— so this measurement retires an objection nobody had costed rather than confirming a prediction.

## The consequence that changed a design decision the same day

**The blank line between two adjacent regions is stripped along with the markers.** Observed in the
injected copy, documented nowhere. So two regions separated only by whitespace *outside* their
markers arrive as one paragraph, and the whitespace that was supposed to separate them is skeleton
rather than content.

**That is why the separator lives inside the region**, where it survives
([[the-injector-writes-the-separator-inside-the-region]]). The alternative placements were all
priced against this fact rather than against taste.

## What is still unmeasured, and it is the half the change was for

**Whether the in-region blank line itself survives is not known.** It cannot be read from the
session that writes it — that context was built before the edit — and the next session's first
minute closes it by comparing its injected `CLAUDE.md` against the file on disk. **If the break is
missing there too, the stripping eats an in-region blank line as well** and only a visible character
would work.

**A measurement that agrees with no expectation is exactly where a second instrument is owed**
([[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]); here the second
instrument is the next session, and it is booked.

## Read this beside what a subagent is handed

The file a subagent receives is the one that existed when the **parent** session started, not the
one on disk ([[claude-code-config-loading]]). So a measurement of what the model reads is a
measurement of a particular session's copy, and the sentence above says which one.
