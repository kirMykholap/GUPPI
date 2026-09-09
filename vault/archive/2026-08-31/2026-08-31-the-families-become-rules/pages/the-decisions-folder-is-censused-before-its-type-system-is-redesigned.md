---
title: "`wiki/decisions/` is censused before its type system is redesigned, and the delta rule is withdrawn"
type: decision
status: archived
authority: decisions-census-precedence
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md"]
tags: [vault, process, record-schema]
---

# The ruling, 2026-08-29

**owner:** «наша задача сейчас разобраться с тем, какие решения вообще лежат и что они описывают.
Мне кажется, что большая часть из них вообще не нужна.»

**The state of the folder is established by a census before anything about its type system is
changed.** What is in there and what each page describes comes first; his own reading is that most of
it is not needed, and that reading is a hypothesis the census tests rather than a premise to build on.

**Rejected: the session's delta-per-session rule over `decisions/`**, which it proposed and then
withdrew in the same turn — a rule about a folder written before anybody had read the folder.

# What it obliges

**The census is mode 2 of [[the-decisions-agent]]**, run on demand and never as part of an ingest,
grouping the decisions by the page each one acts on and naming which of a group is in force. **It has
never run.**

**Nothing here decides what the census will find.** Four measurements exist and none of them is a
verdict on necessity:

- **295 decisions in `wiki/decisions/`** — 263 `binding: prohibition`, 32 `deferral`, **0**
  `divergence`, the sweep of 2026-08-29 having taken every one of the 22.
- **Zero of the 32 deferrals are named in `decided_by:` by any live proposal or rule**, so none of
  them can retire under the model where a decision discharges against the page it caused
  ([[a-decisions-archival-condition-is-read-off-its-binding]]).
- **Nothing anywhere records what a given deferral's *term* is** — no field, no convention, no page —
  so a deferral's exit cannot be judged mechanically at all.
- **16 rule pages carry `decided_by:` naming their decision**, which is the relation "a rule names the
  decision behind it" existing for 16 of 263 prohibitions ([[the-per-folder-frontmatter-schema]]).

# The owner's model of a decision, which no page states in his terms

**A decision is an atomic instrument pointing at the creation or change of a page, and it retires once
that page exists.** That is already the sweep's `decided_by:` criterion, and 44 of the 66 decisions
swept on 2026-08-29 left exactly that way
([[a-decision-is-processed-when-a-live-page-names-it-in-decided-by]]).

**It is written here because it reads as a proposal everywhere else and it is a description of what is
running.** What the census would measure is the gap between that model and the 295: how much of a
decision's own prose — the reasoning and the rejected alternative — is lost when the decision retires
and only the page it caused remains.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*

# This page is suspended for the cleanup — 2026-08-30, and it is not deprecated

**[[the-cleanup-suspends-the-rules-that-would-refuse-it]] lifts this page for the cleanup**, with
three others, on one ratification. **The folder's type system changes without the census having run.**

**The census still has not run.** It is mode 2 of [[the-decisions-agent]], on demand, and the count
this page reports as 295 read **321** on 2026-08-30 — 283 `prohibition`, 36 `deferral`, 2
`divergence`. The `divergence` figure this page records as zero is no longer zero: two were written on
2026-08-30.

**What replaced the census as the thing that establishes the folder's state is a grouping rather than
a reading.** `authority.md` puts the 282 prohibitions into 53 families with no slug left over, and the
53 families with the title of every page in each are in `docs/vault-cleanup-families.md` for the owner
to mark ([[the-authority-register-groups-the-corpus-and-the-family-is-the-unit-of-a-cleanup]]).
**That is 99 verdicts rather than a page-by-page reading, and it is not what this page asked for** —
it asked what each page describes, and a family answers what a group of them is about.

**The census stays owed rather than being cancelled.** The lift makes the redesign legal now; it does
not make the reading unnecessary, and the store has no other instrument that would say which members
of a family are dead.

**This page stays `current`, is not `deprecated` and carries no `superseded_by:`.** A repeal is not a
supersession, ruled 2026-08-30. **The suspension has no stated end.**

**One thing the lift did not have to reach.** The dated cut in `wiki/decisions/_schema.yaml` —
`lifecycle_from: 2026-08-30` — was written on 2026-08-30 specifically so this prohibition was not
crossed: it changes the type system for pages written from that date and leaves the older population
untouched. The lift is about the family sweep, which does touch the older population.
