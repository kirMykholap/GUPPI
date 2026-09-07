---
title: "`lessons/` becomes a queue drained into `proposals/` at the ingest, rather than a store"
type: proposal
status: current
authority: lessons-as-a-queue
basis: human
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-a-claim-is-looked-up-before-a-page-is-written/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md", ".claude/skills/ingest/SKILL.md"]
decided_by: [[the-lessons-queue-is-the-owners-design-and-is-not-built]]
tags: [vault, process, agents]
---

# The owner's design, 2026-08-21

**At the end of an ingest the librarian reads the lessons and produces two records from each**:

- **the fact** — what is now known — into `concepts/` or `decisions/`;
- **the action** — what should therefore be done — into `proposals/`.

**A lesson is archived only once nothing on it lives only there.** That clause is not new: it is
already ratified for proposals, and it is the test that keeps a retirement from deleting a claim
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

**The proposals reach the owner through the brief and he decides.** The librarian never acts on the
action half; producing it is the whole of the job.

# Why it was raised: the folder is a store and nothing drains it

**`lessons/` holds 121 pages.** Every one records something that burned us, and **nothing in the
rituals ever asks what should be done about any of them.** The folder grows monotonically and is read
only when somebody greps into it.

**It is the same shape as a queue only one party can drain**, and this store has already recorded
what that costs ([[a-queue-only-one-party-can-drain-is-unbounded]]).

**And it bears on the plan check.** `lessons/` is deliberately excluded from the wider `/pre-task`
enumeration *because* it is to become a queue — a plan checked against a work list would be reading
intentions as constraints ([[the-pre-task-enumeration-covers-every-folder-but-lessons]]).

# What it would take, and what is open

- **A step in `/ingest`, after the compilation and before the brief.** Its files are
  `.claude/skills/ingest/SKILL.md` and the librarian's own definition.
- **A bound on the first run.** 121 pages read at once is not an ingest step, it is a project; whether
  the drain starts from the ones this ingest touched or sweeps the folder once is undecided.
- **The admission rule applies to what comes out of it.** A proposal per lesson is exactly the
  multiplication the ground rule forbids, so the drain owes the same lookup every other page owes
  ([[occams-razor-is-the-ground-rule-for-the-vault]],
  [[no-new-entity-where-an-existing-one-can-carry-the-claim]]).

**Not built in the session that designed it**, and named as deferred rather than dropped.

# The design splits in two on 2026-08-24, and one half is built while the other stays here

**Half of this proposal moved to a `/vault-lint` dispatch and half did not.**

| the half | where it lives now |
|---|---|
| spot the recurring family across the whole folder | **built**: a `vault-librarian` dispatch in `/vault-lint`, running before the audit, with `uv run python scripts/lessons-queue.py` as its worklist |
| two records per lesson — the fact into `concepts/` or `decisions/`, the action into `proposals/` | **still this page's**, and still the librarian's work at an ingest |

**The reason the first half left the ingest is a position rather than a preference.** At an ingest
the librarian stands inside one session's context, where the seventh instance of a family looks
exactly like the first; a fresh dispatch reading the whole queue has no such context
([[the-librarian-is-blind-to-a-recurring-family-from-where-it-stands]],
[[one-librarian-behind-every-caller]]).

**Cadence: once per sprint, plus on demand — unchanged.** **The collector has never been run.**

**No threshold was set for what counts as a family**, deliberately: «порог не назначаем, смотрим за
работой агента и вносим правки если понадобится» (owner, 2026-08-24).

**The bound this page asked for is answered by the queue rather than by a rule.** The open question
was whether a first drain starts from the lessons an ingest touched or sweeps the folder once;
`scripts/lessons-queue.py` prints the **94 of 140** lessons cited by neither a rule nor a proposal,
which is a sweep of the part that has never been read for this purpose.

## Two corrections to the text above, dated where they stand

**Its figure "121 pages" was the tree of 2026-08-21; `lessons/` holds 140 on 2026-08-24**, of which
21 are cited by a rule, 36 by a proposal, 46 in the union
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**It cites [[a-built-proposal-retires-once-nothing-on-it-lives-only-there]] as live support and that
page is deprecated**, in `archive/2026-08-22/`. The clause it was cited for survived the retirement
in a changed form: a page leaves `wiki/` only once a live page names it, and
`scripts/vault-archive.sh` refuses the move otherwise
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]], [[vault-archive-sh]]).
**The citation is left standing above and corrected here**, because what that sentence asserted on
2026-08-21 is part of the record of why the clause was written.
