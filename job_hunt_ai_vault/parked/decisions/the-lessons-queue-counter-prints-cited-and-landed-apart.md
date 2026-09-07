---
title: "The lessons-queue counter prints `CITED` and `LANDED` apart, where it printed one conflated meaning"
type: decision
status: current
authority: lessons-queue-counter-split
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "scripts/lessons-queue.py"]
tags: [vault, harness, process]
---

# The ruling, 2026-08-26

*(the owner selected it, against throwing `proposals/` out of membership.)*

**Membership in the queue stays as it was** — a lesson leaves the queue when a `rules/` page or a
`proposals/` page cites it — **and the script prints two numbers instead of one**:

| number | what it counts |
|---|---|
| `CITED` | the loop's end state: the lesson has a trace somewhere that points at it |
| `LANDED` | a `rules/` page, or a proposal carrying `status: implemented` |

**Rejected: narrowing membership to `LANDED`.** That would take the end off the loop — a lesson
whose proposal is written but not built would never leave the queue, and the queue would grow
without a way to fall.

# What it measured when it ran

**Measured 2026-08-26, after the edit:** lessons 165; cited by a rule 22, by a proposal 55, by a
decision 120; **`CITED` 128, `LANDED` 27, queue 37.** The queue read **100** before the edit.

**The fall is caused by adding `decisions/` as a citer and not by any work on `lessons/`.** No lesson
was touched. 120 of the 165 lessons are cited by a decision, which is why the number moved by nearly
two thirds ([[the-lessons-queue-counts-a-cited-lesson-as-handled-and-has-a-floor-it-cannot-reach]]).

**Nothing named the size of that effect in advance** — neither the deferral that ordered the repair
nor the plan that carried it out ([[the-lessons-queue-counter-is-fixed-after-the-drafts-are-filed]]).
**The queue number has now changed meaning twice in two days**, so a reading taken before 2026-08-26
is not comparable with one taken after.

# The script carries its own blind spot in prose, and the blind spot is real

**It never scans `archive/`.** An implemented proposal that moves out of `wiki/` drops out of
`LANDED` and raises the queue, with nothing having gone backwards
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

# The title and the collector's brief are rewritten, and that half is not done

*(the owner selected it, 2026-08-26.)* **The docstring title of `scripts/lessons-queue.py` and the
collector's brief in `/vault-lint` describe a population the script no longer measures.** The title
says *lessons nobody has proposed anything about*; membership is now *not cited from anywhere*.
Those are different questions.

**It is a harness line for S3 and was not done this session**
([[the-plans-remaining-phase-moves-to-s3-and-the-ritual-runs-whole]]).
