---
title: "A gate guarantees agreement, never truth, and it was demonstrated live the day it was designed"
type: lesson
status: archived
authority: gate-guarantee
basis: human
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
tags: [harness, testing]
---

# The demonstration, on the day and inside the design

A rule text drafted during the session that designed the harness said **`/ingest` runs at the
retrospective**. It was wrong; the owner caught it **by reading**.

**A wrong rule renders into the harness flawlessly.** Every mechanism designed that day would have
passed it: the region matches the page, the page exists, the slug resolves, the gate is green, and
the harness now states something false in more places than before, with a build system guaranteeing
the copies agree.

## What the two mechanisms actually promise

| | what it guarantees |
|---|---|
| a marked region | the harness file **says what the page says** |
| `asserts:` | the tree **is shaped as the rule claims** |
| neither | that the page is **right** |

**Nothing in the design defends against an error of content; only reading does.** This belongs
written beside the design, because otherwise the mechanism reads as stronger than it is — and the
whole complaint the structure exists to answer is *documents that cannot be read are therefore
trusted* ([[the-unreadable-mass-is-in-the-plans-not-the-vault]]).

## Why this is a lesson rather than a caveat

The same distinction has been drawn here before with the same words in a different place: a
coverage verdict of `page:X` asserts that X exists, never that X is true
([[the-verdict-is-the-write]], [[ingest-is-units-and-verdicts]]), and a check can pass for the wrong
reason ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). **A gate is an
agreement-preserver, and this project keeps having to re-learn that agreement is not correctness.**

The consequence for the build: the harness gate does not retire the semantic pass. `/vault-lint`
and a human reading stay the only instruments aimed at content
([[lint-waits-for-an-open-sprint]], [[the-harness-is-built-by-a-script-and-guarded-by-a-gate]]).

## It was built on 2026-08-17, and the sentence went into the mechanism's own description

The gate exists: rule 11 reads the regions, rule 12 asks whether each agrees with its page **by
running the injector** ([[a-check-asks-by-running-the-writer-it-checks]]), and
`scripts/vault-inject.sh` makes the copies agree.

**Nothing about that makes anything true.** A rule page that is wrong renders flawlessly, byte for
byte, into every file it governs, and every check in this repository stays green. The session that
built it wrote the sentence into the journal unprompted, which is the only evidence available that
the caveat survived the build.

`/vault-lint` and a human reading remain the only instruments aimed at content
([[lint-waits-for-an-open-sprint]]). **The gate multiplies whatever the page says**, which is the
argument for the mechanism and the reason to read the page.

## And on 2026-08-18 it turned out not to be delivering the agreement either

**This page is about the ceiling: agreement is not truth.** A narrower and worse failure was
measured under it — **the comparison that claimed byte equality did not have it**, because both
sides arrived through `$( )` and the shell stripped the difference before either was read. A blank
line hand-added inside any of the ten regions passed the gate, exit 0
([[a-command-substitution-strips-the-newline-a-gate-compares]]).

**Fixed at `97895a9`.** It is worth keeping the two apart: *a gate cannot promise correctness* is a
caveat about a working mechanism, and *a gate did not do what it promised* is a defect. Reading the
first as covering the second is how a known limitation absorbs an unknown fault.

**What the guarantee is worth turns on who is being checked**, and here that is more parties than
the store's one writer: a journal the session wrote, regions the injector wrote, the repository's
`CLAUDE.md` and the per-folder schemas
([[the-gate-judges-more-writers-than-the-librarian]]).
