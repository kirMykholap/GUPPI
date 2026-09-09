---
title: "A proposal page settles who runs which check and when, and writing it is the next session's first work"
type: decision
status: archived
authority: check-system-proposal-order
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md"]
tags: [testing, harness, process]
---

# The ruling, 2026-08-26, in his own words

> **owner:** «Значит формируем конкретную страницу proposal для того, чтобы разобраться с тестами.
> Как и кто их проводит, когда запускаем и прочее. Это первым делом на следующую сессию»

**One `proposals/` page settles the check system**: who runs which check, when each runs, and what
each is evidence for.

# Why the decisions of this day do not already settle it

**Four rulings landed on 2026-08-26 and each answers one question**: the three names
([[gate-smoke-and-suite-name-different-things-and-gate-keeps-its-meaning]]), that smoke is built
([[the-smoke-runner-is-built-first-thing-next-session]]), that the suite leaves the session loop
([[the-suite-stops-running-every-session]]), and that there is a single entry point
([[the-checks-get-a-single-entry-point-and-make-is-the-revived-candidate]]).

**What none of them answers is the arrangement.** Which check runs at which moment of a session,
which ritual calls it, and what a red result from each one means — that is a design, and a design
that would otherwise survive only in a chat log is what `proposals/` is for.

# It is deliberately not pre-empted here

**The proposal is the next session's work and the librarian does not write it in advance.** What this
ingest preserves instead is the design already stated: the smoke composition and its floor, on
[[the-smoke-runner-is-built-first-thing-next-session]]; the naming, on the page above; and the cost
structure that makes one of the four selftests expensive
([[the-selftest-is-a-mutation-test-of-the-gate]]).

# Rejected

**Rejected: leaving the arrangement as four separate decisions.** He asked for one page, and four
pages answering four questions leave the join between them unwritten.
