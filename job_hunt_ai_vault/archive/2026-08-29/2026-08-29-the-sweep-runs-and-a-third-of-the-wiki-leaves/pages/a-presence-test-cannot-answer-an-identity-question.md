---
title: "A presence test cannot answer an identity question, and `grep -l` failed towards a confident wrong answer delivered to the owner"
type: lesson
status: archived
authority: presence-versus-identity
basis: code
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md"]
tags: [testing, process, vault]
---

# The incident, 2026-08-20

**The question was:** are these two lines still sitting in `.superpowers/sdd/vault-feedback.md`
already drained into the previous journal's `Feedback to the librarian` section?

**The instrument was** `grep -l "thirteen unmarked files"` **over the journal.** It matched.

**What the session then reported to the owner:** that `/handoff` had failed to empty the feedback
file, and that tonight's drain would duplicate a line.

**What was actually true:** the match was on unrelated prose in a **different section** of the same
journal, and the section in question holds two entirely different entries. `/handoff` empties the
file correctly.

# The two questions, side by side

| asked | answered |
|---|---|
| is this entry in that section | — |
| — | does this string appear anywhere in that file |

**`grep -l` reports presence in a file and prints no line, no offset and no context.** It cannot
distinguish *the thing I am looking for* from *a sentence that shares five words with it*, and the
`-l` flag removes the one output that would have shown the difference at a glance.

**It failed towards confidence.** A miss would have prompted a second look; a hit read as
confirmation, and the wrong answer was delivered upward before anything was opened.

# What saved it, and it was procedure rather than luck

**Nothing was deleted, because the match was verified before acting on it** — the journal was opened
and the section read. The instrument was wrong and the ritual around it was not
([[a-planted-offender-is-proved-by-reading-it-back]]).

# The general form

**Match the instrument to the question's scope.** An identity question needs the match *located*:
the section, the line, the surrounding text. This project has met the same shape twice from other
directions — a tool that fails silently and green, and a measurement of the wrong thing
([[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]) — and the corpus's own
schema documentation carried a `rg -o` line that compared a field name to itself for the same reason
([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]).

# The same shape one level up, 2026-08-21: a claim reasoned from the page instead of read from the tool

**A brief asserted that moving a rule page between folders leaves its rendering unchanged.** It is
false: `scripts/vault-inject.sh` derives the marker's type word from the **folder**, so all four
markers in the repository's `CLAUDE.md` had to be retyped
([[the-marker-carries-the-records-type]], [[governs-is-a-property-of-wiki-rules-alone]]).

**The claim was reasoned from what the page carries rather than read from the writer**, which is the
same substitution as answering an identity question with a presence test: a cheaper source that
correlates with the answer was consulted instead of the one that determines it. **One level up,
because here the cheaper source was an inference about a mechanism rather than a command.**

**The librarian caught it, in the second consecutive session where the reviewing party found what the
writing party asserted without checking**
([[a-gap-named-by-a-reviewer-is-closed-by-a-mechanism-rather-than-by-care]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

# A verification line can be the wrong instrument on a correct tree — 2026-08-22

**A plan carried the check `grep -c CONTRADICTION ... # 0`.** The tree was right and the right answer
was **2**: the callout had been removed and its words survive verbatim inside a dated section,
because nothing here is deleted ([[the-region-coverage-figure-is-dated-where-it-stands]]).

**The question is *is the callout live*, not *is the word present*.** A live callout is a
`> [!CAUTION] CONTRADICTION` block; the same word inside a quoted paragraph is testimony about a
callout that used to be there, and the two are the same string to `grep`.

**So a verification line written against a corpus that never deletes must ask about the form and not
about the word.** The failure direction here is the safe one — it reddens on a correct tree rather
than passing on a broken one — but a check that cries wolf on every correct outcome is one a reader
stops running ([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).

**It is the same shape as the incident above, arriving from the other side**: there a presence test
answered an identity question wrongly and confidently; here it answered a *liveness* question with a
count of mentions.
