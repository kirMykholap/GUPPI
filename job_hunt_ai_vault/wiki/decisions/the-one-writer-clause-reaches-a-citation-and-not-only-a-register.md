---
title: "The one-writer clause is extended: a session repoints a citation in the change that renames what it points at"
type: decision
status: current
authority: one-writer-scope
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "job_hunt_ai_vault/CLAUDE.md", ".claude/hooks/lock-the-librarian.ps1"]
tags: [vault, agents, process]
supersedes: "[[the-one-writer-rule-covers-the-registers-too]]"
---

# The clause in its new wording, owner's ruling 2026-08-20

> **The librarian owns `wiki/` and the registers; a session repoints a citation in the same change
> that renames what it points at, and every such edit is recorded as a divergence.**

**The middle clause is what moved.** It read *"a session edits a **register** in the same change
that renames what that register points at"* from 2026-08-17
([[the-one-writer-rule-covers-the-registers-too]]). The owner selected the wider wording himself,
and his reason is the shape rather than the reach: **one rule instead of one rule plus a hole.** A
`sources:` line on a `wiki/` page is a citation and was not a register, so the old clause covered
the same act in `index.md` and refused it three files away.

**The first half is untouched.** The librarian owns `wiki/` and the four registers, and `log.md`
keeps its stricter reading — a working agent never writes it at all
([[the-librarian-writes-unattended]]).

## The bound is mechanical, and it is the whole licence

- **lines beginning `sources:` only** — `grep -F` to find, `awk` `index()` to rewrite, and no
  regular expression ever sees a path ([[a-path-is-never-a-pattern]]);
- **prose is never touched**, and the reason is that a prose reference is a claim about where a
  file was at a time, which repointing inverts ([[a-rewriter-must-be-paired-with-a-detector]]);
- **recorded as a divergence**, and **the owner reads the diff before the commit**.

**Exercised the same turn it was ruled**, on four pages — `the-folder-is-the-first-narrowing`,
`the-vault-is-compiled-not-retrieved`,
`the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here`,
`an-alias-may-point-at-a-page-not-only-at-a-tag`. **Eight changed lines and all eight begin with
`sources:`**, verified from the diff; the gate exited 0 afterwards with one standing advisory
([[the-session-wrote-wiki-by-hand-while-the-lock-held-its-only-writer-out]]).

## What produced it: a deadlock nothing had predicted

The owner moved `.claude/agents/vault-librarian/AGENT.md` to `.claude/agents/vault-librarian.md`
mid-session. Four `sources:` lines in `wiki/` went red, and then:

- the gate is red **because of** `wiki/` content;
- `wiki/` has exactly one writer ([[the-librarian-writes-unattended]]);
- the lock refuses that writer while the gate is red ([[the-librarian-lock-hook]]).

**The only sanctioned writer was locked out by the one thing only it could clear.** The vault held
the shape, for a different gate and as an open question — *"a gate that forbids the act that clears
it is a deadlock"* ([[a-gate-that-refuses-work-without-an-open-sprint]]).

## What was rejected

- **Reverting the file move and sequencing the librarian around it.** No rule change, but the
  librarian's own write ritual ends in a gate run that would be red, and the move would be made
  twice.
- **An escape hatch inside the lock.** That is a design rather than a move, and it is already an
  open question on [[a-gate-that-refuses-work-without-an-open-sprint]].

## What is carried forward from the retired page, and what is still owed

**The two clauses still divide the vault by who reads the change, not by which directory it is in**
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]):

| what | writer | what makes a change safe |
|---|---|---|
| `wiki/` and the four registers | the librarian | git plus `log.md`, reviewed after |
| `job_hunt_ai_vault/CLAUDE.md`, `wiki/*/_schema.yaml` | the session | the owner reads the diff **before** the commit |

**And the two properties that make an out-of-band write safe are still written into no rule** — no
concurrency ([[parallel-librarians-break-the-one-writer-property]]) and the owner reading the diff.
**Both held here**, and saying so is not the same as writing them down. That gap was named on
2026-08-17, is unchanged, and remains the owner's to close.

**The retired page also carries a licence cited where none was needed**
([[a-licence-cited-where-none-was-needed-is-named-so-it-is-not-inherited]]) and the finding that the
guard hook was stricter than the text it enforced
([[the-hook-was-stricter-than-the-rule-it-enforced]]). Neither is superseded; both are read from
`archive/`.
