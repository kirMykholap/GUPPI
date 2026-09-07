---
title: "A librarian answer that stops at the agent boundary is not an answer the owner has"
type: lesson
status: archived
authority: agent-boundary-relay
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md"]
tags: [agents, process, vault]
---

# The note existed to prevent exactly what happened

At `/pre-task` for sprint item 3 the librarian named a live tension: S2's blocking question 4 answers
*does product work interleave — it does not*
([[product-work-does-not-interleave-into-the-vault-sprint]]), and item 3 edits `tests/`. It closed
with *"his listing settles it; I note it so nobody re-derives the objection."*

**The session carried the ruling into the work and left the reasoning in the agent's output.** The
owner then asked **«почему мы пошли править сам продукт? я думал мы говорим за вики»** — that
objection, re-derived, one translation later.

**The answer was short and the session had it:** `269c877` is a `feat(harness)` commit that changed
`tests/integration/test_migrations.py` by 11 insertions while building the test-database guard
([[the-test-database-guard]]), so the file was made mixed-language **by the vault work**, and item 3
is that work's own residue rather than a product slice.

# What failed is the relay, not the reasoning

**A librarian answer is read by one session, and the owner sees only what that session repeats.** A
note written to stop an objection recurring is worth nothing if it stops at the agent boundary —
which is the same property already recorded about chat
([[chat-is-not-a-channel-that-survives-the-session]]), one hop earlier in the pipe.

**The rule the session took from it:** when `/pre-task` names a tension between a task and a written
rule, **that tension goes to the owner BEFORE the work starts** — not held as settled because the
answer settled it.

# Why this is worth a page rather than a resolution

**The librarian answered correctly and the outcome was still wrong**, so nothing about the corpus or
the retrieval needs changing. What is missing is a habit at the boundary, and habits in this project
have consistently failed until something ran them
([[knowing-a-rule-is-not-a-mechanism]], [[no-rule-reads-a-harness-file]]). **Whether that habit
becomes a rule is the owner's**; it is recorded here with its one instance so the next one is a
second instance rather than a fresh surprise.

**And it is evidence for a clarifying line elsewhere.** The owner read
[[product-work-does-not-interleave-into-the-vault-sprint]] and item 3 as contradicting; the page bars
product *work* and item 3 is harness residue in a product file, so the page is not wrong — but two
readers landing in the same place is the evidence, not the argument.
