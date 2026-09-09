---
title: "The one-writer rule gains its clause: the librarian owns the registers as well as `wiki/`"
type: decision
status: deprecated
authority: one-writer-scope
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", ".claude/hooks/session-brief.ps1", "job_hunt_ai_vault/CLAUDE.md"]
tags: [vault, agents, process]
superseded_by: [[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]
---

# The clause, in the owner's words, 2026-08-17

> **The librarian owns `wiki/` and the registers; a session edits a register only in the same
> change that deletes or renames what that register points at, and every such edit is recorded as
> a divergence.**

**This is the clause the brief has owed since 2026-08-16**, first written down as a gap on
[[hand-edits-of-the-wiki-are-a-recorded-divergence]] and raised in every brief since.

The registers are `index.md`, `tags.md`, `sprint.md` and `log.md`. `log.md` keeps its stricter
reading — a working agent never writes it at all — because a miss reported by the party being
measured is not evidence ([[the-librarian-writes-unattended]]).

## The finding underneath it: the hook was stricter than the text

The written rule says `wiki/` in **both** places that state it — the vault's `CLAUDE.md` and the
librarian's own definition — while the guard hook also fires on the registers. Two enforcement
surfaces, two scopes, and the disagreement had never been noticed because nobody had edited a
register by hand until this session did.

The lesson is [[the-hook-was-stricter-than-the-rule-it-enforced]]. This page is the resolution the
owner chose: **the hook's scope is the correct one, and the text moves up to meet it.**

## The narrow exception, and why it is narrow

A session may edit a register **only in the change that deletes or renames the thing the register
points at**. That is the case where waiting for the librarian leaves a register pointing at a file
that no longer exists — strictly worse than a recorded divergence, and undetectable by rule 5,
which only asks whether a wikilink resolves.

Everything else waits. In particular: adding a page, retiring a page, minting a tag and moving a
sprint line are all the librarian's, and none of them is an emergency.

## What it does not settle

The two properties that made the 2026-08-17 hand-writes safe are still written into no rule:
**no concurrency** ([[parallel-librarians-break-the-one-writer-property]]) and **the owner reviewed
the diff before the commit**. The clause above covers *who may edit what and when*; it says nothing
about *what makes an out-of-band write safe*, which remains the owner's to state.

## The clause was cited on 2026-08-19 where it was not needed

A brief for the rename sweep invoked the *"a session edits a register only in the same change that
deletes or renames what that register points at"* clause, and treated the sweep of `index.md`,
`sprint.md` and `log.md` as an exercise of it. **There was nothing to license**: the writer was the
librarian, and those three are the librarian's outright under the first half of this clause. **No
divergence occurred and none was recorded.**

**It is named rather than left**, because a cited licence reads as precedent whether or not it was
required, and the next session greps for how a register was edited last time
([[a-licence-cited-where-none-was-needed-is-named-so-it-is-not-inherited]]).

**And the clause still does not reach `job_hunt_ai_vault/CLAUDE.md`.** The registers named above are
four; the schema file is not one of them, and who may write it has now been a recorded gap twice
([[the-session-hand-edited-the-vault-schema-and-the-clause-naming-its-writer-is-still-owed]],
[[hand-edits-of-the-wiki-are-a-recorded-divergence]]).

# And the reach it did not have was granted to somebody else — 2026-08-19

**The closing paragraph above says this clause does not reach `job_hunt_ai_vault/CLAUDE.md`. It still
does not, and that file now has a clause of its own** —
[[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]. What the gate reads as **its own
input** is the session's to write: this file and every `wiki/*/_schema.yaml`.

**So the two clauses divide the vault by who reads the change, not by which directory it is in.**

| what | writer | what makes a change safe |
|---|---|---|
| `wiki/` and the four registers | the librarian | git plus `log.md`, reviewed after |
| `job_hunt_ai_vault/CLAUDE.md`, `wiki/*/_schema.yaml` | the session | the owner reads the diff **before** the commit |

**And the two properties this page says it does not settle are settled for the second row only.** *No
concurrency* and *the owner reviewed the diff* are named in the new clause as the reason it is shaped
that way — they are what a librarian writing its own instructions cannot have, since a change would then
have no reader but its author. **For `wiki/` and the registers they remain unwritten**, exactly as this
page says.

# Retired 2026-08-20: the middle clause was widened by the owner

**The narrow exception this page states — *a session edits a REGISTER only in the change that
deletes or renames what that register points at* — was replaced in the owner's own words** with
*a session repoints a CITATION in the same change that renames what it points at*
([[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]).

**What forced it was a deadlock this page's wording created.** A file move broke four `sources:`
lines inside `wiki/` pages; the gate went red on them; the lock refuses the librarian while the gate
is red; and the clause above licensed the repair three files away in `index.md` while refusing it
where it was needed. **One rule plus a hole became one rule.**

**Read this page for the first half, which is unchanged and is not superseded** — the librarian owns
`wiki/` and the four registers, `log.md` strictly — and for three things the successor cites rather
than repeats: the finding that the guard hook was stricter than the text
([[the-hook-was-stricter-than-the-rule-it-enforced]]), the licence cited on 2026-08-19 where none
was needed ([[a-licence-cited-where-none-was-needed-is-named-so-it-is-not-inherited]]), and the
table dividing the vault by who reads the change
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

**Still owed, and still owed on the successor:** the two properties that make an out-of-band write
safe — no concurrency, and the owner reading the diff — are written into no rule for `wiki/` and the
registers. **Three sessions have now recorded that gap without closing it.**
