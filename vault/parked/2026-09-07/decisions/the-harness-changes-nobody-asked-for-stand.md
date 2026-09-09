---
title: "The harness changes nobody asked for stand, and each is recorded as unrequested"
type: decision
status: current
authority: unrequested-harness-change
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/hook-selftest.ps1", ".claude/skills/ingest/SKILL.md"]
tags: [harness, process, testing]
---

# The ruling, 2026-08-26

**Both stand.** *(owner selected it.)*

1. **`scripts/hook-selftest.ps1`'s `RunCatch` delivers its payload through a UTF-8 file instead of a
   pipe.** It was not in the plan; it was forced by finding that the suite could deliver no
   non-ASCII byte to any hook
   ([[the-hook-selftest-could-deliver-no-non-ascii-byte-to-any-hook]]).
2. **A `## From the librarian` section joins the brief's shape** in
   `.claude/skills/ingest/SKILL.md`, generated from `log.md`
   ([[the-librarian-writes-its-log-and-the-brief-carries-what-it-hands-back]]).

# Why it is a decision at all

**A change nobody asked for is not free even when it is right.** It widens what the session's diff
contains, it is not covered by whatever was reviewed, and the party who ratifies it does so after
the fact. **Naming both as unrequested is what makes the ratification a decision rather than a
silence** ([[a-harness-change-is-recorded-when-it-is-decided]]).

**The first one was forced and the second was offered.** The distinction is worth keeping: the
encoding repair was the only way to make a case honest, while the brief section was a design the
session proposed while building something adjacent.

# Rejected

**Rejected: reverting either and re-proposing it.** The encoding repair would have left a selftest
case accusing a correct hook; the brief section is the replacement channel the prohibition on the
librarian writing `.superpowers/sdd/vault-feedback.md` needs in order to be safe to state.
