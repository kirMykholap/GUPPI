# A published figure carries the command that produced it

**Draft proposal, prepared by the lessons agent on 2026-08-31 from `wiki/lessons/` as it stands.
Not written into the vault. The librarian decides whether it becomes a `wiki/proposals/` page and
what its `authority:` is.**

**The group, in one sentence:** six live lessons are one failure — a number reached a reader
without the command that produced it, so nothing could tell a subtotal from a total, a typed date
from a read one, or a pattern's blind spot from an absence in the file.

## The group, and it splits cleanly in two

**Half A — the figure was typed from what the session had in front of it.**

- `a-subtotal-read-as-a-total` — five dispatchers added up; eleven exist plus sixteen inline cases;
  the true figure was in the corpus while the wrong one was being written into a plan.
- `a-date-is-a-measurement-and-an-inferred-one-is-wrong-wherever-it-was-written` — a date derived
  from the previous session's, wrong by a day, landing in forty-four places, three of them
  arithmetic that stays wrong after the dates are fixed.
- `a-date-typed-into-a-docstring-is-a-measurement-and-goes-wrong-silently` — `2024-08-24` for
  `2026-08-24`; caught only by re-reading the edit, because a date in prose has no reader.

**Half B — the instrument's pattern asserted a shape the file never promised.**

- `a-comment-quoting-the-literal-a-sweep-looks-for-is-counted-by-that-sweep` — `--list` reported
  182 where the file held 181, because the comment explaining the sweep quoted its own literal.
- `a-pattern-requiring-a-dot-after-a-rule-number-cannot-see-a-shared-heading` — fifteen headings
  read as fourteen, and a plan scoped work that never needed doing.
- `an-advisory-word-on-a-continuation-line-inflates-the-count-the-brief-reports` — the brief read
  54 advisories where 30 exist, in every brief that carried the figure.

**What joins the halves:** in all six, the instrument that knew the answer was available and was
not the source of the published number.

## What it would be

**Two clauses, and they are not the same clause.**

1. **A figure written into prose names the command that produced it and the day it was taken.**
   The store already has the parts: `scripts/vault-measure.py` is the only writer of a gauge's
   number, the measure region fences its command in backticks, and rule 10 forbids a count in a
   title. What is missing is that this applies to a figure in a *body*, a *plan* or a *brief*, and
   nothing checks it.
2. **A counting pattern gets a case that pins its count against a real run.** That is the durable
   repair `sweep-counts-its-own-comment` already identified and it is the one that fired — the
   case written 2026-08-29 agreed at 194 on its first run. Half B is three patterns and one such
   case.

## What it would take

- **A gauge for each figure a brief reports.** `grep -c 'advisory:'` is the live example of a
  brief's number produced by a command nobody wrote down; it was wrong for as long as the two
  advisories existed and no reader could have told.
- **A verdict, or an advisory, for the continuation-line rule.** `advisory-continuation-defect`
  says in its own words that a check for exactly that is owed and unbuilt, and that a ruling about
  the shape of output is a contract with whoever greps it.
- **One case per counting pattern**, comparing the pattern's count to a run of the thing counted.

## What is open

- **Whether clause 1 is a rule or a habit.** Every instrument this store has built to force a
  number has been either deleted or ignored: the `quantity:` field was withdrawn after two of its
  declarations were false; the region-coverage advisory read `9 of 15` then `9 of 17` with the
  numerator never moving. `an-advisory-carrying-a-debt-count-does-not-get-paid-down` is the
  standing argument that printing it harder does not work.
- **Whether half A is answerable at all by a mechanism.** A date in prose has no reader, by that
  page's own finding, and the only instrument that has ever caught one is reading the edit back.
  A proposal that promises a check for it would be promising something nobody knows how to build.
- **Whether the two halves are one proposal.** They share a diagnosis and not a repair. The
  librarian may reasonably split them, and if it does, half B is the buildable one.

## What it would oblige

- **A named owner for the brief's figures.** A number a brief prints is either derived at render
  time from a command, or it is a hand-written number in a generated file — and `brief.md` is
  derived and never a source.
- **A dated re-take of the region-coverage advisory**, since it is the store's own worked example
  of a correct number that changed nothing for weeks.

## What it would retire

**Half B in full** — `sweep-counts-its-own-comment`, `shared-rule-heading`,
`advisory-continuation-defect` — once a case pins each pattern against a run.

**Half A only in part.** `subtotal-as-total` retires with half B, since its repair is the same
sentence: read the figure off the instrument, or say the instrument was not run. The two date
pages should stay live: their finding is that no instrument exists, and a lesson recording *where a
rule cannot get an instrument* is exactly what S3's first acceptance criterion asks to be written
down rather than closed.
