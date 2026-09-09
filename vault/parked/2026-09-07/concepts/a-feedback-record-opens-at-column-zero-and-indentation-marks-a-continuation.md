---
title: "A feedback record opens at column zero, and indentation is what marks a continuation"
type: concept
status: current
authority: feedback-record-parsing
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", ".claude/hooks/catch-the-feedback.ps1"]
tags: [harness, process, vault]
---

# The mechanism

**One variable decides what opens a record.** A record starts at column zero, optionally behind a
list dash, and nowhere else; a line that starts with whitespace belongs to the record above it.
`Split-Records` then turns one fence into one entry per kind line.

**The old parser matched a kind at the start of a line with leading whitespace allowed and no dash
allowed.** Whitespace passes; a dash does not. And the character class for the kind swallows a dash,
so the parser consumed the dash as part of the kind, found no colon after it, and dropped the whole
block into `unknown:`.

# Why the two halves are not one bug

**The dash half is a disagreement between two renderings of one rule.** The rendered rule in the
repository's `CLAUDE.md` shows the dashed form, and the template in the feedback file shows the
undashed one — so the hook understood the form nobody follows
([[the-drain-and-the-template-disagree-about-the-feedback-vocabulary]]).

**The one-kind-per-fence half is a different mistake**: the parser read one kind off the first line
and applied it to the block, where the rule shows four kinds inside one block.

# Why the leading whitespace is dropped deliberately rather than by accident

**Indentation carries meaning here.** A `miss:` is obliged to say where it surfaced, and that
sentence lands on the next line and may itself open with a word and a colon. A parser that skips
leading whitespace tears such a sentence into a record of its own — which is exactly what happened
when the parser was made eager to prove the guard could fail
([[a-case-green-before-its-mechanism-is-proved-by-removing-the-guard]]).
