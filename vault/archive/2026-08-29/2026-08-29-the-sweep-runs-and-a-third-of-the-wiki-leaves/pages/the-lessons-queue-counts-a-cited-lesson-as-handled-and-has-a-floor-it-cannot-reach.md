---
title: "The lessons queue counts a cited lesson as handled, and it has a floor nothing can drain it below"
type: lesson
status: archived
authority: lessons-queue-instrument-defects
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/lessons-queue.py"]
tags: [vault, process, testing]
---

# Two defects in one instrument, found by its own first consumer

**`scripts/lessons-queue.py` counts a lesson as *handled* when a rule or a proposal cites it.** So
filing the five proposal drafts the collector returned would move roughly **25 lessons** out of the
queue at a stroke, without any of them being acted on. The collector found this in its own input and
said so; nothing in the vault named it before 2026-08-26.

**About a tenth of the queue records a method that worked rather than a failure** — ten pages by the
collector's count — and **no proposal can ever drain them.** The script cannot tell them from the
rest, so the queue has a floor it will never go below and nothing states what that floor is.

# What the queue's number actually counts

**Measured 2026-08-26: 157 lesson pages. One is cited by nothing live at all; 12 are cited only by
other lessons; 144 are cited by something outside `lessons/`.** The queue reads **104** because the
script counts only `rules/` and `proposals/` as citers and **does not see `decisions/`**.

**So three different populations are in play** — what the queue reports, what is genuinely
uncited, and what the archiver's criterion would move — and the first is the one nobody derived
from the other two ([[the-lessons-cycle-is-the-owners-and-a-lesson-leaves-when-a-page-outside-lessons-cites-it]]).

# The consequence that was ruled on rather than left

**The counter is fixed after the drafts are filed, not before** (owner, 2026-08-26), and the
queue's fall from 104 is recorded as an artefact rather than as progress
([[the-lessons-queue-counter-is-fixed-after-the-drafts-are-filed]]).

**The general shape: a progress instrument whose denominator it does not own will report the
librarian's own writing as work done.** Every page filed in response to the queue moves the queue,
which is the one number the exercise was supposed to be judged by
([[a-printed-register-cannot-drift-and-a-maintained-one-always-has]]).

# The counter now prints two numbers, and the queue fell from 100 to 37 — 2026-08-26

**The conflation this page names is what was repaired.** `CITED` is the loop's end state; `LANDED`
counts a `rules/` page or a proposal carrying `status: implemented`
([[the-lessons-queue-counter-prints-cited-and-landed-apart]]).

**Measured after the edit:** lessons 165; cited by rule 22, by proposal 55, by decision 120; `CITED`
128, `LANDED` 27, **queue 37**. It was **100** before.

**The fall is caused by teaching the counter to see `decisions/` as a citer, and by nothing else.**
No lesson was touched, and **120 of the 165 lessons are cited by a decision** — which is the size of
the blind spot this page recorded without measuring.

**Nothing named that effect in advance.** Neither the deferral that ordered the repair nor the plan
that carried it out estimated it ([[the-lessons-queue-counter-is-fixed-after-the-drafts-are-filed]]).

**So the queue number has changed meaning twice in two days, and a reading taken before 2026-08-26 is
not comparable with one taken after.**

**The floor this page names is untouched** — about a tenth of the queue records a method that worked
rather than a failure, and no proposal can ever drain those.

**And the width of membership was ruled on the same day and did not move**: a citation from anywhere
takes a lesson out of the queue, on the ground that a mention is a trace
([[a-citation-from-a-decision-takes-a-lesson-out-of-the-queue]]).

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
