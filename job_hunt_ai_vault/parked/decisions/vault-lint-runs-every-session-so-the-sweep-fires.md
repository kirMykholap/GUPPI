---
title: "`/vault-lint` runs every session, so the sweep inside it actually fires"
type: decision
status: current
authority: lint-cadence
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-30
target_kind: action
target: vault-lint-runs-every-session
supersedes: [[lint-waits-for-an-open-sprint]]
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", ".claude/skills/vault-lint/SKILL.md"]
tags: [vault, process, harness]
---

# Context

**One mechanism grows `wiki/` and one shrinks it, and only the first runs reliably.** `/ingest`
compiles a journal into pages; the sweep in `scripts/vault-archive.sh` moves what has earned its way
out. The sweep is a step of `/vault-lint`, and `/vault-lint` is a per-sprint ritual.

**On 2026-08-29 `/ingest` ran twice and `/vault-lint` did not run at all.** `wiki/` went from 556 to
568 pages and nothing was retired.

# The question

**At what cadence does `/vault-lint` run, given that the only mechanism which shrinks the corpus lives
inside it?**

# How it works after

**`/vault-lint` becomes a per-session ritual rather than a per-sprint one.** The sweep stays where it
is — inside the script, held by that skill — and its **venue does not move**; what changes is how
often the ritual that supplies its two arguments and its human dry-run reading is performed
([[the-archive-mover-is-a-sweep-inside-the-archive-script-at-the-lint-stage]]).

**Case 2.4 depends on this and buys nothing without it.** The archiver marks and moves in one pass
([[the-archiver-marks-and-moves-a-decision-in-one-pass]]) — but if the pass never runs, nothing is
marked and nothing moves.

# Recommendation

**Change the cadence, not the venue.** The two rulings do not conflict: the sweep's placement was
decided on its own ground, and this is about how often the ritual holding it is run.

# Ratification

**The owner said it**, on 2026-08-29, in his own words: «sweep должен происходить каждый ingest.
Почему сегодня не прошел? vault-lint выглядит как то, что мы должны делать каждую сессию».

**RECORDED AND NOT EXECUTED, twice.** It was filed on 2026-08-29 and not built; it was carried into
2026-08-30 and not built again. It is written as a decision page here so that it stops depending on a
feedback line surviving two drains.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
