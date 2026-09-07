---
title: "A path move rewrites `archive/` and never `log.md`"
type: decision
status: archived
authority: path-rewrite-reach
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-archive.sh"]
tags: [vault, process, harness]
---

# Decided 2026-08-20 by the owner, and both halves follow one predicate

**`archive/` IS rewritten.** The predicate is the vault's own: what a page **asserts** is frozen,
how it is **found** is live, and a `sources:` line is an address rather than a claim
([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]). This closes the question
[[emptying-raw-by-a-script-that-moves-and-rewrites-its-citations]] named as open.

**`log.md` is NEVER rewritten, at all.**

> «Лог — это то, что было и как это записали. Мы могли неправильно записать, окей, бывает.»

**Rejected: correcting a log entry in place**, which destroys the evidence that the process
produced a wrong entry. It follows the wider principle the owner stated the same day
([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).

## The log is different in kind, not merely out of reach

Until this ruling, `log.md` was outside a rewrite because the gate's link rules do not read it
([[log-md-is-outside-the-link-set-the-check-reads]]) — a mechanical accident that had been paid
for by hand sweeps at every rename ([[a-page-rename-is-sed-and-verify]]). Now it is outside by
decision: **the old paths in `log.md` are correct as written rather than stale.**

## Measured the same day, and it is why `archive/` had to be settled

The probe scaffolding was cited by **nine** pages, not seven: seven `sources:` lines in `wiki/`
plus two in `archive/`. **Rule 2 of the gate reads `wiki/` only, so the archived two never redden
— they dangle silently.** An archived citation is therefore not self-correcting, which is the
practical half of the argument for rewriting it.
