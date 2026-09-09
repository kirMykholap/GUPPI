---
title: "The wide half of the per-type schema is a conversation about each type, not a task, and it waits"
type: decision
status: archived
authority: per-type-schema-sequencing
binding: deferral
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "job_hunt_ai_vault/sprint.md"]
tags: [record-schema, vault, process]
---

# Deferred by the owner on 2026-08-19

> **owner: the wide half is a conversation about each type, not a task**, and running it at the end
> of a long session would run it badly.

**What was built** is the field half: each `wiki/` folder carries a `_schema.yaml` naming the keys a
page there must and may hold, and the gate reads it
([[the-per-folder-frontmatter-schema]], [[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]).

**What is deferred** is the wide reading — **what a record of each type asserts, and what expires
it** — as a fixture the selftest runs. That is the design on
[[a-schema-per-type-says-what-a-record-asserts]], and it is what S2's first acceptance criterion asks
for.

**Rejected: finishing it the same night.** The field half is mechanical and a script can be pointed at
it. The wide half is six judgements — *what does a `lesson` assert; when has a `concept` expired* —
and each is the owner's. A session that had already executed a five-step ruling and four retro builds
would have produced six answers nobody had thought about.

# The consequence of not doing it

**S2's criterion 1 is part-built and is not met**, and the part that is built is the part that was
never the hard half. **No criterion is read off here**; that is the owner's
([[a-sprint-closes-on-its-goal]]).

**The `record-schema` corpus sweep waits on this too.** Seven `decisions/` pages and three elsewhere
carry record-schema subject matter and no such tag, and **the boundary of that sweep is what the
per-type reading settles** — sweeping now would sweep against a moving line
([[the-schema-tag-splits-into-db-schema-and-record-schema]]).

**And two field questions stay open with it**: whether `basis` belongs in the core
([[the-gate-learns-the-legal-key-set-from-a-yaml-per-folder]]), and whether `idea` joins the status
set as S2's second blocking question decided it should
([[proposals-are-a-folder-not-a-status]]).

# What makes it startable

**Nothing is blocking it.** It needs a conversation with the owner, per type, with the corpus in front
of him — the shape [[the-owner-decides-how-a-slice-is-executed]] describes for anything whose answers
are judgements. The proposal carries the design; this page carries only the ruling that the design
waits and why.
