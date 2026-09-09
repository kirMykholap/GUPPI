---
title: "A denominator is walked off the input list, never off what the scanner managed to read"
type: concept
status: current
authority: coverage-denominator-source
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-check.sh"]
tags: [harness, testing]
---

# The bug that was avoided, and it is worth stating as a rule

Rule 11 reports **`N of M` harness markdown files covered**. `M` is walked off `ARGV` — the list
awk was **handed** — and not off the set of files awk actually entered.

**Awk runs no rule at all for a 0-byte file.** A governed file that is empty produces no records,
so a denominator built from `FILENAME` as the scan proceeds would never have seen it. The file
would drop out of the bottom of the fraction and the number would read **better than the tree is**.

And an empty harness file is precisely the case this rule most wants counted: a skill file that
exists and says nothing is the strongest possible instance of *the harness carries no rule here*.

## The general form

**The denominator must come from a source that does not depend on the work succeeding.** If the
same pass both enumerates the subjects and processes them, every subject that fails to be processed
also fails to be counted, and the score rises as the failures do.

This store has the same rule written from the other end: the ingest's completeness works **only
because the denominator is produced by a separate script**, `vault-units.sh`, rather than by the
party accounting for the units ([[ingest-is-units-and-verdicts]], [[the-verdict-is-the-write]]). A
party that both lists and answers can simply never list what it cannot answer.

The failure it prevents has happened here: an instrument reporting a clean result over a set it had
silently shrunk ([[an-instrument-that-contains-its-own-answers-can-be-gamed]],
[[a-test-green-under-any-implementation]]).
