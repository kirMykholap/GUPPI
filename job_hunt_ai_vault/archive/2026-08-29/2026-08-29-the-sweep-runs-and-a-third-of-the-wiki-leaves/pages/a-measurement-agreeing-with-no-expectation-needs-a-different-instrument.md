---
title: "A silent tool failure and a wrong denominator lied in opposite directions in one day: a figure that agrees with no expectation needs a different instrument before it is quoted"
type: lesson
status: archived
authority: instrument-failure
basis: measurement
sprint: S1
created: 2026-08-15
sources: ["archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md", "log.md", "CLAUDE.md"]
tags: [testing, process]
---

# Both wrong, in opposite directions, on the same day

**Instance 1 — the tool failed silently and green.** `grep -P` with a Cyrillic range reported
**zero** matches in a repository holding **10,947** lines containing Cyrillic. `-P` is unsupported
in this environment: the flag produced no error anyone read, exit status did not distinguish "no
matches" from "cannot do that", and the answer *zero* is a perfectly ordinary answer to that
question. The number that survived is the one taken with `rg -l --no-ignore '[\x{0400}-\x{04FF}]'`,
and it is on [[migrating-the-repository-to-english]] with the command beside it.

**Instance 2 — the measurement was fine and the thing measured was wrong.** Counting AST boundary
tests by globbing a filename gave **eight**. One of the eight is `_ast_boundary.py`, the shared
helper. The corpus's **seven** was right, and the "correction" was the error
([[architectural-boundaries]]).

The pair is the point. One instrument under-reported to zero and one over-reported by one, in the
same session, in a store whose most-recorded defect is a number that has drifted from its list
([[a-stated-count-drifts-from-the-list-it-heads]]).

*(The title read "Two measurements lied in opposite directions in one day: a figure that agrees
with no expectation needs a second instrument before it is quoted" until 2026-08-18, and the
instances above are where the count now lives, as evidence rather than as a headline. **Two was a
reading of one past day**, not of the world: that session is over, and a third instance cannot
arrive in it. That reasoning stood in a `quantity:` line until the field was rejected and the rule
made unconditional over titles and filenames alike
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]) — a number that cannot drift
still leaves the title, because the mechanism that let a page say so has been withdrawn. The title
now names the pair of failures instead of counting them
([[a-title-names-what-is-counted-instead-of-counting-it]]). **The ordinal went the same way**
(owner, 2026-08-18, ruling ordinals into rule 10's word list —
[[ordinals-count-and-first-does-not]], where this page's own title is one of the three
measurements the ruling was taken over): the title asks for *a different
instrument*, which is what the section below already glosses it as — *a different command, or a
different tool, answering the same question*. **The rule sentence below said *a second instrument*
until 2026-08-18 as well**, and is brought into line on the same date: it is the sentence a reader
quotes, and leaving it behind the title would keep the ordinal in circulation from the very page
that retired it. The **filename** still carries that ordinal and waits for its rename, which moves
an address ([[the-title-rule-extends-to-filenames]],
[[a-page-rename-is-sed-and-verify]]). A correction in place is not a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).
**Closed 2026-08-19: the rename landed and the name counts nothing.** The sentence above was
written on 2026-08-18 and stood for one day; the wait is the record rather than an oversight,
because a filename is an address and the repair was scheduled as one sweep of sixteen names in a
single change, not taken by whichever session happened to open this page next.)*

## The rule that comes out of it

**A measurement that agrees with no expectation deserves a different instrument before it is
quoted.** Not a second run of the same command — a different command, or a different tool, answering the same
question.

The two failure modes it guards are different and both are cheap to hit:

- **a silent tool failure**, where the instrument returns a legal-looking value instead of an
  error. Zero is the dangerous value, because it reads as a clean bill of health;
- **a wrong denominator**, where the instrument is perfect and the set it was pointed at is not.
  A glob is a set defined by a name, and names include helpers, fixtures and `__init__.py`.

This is why *"measure it, and write the date and the command beside it"* is stated as **the
command**, not the number: a command can be re-run by the next reader and a number cannot be
audited at all. It is also why a figure that overturns a written page is the one to double-check
first — the page is an expectation, and this session had one that was right.

The cost of skipping it is on record: the 2026-08-14 correction of "five AST tests" to seven was
right, and the 2026-08-15 correction of seven to eight had to be undone —
[[an-unsourced-number-is-dropped-not-chosen]] is the sibling rule for the case where no instrument
can be found at all.

# A third instance, and the instrument was right about a different question — 2026-08-20

**`grep -l` answered *does this string appear in this file* to a question that was *is this entry in
that section*, and the wrong answer went to the owner before anything was opened**
([[a-presence-test-cannot-answer-an-identity-question]]).

**It belongs beside the two above because the failure is one step earlier than either.** Instance 1
is a tool that could not do what was asked and said nothing; instance 2 is a correct measurement of
the wrong set. This one is a **correct measurement of a different question**, delivered as an answer
to the one that was asked — and the flag that made it terse, `-l`, is what removed the evidence that
would have shown the difference.
