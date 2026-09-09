---
title: "DIVERGENCE: `/pre-task` was skipped again, and a divergence recorded in consecutive sessions is a recurrence rather than an incident"
type: decision
status: archived
authority: divergence-recurrence-reading
basis: human
binding: divergence
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "CLAUDE.md"]
tags: [process, agents, vault]
---

# The divergence, recorded 2026-08-20

**What the rule says:** `/pre-task` runs before anything non-trivial, and before touching an area
not touched this session ([[a-pre-task-runs-before-anything-non-trivial]]).

**What was done:** two hooks and a selftest were edited — `.claude/hooks/lock-the-librarian.ps1`,
`.claude/hooks/check-the-journal.ps1`, `scripts/hook-selftest.ps1` — in an area untouched this
session, with no `/pre-task`.

**Why it looked unnecessary:** the acceptance test was framed as *one move*, the defect surfaced
while running it, and the repair felt like part of the test rather than like implementation.
**It was implementation.**

**Rejected: obey the rule.**

**And it paid where it was run.** `/pre-task` ran before sprint items 1 and 3 and paid twice: it
named the verdict the vault held no answer to ([[an-absent-render-is-red-on-a-page-that-renders]])
and it named the hole that `--collect-only` cannot see
([[collect-only-cannot-exercise-an-assertion-message]]).

## A second skip under the same head, named separately

**The `sources:` rewrite also went without `/pre-task`**, under the same ruling that authorised the
write ([[the-session-wrote-wiki-by-hand-while-the-lock-held-its-only-writer-out]]). It is named on
its own line because **the owner's authorisation covers the write, not the skipped check** — one
permission does not silently extend to a different rule.

# The shape of the record is now a question, and it is the owner's

**This rule has been recorded as diverged from in consecutive sessions**, and each record is titled
for a single session:

| when | the page | what it was |
|---|---|---|
| 2026-08-19 | [[the-pre-task-was-skipped-and-the-rule-has-no-by-hand-form]] | the ritual was unavailable and the rule has no by-hand form |
| 2026-08-20, earlier session | [[pre-task-was-not-run-before-the-first-items-of-this-session]] | the brief felt pre-checked |
| 2026-08-20, this session | this page | a repair inside an acceptance test did not read as implementation |

**Three causes, one rule, and no page holds the class.** The librarian records the third instance
and does not fold the three together: choosing whether a repeated divergence becomes one class page
— or whether the rule itself needs a trigger a session cannot mistake — is a judgement about the
project rather than about the store ([[the-librarian-writes-unattended]]). **It is raised in the
brief.**

**What the three do have in common, stated without deciding anything:** in none of them did the
session believe it was starting implementation. The rule keys on *non-trivial work*, and each skip
happened at a moment the session had classified as something else — an unavailable ritual, a
pre-checked brief, a test run. That is evidence about the trigger, not about the diligence
([[knowing-a-rule-is-not-a-mechanism]]).

# The owner answered the question this page raised — 2026-08-20, later the same day

**He changed the trigger.** `/pre-task` now runs between a plan and its approval, and before the
first write of a session that presents no plan
([[the-pre-task-trigger-becomes-the-plan-and-the-first-write]]). *Non-trivial* is gone, and so is
the half about an untouched area — the second removal is a narrowing taken knowingly and stated on
that page.

**The evidence this page recorded is what decided it**, in the owner's hearing and in these terms:
three skips, three causes, and in none of them did the session believe it was starting
implementation. The table above is the record the ruling was made against.

**Neither of the alternatives this page named was taken as written.** It is not one class page, and
the rule was not left alone: the trigger was replaced by facts a hook can see, and the ritual now
leaves an artefact ([[the-pre-task-ledger]], [[the-plan-check-hook]]). **The divergence records
themselves stand unchanged** — what happened is not revised by what was decided afterwards.
