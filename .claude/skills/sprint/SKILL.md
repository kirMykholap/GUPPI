---
name: sprint
description: Open, inspect or close a sprint. Use when starting a new body of work, when asked what the current sprint is, or at a retrospective.
---

# Sprint

All work happens inside a sprint, and a sprint is **declared explicitly** — not inferred from
merges or branches, because "sprint" must mean what the owner intends rather than what happened to
coincide with a branch.

The record is `sprint.md` in the vault — the top-level directory holding a `wiki/`. Read it; never
restate a sprint from memory.

## Opening one

Ask the owner for a **goal written as a checkable statement**, not a theme. "Improve collection"
cannot be checked; "collection starts from the browser and its progress is visible" can be, by
looking. Then ask for **2–4 acceptance criteria**.

**Write the criteria now, at the opening.** At the end the owner is motivated to close; only
criteria fixed in advance are honest. This project has an instance already: the visual slice's
single criterion was *"has the owner started opening `/vacancies`"*.

Record it in `$VAULT/sprint.md`, incrementing the number. From then on new vault pages carry that
sprint in `sprint:` — meaning **where the page came from**, never what it belongs to.

## Closing one

**Closure is decided on the goal, not on an empty backlog.** Requiring every task closed makes the
sprint a consequence of the backlog rather than a frame for it, and leaves only two outcomes:
closing tasks for form's sake, or a sprint that never ends.

Leftover work is carried over or dropped — and **dropping is a decision with a reason**, so it
becomes a `decisions/` page. That is the payoff: at the retrospective you can see not only what was
done but what you stopped doing and why, which is otherwise lost in silence.

You may report — "goal of S1: …; 7 of 9 epics closed; two open" — and you may record a closure once
the owner declares it. **You never close a sprint yourself**, for the same reason you never resolve
a contradiction.

On closing: move the sprint's block in `$VAULT/sprint.md` to "Closed sprints". **Closing a sprint
archives nothing** — and since 2026-08-21 that is because archiving happens somewhere else, not
because it would be wrong.

**What this paragraph said until then, and why it was right when written.** An earlier draft
archived the handoffs into `archive/sprints/S<N>/`, and that was measured before it was ever run:
31 pages cited `raw/handoffs/2026-08-12-...` in their `sources:`, so the first close would have
turned the check red on all 31 and demanded a frontmatter rewrite — the exact failure the
source-path rule exists to catch. It would also have made those files' own wikilinks load-bearing,
reversing on purpose a decision the check makes on purpose: `raw/` is excluded from the link set
precisely so that an immutable file naming a page nobody wrote cannot make the vault permanently
red.

**What answered that objection was a mechanism, not an argument.** `scripts/vault-archive.sh` moves
a file and rewrites every `^sources:` citation of it as ONE run, then runs the gate itself — so the
31 red pages the objection was built on are the thing the script exists to prevent. `/ingest`
archives the journal it compiled as its last step, into `archive/<date>/<session>/handoffs/`.

**The unit is a session and never a sprint**, and that is the part worth keeping. A sprint is
declared by a person and may run for weeks; an ingest has one source in its hands and knows exactly
what has left the working set. Archiving on an event nobody can misjudge beats archiving on a
boundary somebody has to declare.
