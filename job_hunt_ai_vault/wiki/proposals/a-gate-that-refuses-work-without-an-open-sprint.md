---
title: "A gate that refuses work while no sprint is open"
type: proposal
status: current
authority: sprint-gate-refusal
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "sprint.md", ".claude/settings.json"]
decided_by: [[what-the-harness-build-waits-on]]
tags: [harness, process]
---

# The shape, agreed 2026-08-17 and not built

**A `UserPromptSubmit` hook that denies while `sprint.md` declares no open sprint.**

**`SessionStart` cannot do it.** It injects context and has no way to refuse — which is a property of
the event, not of the script, and it is why the brief hook only ever warns
([[session-hooks]]). The refusal has to sit on an event that can deny, and the first prompt of a
session is the earliest one that can.

# The consequence of not having it

**Nothing stopped the session of 2026-08-17 from working a whole day outside a sprint**, between S1
closing and S2 opening, and nothing would stop the next one. The owner named that failure the same
day and then opened S2 immediately rather than next session, precisely to avoid repeating it
([[a-sprint-closes-on-its-goal]]).

The vault already refuses one thing on this ground — `/vault-lint` waits for an open sprint
([[lint-waits-for-an-open-sprint]]) — so the rule exists and only its enforcement is missing.

# What is open

- **What counts as "declares an open sprint"**, mechanically. `sprint.md` is prose with a `Closed: —`
  line; a gate needs a predicate, and inventing one silently is how a check comes to pass for the
  wrong reason ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).
- **What the escape hatch is.** Opening a sprint is itself work, and a gate that forbids the act
  that clears it is a deadlock.
- Whether it denies or warns. Every hook in this harness so far warns
  ([[the-journal-gate-hook]]), and this would be the first that refuses.

Retired with `superseded_by:` the day it is built or refused
([[proposals-are-a-folder-not-a-status]]).

# The deadlock this page names as an open question happened, to a different gate — 2026-08-20

**"A gate that forbids the act that clears it is a deadlock" stopped being hypothetical.** The
librarian lock refused the only writer permitted to repair the `wiki/` content that had made the
gate red ([[the-librarian-lock-hook]], [[the-librarian-writes-unattended]]).

**It was resolved by widening a rule rather than by building a hatch** — a session may repoint a
citation in the same change that renames what it points at
([[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]). **An escape hatch inside the
lock was considered and rejected as a design rather than a move**, and the owner named this page as
where that design already lives.

**So this page's third open question now has evidence attached and a second argument for it.** A
lock on a red tree also hides the health of the thing it guards, because it denies before the agent
type is resolved ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]) — so a hatch buys
diagnostics as well as an exit.

**What it does not change:** this proposal is about a sprint gate, not a librarian lock, and it is
still unbuilt.
