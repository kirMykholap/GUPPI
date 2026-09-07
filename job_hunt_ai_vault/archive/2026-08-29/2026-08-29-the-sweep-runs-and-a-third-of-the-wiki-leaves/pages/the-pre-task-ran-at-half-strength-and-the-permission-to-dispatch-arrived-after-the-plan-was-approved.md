---
title: "DIVERGENCE: `/pre-task` ran at half strength, and the standing permission to dispatch inside a ritual arrived after the plan was approved"
type: decision
status: archived
authority: pre-task-half-strength
binding: divergence
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-22
sources: ["archive/2026-08-21/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md", ".claude/agents/pre-task.md"]
tags: [process, agents, vault]
---

# What happened, 2026-08-21

**The rule places the ritual between the plan and its approval, and half of it ran**
([[a-pre-task-runs-between-the-plan-and-its-approval]]).

**Phase 1 ran.** `bash scripts/vault-catalogue.sh` over 576 rows, 17 constraining pages selected,
about 12 opened in full; the plan's `Constraints` section is its output.

**Phase 2 did not**, and what was lost is specific rather than general. Phase 2 carries the clause
*say what is missing from this shortlist*, and **that clause is the only thing in the design that
reviews phase 1** ([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]). So the
plan was checked against pages its own author had chosen, and approved on that check.

**The cause was a session-level instruction forbidding an unrequested dispatch** — not a rule of
this repository. It was reported rather than worked around
([[ask-before-weakening-or-working-around-a-rule]]).

# The owner lifted the cause at the retro

> **owner: да, разрешаю**

**A standing permission to dispatch agents inside the vault's rituals** — `/pre-task` phase 2,
`/vault-ask`, `/ingest`. Given after the session reported that the instruction had cut phase 2 out
of this session's own ritual and was about to stop `/ingest`.

**It is a permission and not an instruction to dispatch.** What it removes is the ground for
declining: a ritual that names a dispatch may perform it without asking again. Everything the store
already says about dispatching stands — in parallel for reading only
([[dispatch-librarians-in-parallel-only-for-reading]]), one librarian behind every caller
([[one-librarian-behind-every-caller]]), and a round trip that is not free
([[agent-round-trip-cost]]).

# Why it is recorded here rather than as a lapse

**A ritual with an external cause of failure is a different finding from a ritual that was
forgotten**, and this project has both on the record now
([[pre-task-was-skipped-again-and-the-record-is-a-recurrence-rather-than-an-incident]],
[[the-pre-task-was-skipped-and-the-rule-has-no-by-hand-form]]). The trigger was not at fault: it
fired, and the ritual started.

**The ledger recorded the whole argument without being asked to.** Two advisories fired, both
correct by their own data and both wrong — phase 1 had run, and the row saying so landed six minutes
later, because recording is a write and plan mode forbids writes
([[the-pre-task-ledger]], [[the-miss-was-carried-rather-than-written-because-plan-mode-disarms-the-party-the-rule-binds]]).

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# The citation is repointed, and the failure recorded here is no longer available in this shape — 2026-08-22

**`sources:` cited `.claude/skills/pre-task/SKILL.md` and now cites `.claude/agents/pre-task.md`.**
The skill was deleted on this date ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]),
and rule 5 of the gate requires every repository path in `sources:` to resolve — a citation to a file
that is not there reads as provenance and is not ([[vault-scripts]]). **The address moves and the
history stays readable**: this divergence happened against the skill and is recorded as it happened.

**The two phases survived the move; the seam between them did not.** In the agent both phases run in
one body, so **there is no moment at which a session can have paid for phase 1 and then decline phase
2** — which is what happened here. The half-strength run this page records is unreachable in that
shape, and the agent's definition gives this page's own reasoning as the ground.

**What is still reachable is not dispatching the agent at all**, and that failure is louder: it
leaves no `dispatch:pre-task` row, where a half-strength run left a ledger that looked like a
completed ritual ([[the-pre-task-ledger]], [[the-dispatch-record-hook]]).

**The cause recorded here was external and is spent.** A session-level instruction against an
unrequested dispatch cut phase 2 out; the owner's standing permission removed the ground for
declining, and the ruling of this morning removed the choice
([[the-pre-task-always-dispatches-its-narrow-phase]]).
