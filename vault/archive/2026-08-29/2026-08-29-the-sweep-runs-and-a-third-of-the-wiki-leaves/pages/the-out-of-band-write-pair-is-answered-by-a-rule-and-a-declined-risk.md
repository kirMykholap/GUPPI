---
title: "The out-of-band write pair: concurrency becomes a rule, and diff-reading is declined with the risk accepted"
type: decision
status: archived
authority: out-of-band-write-pair
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "CLAUDE.md"]
tags: [vault, agents, process]
---

# One page, by the owner's verdict, because apart they read as an unfinished thought

**The pair had stood open in the brief for three sessions**: the two properties that make a write to
`wiki/` from outside the librarian safe — **no concurrency**, and **the owner reading the diff** —
were named on no rule ([[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]). Both
halves were answered on 2026-08-20 and they were answered **differently**.

# The half that becomes a rule

**Concurrency.** *Dispatch librarians in parallel only for reading* is now a rule rendered into the
repository's `CLAUDE.md` ([[dispatch-librarians-in-parallel-only-for-reading]]).

> **owner:** «Записать правилом: "параллельно — только на чтение". Но у нас уже было это правило,
> если я правильно помню. Если было - настало время выносить это в `CLAUDE.md`.»

He remembered correctly and more precisely than expected: the sentence already existed verbatim on
[[parallel-librarians-break-the-one-writer-property]], a `type: lesson` page with no `governs:` and
no `render:`, **delivered nowhere**.

# The half that is declined

**Diff-reading.**

> **owner:** «что касается дифов - я их не читаю. Стоило бы, но я принимаю этот риск в угоду
> скорости. Ошибиться можно, главное чтобы была возможность найти ошибку.»

**Rejected: making diff-reading a rule as well.** The condition he keeps is not *no mistakes* but
*a mistake can be found*.

# The asymmetry is the argument

**A concurrency failure is invisible in every channel this project has.** The losing write never
happened, so `git diff` shows the survivor, `log.md` records one action and the gate passes a
well-formed register ([[parallel-librarians-break-the-one-writer-property]]). Nothing can find it
afterwards, which fails the condition above outright — so it becomes a rule.

**A diff-reading failure is visible.** A wrong page is findable by scripts, tests, hooks, `log.md`
and the journal, and the gate reads the corpus whole
([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]). So it may be declined, and the
residual risk is the owner's and is accepted in his own words.

# What it obliges

- **The one-writer property stays a convention about who is dispatched**, now with one of its two
  failure modes written into the file every session reads and the other one explicitly waived.
- **Nothing may be built that assumes the diff is read.** A mechanism whose safety rests on the
  owner reading a diff is resting on something he has said he does not do — and the repair for that
  class is an instrument, not a reminder ([[knowing-a-rule-is-not-a-mechanism]]).
