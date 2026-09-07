---
title: "`log.md` is filled mechanically and rotates when the sprint closes"
type: decision
status: current
authority: log-writer-and-rotation-trigger
binding: deferral
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "log.md", "scripts/vault-archive.sh"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-29

**owner:** «sweep дописывает строку в log.md И сообщает тому, кто вызвал(библиотекарю). Библиотекарь в
иделае вообще не должен трогать log.md. Лог должен заполнятсья механичсеки. И так же механичсеки
архивироваться в конце архиватор полностью, а на его месте появистя пустой log.md»

Four claims, and only the first is built:

1. **A sweep appends its own line to `log.md` *and* reports to whoever called it.** Built 2026-08-29.
2. **The librarian should ideally not touch `log.md` at all.** Not built.
3. **The log is filled mechanically.** Not built.
4. **At the sprint's end the archiver moves the whole file away and an empty `log.md` takes its
   place.** Not built.

**And the rotation is tied to the sprint close.** He selected that against tying it to `/vault-lint`
or to a sweep run, on the ground that **a sweep may fire three times in a sprint or not at all** — a
trigger that fires an unpredictable number of times cannot be a rotation.

**Rejected: rotating at `/vault-lint`, and rotating at each sweep.**

# What is built today, and what it settled on the way

**One line, written by `scripts/vault-archive.sh` when its sweep runs**, naming what it moved, marked,
rewrote and refused. It is the first line in this store's history written into a register by something
other than the librarian.

**No page said whether a script may append to `log.md`.** The one-writer clause names the librarian and
is written about agents; [[the-steward-is-scripts-that-run-after-the-librarian]] is adjacent and does
not rule it. The gap surfaced only when the owner ordered the sweep to record its actions, and this
ruling is what closes it ([[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]]).

# What it obliges, and where it is picked up

**A redesign of who holds the pen over the journal**, which needs an item of its own: the librarian
stops writing `log.md`, and whatever writes it instead has to carry the `- miss:`, `- measure:`,
`- decision:` and `- ingest:` kinds a session and an ingest produce today.

**The design that would carry it already exists and is older than this ruling**
([[log-md-rotates-per-session-into-the-dated-archive]]), and this ruling changes its trigger: **per
sprint, not per session.**

**Until then the librarian goes on writing it**, which is the arrangement every rule in this store
still describes.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# A live proposal designs the rotation the other way, and neither page named the other — 2026-08-29

> [!NOTE] RAISED, NOT RESOLVED — different `authority:` slugs, so rule 3 of the gate cannot see it and
> no `CONTRADICTION` block is legal
> **This page ties rotation to the sprint close** and explicitly rejects rotating at `/vault-lint` or at
> each sweep. **[[log-md-rotates-per-session-into-the-dated-archive]] is `current` and per session** —
> *a new session starts a new `log.md`* — and still lists *whether the rotation runs at `/ingest` or at
> session start* as open. **Both live, neither superseding the other.**

**The session of 2026-08-29 carried this as an unanswered question and the corpus carried it as two
live answers.** He was asked, the sizes were measured, and he did not answer; **his ruling of
2026-08-29 tying rotation to the sprint close stands unrevised.**

**The measurement, taken the same day**: `log.md` is 972,717 bytes over 10,464 lines, **69% of the
registers by size**; split at the S3 boundary, 503,239 bytes before 2026-08-23 and 469,478 after; one
day's section alone is 33,038. **A sprint-close rotation halves the file; a per-session one would leave
33–67k.** Neither figure says anything about tokens, which depends on how much of the file is read
([[vault-scripts]]).

**This is the third instance of the slug-blind class the brief carries**, and the first found by an
agent rather than by a reader stumbling on it ([[the-decisions-agent]]).

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
