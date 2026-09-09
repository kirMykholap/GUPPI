---
title: "DIVERGENCE: the catcher's note was built against the plan's letter and the owner was told afterwards"
type: decision
status: archived
authority: b3-plan-deviation
binding: divergence
basis: code
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", ".claude/hooks/catch-the-feedback.ps1"]
tags: [harness, process, vault]
---

# What the plan said and what was built

**The committed plan specified a note on a `decision:` mark carrying `the owner said it` and **no
Cyrillic byte**.** The session built the note on the **absent guillemet quotation** instead, and
told the owner afterwards rather than before.

# Why it looked unnecessary at the time

**The measurement made the deviation look free.** `log.md` holds 1218 records, 125 of them
`decision:`; 81 carry the mark; 66 have a quotation and 15 do not, **and all 15 are Cyrillic**.

**So the specified test fires on zero of them, and the built one is a strict superset** catching all
15. The three no-Cyrillic records a naive test would flag are one `ingest:` and two `measure:`
records *about* the phrase, which is why the note is scoped to `decision:`
([[a-guard-that-matches-a-phrase-anywhere-flags-the-record-that-discusses-it]]).

# The reasoning holds and the timing does not

**The owner ratified the built version at the retro**
([[the-alphabet-test-behind-the-owner-block-advisory-is-overturned]]), so the deviation was correct
about the mechanism.

**What is recorded here is that it was a session's call, taken silently, on a plan he had read and
approved.** The rejected alternative — and it is what the plan itself prescribes — was to build the
specified test and record its blind spot
([[ask-before-weakening-or-working-around-a-rule]],
[[a-plan-can-be-factually-wrong-about-the-tree-and-the-pre-task-is-what-reads-the-tree]]).

**The measurement is what made it look free, and a measurement is not an authorisation.** Being
right about the predicate is a different question from being entitled to change one
([[the-owner-decides-how-a-slice-is-executed]]).
