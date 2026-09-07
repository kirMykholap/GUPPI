---
title: "The audit is its own dispatch, run after the writes, and the extra fixed cost was paid on purpose"
type: decision
status: current
authority: audit-dispatch-order
binding: prohibition
basis: inference
sprint: S1
decided: 2026-08-15
created: 2026-08-15
sources: ["archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md", ".claude/skills/vault-lint/SKILL.md"]
tags: [agents, vault]
---

# An audit of a corpus that is about to change is an audit of nothing

**The session's own decision, 2026-08-15, stated for the record** — not the owner's, which is why
this page is `basis: inference` and says whose call it was in its first line.

Four `vault-librarian` dispatches ran that day. The audit was **not** folded into the writing
dispatch and **not** run before it: it was given a dispatch of its own, after the corpus had
finished moving.

**Rejected: one dispatch that writes and then audits, or an audit run first.** An audit run before
the writes examines a corpus that is about to change — every count it takes is stale before the
report is read, and this is a store where a count going stale is the most frequently observed
defect it has ([[a-stated-count-drifts-from-the-list-it-heads]]). An audit folded into the writing
dispatch is worse still: the agent grades its own diff, which is the instrument-gaming shape
already recorded here ([[an-instrument-that-contains-its-own-answers-can-be-gamed]]).

**The price, measured: one extra fixed part, about 15 minutes.** That is the right order of
magnitude to expect, because the four figures of that day say the **fixed cost of a dispatch
dominates a small one** — [[agent-round-trip-cost]] carries the table.

## What it obliges

An audit is scheduled **after** the last write of the thing it audits, and it is a separate
dispatch. The corollary is that a session which writes after its audit has not audited what it
shipped, and owes the note saying so.

The evidence that the discipline paid on the day: the catalogue's first regeneration after the
audit was **byte-identical**, which is the cheap proof that sixteen rewritten pages changed no
frontmatter at all ([[the-catalogue-is-generated-not-maintained]]).
