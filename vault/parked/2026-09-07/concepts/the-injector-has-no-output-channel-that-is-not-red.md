---
title: "The injector has no output channel that is not red"
type: concept
status: current
authority: injector-output-severity
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, vault, record-schema]
---

# The mechanism, at both ends

**At the injector's end:** its only output channel is `say()`, which raises `problems` and forces
exit 1. There is no second function that prints without failing.

**At the gate's end:** rule 12 reads **every** `vault-inject: ` line into `note()`, and anything it
does not recognise into a *said something rule 12 does not understand* verdict — **also red**
([[a-check-asks-by-running-the-writer-it-checks]],
[[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]]).

**So the injector cannot say anything today that is not a failure.**

# What that decides, and it decides it cheaply

**An advisory from the injector is not a wording choice, it is a second ruling.** Making one would
mean opening rule 12's `case` statement and deciding which verdicts are advisory there — a change to
the gate's severity model, not to a message ([[severity-in-the-gate-is-decidable-which-is-what-lets-a-flag-be-safe]]).

**That is why *absent `render:` is red* was the cheap answer and *advisory* was not**
([[an-absent-render-is-red-on-a-page-that-renders]]). The alternative that costs nothing —
saying nothing at all — is forbidden outright
([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).

# The shape to notice

**A tool with one severity makes every future verdict a red one by default**, and the cost of the
missing channel is paid at the moment somebody wants to warn rather than refuse. The gate itself
already paid this and split its own channel behind a flag
([[the-tag-density-advisories-move-behind-lint]]); the injector has not.
