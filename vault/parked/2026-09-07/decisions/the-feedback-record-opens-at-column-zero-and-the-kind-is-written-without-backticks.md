---
title: "A feedback record opens at column zero and the kind is written without backticks"
type: decision
status: current
authority: feedback-record-grammar
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", ".claude/hooks/catch-the-feedback.ps1", ".superpowers/sdd/vault-feedback.md"]
tags: [vault, process, harness]
---

# The grammar, decided and built 2026-08-24

**One record per line, and a record opens at column zero — optionally behind a list dash — and
nowhere else.** An indented line is a continuation of the record above it.

**One entry per kind line, not one per fence.** The rendered rule in the repository's `CLAUDE.md`
shows four kinds inside one block, and the catcher used to take the first line's kind and apply it
to the whole block.

**The kind is written bare.** Neither `` `miss`: text `` nor `` `miss:` text `` is a record.

> **owner:** «Если ты утверждаешь что все работает - окей»

**Rejected: teaching the parser to accept a kind wrapped in backticks.** All four forms were tested
against the regex rather than reasoned about: `miss: text` matches, and the dashed, half-quoted and
fully-quoted forms do not ([[a-feedback-record-opens-at-column-zero-and-indentation-marks-a-continuation]]).

# Why the leading `\s*` is refused rather than merely unnecessary

**Indentation is what separates a continuation from a record.** A `miss:` is obliged to say where it
surfaced, and that sentence lands on the following line and may itself open with a word and a colon.
A parser that skips leading whitespace tears such a sentence into a record of its own.

# What it obliges

**The two renderings of this rule must agree.** They did not: the rendered rule shows a leading
dash, the template in `.superpowers/sdd/vault-feedback.md` shows the form without one, and the hook
understood only the second ([[the-drain-and-the-template-disagree-about-the-feedback-vocabulary]]).
