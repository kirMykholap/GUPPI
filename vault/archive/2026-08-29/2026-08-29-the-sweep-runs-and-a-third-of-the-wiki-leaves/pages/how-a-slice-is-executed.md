---
title: "A slice is written in the main session; review stays with agents and stays whole"
type: decision
status: archived
authority: slice-execution
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-11
created: 2026-08-13
sources: ["CLAUDE.md", "archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md"]
tags: [process, agents]
---

# A slice is written in the main session

**Decided by the owner on 2026-08-11**, after slice 3 cost a session of eight to ten hours. His
words, which this recalibration answers: «столько времени тратить на отсутствие результата — это
просто ужасно».

Where any skill contradicts this, this wins: the skills describe a default, and this is the
project's own calibration of it.

- **Code is written in the main session, against the plan** — `superpowers:executing-plans`, not
  `subagent-driven-development`. No implementer subagents. The implementer trip and the fix-wave
  trip are the two that buy nothing an edit made here does not. See [[agent-round-trip-cost]].
- **Review stays with agents, and the cycle stays whole.** One independent reviewer per task, and
  its findings are re-reviewed after they are fixed — including a fix that only touches a comment
  or a test. What was cut is *who writes the code*, not *who checks it*.
- **The final whole-branch review stays at three reviewers with different lenses.** It is the most
  expensive step that has paid for itself: it found slice 3's Critical.
- **A browser walk stays in every task**, walked in the main session through the Playwright MCP.
  Its cost was never the walking — it was being inside an agent's turn.
- **A Minor finding is never dispatched to an agent.** Record it in the ledger; fix it here if it
  is worth fixing at all.
- **A second opinion does not have to be an agent.** Reading the diff in the main session is a
  legitimate review when the change is small or already covered by tests verified by removal — say
  in the ledger that this is what was done and what was checked.

## What was rejected

- one review per task with re-review only when a fix changes behaviour;
- one final reviewer instead of three;
- one browser walk per slice instead of per task;
- no review at all for small or mechanical tasks.

**The pattern in the rejections is single:** every proposal that cut *checking* was refused, and
every proposal that cut *round trips around checking* was adopted.

What a full suite run costs, and why a subagent runs only its own tests: [[test-suite-wall-clock]].

## Where the rules being changed came from

The owner asked, and the answer is not "the assistant invented them". Each part of the process that
was renegotiated had a written source:

| Rule | Source |
|---|---|
| implementer → review → fix → **re-review**, per task | `superpowers:subagent-driven-development` — «Don't skip the re-review» |
| a broad whole-branch review at the end, most capable model | the same skill |
| full suite once per task, in the main session | the repository's own `CLAUDE.md` ([[test-suite-wall-clock]]) |
| execute slice 3 with subagents at all | §0 of `docs/HANDOFF.md`, written by the previous session |
| three reviewers with different lenses | §5д of the same file, describing how slice 2b ran |

**So the process was prescribed by a skill and by this project's own documents — which is exactly
why changing it meant changing those documents.** The recalibration's closing instruction is the
durable half of it: whatever is agreed, write it into `CLAUDE.md`, so it is a project rule rather
than a per-session judgement call. A rule that lives only in a session's reasoning is re-argued
every session.

**One recorded exception exists**, and it is not this rule being loosened but a slice going without
it: the visual slice's final three-lens review was skipped by the owner's decision on 2026-08-12.
See [[the-palette-grows-into-a-design-system]].

## Two gaps in the evidence, recorded on 2026-08-13

- **Reviewer round trips were never measured.** The 5–35 minute figure came from implementer and
  fix-wave trips; review was kept on the strength of what it *found*, not on what it cost. Whether
  keeping the whole cycle is affordable is therefore an unmeasured claim.
- **This recalibration has no post-hoc confirmation.** It was decided on 2026-08-11 after slice 3;
  no slice has since been executed under it and compared. The first slice that is should record its
  wall-clock, or the decision stays an argument rather than a measurement. **Half of that gap
  closed on 2026-08-13 — see below; the wall-clock half did not.**

## The first post-hoc confirmation, and it covers only the review half

The second-brain branch (2026-08-13, ten tasks) was executed under this rule, and it confirms the
part about *checking* in both directions:

- **keeping the re-review whole paid.** Three passes over the same tooling found **four defects
  inside the previous pass's own fixes**. A fix wave is work, and work is reviewed;
