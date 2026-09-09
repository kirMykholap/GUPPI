---
title: "One `/pre-task` per approved scope, and the answer comes back per item"
type: decision
status: current
authority: pre-task-dispatch-unit
binding: prohibition
basis: measurement
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/agents/pre-task.md"]
tags: [agents, process, harness]
---

# The unit is the approved scope, not the item and not the area

**Chosen:** one dispatch per plan, asking for **per-item answers**. **Rejected:** one dispatch per
plan item.

**The arithmetic is the argument.** A pre-task's expensive half is the sweep across every
`decisions/` page, and that sweep is identical for one item or for ten; the half that degrades with
breadth is *open only what touches the plan*. So the dispatch asks for answers per item and pays for
the sweep once. **Measured: one pre-task question is 5m54s** ([[agent-round-trip-cost]]), so ten
dispatches would be about an hour for one plan.

# The area was measured and then dismantled as a unit

**Areas touched per working session, over three real commits with the vault excluded: 4 and 6 at the
top level, against 71 and 108 files.** That measurement was taken for an approach keyed on *areas*,
and the owner dismantled it on better grounds than the number: **an area is a property of the
answer, and the ritual happens before the answer exists.** A plan names what it will do; which areas
it will touch is known only once the work is done.

# What it obliges

**The state machine keys on the approved scope** — a pre-task belongs to the plan it checked, and
once that plan is approved the scope closes and the next plan inherits nothing
([[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]).

**A ranked partial answer is the dangerous one here**, which is why the dispatch enumerates
frontmatter across every `decisions/` page and opens only what the titles implicate
([[a-pre-task-runs-between-the-plan-and-its-approval]]).

# The folder scope this page states was ruled too narrow — 2026-08-21

**The sentence above naming the enumeration as *every `decisions/` page* still describes the tree
and no longer describes what is intended.** The owner ruled that the enumeration must cover
`concepts/`, `entities/`, `proposals/` and `rules/` as well, with `lessons/` deliberately excluded;
it was not built, and the ruling lives on its own page
([[the-pre-task-enumeration-covers-every-folder-but-lessons]]).

**Nothing here is superseded.** The dispatch unit — one `/pre-task` per approved scope, the answer
per item — is untouched by that ruling; only the breadth of what each dispatch reads is.

# The citation is repointed to the agent, and only half of what it carried is at the new address — 2026-08-22

**`sources:` cited `.claude/skills/pre-task/SKILL.md` and now cites `.claude/agents/pre-task.md`.**
The skill was deleted on this date ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]),
and rule 5 of the gate requires every repository path in `sources:` to resolve — a citation to a file
that is not there reads as provenance and is not ([[vault-scripts]]). **The address moves and the
history stays readable**: this page was compiled from the skill on 2026-08-20.

**The answer shape survived whole.** *Per item of the plan, never for the batch*, with this page's own
argument — "touches the plan" softens into "touches any of ten" across a heterogeneous scope — is the
agent's own instruction.

**The unit did not, and it could not have.** *One `/pre-task` per approved scope* is a rule about the
**caller**, and an agent's definition is read only once the caller has already dispatched it, so
nothing in `.claude/agents/pre-task.md` states it. The rule that reaches a caller says *how* to
perform the ritual and not *how often per scope*
([[a-pre-task-runs-between-the-plan-and-its-approval]]). **So this decision is now carried by this
page alone**, and the file cited beside it cannot be checked against it.
