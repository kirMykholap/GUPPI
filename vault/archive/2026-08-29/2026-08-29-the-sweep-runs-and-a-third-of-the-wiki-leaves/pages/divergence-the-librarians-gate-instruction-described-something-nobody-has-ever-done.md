---
title: "DIVERGENCE: the librarian's gate instruction described something nobody has ever done, and the wording moved rather than the ritual"
type: decision
status: archived
authority: librarian-gate-cadence
binding: divergence
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", ".claude/agents/vault-librarian.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, harness, process]
---

# What was written and what happens

**The rule as written:** `.claude/agents/vault-librarian.md` said *"After any write, run
`bash scripts/vault-check.sh` and fix everything it reports"*. The vault's own `CLAUDE.md` carries
the same shape.

**What actually happens:** `/ingest` runs the gate **once, at its step 10**, after all the writing.
The librarian follows the ritual, not its own instruction, and **nobody had noticed the difference**.

# The ruling, 2026-08-26, in his own words

> **owner:** «Тогда нужно исправить инсутркцию для библиотекаря, если она врет. ingest говорит
> делать gate один раз в конце - это окей. Я не замечал каких-то проблем с тем, что библиотекарь не
> проверяет каждую запись через gate.»

**The wording moved.** The agent file now says *at the end of a writing pass*, injector first, with
the discrepancy written beside it.

# Why it looked free and was false at the same time

***After any write* is the strictly safer wording and nothing measured what it costs.** Taken
literally, an ingest that writes 29 pages pays **about ten minutes of gate alone**, at 21.5 s a run
on a 682-file corpus.

**Nobody has ever paid it**, which is exactly why the instruction survived: an obligation nobody
performs generates no evidence against itself
([[knowing-a-rule-is-not-a-mechanism]], [[a-boundary-stronger-in-prose-than-in-code]]).

# Rejected

**Rejected: making the ritual match the instruction.** The owner ruled the ritual correct on the
evidence he has — no problem he has noticed — so the wording moved instead.

# What is still owed

**The vault's own `CLAUDE.md` carries the same shape and is not the librarian's to write**
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]). **And no `wiki/rules/` page
governs either file**, so the two copies drift independently and nothing compares them
([[no-rule-reads-a-harness-file]], [[a-copied-list-drifts-and-a-sweep-cannot]]).