- **one fix was worse than the defect it fixed.** A verdict-grammar rule was tightened to catch a
  malformed page name and began rejecting the free prose the file's own header promises — eleven
  `BAD VERDICT` lines, and the ingest gate red on data committed six commits earlier, with no legal
  fix available ([[vault-scripts]]). Nothing but a re-review looks at that;
- **the three-lens whole-branch review earned its cost again, and each lens found what the others
  could not.** The corpus lens found a lesson page that had inverted its own rule; the loop lens
  found **both seam Criticals** — that no document said a session ends by writing its journal, and
  that an overtaken brief is indistinguishable from a current one
  ([[journal-vault-brief-each-artefact-has-one-owner]], [[the-brief-is-stamped-with-its-commit]]); the arrival lens
  found that a shrunk `CLAUDE.md` had dropped the only statement of **where our own JavaScript
  lives**, so the owed AST test would have been written to scan `static/`, found nothing of ours,
  and passed having read nothing ([[javascript-policy]]).

**Both Criticals were about how the parts join rather than about any part**, which is precisely
what a per-task review cannot see.

## A second confirmation, 2026-08-15, and this one is about reviewing an agent's report

The rule has a second half nobody had tested: **a dispatch is checked against the tree, never
against its own report.** Four librarian dispatches ran that day and each was reviewed against
`git diff`, the registers and a fidelity sample. **Three of the four were wrong in their own
reports, and all three errors were in the direction of "it went fine":**

- the first **miscounted its own sidecar by one in each direction** — 28 `page:` and 10 `skip:`
  reported against **27 and 11** measured with `cut -f2 | sort | uniq -c`. Harmless, because the
  sidecar is the artefact and the script reads it rather than the report — and it is another
  instance of [[a-stated-count-drifts-from-the-list-it-heads]], inside the agent that maintains the
  page saying so;
- the fourth was **off by one insertion** against the diff;
- the third **corrected two figures in the brief it was handed** rather than repeating them: 217
  tag assignments was stale by twelve, and "35 python files" is 34 plus `app.css`. It also
  **refused to write a number no source records and no measurement can now recover**, which is
  [[an-unsourced-number-is-dropped-not-chosen]] applied by an agent to itself.

**The generalisation is the reason to keep the review half at all: an agent's report is testimony,
and testimony about work is checked the same way testimony about a tree is** — against the
artefact, not against the account ([[journal-vault-brief-each-artefact-has-one-owner]]). None of the three errors
would have been found by reading the report more carefully.

**The boundary of this evidence, which matters as much as the evidence.** The branch produced
documents, skills and shell scripts — not `src/`, not a browser walk, and no implementer subagent
was even a candidate. It confirms that the checking was worth its cost. It says nothing about the
wall-clock claim, which is still what the first real slice has to measure.

One process observation from the same session is worth keeping because it has a cost attached: the
owner asked **when the final review should be run**, and answering it then rather than deferring is
what made the two seam findings arrive **while the branch could still absorb them**. See
[[the-owners-question-was-how-would-you-check-that]] for the pattern of his questions changing the
design rather than the schedule.

# One at a time, and the plan is what carries between them — owner, 2026-08-23

> **owner: по одной, но нужен четкий план, который мы не потеряем и будем двигаться по пунктам**

**Asked about how S3's work would be executed, he chose one item at a time — with a condition
attached to the choice rather than to the work.** The plan has to be concrete enough that it is not
lost between the items, and the work moves through it point by point.

**The condition is what is new.** Serial execution has been the shape since 2026-08-11; what he
added is that the *record* of what comes next may not live in the session, because the session ends.
He said the same thing again about the sprint, in stronger words:

> **owner: Давай тогда частично закроем s2. Все, что в нем осталось - переносим на s3. На s3 нуже
> будет прям конкретный и детальный план, потому что я уже чувствую что мы расходимся в некоторых
> вещах**

**«Я уже чувствую что мы расходимся» is the ground and it is not about throughput.** A detailed
plan is asked for as an instrument against divergence — something he can read and compare against
what happens — rather than as project management. That is the same complaint as the harness being
invisible to its owner, applied to a single sprint's work
([[the-harness-is-no-longer-visible-to-its-owner]]).

**Where the plan lives is already ruled**: the plan he reads in order to approve it is written in
Russian and lives outside the repository
([[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]]). **What is not ruled is what
keeps it from being lost** — nothing in this repository holds an approved plan, and `sprint.md`
holds criteria rather than steps.
