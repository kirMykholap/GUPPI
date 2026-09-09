---
title: "Narrowing an approved scope is a notification; replacing or widening it is a question"
type: decision
status: current
authority: scope-change-protocol
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md"]
tags: [process, agents, harness]
---

# The owner's rule, derived from two divergences on 2026-08-18

**Doing less than was approved is announced and proceeds. Doing something else, or more, waits for
an answer.**

| What happened | Which side | What was owed |
|---|---|---|
| three approved verdicts, two shipped, the third **replaced** by a different one | replacing | a question — it was announced instead ([[the-unreachable-verdict-is-dropped-and-replaced]]) |
| a region **replacing** hand-written prose rather than standing beside it, with the question already put and unanswered | replacing | a question — the answer was reasoned out instead ([[the-maps-region-replaces-the-prose-it-duplicated]]) |

Both were resolved by the session on stated reasoning and both were ratified afterwards. **Neither
was legal at the time**, and the rule exists so the next one does not need a retrospective to find
that out.

## Why the asymmetry is the right shape

**A narrowing is visible in the artefact and reversible.** The owner sees less than he approved and
can say so; nothing was built on the wrong ground in the meantime.

**A replacement is invisible in exactly the same artefact.** What shipped looks like an
implementation of what was approved, and the substitution only surfaces if somebody compares the
two — which is what a retrospective is for and is the most expensive place to find it.

## It sits under the rule it refines, not beside it

`CLAUDE.md` already says *ask before you weaken, remove or work around any rule*
([[ask-before-weakening-or-working-around-a-rule]]). That covers the rules; this covers the
**scope of an approved piece of work**, which is the thing a session actually holds in its hands
during a build. The companion rule about the answer, in the owner's own words, is on
[[the-maps-region-replaces-the-prose-it-duplicated]]: *a question once asked is closed by the owner
and by nobody else.*

## A third instance, the day after the rule was written — 2026-08-18

| What happened | Which side | What was owed |
|---|---|---|
| an approved **multi-line** advisory shape shipped as a single comma-run | replacing | a question — neither a question nor a notification happened ([[the-filename-advisory-prints-one-name-per-line]]) |

**Nobody decided to override the owner**; the house style of the two advisories beside it applied
itself. That is what makes this instance worth adding rather than merely counting: **the content was
identical and only the arrangement moved**, so the substitution was invisible to the check a
reviewer actually runs ([[a-replaced-shape-reads-as-no-replacement-when-only-the-shape-moved]]).

**Confessed unprompted at the retrospective and corrected the same session** — which is the outcome
this rule is written to make unnecessary rather than to make prompt.

# A widening that was forced rather than chosen — 2026-08-20

**A session stamp and an edit to a hook were added outside an approved plan of ten items**, because
a script the session runs is handed no `session_id` and the ritual could not otherwise record itself
at all ([[an-approved-scope-was-widened-by-a-step-that-was-forced-rather-than-chosen]]).

**The rule keys on whether the scope grew, not on whether the growth was avoidable**, and this
instance is named because it is the shape most likely to recur: *this cannot be done without also
doing that* is a normal discovery inside implementation, and it reads as part of the item rather
than as an addition to it. Ratified by the owner after the fact.

# A narrower clause for the forced repair, ruled 2026-08-22

**A repair without which the approved work does not run does not have to be asked for, provided it
is named in the report.** That is the owner's wording of the exception, and it is written here rather
than on a page of its own so that a plan check reading this rule reads the exception with it.

**Rejected: *files that are already the session's***, which was the session's own framing and admits
anything under `scripts/`. The clause keys on **whether the approved work runs without it**, which is
a question with an answer, not on whose file it is.

**The two instances it was ruled on are both from 2026-08-22**, and both were genuinely forced: the
first made an acceptance criterion the owner had set a minute earlier undecidable
([[an-instrument-that-answers-half-a-question-in-the-voice-of-a-whole-one]]), the second turned the
whole selftest suite red
([[an-approved-scope-was-widened-by-a-step-that-was-forced-rather-than-chosen]]).

**What did not change: the naming is not optional.** The exception removes the question and keeps the
record, which is the half that makes the next such step visible
([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).

**And the rule above still keys on whether the scope grew.** A forced *feature* is still a widening;
what this clause exempts is a repair to something the approved work is standing on.
