---
title: "A skill is a role mask and a subagent is an extra body"
type: concept
status: current
authority: skill-versus-subagent
basis: human
sprint: S1
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md"]
tags: [agents, process, vault]
---

# The owner's model, stated 2026-08-16

- **A skill is a role mask** the agent puts on for a specific piece of work, with isolated context.
- **A subagent is an extra body** — called for parallel work, or for a chain of masks worn one
  after another. Under this model **a subagent is essentially a workflow described in advance.**

That is a model of the tooling, not of this project, and it is the owner's. It explains a shape
this vault has recorded from the other end: [[one-librarian-behind-every-caller]] keeps one agent with
four callers so the instructions cannot diverge, and each caller is exactly a mask over the same
body.

## The consequence is immediate and costly

**`/vault-ask` dispatches the librarian today**, paying 15–30 minutes ([[agent-round-trip-cost]])
for a search which, under this model, is a mask the main agent could wear.

**The counter-argument is already recorded.** `/pre-task` says the reading must happen outside the
main context or it settles there permanently — a main agent that reads twenty pages to answer one
question carries those twenty pages for the rest of the session.

**So the trade is context pollution against tokens and wall-clock**, not cheap against expensive.
It is a fork rather than an obvious win, and it is deferred on exactly that ground
([[structure-work-agreed-and-not-executed]]).

## What would decide it, and does not exist

Nothing here measures context pollution. The cost side has numbers — five dispatch measurements and
a 14–29 minute band ([[agent-round-trip-cost]]) — and the pollution side has an argument. Deciding
a fork by the half that happens to be measured is the failure
[[an-unsourced-number-is-dropped-not-chosen]] names, so the honest state is that both halves are
written down and neither wins yet.

# The mask has a documented mechanism now, and the word for it collides — 2026-08-29

**`context: fork` in a skill's frontmatter runs the skill as a subagent whose prompt is the `SKILL.md`,
with no access to the caller's conversation history.** That is the mask made mechanical: an isolated
context, exactly as the owner's model describes.

**And it is the opposite of a `/subtask` fork, which inherits the entire parent conversation and reuses
its prompt cache.** Two mechanisms, one word — the shape that cost this store three days over
*retrospective* ([[a-forked-skill-starts-empty-and-a-subtask-fork-inherits-everything]]).

**It sharpens the trade this page records rather than settling it.** Under `context: fork` the
pollution side of the fork is genuinely bought — the caller's context is untouched — and the price
becomes that everything the fork needs must travel as an argument. **`vault-ask` as a forked skill is
designed and unbuilt**, and the first fork is the measurement.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
