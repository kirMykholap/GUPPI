---
title: "A test that scans text for a literal must be shown to fail — prose in a comment satisfies it"
type: lesson
status: archived
authority: literal-scanning-tests
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [testing, web]
---

# A search for a literal is satisfied by an example of it

`base.html` carries the literal `<div id="collection">` **in prose, inside a `<script>` comment**.
The id-presence check searched the whole response, so the target counted as satisfied on every
page — for a slice and a half.

**The invariant that exists because htmx fails silently was itself failing silently.** See
[[htmx-swap-target-invariant]], which now strips `<script>` blocks on both sides, with assertions
pinned to the strip so that deleting it goes red.

## It is a family, not an incident

The old handoff notes this was **the third time the class was paid for**. It happened a fourth
time within a day of the vault being built: `vault-check.sh` reported broken links for
`[[old-page]]` and `[[new-page]]` — its own schema's *examples* — and the fix was the same strip,
extended to inline code as well as fenced blocks.

And a fifth, in the other direction, on the same script: an unquoted `$(find ...)` word-split a
directory name containing a space, every read failed, and the check printed **ok** having examined
nothing.

## The rule

**A check that matches text must be shown to fail.** Introduce the thing it should catch and watch
it go red; then remove it and watch it go green. A check that has never failed in your presence is
a check whose reach you are guessing at.

See [[a-test-green-under-any-implementation]] for the general form, and
[[a-boundary-stronger-in-prose-than-in-code]] for what happens when documentation overstates a
check's reach.

**And a sixth**, on 2026-08-13: a 0-byte file satisfying a wikilink to a page that did not exist.
The full tally of one session, and what each instance became,
is [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]].
