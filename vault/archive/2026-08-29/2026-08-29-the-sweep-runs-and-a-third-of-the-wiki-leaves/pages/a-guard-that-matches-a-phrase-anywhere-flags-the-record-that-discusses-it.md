---
title: "A guard that matches a phrase anywhere in a record flags the record that discusses the phrase"
type: lesson
status: archived
authority: guard-match-anchoring
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", ".claude/hooks/catch-the-feedback.ps1"]
tags: [harness, testing, process]
---

# The incident, 2026-08-26

**The catcher's new note fired on its own first live encounter.** It looks for a `decision:` record
whose shape declaration is *the owner said it* and which carries no guillemet quotation.

**What it flagged was a record opening `decision: the owner selected it` and going on to name the
phrase `the owner said it` as its subject.** The record was correct; the guard read the phrase
wherever it stood.

**Repaired by anchoring the match to the shape declaration at the head of the record**, and a case
pins it.

# Why this recurs rather than being one typo

**A register whose records are *about* its own vocabulary will always contain its own tokens.**
`log.md` holds 1218 records, and among them are `ingest:` and `measure:` records whose subject is
the phrase `the owner said it` — three of them carry no Cyrillic and a naive test would flag all
three ([[the-alphabet-test-behind-the-owner-block-advisory-is-overturned]]).

**So the position of a token is part of its meaning here**, and a guard over this file has to read
position rather than presence. The same shape has already bitten this repository twice through
fenced examples: an example inside a code block satisfies a search
([[an-example-inside-a-code-block-satisfies-a-search]]).

# What it is worth

**The false positive cost one repair and produced one case.** The general form is cheap to state
and expensive to rediscover: **a predicate written over a corpus that documents the predicate is
self-referential**, and it must be anchored to structure — a field, a head, a line position — rather
than to a substring.
