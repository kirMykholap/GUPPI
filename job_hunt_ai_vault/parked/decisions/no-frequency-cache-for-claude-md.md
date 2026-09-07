---
title: "No frequency cache for `CLAUDE.md`, and the statistics are collected before adoption is considered"
type: decision
status: current
authority: rule-frequency-cache
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md"]
tags: [harness, process, agents]
---

# Refused now, and the data is collected anyway — owner, 2026-08-18

The idea: keep the most-asked rules in `CLAUDE.md` and let the rest be fetched, with a counter
deciding which is which. **owner: collect the statistics, consider adoption when it makes sense.**
Collection is approved; adoption is not.

**Three grounds, and each is enough on its own:**

- **The counter starves what it caches.** A rule sitting in `CLAUDE.md` is never asked about,
  because it is already there — so its frequency reads as zero, it is evicted, it starts being
  asked about, and it comes back. A cache whose input is suppressed by its own output oscillates.
- **Frequency evicts exactly the wrong rules.** The rules whose failure is rare and catastrophic are
  the rarely-asked ones; the test-database rule is asked about approximately never
  ([[the-suite-never-runs-against-the-production-database]]).
- **It would make `CLAUDE.md` non-deterministic** — two clones of the same repository would instruct
  their sessions differently, which is the property this project has been building the opposite of
  ([[the-harness-is-compiled-not-maintained]]).

## The open design point, recorded so it is not derived again

**What counts as "asked"**, given that a rule already in `CLAUDE.md` is never asked about. Any
collection design has to answer that before its numbers mean anything, and it is the same shape as
the criterion above rather than an implementation detail.

**The criterion that decides membership today is not frequency at all** — it is what bootstraps the
asking and what is irreversible if missed
([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]]).
