---
title: "A gap named by a reviewer is closed by a mechanism rather than by care"
type: lesson
status: archived
authority: gap-closed-by-mechanism
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "tests/integration/test_migrations.py"]
tags: [testing, process, harness]
---

# The gap, and the answer that was not given

**The librarian named it at `/pre-task`:** `pytest --collect-only` cannot exercise an assertion
message, so a malformed f-string inside one passes collection, `ruff check` and
`ruff format --check` alike ([[collect-only-cannot-exercise-an-assertion-message]]).

**The available answer was *read it carefully*, and it would have proved nothing.** The change was
59 replacements across a 951-line file; a reader who has just rewritten every message in it is the
worst possible instrument for noticing that one of them is now wrong.

# The mechanism that was built instead

**An `ast` pass, run before and after the change:** every `FormattedValue` expression with its
conversion and format spec, plus every plain string carrying a literal brace, compared as a set.
Line numbers stripped, because they move. **28 interpolations, byte-identical as a set.**

**And the instrument was proved before it was trusted.** A no-op run of the replacement tool over
the file left `git diff` empty — which is what established that reading and rewriting does not
itself convert a `w/crlf` working copy against an `i/lf` index
([[a-planted-offender-is-proved-by-reading-it-back]],
[[line-endings-make-git-status-overstate-what-changed]]).

# The general claim

**A reviewer's finding is a specification for a check, not a request for attention.** Every time
this project has answered a named gap with care, the gap has come back
([[knowing-a-rule-is-not-a-mechanism]], [[a-guard-remembered-per-file-is-forgotten-in-the-next-file]]);
every time it has answered with something that runs, the answer has held.

**The cost is the argument, not the principle.** The `ast` pass is a few lines and one run; it
converts an unfalsifiable claim — *the messages are still correct* — into a set comparison anybody
can repeat ([[the-owners-question-was-how-would-you-check-that]]).

**It is also what a `/pre-task` bought that nothing else would have.** The gap was invisible from
inside the task; it came from a party reading the plan rather than executing it
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]],
[[breadth-was-what-was-missing-and-pre-task-is-one-way-to-buy-it]]).

# The review arrangement itself produced evidence twice running — 2026-08-21

**The librarian's own report caught two errors in the briefs it was given, and both were the
session's**: a claim about what a folder move does to a rendering, and a figure in a brief written to
serve the rule it contradicted
([[a-presence-test-cannot-answer-an-identity-question]],
[[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).

**It is the second consecutive session in which the reviewing party found what the writing party
asserted without checking.** Kept because it is evidence about the *arrangement* rather than about
either error: the value of a reviewer here is not care, it is that the reviewer holds a different
source — the tree, or the corpus — from the one the writer reasoned out of.

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
