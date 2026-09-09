---
title: "A sprint closes on its goal, not on an empty backlog — and the librarian never closes it"
type: decision
status: current
authority: sprint-closure
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-13
created: 2026-08-13
sources: ["docs/superpowers/specs/2026-08-13-second-brain-design.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", ".claude/skills/sprint/SKILL.md", "raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md"]
tags: [process, vault]
---

# A sprint closes on its goal

**Decided on 2026-08-13.** Rejected: closure when every task is done. That makes the sprint a
consequence of the backlog rather than a frame for it, and it leaves only two outcomes — closing
tasks for form's sake, or a sprint that never ends.

- **A sprint is declared explicitly**, never derived from merges or slices. "Sprint" must mean what
  the owner intends: the design conversation that produced this vault was not a slice and yielded a
  great deal of knowledge.
- **The goal is a checkable statement with 2–4 acceptance criteria, written when the sprint
  opens.** "Improve collection" cannot be checked; "collection starts from the browser and its
  progress is visible" can be, by looking. Criteria are fixed in advance deliberately — at the end
  you are motivated to close, and only criteria written in advance are honest. This project already
  has an instance: the visual slice's single criterion was *«has the owner started opening
  `/vacancies`»*.
- **Leftover work is carried over or dropped, and dropping is a decision with a reason** — so it
  becomes a page in `decisions/`. That is the payoff: at the retrospective you can see not only
  what was done but *what you stopped doing and why*, which is otherwise lost in silence.

## The note's trigger was the retrospective, and half of it survived

The instructions note introduces its two closure steps with a line of its own —
«**По завершении ретроспективы:**», *when the retrospective is finished*. It is the only trigger
either of the owner's notes gives for a closure, and the method note repeats the frame: an active
phase, then a retrospective, then compilation
([[the-owners-method-note-and-what-was-built-from-it]]).

**The retrospective survived, and it is still the vault's only per-sprint cadence** — `/vault-lint`
is defined against it and nothing else is ([[lint-waits-for-an-open-sprint]]), and it is where
dropped work becomes visible, which is the payoff named above.

**What did not survive is closure as its consequence.** A sprint closes when the owner declares it
closed against the goal — at a retrospective, or anywhere else, or not at all while the goal is
unmet. The retrospective is when the question gets *asked*; it is never what answers it. That
distinction is the whole of the section below on who does what, and it is why the librarian may sit
through a retrospective and still close nothing.

## Closing a sprint does not move its handoffs

**Decided 2026-08-13, before `/sprint` was ever run, and by measurement.** The owner's own note
asked for the opposite — «переместить файлы текущего спринта из `raw/handoffs/` в
`archive/sprints/sprint-N/`», the last of its two closure steps
([[the-owners-instructions-note-and-what-was-built-from-it]],
[[the-handoff-splits-into-a-handoff-and-a-knowledge-base]]). **Its first step — a final `/ingest`
at closure — was built stronger than asked**: an ingest ends every session, so a sprint never
closes over uncompiled journals.

**Rejected, because 31 pages cited `raw/handoffs/…` in `sources:`.** The first close would have
turned `vault-check.sh` red on all 31 at once — *the exact failure that rule exists to catch*
([[vault-scripts]]) — and the only repair would have been to make an immutable file's path
load-bearing in 31 places at every future close.

**Re-measured 2026-08-15, at the first `/vault-lint`: it is now 95 of 111 pages**, counted from the
frontmatter of every page in `wiki/` and `archive/`. The 31 was the reading of 2026-08-13 and the
number was carried across two ingests without being taken again — the shape on
[[a-stated-count-drifts-from-the-list-it-heads]], here on the page whose whole argument is the
number. **The argument is three times stronger than it was written**, and the direction matters:
this is a rejection that gets harder to reverse with every ingest, so if archiving handoffs is ever
wanted, the cost is paid at the *first* close and never gets cheaper.

So `sprint.md` records the closure and the journals stay where they are. `archive/` keeps its other
job: retired pages. The handoffs are already immutable; moving them buys tidiness and costs
provenance.

**Both notes asked for it, which the measurement did not change.** The method note's last line
puts it more strongly than the instructions note did — *«Архивация: Промежуточные файлы сессии
уходят в архив, в базе остается только синтезированный результат»*, the session's intermediate
files leaving so that only the synthesised result remains. That is the ask this rejection is
against, stated twice by the same person on the same day
([[the-owners-method-note-and-what-was-built-from-it]]), and the count is what answers it.

## Who does what

The librarian **reports** — "goal of S4: …; 7 of 9 closed; two open" — and records the closure once
it is declared. **It never closes a sprint**, for the same reason it never resolves an `authority`
conflict: [[the-librarian-writes-unattended]].

What bounds a sprint in practice is not the calendar but the size of the brief:
[[the-growth-signal-is-the-brief]].

## Deferred, explicitly, on 2026-08-18: what a sprint *is*

**The owner deferred the question of what a sprint is and how it is worked with**, in as many words.
Nothing on this page changes: it answers when a sprint *closes* and who declares it, and that half
is decided.

**What has no answer is the shape of the thing itself** — how one is scoped, what belongs inside it,
how a sprint retrospective is run and what it produces. The last of those is a term with nothing
behind it by design ([[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]]), and the next
session to reach a sprint boundary meets that gap.

**Consequence of leaving it deferred:** each sprint is opened and read off by precedent, and the
precedent is `sprint.md` plus the `/sprint` skill rather than a record anybody agreed to.

# Correction, 2026-08-30: the sentence about `/vault-lint`'s cadence is false

**The paragraph above says the retrospective "is still the vault's only per-sprint cadence" and that
`/vault-lint` is defined against it.** That stopped being true on 2026-08-30.

**`/vault-lint` is now a per-session ritual** ([[vault-lint-runs-every-session-so-the-sweep-fires]]),
because the sweep that lives inside it is the only mechanism that shrinks `wiki/` and it had not fired
while `/ingest` ran twice. The page cited in that paragraph is retired.

**This page's own claim is untouched.** A sprint still closes on its goal and on the owner's
declaration; only the cadence sentence went false, and it is corrected here rather than the page
retired.

*(Corrected 2026-08-30 from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
